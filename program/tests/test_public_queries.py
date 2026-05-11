from datetime import date, time

import pytest

from program.models import (
    BREAK,
    CANCELLED,
    CONFIRMED,
    DRAFT,
    HIDDEN,
    PENDING,
    PUBLISHED,
    TALK,
    ProgramDay,
    ProgramSession,
    ProgramTalk,
    Speaker,
    get_public_program_by_day,
)


@pytest.mark.django_db
def test_public_program_is_grouped_and_ordered_deterministically():
    day_two = ProgramDay.objects.create(date=date(2026, 11, 12), title="Dia 2", sort_order=2)
    day_one = ProgramDay.objects.create(date=date(2026, 11, 11), title="Dia 1", sort_order=1)
    later = ProgramSession.objects.create(
        day=day_one,
        start_time=time(10),
        end_time=time(11),
        title="Later",
        activity_type=TALK,
        status=PUBLISHED,
        sort_order=2,
    )
    earlier = ProgramSession.objects.create(
        day=day_one,
        start_time=time(9),
        end_time=time(10),
        title="Earlier",
        activity_type=TALK,
        status=PUBLISHED,
        sort_order=1,
    )
    day_two_session = ProgramSession.objects.create(
        day=day_two,
        start_time=time(9),
        end_time=time(10),
        title="Second day",
        activity_type=BREAK,
        status=PUBLISHED,
    )
    ProgramTalk.objects.create(session=later, title="Later talk", status=CONFIRMED)
    ProgramTalk.objects.create(session=earlier, title="Earlier talk", status=CONFIRMED)

    data = get_public_program_by_day()

    assert [group["day"].title for group in data] == ["Dia 1", "Dia 2"]
    assert [item["session"].title for item in data[0]["sessions"]] == ["Earlier", "Later"]
    assert data[1]["sessions"][0]["session"] == day_two_session


@pytest.mark.django_db
@pytest.mark.parametrize("status", [DRAFT, PENDING, CANCELLED])
def test_public_program_excludes_non_published_sessions(status):
    day = ProgramDay.objects.create(date=date(2026, 11, 11), title="Dia 1")
    session = ProgramSession.objects.create(
        day=day,
        start_time=time(9),
        end_time=time(10),
        title="Private session",
        activity_type=TALK,
        status=status,
    )
    ProgramTalk.objects.create(session=session, title="Talk", status=CONFIRMED)

    assert get_public_program_by_day() == []


@pytest.mark.django_db
@pytest.mark.parametrize("speaker_status", [PENDING, HIDDEN])
def test_public_program_does_not_expose_pending_or_hidden_speaker_details(speaker_status):
    day = ProgramDay.objects.create(date=date(2026, 11, 11), title="Dia 1")
    session = ProgramSession.objects.create(
        day=day,
        start_time=time(9),
        end_time=time(10),
        title="Private speaker session",
        activity_type=TALK,
        status=PUBLISHED,
    )
    speaker = Speaker.objects.create(
        name="Private Speaker",
        institution="Private Institution",
        bio="Private bio",
        status=speaker_status,
    )
    ProgramTalk.objects.create(session=session, title="Talk", speaker=speaker, status=CONFIRMED)

    assert get_public_program_by_day() == []


@pytest.mark.django_db
def test_confirmed_speakers_linked_to_public_activities_are_available_for_index():
    day = ProgramDay.objects.create(date=date(2026, 11, 11), title="Dia 1")
    session = ProgramSession.objects.create(
        day=day,
        start_time=time(9),
        end_time=time(10),
        title="Public session",
        activity_type=TALK,
        status=PUBLISHED,
    )
    confirmed = Speaker.objects.create(name="Confirmed Speaker", status=CONFIRMED, institution="UFMG")
    pending = Speaker.objects.create(name="Pending Speaker", status=PENDING)
    ProgramTalk.objects.create(session=session, title="Public talk", speaker=confirmed, status=CONFIRMED)
    ProgramTalk.objects.create(session=session, title="Pending talk", speaker=pending, status=CONFIRMED)

    assert list(Speaker.objects.linked_to_public_program()) == [confirmed]
