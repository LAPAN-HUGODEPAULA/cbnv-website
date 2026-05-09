import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone

from pages.models import Announcement


@pytest.mark.django_db
def test_published_announcements_exclude_drafts_and_future_items():
    now = timezone.now()
    published = Announcement.objects.create(
        title="Programação preliminar publicada",
        slug="programacao-preliminar-publicada",
        status=Announcement.Status.PUBLISHED,
        published_at=now,
        featured_on_home=True,
    )
    Announcement.objects.create(
        title="Rascunho interno",
        slug="rascunho-interno",
        status=Announcement.Status.DRAFT,
        published_at=now,
        featured_on_home=True,
    )
    Announcement.objects.create(
        title="Publicação futura",
        slug="publicacao-futura",
        status=Announcement.Status.PUBLISHED,
        published_at=now + timezone.timedelta(days=1),
        featured_on_home=True,
    )

    assert list(Announcement.objects.published()) == [published]
    assert list(Announcement.objects.featured()) == [published]


@pytest.mark.django_db
def test_recent_announcements_pin_items_first():
    now = timezone.now()
    latest = Announcement.objects.create(
        title="Notícia recente",
        slug="noticia-recente",
        status=Announcement.Status.PUBLISHED,
        published_at=now,
    )
    pinned = Announcement.objects.create(
        title="Notícia fixada",
        slug="noticia-fixada",
        status=Announcement.Status.PUBLISHED,
        published_at=now - timezone.timedelta(days=5),
        pinned=True,
    )

    assert list(Announcement.objects.recent()) == [pinned, latest]


@pytest.mark.django_db
def test_published_announcement_requires_publication_date():
    announcement = Announcement(
        title="Sem data",
        status=Announcement.Status.PUBLISHED,
    )

    with pytest.raises(ValidationError):
        announcement.full_clean()


@pytest.mark.django_db
def test_duplicate_title_auto_slug_raises_validation_error():
    Announcement.objects.create(
        title="Evento cancelado",
        slug="evento-cancelado",
        status=Announcement.Status.PUBLISHED,
        published_at=timezone.now(),
    )
    duplicate = Announcement(
        title="Evento cancelado",
        status=Announcement.Status.DRAFT,
    )

    with pytest.raises(ValidationError):
        duplicate.full_clean()
