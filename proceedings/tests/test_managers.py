import pytest
from accounts.models import User
from proceedings.models import FinalMaterial
from submissions.models import Submission, SubmissionAuthor, ThematicAxis


@pytest.fixture
def axis():
    return ThematicAxis.objects.create(name="Neurociência", order=1)


@pytest.fixture
def user():
    return User.objects.create_user(
        username="author1", email="a@test.com", password="pw",
        first_name="Autor", last_name="Teste", institution="UFMG",
        country="BR", is_author=True,
    )


@pytest.fixture
def accepted_submissions(user, axis):
    s1 = Submission.objects.create(
        title="S1", abstract="R1.", keywords=["a", "b", "c"],
        thematic_axis=axis, submitter=user, status="accepted_oral",
        final_modality="oral",
    )
    SubmissionAuthor.objects.create(
        submission=s1, first_name="Autor", last_name="Teste",
        email="a@test.com", institution="UFMG", is_corresponding=True,
    )
    s2 = Submission.objects.create(
        title="S2", abstract="R2.", keywords=["d", "e", "f"],
        thematic_axis=axis, submitter=user, status="accepted_poster",
        final_modality="poster",
    )
    SubmissionAuthor.objects.create(
        submission=s2, first_name="Autor", last_name="Teste",
        email="a@test.com", institution="UFMG", is_corresponding=True,
    )
    s3 = Submission.objects.create(
        title="S3", abstract="R3.", keywords=["g", "h", "i"],
        thematic_axis=axis, submitter=user, status="published_in_proceedings",
    )
    SubmissionAuthor.objects.create(
        submission=s3, first_name="Autor", last_name="Teste",
        email="a@test.com", institution="UFMG", is_corresponding=True,
    )
    return [s1, s2, s3]


@pytest.mark.django_db
class TestFinalMaterialManager:
    def test_materials_status_empty(self, accepted_submissions):
        status = FinalMaterial.objects.materials_status()
        assert status["total_accepted"] == 3
        assert status["with_materials"] == 0
        assert status["pending_materials"] == 3
        assert status["published"] == 1

    def test_materials_status_with_materials(self, accepted_submissions):
        from django.utils import timezone
        FinalMaterial.objects.create(
            submission=accepted_submissions[0],
            video_url="https://youtube.com/watch?v=abc123",
            received_at=timezone.now(),
        )
        status = FinalMaterial.objects.materials_status()
        assert status["with_materials"] == 1
        assert status["pending_materials"] == 2
        assert status["with_video"] == 1

    def test_export_queryset(self, accepted_submissions):
        from django.utils import timezone
        FinalMaterial.objects.create(
            submission=accepted_submissions[0],
            video_url="https://youtube.com/watch?v=abc123",
            received_at=timezone.now(),
        )
        qs = FinalMaterial.objects.export_queryset()
        assert qs.count() == 1
