import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client
from django.urls import reverse

from accounts.models import User
from accounts.tests.factories import create_user_with_profile
from submissions.models import Submission, SubmissionFile, ThematicAxis


@pytest.fixture
def db_setup(db):
    axis = ThematicAxis.objects.create(name="Neurociência da Visão", order=1)
    user = create_user_with_profile(
        username="author",
        email="author@example.com",
        password="testpass123",
        first_name="João",
        last_name="Silva",
        institution="UFMG",
        country="BR",
        is_author=True,
    )
    return user, axis


@pytest.fixture
def auth_client(db_setup):
    client = Client()
    user, _ = db_setup
    client.force_login(user)
    return client, user


@pytest.fixture
def incomplete_user(db):
    return create_user_with_profile(
        username="incomplete",
        email="incomplete@example.com",
        password="testpass123",
        is_author=True,
    )


class TestDashboardAccess:
    def test_author_sees_dashboard(self, auth_client):
        client, user = auth_client
        response = client.get("/painel/autor/")
        assert response.status_code == 200

    def test_incomplete_profile_redirects(self, db, incomplete_user):
        client = Client()
        client.force_login(incomplete_user)
        response = client.get("/painel/autor/")
        assert response.status_code == 302
        assert response.url == "/conta/perfil/editar/"

    def test_non_author_redirected(self, db):
        user = create_user_with_profile(
            username="staff", password="p", is_staff=True,
        )
        client = Client()
        client.force_login(user)
        response = client.get("/painel/autor/")
        assert response.status_code == 302

    def test_dashboard_lists_submissions(self, auth_client, db_setup):
        client, user = auth_client
        _, axis = db_setup
        Submission.objects.create(
            title="Trabalho 1", abstract="R.", keywords=["a", "b", "c"],
            thematic_axis=axis, submitter=user,
        )
        response = client.get("/painel/autor/")
        assert response.status_code == 200
        assert "Trabalho 1" in response.content.decode()


class TestWizardAccess:
    def test_anonymous_redirected_to_login(self, db):
        client = Client()
        response = client.get(reverse("submissions:wizard_step1"))
        assert response.status_code == 302
        assert "/conta/entrar/" in response.url

    def test_incomplete_profile_redirected(self, db, incomplete_user):
        client = Client()
        client.force_login(incomplete_user)
        response = client.get(reverse("submissions:wizard_step1"))
        assert response.status_code == 302
        assert response.url == "/conta/perfil/editar/"

    def test_author_can_access_wizard(self, auth_client):
        client, _ = auth_client
        response = client.get(reverse("submissions:wizard_step1"))
        assert response.status_code == 200


