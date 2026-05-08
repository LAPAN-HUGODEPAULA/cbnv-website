import pytest
from django.utils import timezone
from accounts.models import User
from reviews.models import Review, ReviewerAssignment
from submissions.models import Submission, SubmissionAuthor, ThematicAxis


@pytest.fixture
def reviewer_a():
    return User.objects.create_user(
        username="rev_a", email="ra@test.com", password="pw",
        first_name="Revisor", last_name="Um", institution="UFMG",
        country="BR", is_reviewer=True,
    )


@pytest.fixture
def reviewer_b():
    return User.objects.create_user(
        username="rev_b", email="rb@test.com", password="pw",
        first_name="Revisor", last_name="Dois", institution="USP",
        country="BR", is_reviewer=True,
    )


@pytest.fixture
def author_user():
    return User.objects.create_user(
        username="author1", email="a@test.com", password="pw",
        first_name="Autor", last_name="Teste", institution="UFMG",
        country="BR", is_author=True,
    )


@pytest.fixture
def axis():
    return ThematicAxis.objects.create(name="Neurociência", order=1)


@pytest.fixture
def submissions_with_reviews(author_user, reviewer_a, reviewer_b, axis):
    s1 = Submission.objects.create(
        title="S1", abstract="R1.", keywords=["a", "b", "c"],
        thematic_axis=axis, submitter=author_user, status="under_review",
    )
    SubmissionAuthor.objects.create(
        submission=s1, first_name="Autor", last_name="Teste",
        email="a@test.com", institution="UFMG", is_corresponding=True,
    )
    a1 = ReviewerAssignment.objects.create(reviewer=reviewer_a, submission=s1)
    Review.objects.create(
        assignment=a1, recommendation="accept",
        comments="Bom trabalho.", submitted_at=timezone.now(),
    )
    a2 = ReviewerAssignment.objects.create(reviewer=reviewer_b, submission=s1)
    Review.objects.create(
        assignment=a2, recommendation="reject",
        comments="Precisa melhorar.", submitted_at=timezone.now(),
    )
    s2 = Submission.objects.create(
        title="S2", abstract="R2.", keywords=["d", "e", "f"],
        thematic_axis=axis, submitter=author_user, status="under_review",
    )
    SubmissionAuthor.objects.create(
        submission=s2, first_name="Autor", last_name="Teste",
        email="a@test.com", institution="UFMG", is_corresponding=True,
    )
    ReviewerAssignment.objects.create(reviewer=reviewer_a, submission=s2)
    return [s1, s2]


@pytest.mark.django_db
class TestReviewerAssignmentManager:
    def test_by_reviewer(self, submissions_with_reviews):
        result = list(ReviewerAssignment.objects.by_reviewer())
        assert len(result) == 2
        assert all("assigned" in r and "completed" in r for r in result)

    def test_by_reviewer_ordering(self, submissions_with_reviews):
        result = list(ReviewerAssignment.objects.by_reviewer())
        assert result[0]["completed"] >= result[1]["completed"]

    def test_completion_stats(self, submissions_with_reviews):
        stats = ReviewerAssignment.objects.completion_stats()
        assert stats["total_assigned"] == 3
        assert stats["completed"] == 2
        assert stats["pending"] == 1

    def test_top_reviewers(self, submissions_with_reviews):
        result = list(ReviewerAssignment.objects.top_reviewers(limit=1))
        assert len(result) == 1

    def test_export_queryset(self, submissions_with_reviews):
        qs = ReviewerAssignment.objects.export_queryset()
        assert qs.count() == 3


@pytest.mark.django_db
class TestReviewManager:
    def test_by_recommendation(self, submissions_with_reviews):
        result = list(Review.objects.by_recommendation())
        rec_map = {r["recommendation"]: r["count"] for r in result}
        assert rec_map["accept"] == 1
        assert rec_map["reject"] == 1

    def test_export_queryset(self, submissions_with_reviews):
        qs = Review.objects.export_queryset()
        assert qs.count() == 2
