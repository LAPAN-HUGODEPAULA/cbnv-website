import pytest
from django.test import Client
from django.urls import reverse

from accounts.models import User


@pytest.fixture
def chair_user():
    return User.objects.create_user(
        username="chair1", email="chair@test.com", password="pw",
        first_name="Maria", last_name="Silva", institution="UFMG",
        country="BR", is_chair=True,
    )


@pytest.fixture
def staff_user():
    return User.objects.create_user(
        username="staff1", email="staff@test.com", password="pw",
        first_name="Admin", last_name="Teste", institution="UFMG",
        country="BR", is_staff=True,
    )


@pytest.fixture
def author_user():
    return User.objects.create_user(
        username="author1", email="author@test.com", password="pw",
        first_name="João", last_name="Costa", institution="USP",
        country="BR", is_author=True,
    )


@pytest.fixture
def reviewer_user():
    return User.objects.create_user(
        username="rev1", email="rev@test.com", password="pw",
        first_name="Ana", last_name="Revisora", institution="UNICAMP",
        country="BR", is_reviewer=True,
    )


REPORTS_URLS = [
    "reports:dashboard",
    "reports:export_indicators",
    "reports:export_submissions",
    "reports:export_reviews",
    "reports:export_proceedings",
    "reports:export_authors",
]


@pytest.mark.django_db
class TestReportPermissions:
    def test_author_gets_403(self, client, author_user):
        client.login(username="author1", password="pw")
        for url_name in REPORTS_URLS:
            response = client.get(reverse(url_name))
            assert response.status_code == 403, f"{url_name} should return 403 for author"

    def test_reviewer_gets_403(self, client, reviewer_user):
        client.login(username="rev1", password="pw")
        for url_name in REPORTS_URLS:
            response = client.get(reverse(url_name))
            assert response.status_code == 403, f"{url_name} should return 403 for reviewer"

    def test_chair_can_access(self, client, chair_user):
        client.login(username="chair1", password="pw")
        for url_name in REPORTS_URLS:
            response = client.get(reverse(url_name))
            assert response.status_code == 200, f"{url_name} should return 200 for chair"

    def test_staff_can_access(self, client, staff_user):
        client.login(username="staff1", password="pw")
        for url_name in REPORTS_URLS:
            response = client.get(reverse(url_name))
            assert response.status_code == 200, f"{url_name} should return 200 for staff"

    def test_unauthenticated_gets_redirect(self, client):
        for url_name in REPORTS_URLS:
            response = client.get(reverse(url_name))
            assert response.status_code in (302, 403), f"{url_name} should redirect or 403"


@pytest.mark.django_db
class TestCSVExport:
    @pytest.fixture(autouse=True)
    def setup(self, chair_user):
        self.client = Client()
        self.client.login(username="chair1", password="pw")

    def test_indicators_csv_has_header(self):
        resp = self.client.get(reverse("reports:export_indicators"), {"format": "csv"})
        assert resp.status_code == 200
        assert resp["Content-Type"].startswith("text/csv")
        lines = resp.content.decode("utf-8-sig").strip().split("\n")
        assert "tipo" in lines[0]

    def test_submissions_csv_has_header(self):
        resp = self.client.get(reverse("reports:export_submissions"), {"format": "csv"})
        assert resp.status_code == 200
        assert b"ID" in resp.content

    def test_reviews_csv_has_header(self):
        resp = self.client.get(reverse("reports:export_reviews"), {"format": "csv"})
        assert resp.status_code == 200
        assert b"Revisor" in resp.content

    def test_proceedings_csv_has_header(self):
        resp = self.client.get(reverse("reports:export_proceedings"), {"format": "csv"})
        assert resp.status_code == 200
        assert b"Submiss" in resp.content

    def test_authors_csv_has_header(self):
        resp = self.client.get(reverse("reports:export_authors"), {"format": "csv"})
        assert resp.status_code == 200
        assert b"Nome" in resp.content

    def test_submissions_csv_empty_no_500(self):
        resp = self.client.get(reverse("reports:export_submissions"), {"format": "csv"})
        assert resp.status_code == 200
        lines = resp.content.decode("utf-8-sig").strip().split("\n")
        assert len(lines) == 1  # header only

    def test_submissions_csv_with_status_filter(self):
        resp = self.client.get(
            reverse("reports:export_submissions"),
            {"format": "csv", "status": "accepted_oral"},
        )
        assert resp.status_code == 200


@pytest.mark.django_db
class TestJSONExport:
    @pytest.fixture(autouse=True)
    def setup(self, chair_user):
        self.client = Client()
        self.client.login(username="chair1", password="pw")

    def test_indicators_json_structure(self):
        import json

        resp = self.client.get(reverse("reports:export_indicators"), {"format": "json"})
        assert resp.status_code == 200
        data = json.loads(resp.content)
        assert "resumo_geral" in data
        assert "revisoes" in data
        assert "autores_e_instituicoes" in data
        assert "materiais" in data

    def test_submissions_json_is_list(self):
        import json

        resp = self.client.get(reverse("reports:export_submissions"), {"format": "json"})
        assert resp.status_code == 200
        data = json.loads(resp.content)
        assert isinstance(data, list)

    def test_reviews_json_is_list(self):
        import json

        resp = self.client.get(reverse("reports:export_reviews"), {"format": "json"})
        assert resp.status_code == 200
        data = json.loads(resp.content)
        assert isinstance(data, list)

    def test_empty_json_no_500(self):
        import json

        resp = self.client.get(reverse("reports:export_submissions"), {"format": "json"})
        assert resp.status_code == 200
        data = json.loads(resp.content)
        assert isinstance(data, list)
        assert len(data) == 0


@pytest.mark.django_db
class TestAggregateConsistency:
    def test_indicators_counts_match_manual(self, client, chair_user):
        from submissions.models import Submission, SubmissionAuthor, ThematicAxis
        from accounts.models import User

        axis = ThematicAxis.objects.create(name="Teste", order=1)
        user = User.objects.create_user(
            username="sub1", email="sub@test.com", password="pw",
            first_name="Sub", last_name="Teste", institution="UFMG",
            country="BR", is_author=True,
        )

        for i in range(3):
            s = Submission.objects.create(
                title=f"Sub {i}", abstract=f"Resumo {i}.",
                keywords=["a", "b", "c"], thematic_axis=axis,
                submitter=user, status="draft",
            )
            SubmissionAuthor.objects.create(
                submission=s, first_name="Autor", last_name=f"{i}",
                email=f"a{i}@test.com", institution="UFMG",
            )

        client.login(username="chair1", password="pw")
        resp = client.get(reverse("reports:export_indicators"), {"format": "json"})
        import json

        data = json.loads(resp.content)
        assert data["resumo_geral"]["total_submissoes"] == 3
        assert data["resumo_geral"]["por_status"]["draft"] == 3
        assert data["autores_e_instituicoes"]["total_autores"] == 3
