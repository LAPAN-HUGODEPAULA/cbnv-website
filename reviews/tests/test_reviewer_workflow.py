import pytest
from django.core import mail
from django.test import Client
from django.urls import reverse

from accounts.models import User
from reviews.models import Review, ReviewerAssignment
from submissions.models import Submission, SubmissionAuthor, ThematicAxis


@pytest.fixture
def review_fixtures(db):
    axis = ThematicAxis.objects.create(name="Neurociência da Visão", order=1)
    author = User.objects.create_user(
        username="author",
        email="author@example.com",
        password="testpass123",
        first_name="João",
        last_name="Silva",
        institution="UFMG",
        country="BR",
        is_author=True,
    )
    reviewer = User.objects.create_user(
        username="reviewer1",
        email="reviewer@example.com",
        password="testpass123",
        first_name="Maria",
        last_name="Oliveira",
        institution="USP",
        country="BR",
        is_reviewer=True,
    )
    chair = User.objects.create_user(
        username="chair1",
        email="chair@example.com",
        password="testpass123",
        first_name="Carlos",
        last_name="Mendes",
        institution="UnB",
        country="BR",
        is_chair=True,
    )
    submission = Submission.objects.create(
        title="Trabalho de Teste",
        abstract="Resumo do trabalho.",
        keywords=["neurociência", "visão", "percepção"],
        thematic_axis=axis,
        submitter=author,
    )
    submission.transition_to("submitted")
    submission.transition_to("admin_screening")
    SubmissionAuthor.objects.create(
        submission=submission,
        first_name="João",
        last_name="Silva",
        email="author@example.com",
        institution="UFMG",
        order=1,
        is_corresponding=True,
    )
    return {
        "axis": axis,
        "author": author,
        "reviewer": reviewer,
        "chair": chair,
        "submission": submission,
    }


@pytest.mark.django_db
class TestReviewerAssignment:
    def test_create_assignment(self, review_fixtures):
        sub = review_fixtures["submission"]
        rev = review_fixtures["reviewer"]
        assignment = ReviewerAssignment.objects.create(
            reviewer=rev, submission=sub
        )
        assert assignment.pk is not None
        assert str(rev.pk) in str(assignment)

    def test_unique_assignment(self, review_fixtures):
        sub = review_fixtures["submission"]
        rev = review_fixtures["reviewer"]
        ReviewerAssignment.objects.create(reviewer=rev, submission=sub)
        with pytest.raises(Exception):
            ReviewerAssignment.objects.create(reviewer=rev, submission=sub)


@pytest.mark.django_db
class TestReviewerPermissions:
    def test_reviewer_can_access_submissions(self, review_fixtures):
        client = Client()
        client.force_login(review_fixtures["reviewer"])
        response = client.get(reverse("reviews:reviewer_submissions"))
        assert response.status_code == 200

    def test_author_cannot_access_reviewer_portal(self, review_fixtures):
        client = Client()
        client.force_login(review_fixtures["author"])
        response = client.get(reverse("reviews:reviewer_submissions"))
        assert response.status_code == 302

    def test_anonymous_cannot_access_reviewer_portal(self, db):
        client = Client()
        response = client.get(reverse("reviews:reviewer_submissions"))
        assert response.status_code == 302

    def test_chair_can_access_manage_submissions(self, review_fixtures):
        client = Client()
        client.force_login(review_fixtures["chair"])
        response = client.get(reverse("reviews:manage_submissions"))
        assert response.status_code == 200

    def test_reviewer_cannot_access_manage_submissions(self, review_fixtures):
        client = Client()
        client.force_login(review_fixtures["reviewer"])
        response = client.get(reverse("reviews:manage_submissions"))
        assert response.status_code == 302


@pytest.mark.django_db
class TestReviewSubmission:
    def _assign(self, review_fixtures):
        sub = review_fixtures["submission"]
        rev = review_fixtures["reviewer"]
        return ReviewerAssignment.objects.create(reviewer=rev, submission=sub)

    def test_reviewer_can_submit_review(self, review_fixtures):
        assignment = self._assign(review_fixtures)
        client = Client()
        client.force_login(review_fixtures["reviewer"])
        response = client.post(
            reverse("reviews:review_detail", args=[assignment.pk]),
            {
                "recommendation": "accept",
                "comments": "Bom trabalho.",
                "confidential_notes": "",
            },
            follow=False,
        )
        assert response.status_code == 302
        assert Review.objects.count() == 1
        review = Review.objects.first()
        assert review.recommendation == "accept"
        assert review.comments == "Bom trabalho."

    def test_reviewer_can_update_review(self, review_fixtures):
        assignment = self._assign(review_fixtures)
        review = Review.objects.create(
            assignment=assignment,
            recommendation="corrections",
            comments="Precisa ajustes.",
        )
        client = Client()
        client.force_login(review_fixtures["reviewer"])
        client.post(
            reverse("reviews:review_detail", args=[assignment.pk]),
            {
                "recommendation": "accept",
                "comments": "Agora está bom.",
                "confidential_notes": "",
            },
        )
        review.refresh_from_db()
        assert review.recommendation == "accept"

    def test_cannot_review_other_reviewer_assignment(self, review_fixtures):
        assignment = self._assign(review_fixtures)
        other = User.objects.create_user(
            username="reviewer2", password="p", is_reviewer=True,
            first_name="Outro", last_name="Revisor",
        )
        client = Client()
        client.force_login(other)
        response = client.get(
            reverse("reviews:review_detail", args=[assignment.pk])
        )
        assert response.status_code == 404


