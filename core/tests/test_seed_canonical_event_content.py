import pytest
from django.core.management import call_command
from wagtail.models import Site

from core.models import CoreSettings
from sponsors.models import Sponsor, SponsorTier


@pytest.mark.django_db
def test_seed_canonical_event_content_creates_settings_if_missing():
    site = Site.objects.get(is_default_site=True)
    CoreSettings.objects.filter(site=site).delete()

    call_command("seed_canonical_event_content")

    settings = CoreSettings.for_site(site)
    assert settings.event_name == "XII Congresso Brasileiro de Neurociências da Visão"
    assert settings.short_event_name == "CBNV 2026"
    assert settings.edition == "XII"
    assert settings.theme == "Neurovisão na Era da Inteligência Artificial"
    assert settings.start_date.isoformat() == "2026-11-11"
    assert settings.end_date.isoformat() == "2026-11-13"
    assert settings.format_label == "Presencial com transmissão híbrida"
    assert settings.city == "Belo Horizonte"
    assert settings.state == "Minas Gerais"
    assert settings.country == "Brasil"
    assert settings.venue_name == "Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha"
    assert settings.venue_short_name == "CAD-1/UFMG"
    assert "R. Prof. Baeta Viana" in settings.location
    assert settings.google_maps_url == "https://maps.app.goo.gl/xzqJ2LCAHVP4hsFp6"
    assert "FAPEMIG" in settings.fapemig_text
    assert settings.default_seo_title


@pytest.mark.django_db
def test_seed_canonical_event_content_updates_canonical_fields_and_preserves_protected_text():
    site = Site.objects.get(is_default_site=True)
    settings = CoreSettings.for_site(site)
    settings.event_name = "Old event name"
    settings.fapemig_text = "Manual FAPEMIG text."
    settings.default_seo_description = "Manual SEO description."
    settings.save()

    call_command("seed_canonical_event_content")

    settings.refresh_from_db()
    assert settings.event_name == "XII Congresso Brasileiro de Neurociências da Visão"
    assert settings.fapemig_text == "Manual FAPEMIG text."
    assert settings.default_seo_description == "Manual SEO description."


@pytest.mark.django_db
def test_seed_canonical_event_content_force_updates_protected_text():
    site = Site.objects.get(is_default_site=True)
    settings = CoreSettings.for_site(site)
    settings.fapemig_text = "Manual FAPEMIG text."
    settings.save()

    call_command("seed_canonical_event_content", "--force")

    settings.refresh_from_db()
    assert settings.fapemig_text.startswith("Apoio institucional: FAPEMIG")


@pytest.mark.django_db
def test_seed_canonical_event_content_creates_supporting_entities_once():
    call_command("seed_canonical_event_content")
    call_command("seed_canonical_event_content")

    expected_names = {
        "UFMG",
        "FUNDEP",
        "FAPEMIG",
        "Sociedade Brasileira de Neurovisão",
        "Hospital de Olhos de Minas Gerais / HOLHOS",
        "UFRJ",
        "USP",
        "UFRN",
        "UEMG",
    }

    assert SponsorTier.objects.filter(slug="apoio-institucional-e-cientifico").count() == 1
    assert set(Sponsor.objects.filter(name__in=expected_names).values_list("name", flat=True)) == expected_names
    for name in expected_names:
        assert Sponsor.objects.filter(name=name).count() == 1

    fapemig = Sponsor.objects.get(name="FAPEMIG")
    assert fapemig.category == Sponsor.Category.FUNDING_AGENCY
    assert fapemig.status == Sponsor.Status.ACTIVE
    assert fapemig.show_in_footer is True


@pytest.mark.django_db
def test_seed_canonical_event_content_uses_coming_soon_for_unknown_links():
    site = Site.objects.get(is_default_site=True)
    settings = CoreSettings.for_site(site)
    settings.registration_link = ""
    settings.registration_status = CoreSettings.LinkStatus.AVAILABLE
    settings.livestream_link = ""
    settings.livestream_status = CoreSettings.LinkStatus.AVAILABLE
    settings.save()

    call_command("seed_canonical_event_content")

    settings.refresh_from_db()
    assert settings.registration_link == ""
    assert settings.registration_status == CoreSettings.LinkStatus.COMING_SOON
    assert settings.livestream_link == ""
    assert settings.livestream_status == CoreSettings.LinkStatus.COMING_SOON


@pytest.mark.django_db
def test_seed_canonical_event_content_preserves_known_external_links():
    site = Site.objects.get(is_default_site=True)
    settings = CoreSettings.for_site(site)
    settings.registration_link = "https://example.com/inscricoes"
    settings.registration_status = CoreSettings.LinkStatus.AVAILABLE
    settings.save()

    call_command("seed_canonical_event_content")

    settings.refresh_from_db()
    assert settings.registration_link == "https://example.com/inscricoes"
    assert settings.registration_status == CoreSettings.LinkStatus.AVAILABLE


@pytest.mark.django_db
def test_seed_canonical_event_content_outputs_summary(capsys):
    call_command("seed_canonical_event_content")

    output = capsys.readouterr().out
    assert "Seed canonical event content" in output
    assert "Settings:" in output
    assert "Supporting entities:" in output
    assert "Announcements: skipped" in output
    assert "Done" in output
