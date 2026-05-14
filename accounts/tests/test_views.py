import pytest
from django.test import TestCase, Client
from django.urls import reverse

from accounts.models import User
from accounts.tests.factories import create_user_with_profile


class RegistrationTest(TestCase):
    def test_register_page_loads(self):
        response = self.client.get(reverse("accounts:register"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Criar conta")

    def test_successful_registration_creates_author(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "newauthor",
                "email": "author@example.com",
                "first_name": "Maria",
                "last_name": "Silva",
                "password1": "SecurePass123!",
                "password2": "SecurePass123!",
                "institution": "USP",
                "country": "BR",
                "position": "Graduanda",
                "consent_privacy": "on",
                "consent_image": "",
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username="newauthor")
        self.assertTrue(user.is_author)
        self.assertEqual(user.first_name, "Maria")
        self.assertEqual(user.get_full_name(), "Maria Silva")

    def test_registration_without_consents_fails(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "noconsent",
                "email": "noconsent@example.com",
                "first_name": "João",
                "last_name": "Costa",
                "password1": "SecurePass123!",
                "password2": "SecurePass123!",
                "institution": "UFF",
                "country": "BR",
                "position": "Professor",
                "consent_privacy": "",
                "consent_image": "",
            },
        )
        self.assertEqual(User.objects.filter(username="noconsent").count(), 0)
        self.assertEqual(response.status_code, 200)

    def test_registration_login_redirects_to_dashboard(self):
        self.client.post(
            reverse("accounts:register"),
            {
                "username": "autoauthor",
                "email": "auto@example.com",
                "first_name": "Ana",
                "last_name": "Paula",
                "password1": "SecurePass123!",
                "password2": "SecurePass123!",
                "institution": "UFMG",
                "country": "BR",
                "position": "Doutoranda",
                "consent_privacy": "on",
                "consent_image": "",
            },
            follow=True,
        )
        user = User.objects.get(username="autoauthor")
        response = self.client.get(reverse("dashboard:redirect"))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith("/painel/autor/"))


class DashboardAccessTest(TestCase):
    def setUp(self):
        self.author = create_user_with_profile(
            username="author", password="pass", is_author=True,
            first_name="Autor",
        )
        self.reviewer = create_user_with_profile(
            username="reviewer", password="pass", is_reviewer=True,
            first_name="Revisor",
        )
        self.chair = create_user_with_profile(
            username="chair", password="pass", is_chair=True,
            first_name="Comissão",
        )

    def test_dashboard_redirect_for_author(self):
        self.client.login(username="author", password="pass")
        response = self.client.get(reverse("dashboard:redirect"))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith("/painel/autor/"))

    def test_dashboard_redirect_for_reviewer(self):
        self.client.login(username="reviewer", password="pass")
        response = self.client.get(reverse("dashboard:redirect"))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith("/painel/revisor/"))

    def test_dashboard_redirect_for_chair(self):
        self.client.login(username="chair", password="pass")
        response = self.client.get(reverse("dashboard:redirect"))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.endswith("/painel/comissao/"))

    def test_redirect_to_login_when_anonymous(self):
        response = self.client.get(reverse("dashboard:redirect"))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith("/conta/entrar/"))

    def test_author_cannot_access_reviewer_dashboard(self):
        self.client.login(username="author", password="pass")
        response = self.client.get(reverse("dashboard:reviewer"))
        self.assertEqual(response.status_code, 302)

    def test_reviewer_cannot_access_chair_dashboard(self):
        self.client.login(username="reviewer", password="pass")
        response = self.client.get(reverse("dashboard:chair"))
        self.assertEqual(response.status_code, 302)

    def test_chair_can_access_all_dashboards(self):
        chair_multi = create_user_with_profile(
            username="chair_all", password="pass",
            is_chair=True, is_reviewer=True, is_author=True,
            first_name="Chair", last_name="User",
            institution="LAPAN", country="BR",
        )
        self.client.login(username="chair_all", password="pass")
        response = self.client.get(reverse("dashboard:author"))
        self.assertEqual(response.status_code, 200)
        
        # Now these redirect to scientific workflow views
        response = self.client.get(reverse("dashboard:reviewer"))
        self.assertEqual(response.status_code, 302)
        
        response = self.client.get(reverse("dashboard:chair"))
        self.assertEqual(response.status_code, 302)

    def test_login_view_loads(self):
        response = self.client.get(reverse("accounts:login"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Entrar")

    def test_successful_login(self):
        response = self.client.post(
            reverse("accounts:login"),
            {"username": "author", "password": "pass"},
        )
        self.assertEqual(response.status_code, 302)

    def test_profile_edit_requires_login(self):
        response = self.client.get(reverse("accounts:profile_edit"))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith("/conta/entrar/"))

    def test_profile_edit_for_author(self):
        self.client.login(username="author", password="pass")
        response = self.client.get(reverse("accounts:profile_edit"))
        self.assertEqual(response.status_code, 200)


@pytest.mark.django_db
class TestHasCompleteAuthorProfile:
    def test_complete_profile(self):
        user = create_user_with_profile(
            username="complete", password="p",
            first_name="João", last_name="Silva",
            institution="UFMG", country="BR", is_author=True,
        )
        assert user.has_complete_author_profile is True

    def test_missing_first_name(self):
        user = create_user_with_profile(
            username="mfn", password="p",
            last_name="Silva", institution="UFMG", country="BR", is_author=True,
        )
        assert user.has_complete_author_profile is False

    def test_missing_last_name(self):
        user = create_user_with_profile(
            username="mln", password="p",
            first_name="João", institution="UFMG", country="BR", is_author=True,
        )
        assert user.has_complete_author_profile is False

    def test_missing_institution(self):
        user = create_user_with_profile(
            username="minst", password="p",
            first_name="João", last_name="Silva", country="BR", is_author=True,
        )
        assert user.has_complete_author_profile is False

    def test_missing_country(self):
        user = create_user_with_profile(
            username="mcountry", password="p",
            first_name="João", last_name="Silva", institution="UFMG", is_author=True,
        )
        assert user.has_complete_author_profile is False

    def test_whitespace_only_fails(self):
        user = create_user_with_profile(
            username="ws", password="p",
            first_name="   ", last_name="   ",
            institution="   ", country="   ", is_author=True,
        )
        assert user.has_complete_author_profile is False


@pytest.mark.django_db
class TestProfileCompletenessRedirect:
    def test_dashboard_redirects_incomplete(self):
        user = create_user_with_profile(
            username="incomplete", password="p", is_author=True,
        )
        client = Client()
        client.force_login(user)
        response = client.get("/painel/autor/")
        assert response.status_code == 302
        assert response.url == "/conta/perfil/"

    def test_dashboard_allows_complete(self):
        user = create_user_with_profile(
            username="complete2", password="p",
            first_name="João", last_name="Silva",
            institution="UFMG", country="BR", is_author=True,
        )
        client = Client()
        client.force_login(user)
        response = client.get("/painel/autor/")
        assert response.status_code == 200
