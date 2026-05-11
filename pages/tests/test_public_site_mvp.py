from datetime import date, time

import pytest
from django.utils import timezone
from wagtail.models import Page, Site

from core.models import CoreSettings
from pages.models import (
    AboutPage,
    Announcement,
    ContactPage,
    HomePage,
    PreviousEditionsPage,
    ProgramPage,
    RegistrationPage,
    SpeakerIndexPage,
    SponsorsPage,
    SubmissionsPage,
)
from program.models import BREAK, CONFIRMED, HIDDEN, PUBLISHED, TALK, ProgramDay, ProgramSession, ProgramTalk, Speaker
from sponsors.models import Sponsor, SponsorTier


@pytest.fixture
def public_site(db):
    root = Page.objects.get(id=1)
    for child in root.get_children():
        child.delete()
    Site.objects.all().delete()

    home = HomePage(title="Home", slug="home", intro="Página pública do CBNV 2026.")
    root.add_child(instance=home)
    home.refresh_from_db()

    site = Site.objects.create(hostname="localhost", port=80, root_page=home, is_default_site=True)
    settings = CoreSettings.for_site(site)
    settings.event_name = "CBNV 2026"
    settings.short_event_name = "CBNV 2026"
    settings.theme = "Neurovisão na Era da Inteligência Artificial"
    settings.dates = "11 a 13 de novembro de 2026"
    settings.location = "CAD-1 — UFMG, Belo Horizonte, MG"
    settings.venue_name = "Centro de Atividades Didáticas 1 da UFMG"
    settings.venue_short_name = "CAD-1/UFMG"
    settings.venue_address = "Av. Antônio Carlos, 6627\nPampulha"
    settings.city = "Belo Horizonte"
    settings.state = "Minas Gerais"
    settings.country = "Brasil"
    settings.contact_email = "contato@cbnv.org.br"
    settings.submissions_contact_email = "submissoes@cbnv.org.br"
    settings.sponsorship_contact_email = "apoio@cbnv.org.br"
    settings.registration_status = CoreSettings.LinkStatus.COMING_SOON
    settings.registration_link = ""
    settings.google_maps_url = "https://maps.google.com/?q=CAD-1+UFMG"
    settings.save()

    pages = {
        "home": home,
        "about": AboutPage(title="Sobre", slug="sobre"),
        "program": ProgramPage(title="Programação", slug="programacao", intro="Agenda pública."),
        "speakers": SpeakerIndexPage(title="Palestrantes", slug="palestrantes"),
        "submissions": SubmissionsPage(title="Submissões", slug="submissoes"),
        "registration": RegistrationPage(title="Inscrição", slug="inscricao"),
        "sponsors": SponsorsPage(title="Patrocínio", slug="patrocinadores"),
        "previous": PreviousEditionsPage(title="Edições Anteriores", slug="edicoes-anteriores"),
        "contact": ContactPage(title="Contato", slug="contato"),
    }
    for key, page in pages.items():
        if key != "home":
            home.add_child(instance=page)
            page.refresh_from_db()

    return pages


@pytest.mark.django_db
def test_required_public_pages_render(client, public_site):
    for page in public_site.values():
        response = client.get(page.url)

        assert response.status_code == 200, page.title


@pytest.mark.django_db
def test_home_renders_settings_announcements_program_and_sponsors(client, public_site):
    Announcement.objects.create(
        title="Chamada pública aberta",
        slug="chamada-publica-aberta",
        summary="Primeiro comunicado público.",
        status=Announcement.Status.PUBLISHED,
        published_at=timezone.now(),
        featured_on_home=True,
    )
    day = ProgramDay.objects.create(date=date(2026, 11, 11), title="Dia 1")
    ProgramSession.objects.create(
        day=day,
        start_time=time(9),
        end_time=time(10),
        title="Credenciamento",
        activity_type=BREAK,
        status=PUBLISHED,
    )
    tier = SponsorTier.objects.create(name="Apoio", slug="apoio")
    Sponsor.objects.create(
        name="Universidade Federal de Minas Gerais",
        category=Sponsor.Category.ORGANIZING_INSTITUTION,
        tier=tier,
        status=Sponsor.Status.ACTIVE,
        show_on_home=True,
    )

    response = client.get(public_site["home"].url)
    html = response.content.decode()

    assert "Neurovisão na Era da Inteligência Artificial" in html
    assert "CAD-1 — UFMG, Belo Horizonte, MG" in html
    assert "Chamada pública aberta" in html
    assert "Credenciamento" in html
    assert "Universidade Federal de Minas Gerais" in html
    assert "maior evento de Neurovisão da América Latina" not in html


@pytest.mark.django_db
def test_speakers_page_excludes_hidden_speakers(client, public_site):
    day = ProgramDay.objects.create(date=date(2026, 11, 11), title="Dia 1")
    session = ProgramSession.objects.create(
        day=day,
        start_time=time(10),
        end_time=time(11),
        title="Sessão pública",
        activity_type=TALK,
        status=PUBLISHED,
    )
    visible = Speaker.objects.create(name="Palestrante Confirmada", status=CONFIRMED, institution="UFMG")
    hidden = Speaker.objects.create(name="Palestrante Oculta", status=HIDDEN, institution="UFMG")
    ProgramTalk.objects.create(session=session, title="Palestra confirmada", speaker=visible, status=CONFIRMED)
    ProgramTalk.objects.create(session=session, title="Palestra oculta", speaker=hidden, status=CONFIRMED)

    response = client.get(public_site["speakers"].url)
    html = response.content.decode()

    assert "Palestrante Confirmada" in html
    assert "Palestra confirmada" in html
    assert "Palestrante Oculta" not in html
    assert "Palestra oculta" not in html


@pytest.mark.django_db
def test_registration_coming_soon_does_not_render_broken_link(client, public_site):
    response = client.get(public_site["registration"].url)
    html = response.content.decode()

    assert "Inscrição Em Breve" in html
    assert "Link Em Breve" in html
    assert 'href="#"' not in html


@pytest.mark.django_db
def test_submissions_page_states_initial_video_is_not_required(client, public_site):
    response = client.get(public_site["submissions"].url)
    html = response.content.decode()

    assert "A submissão inicial não requer vídeo" in html
    assert "Submissões Em Breve" in html


@pytest.mark.django_db
def test_contact_page_renders_current_venue_and_contact_channels(client, public_site):
    response = client.get(public_site["contact"].url)
    html = response.content.decode()

    assert "Centro de Atividades Didáticas 1 da UFMG" in html
    assert "Av. Antônio Carlos, 6627" in html
    assert "contato@cbnv.org.br" in html
    assert "submissoes@cbnv.org.br" in html
    assert "apoio@cbnv.org.br" in html
