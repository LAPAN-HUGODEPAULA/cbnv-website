import pytest
from django.test import Client
from wagtail.models import Site
from core.models import CoreSettings
from accounts.tests.factories import create_user_with_profile

@pytest.fixture
def author_user(db):
    return create_user_with_profile(
        username="author",
        email="author@example.com",
        password="testpass123",
        first_name="João",
        last_name="Silva",
        institution="UFMG",
        country="BR",
        is_author=True,
    )

@pytest.fixture
def core_settings(db):
    site = Site.objects.get(is_default_site=True)
    settings = CoreSettings.for_site(site)
    return settings

class TestSubmissionWindow:
    def test_dashboard_shows_button_when_open(self, db, author_user, core_settings):
        core_settings.submissions_status = "available"
        core_settings.save()
        
        client = Client()
        client.force_login(author_user)
        response = client.get("/painel/autor/")
        
        assert response.status_code == 200
        # The "Nova submissão" button should be present
        assert "Nova submissão" in response.content.decode()
        assert "Começar submissão" in response.content.decode()

    def test_dashboard_hides_button_when_closed(self, db, author_user, core_settings):
        core_settings.submissions_status = "unavailable"
        core_settings.save()
        
        client = Client()
        client.force_login(author_user)
        response = client.get("/painel/autor/")
        
        assert response.status_code == 200
        # The "Nova submissão" button should NOT be present
        assert "Nova submissão" not in response.content.decode()
        assert "Começar submissão" not in response.content.decode()
        assert "A criação de novas submissões será liberada" in response.content.decode()

    def test_dashboard_hides_button_when_coming_soon(self, db, author_user, core_settings):
        core_settings.submissions_status = "coming_soon"
        core_settings.save()
        
        client = Client()
        client.force_login(author_user)
        response = client.get("/painel/autor/")
        
        assert response.status_code == 200
        assert "Nova submissão" not in response.content.decode()
        assert "Começar submissão" not in response.content.decode()