class TestWizardFlow:
    def test_step1_creates_draft(self, auth_client, db_setup):
        client, user = auth_client
        _, axis = db_setup
        response = client.post(
            reverse("submissions:wizard_step1"),
            {
                "title": "Teste de Submissão",
                "abstract": "Resumo do trabalho de teste.",
                "thematic_axis": axis.pk,
                "keywords_input": "neurociência, visão, percepção",
                "authors-TOTAL_FORMS": "1",
                "authors-INITIAL_FORMS": "0",
                "authors-MIN_NUM_FORMS": "1",
                "authors-0-first_name": "João",
                "authors-0-last_name": "Silva",
                "authors-0-email": "author@example.com",
                "authors-0-institution": "UFMG",
                "authors-0-order": "1",
                "authors-0-is_corresponding": "on",
            },
            follow=False,
        )
        assert response.status_code == 302
        assert Submission.objects.count() == 1
        assert Submission.objects.first().status == "draft"

    def test_step1_redirects_to_step2(self, auth_client, db_setup):
        client, user = auth_client
        _, axis = db_setup
        response = client.post(
            reverse("submissions:wizard_step1"),
            {
                "title": "Teste",
                "abstract": "Resumo.",
                "thematic_axis": axis.pk,
                "keywords_input": "a, b, c",
                "authors-TOTAL_FORMS": "1",
                "authors-INITIAL_FORMS": "0",
                "authors-MIN_NUM_FORMS": "1",
                "authors-0-first_name": "J",
                "authors-0-last_name": "S",
                "authors-0-email": "j@s.com",
                "authors-0-institution": "UFMG",
                "authors-0-order": "1",
                "authors-0-is_corresponding": "on",
            },
            follow=False,
        )
        assert "passo-2" in response.url

    def test_step2_upload_pdf(self, auth_client, db_setup):
        client, user = auth_client
        _, axis = db_setup
        sub = Submission.objects.create(
            title="T", abstract="R.", keywords=["a", "b", "c"],
            thematic_axis=axis, submitter=user,
        )
        pdf = SimpleUploadedFile("test.pdf", b"%PDF-1.4 fake")
        response = client.post(
            reverse("submissions:wizard_step2", args=[sub.pk]),
            {"file": pdf},
            follow=False,
        )
        assert response.status_code == 302
        assert "passo-3" in response.url
        assert SubmissionFile.objects.count() == 1

    def test_step2_rejects_non_pdf(self, auth_client, db_setup):
        client, user = auth_client
        _, axis = db_setup
        sub = Submission.objects.create(
            title="T", abstract="R.", keywords=["a", "b", "c"],
            thematic_axis=axis, submitter=user,
        )
        txt = SimpleUploadedFile("test.txt", b"not a pdf")
        response = client.post(
            reverse("submissions:wizard_step2", args=[sub.pk]),
            {"file": txt},
        )
        assert response.status_code == 200

    def test_step3_submit_changes_status(self, auth_client, db_setup):
        client, user = auth_client
        _, axis = db_setup
        sub = Submission.objects.create(
            title="T", abstract="R.", keywords=["a", "b", "c"],
            thematic_axis=axis, submitter=user,
        )
        response = client.post(
            reverse("submissions:wizard_step3", args=[sub.pk]),
        )
        assert response.status_code == 302
        sub.refresh_from_db()
        assert sub.status == "submitted"


class TestSecureFileDownload:
    def test_owner_can_download(self, auth_client, db_setup):
        client, user = auth_client
        _, axis = db_setup
        sub = Submission.objects.create(
            title="T", abstract="R.", keywords=["a", "b", "c"],
            thematic_axis=axis, submitter=user,
        )
        pdf = SimpleUploadedFile("test.pdf", b"%PDF-1.4 fake content")
        sf = SubmissionFile.objects.create(submission=sub, file=pdf)
        response = client.get(
            reverse("submissions:download_file", args=[sf.pk])
        )
        assert response.status_code == 200
        assert response.get("Content-Disposition") is not None

    def test_non_owner_forbidden(self, db_setup):
        user1, axis = db_setup
        user2 = create_user_with_profile(
            username="other", password="p", is_author=True,
            first_name="Outro", last_name="User",
            institution="X", country="BR",
        )
        sub = Submission.objects.create(
            title="T", abstract="R.", keywords=["a", "b", "c"],
            thematic_axis=axis, submitter=user1,
        )
        pdf = SimpleUploadedFile("test.pdf", b"%PDF-1.4")
        sf = SubmissionFile.objects.create(submission=sub, file=pdf)
        client = Client()
        client.force_login(user2)
        response = client.get(
            reverse("submissions:download_file", args=[sf.pk])
        )
        assert response.status_code == 403

    def test_anonymous_forbidden(self, db_setup):
        user, axis = db_setup
        sub = Submission.objects.create(
            title="T", abstract="R.", keywords=["a", "b", "c"],
            thematic_axis=axis, submitter=user,
        )
        pdf = SimpleUploadedFile("test.pdf", b"%PDF-1.4")
        sf = SubmissionFile.objects.create(submission=sub, file=pdf)
        client = Client()
        response = client.get(
            reverse("submissions:download_file", args=[sf.pk])
        )
        assert response.status_code == 302
