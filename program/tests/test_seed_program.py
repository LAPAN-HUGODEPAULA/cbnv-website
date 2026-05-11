import pytest
from django.core.management import call_command

from program.models import ProgramDay, ProgramSession, ProgramTalk, Speaker


@pytest.mark.django_db
def test_seed_program_is_idempotent(capsys):
    call_command("seed_program")
    first_counts = (
        ProgramDay.objects.count(),
        ProgramSession.objects.count(),
        ProgramTalk.objects.count(),
        Speaker.objects.count(),
    )

    call_command("seed_program")
    second_counts = (
        ProgramDay.objects.count(),
        ProgramSession.objects.count(),
        ProgramTalk.objects.count(),
        Speaker.objects.count(),
    )

    assert second_counts == first_counts
    output = capsys.readouterr().out
    assert "Program records:" in output
    assert "skipped" in output
