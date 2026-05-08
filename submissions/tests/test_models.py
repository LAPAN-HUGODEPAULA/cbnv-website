import pytest
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

from accounts.models import User
from accounts.tests.factories import create_user_with_profile
from submissions.models import (
    IllegalStateTransitionError,
    Submission,
    SubmissionAuthor,
    SubmissionFile,
    ThematicAxis,
)


@pytest.fixture
def thematic_axis():
    return ThematicAxis.objects.create(name="Neurociência da Visão", order=1)


@pytest.fixture
def author_user():
    return create_user_with_profile(
        username="author1",
        email="author@example.com",
        password="testpass123",
        first_name="João",
        last_name="Silva",
        institution="UFMG",
        country="BR",
        is_author=True,
    )


@pytest.fixture
def submission(author_user, thematic_axis):
    return Submission.objects.create(
        title="Estudo sobre visão",
        abstract="Resumo do estudo sobre neurociência da visão.",
        keywords=["neurociência", "visão", "percepção"],
        thematic_axis=thematic_axis,
        submitter=author_user,
    )


@pytest.mark.django_db
class TestSubmissionCreation:
    def test_create_submission_generates_id(self, author_user, thematic_axis):
        s = Submission.objects.create(
            title="Trabalho teste",
            abstract="Resumo teste.",
            keywords=["a", "b", "c"],
            thematic_axis=thematic_axis,
            submitter=author_user,
        )
        assert s.submission_id.startswith("CBNV-2026-")
        assert len(s.submission_id.split("-")[-1]) == 4

    def test_create_submission_default_status_draft(self, submission):
        assert submission.status == "draft"

    def test_sequential_id_generation(self, author_user, thematic_axis):
        s1 = Submission.objects.create(
            title="Primeiro", abstract="R1.", keywords=["a", "b", "c"],
            thematic_axis=thematic_axis, submitter=author_user,
        )
        s2 = Submission.objects.create(
            title="Segundo", abstract="R2.", keywords=["a", "b", "c"],
            thematic_axis=thematic_axis, submitter=author_user,
        )
        num1 = int(s1.submission_id.split("-")[-1])
        num2 = int(s2.submission_id.split("-")[-1])
        assert num2 == num1 + 1


@pytest.mark.django_db
class TestSubmissionValidation:
    def test_keywords_minimum_3(self, author_user, thematic_axis):
        s = Submission(
            title="T", abstract="R.", keywords=["a", "b"],
            thematic_axis=thematic_axis, submitter=author_user,
        )
        with pytest.raises(ValidationError):
            s.clean()

    def test_keywords_maximum_5(self, author_user, thematic_axis):
        s = Submission(
            title="T", abstract="R.", keywords=["a", "b", "c", "d", "e", "f"],
            thematic_axis=thematic_axis, submitter=author_user,
        )
        with pytest.raises(ValidationError):
            s.clean()

    def test_abstract_max_2500(self, author_user, thematic_axis):
        s = Submission(
            title="T", abstract="x" * 2501, keywords=["a", "b", "c"],
            thematic_axis=thematic_axis, submitter=author_user,
        )
        with pytest.raises(ValidationError):
            s.clean()

    def test_valid_submission_passes_clean(self, submission):
        submission.full_clean()