@pytest.mark.django_db
class TestChairDecision:
    def _setup_for_decision(self, review_fixtures):
        sub = review_fixtures["submission"]
        rev = review_fixtures["reviewer"]
        ReviewerAssignment.objects.create(reviewer=rev, submission=sub)
        Review.objects.create(
            assignment=rev.review_assignments.first(),
            recommendation="accept",
            comments="Excelente trabalho.",
        )
        sub.transition_to("assigned_to_reviewers")
        sub.transition_to("under_review")
        sub.transition_to("reviews_completed")
        sub.transition_to("decision_pending")
        return sub

    def test_chair_can_issue_acceptance(self, review_fixtures):
        sub = self._setup_for_decision(review_fixtures)
        client = Client()
        client.force_login(review_fixtures["chair"])
        response = client.post(
            reverse("reviews:issue_decision", args=[sub.pk]),
            {
                "action": "accepted_oral",
                "decision_notes": "Parabéns!",
            },
            follow=False,
        )
        assert response.status_code == 302
        sub.refresh_from_db()
        assert sub.status == "accepted_oral"
        assert sub.final_modality == "oral"
        assert sub.decision_notes == "Parabéns!"

    def test_chair_can_issue_rejection(self, review_fixtures):
        sub = self._setup_for_decision(review_fixtures)
        client = Client()
        client.force_login(review_fixtures["chair"])
        client.post(
            reverse("reviews:issue_decision", args=[sub.pk]),
            {"action": "rejected", "decision_notes": "Não atendeu."},
        )
        sub.refresh_from_db()
        assert sub.status == "rejected"
        assert sub.final_modality == ""

    def test_decision_sends_notification(self, review_fixtures):
        sub = self._setup_for_decision(review_fixtures)
        mail.outbox.clear()
        client = Client()
        client.force_login(review_fixtures["chair"])
        client.post(
            reverse("reviews:issue_decision", args=[sub.pk]),
            {"action": "accepted_poster", "decision_notes": "Aprovado."},
        )
        assert len(mail.outbox) == 1
        email = mail.outbox[0]
        assert email.to == ["author@example.com"]

    def test_chair_assignment_transitions_submission(self, review_fixtures):
        sub = review_fixtures["submission"]
        rev = review_fixtures["reviewer"]
        assert sub.status == "admin_screening"
        client = Client()
        client.force_login(review_fixtures["chair"])
        mail.outbox.clear()
        response = client.post(
            reverse("reviews:assign_reviewers", args=[sub.pk]),
            {"reviewers": [rev.pk]},
            follow=False,
        )
        assert response.status_code == 302
        sub.refresh_from_db()
        assert sub.status == "assigned_to_reviewers"
        assert len(mail.outbox) == 1


@pytest.mark.django_db
class TestDecisionBundle:
    def test_bundle_includes_all_reviews(self, review_fixtures):
        from notifications.services import build_decision_bundle

        sub = review_fixtures["submission"]
        rev = review_fixtures["reviewer"]
        assignment = ReviewerAssignment.objects.create(reviewer=rev, submission=sub)
        Review.objects.create(
            assignment=assignment,
            recommendation="accept",
            comments="Muito bom.",
        )
        sub.decision_notes = "Parabéns ao autor."
        sub.save()
        bundle = build_decision_bundle(sub)
        assert len(bundle["reviews"]) == 1
        assert bundle["reviews"][0]["recommendation"] == "Aceitar"
        assert bundle["reviews"][0]["comments"] == "Muito bom."
        assert bundle["chair_notes"] == "Parabéns ao autor."

    def test_notification_contains_decision_bundle(self, review_fixtures):
        from notifications.services import notify_decision

        sub = review_fixtures["submission"]
        rev = review_fixtures["reviewer"]
        assignment = ReviewerAssignment.objects.create(reviewer=rev, submission=sub)
        Review.objects.create(
            assignment=assignment,
            recommendation="reject",
            comments="Falta fundamentação.",
        )
        sub.transition_to("assigned_to_reviewers")
        sub.transition_to("under_review")
        sub.transition_to("reviews_completed")
        sub.transition_to("decision_pending")
        sub.transition_to("rejected")
        sub.decision_notes = "Não atendeu os critérios."
        sub.save()

        mail.outbox.clear()
        notify_decision(sub)
        assert len(mail.outbox) == 1
        email = mail.outbox[0]
        assert "Não atendeu" in email.body
        assert "Falta fundamentação" in email.body
        assert "João Silva" not in email.body or "autor correspondente" not in email.body.lower()


@pytest.mark.django_db
class TestCSVExport:
    def test_export_contains_decisions(self, review_fixtures):
        sub = review_fixtures["submission"]
        sub.transition_to("assigned_to_reviewers")
        sub.transition_to("under_review")
        sub.transition_to("reviews_completed")
        sub.transition_to("decision_pending")
        sub.transition_to("accepted_oral")
        sub.final_modality = "oral"
        sub.save()

        client = Client()
        client.force_login(review_fixtures["chair"])
        response = client.get(reverse("reports:export_decisions"))
        assert response.status_code == 200
        assert response["Content-Type"] == "text/csv; charset=utf-8-sig"
        assert "CBNV-2026-" in response.content.decode("utf-8-sig")
        assert "Oral" in response.content.decode("utf-8-sig")

    def test_author_cannot_export(self, review_fixtures):
        client = Client()
        client.force_login(review_fixtures["author"])
        response = client.get(reverse("reports:export_decisions"))
        assert response.status_code == 302
