import pytest
from accounts.models import User
from accounts.tests.factories import create_user_with_profile
from submissions.models import Submission, SubmissionAuthor, ThematicAxis


@pytest.fixture
def axis_a():
    return ThematicAxis.objects.create(name="Neurociência", order=1)


@pytest.fixture
def axis_b():
    return ThematicAxis.objects.create(name="Oftalmologia", order=2)


@pytest.fixture
def user_a():
    return create_user_with_profile(
        username="user_a", email="a@test.com", password="pw",
        first_name="Ana", last_name="Silva", institution="UFMG",
        country="BR", is_author=True,
    )


@pytest.fixture
def user_b():
    return create_user_with_profile(
        username="user_b", email="b@test.com", password="pw",
        first_name="Bia", last_name="Costa", institution="USP",
        country="BR", is_author=True,
    )


@pytest.fixture
def submissions_bulk(user_a, user_b, axis_a, axis_b):
    s1 = Submission.objects.create(
        title="S1", abstract="Resumo 1.", keywords=["a", "b", "c"],
        thematic_axis=axis_a, submitter=user_a, status="accepted_oral",
        final_modality="oral",
    )
    SubmissionAuthor.objects.create(
        submission=s1, first_name="Ana", last_name="Silva",
        email="ana@test.com", institution="UFMG", is_corresponding=True,
    )
    s2 = Submission.objects.create(
        title="S2", abstract="Resumo 2.", keywords=["d", "e", "f"],
        thematic_axis=axis_a, submitter=user_a, status="rejected",
    )
    SubmissionAuthor.objects.create(
        submission=s2, first_name="Bia", last_name="Costa",
        email="bia@test.com", institution="USP", is_corresponding=True,
    )
    s3 = Submission.objects.create(
        title="S3", abstract="Resumo 3.", keywords=["g", "h", "i"],
        thematic_axis=axis_b, submitter=user_b, status="accepted_poster",
        final_modality="poster",
    )
    SubmissionAuthor.objects.create(
        submission=s3, first_name="Ana", last_name="Silva",
        email="ana@test.com", institution="UFMG", is_corresponding=True,
    )
    return [s1, s2, s3]


@pytest.mark.django_db
class TestSubmissionManager:
    def test_by_status(self, submissions_bulk):
        result = list(Submission.objects.by_status())
        status_map = {r["status"]: r["count"] for r in result}
        assert status_map["accepted_oral"] == 1
        assert status_map["rejected"] == 1
        assert status_map["accepted_poster"] == 1

    def test_by_status_ordered_by_count(self, submissions_bulk):
        result = list(Submission.objects.by_status())
        counts = [r["count"] for r in result]
        assert counts == sorted(counts, reverse=True)

    def test_by_topic(self, submissions_bulk):
        result = list(Submission.objects.by_topic())
        topic_map = {r["thematic_axis__name"]: r["count"] for r in result}
        assert topic_map["Neurociência"] == 2
        assert topic_map["Oftalmologia"] == 1

    def test_by_modality(self, submissions_bulk):
        result = list(Submission.objects.by_modality())
        mod_map = {r["final_modality"]: r["count"] for r in result}
        assert mod_map["oral"] == 1
        assert mod_map["poster"] == 1

    def test_by_institution(self, submissions_bulk):
        result = list(Submission.objects.by_institution())
        inst_map = {r["authors__institution"]: r["count"] for r in result}
        assert inst_map["UFMG"] == 2
        assert inst_map["USP"] == 1

    def test_summary_stats(self, submissions_bulk):
        stats = Submission.objects.summary_stats()
        assert stats["total"] == 3
        assert "by_status" in stats
        assert stats["first_created"] is not None
        assert stats["last_created"] is not None

    def test_export_queryset_no_filters(self, submissions_bulk):
        qs = Submission.objects.export_queryset()
        assert qs.count() == 3

    def test_export_queryset_with_filters(self, submissions_bulk):
        qs = Submission.objects.export_queryset(
            filters={"status": "accepted_oral"}
        )
        assert qs.count() == 1
        assert qs.first().status == "accepted_oral"