@pytest.mark.django_db
class TestStateTransitions:
    def test_draft_to_submitted(self, submission):
        submission.submit()
        submission.refresh_from_db()
        assert submission.status == "submitted"

    def test_submitted_to_draft(self, submission):
        submission.submit()
        submission.refresh_from_db()
        submission.withdraw_to_draft()
        submission.refresh_from_db()
        assert submission.status == "draft"

    def test_invalid_transition_raises(self, submission):
        with pytest.raises(IllegalStateTransitionError):
            submission.transition_to("admin_screening")

    def test_draft_cannot_go_to_accepted(self, submission):
        with pytest.raises(IllegalStateTransitionError):
            submission.transition_to("accepted_oral")

    def test_submitted_to_admin_screening(self, submission):
        submission.submit()
        submission.refresh_from_db()
        submission.transition_to("admin_screening")
        submission.refresh_from_db()
        assert submission.status == "admin_screening"

    def test_full_review_cycle(self, submission):
        submission.submit()
        submission.transition_to("admin_screening")
        submission.transition_to("assigned_to_reviewers")
        submission.transition_to("under_review")
        submission.transition_to("reviews_completed")
        submission.transition_to("decision_pending")
        submission.transition_to("accepted_oral")
        submission.transition_to("final_materials_pending")
        submission.transition_to("ready_for_proceedings")
        submission.transition_to("published_in_proceedings")
        submission.refresh_from_db()
        assert submission.status == "published_in_proceedings"


@pytest.mark.django_db
class TestStatusLabels:
    def test_draft_label(self, submission):
        assert submission.status_label == "Rascunho"

    def test_submitted_label(self, submission):
        submission.submit()
        submission.refresh_from_db()
        assert submission.status_label == "Enviado"

    def test_review_labels_are_em_avaliacao(self, submission):
        for state in [
            "assigned_to_reviewers", "under_review",
            "reviews_completed", "decision_pending",
        ]:
            assert Submission(status=state).status_label == "Em avaliação"


@pytest.mark.django_db
class TestSubmissionAuthor:
    def test_create_author(self, submission):
        author = SubmissionAuthor.objects.create(
            submission=submission,
            first_name="Maria",
            last_name="Oliveira",
            email="maria@example.com",
            institution="USP",
            order=1,
            is_corresponding=True,
        )
        assert author.full_name == "Maria Oliveira"
        assert str(author) == "Maria Oliveira"

    def test_corresponding_author_property(self, submission):
        SubmissionAuthor.objects.create(
            submission=submission, first_name="A", last_name="B",
            email="a@b.com", institution="X", order=1, is_corresponding=True,
        )
        SubmissionAuthor.objects.create(
            submission=submission, first_name="C", last_name="D",
            email="c@d.com", institution="Y", order=2, is_corresponding=False,
        )
        corresponding = submission.get_corresponding_author()
        assert corresponding.first_name == "A"

    def test_author_ordering(self, submission):
        SubmissionAuthor.objects.create(
            submission=submission, first_name="Z", last_name="Z",
            email="z@z.com", institution="Z", order=3, is_corresponding=False,
        )
        SubmissionAuthor.objects.create(
            submission=submission, first_name="A", last_name="A",
            email="a@a.com", institution="A", order=1, is_corresponding=True,
        )
        names = [a.full_name for a in submission.authors.all()]
        assert names == ["A A", "Z Z"]


@pytest.mark.django_db
class TestSubmissionFile:
    def test_file_creation(self, submission):
        f = SimpleUploadedFile("test.pdf", b"%PDF-1.4 fake content")
        sf = SubmissionFile.objects.create(submission=submission, file=f)
        assert sf.filename.endswith(".pdf")

    def test_filesize_display(self, submission):
        f = SimpleUploadedFile("test.pdf", b"x" * 1024)
        sf = SubmissionFile.objects.create(submission=submission, file=f)
        assert "KB" in sf.filesize


@pytest.mark.django_db
class TestSubmissionQuerySet:
    def test_for_user(self, author_user, thematic_axis):
        other = create_user_with_profile(
            username="other", password="p", is_author=True,
        )
        Submission.objects.create(
            title="Meu", abstract="R.", keywords=["a", "b", "c"],
            thematic_axis=thematic_axis, submitter=author_user,
        )
        Submission.objects.create(
            title="Dele", abstract="R.", keywords=["a", "b", "c"],
            thematic_axis=thematic_axis, submitter=other,
        )
        assert Submission.objects.for_user(author_user).count() == 1
        assert Submission.objects.for_user(author_user).first().title == "Meu"
