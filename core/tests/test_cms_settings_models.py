import pytest
from wagtail.models import Site

from core.models import CoreSettings


@pytest.mark.django_db
def test_core_settings_store_global_event_metadata():
    site = Site.objects.get(is_default_site=True)
    settings = CoreSettings.for_site(site)

    settings.event_name = "XII Congresso Brasileiro de Neurociências da Visão"
    settings.short_event_name = "CBNV 2026"
    settings.start_date = "2026-11-11"
    settings.end_date = "2026-11-13"
    settings.city = "Belo Horizonte"
    settings.format_label = "Presencial"
    settings.contact_email = "contato@example.com"
    settings.submissions_contact_email = "submissoes@example.com"
    settings.sponsorship_contact_email = "patrocinios@example.com"
    settings.fapemig_text = "Apoio institucional FAPEMIG."
    settings.default_seo_title = "CBNV 2026"
    settings.save()

    settings.refresh_from_db()

    assert settings.short_event_name == "CBNV 2026"
    assert settings.city == "Belo Horizonte"
    assert settings.format_label == "Presencial"
    assert settings.submissions_contact_email == "submissoes@example.com"
    assert settings.fapemig_text == "Apoio institucional FAPEMIG."


def test_core_settings_link_status_helpers():
    settings = CoreSettings(
        registration_status=CoreSettings.LinkStatus.COMING_SOON,
        registration_link="https://example.com/inscricoes",
        livestream_status=CoreSettings.LinkStatus.AVAILABLE,
        livestream_link="https://youtube.com/live/example",
        youtube_channel_url="https://youtube.com/@cbnv",
        youtube_url="https://youtube.com/legacy",
    )

    assert settings.registration_is_available is False
    assert settings.livestream_is_available is True
    assert settings.primary_youtube_url == "https://youtube.com/@cbnv"
