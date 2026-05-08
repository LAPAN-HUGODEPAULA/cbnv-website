import pytest
from django.core import mail

from accounts.models import User
from submissions.models import Submission, SubmissionAuthor, ThematicAxis


@pytest.fixture
def submission_with_author(db):
    axis = ThematicAxis.objects.create(name="Neurociência da Visão", order=1)
    user = User.objects.create_user(
        username="author",
        email="author@example.com",
        password="testpass123",
        first_name="João",
        last_name="Silva",
        institution="UFMG",
        country="BR",
        is_author=True,
    )
    sub = Submission.objects.create(
        title="Trabalho de Teste",
        abstract="Resumo do trabalho.",
        keywords=["neurociência", "visão", "percepção"],
        thematic_axis=axis,
        submitter=user,
    )
    SubmissionAuthor.objects.create(
        submission=sub,
        first_name="João",
        last_name="Silva",
        email="author@example.com",
        institution="UFMG",
        order=1,
        is_corresponding=True,
    )
    return sub


class TestSubmissionConfirmationEmail:
    def test_email_sent_on_submit(self, submission_with_author):
        from notifications.services import send_submission_confirmation

        sub = submission_with_author
        mail.outbox.clear()
        send_submission_confirmation(sub)
        assert len(mail.outbox) == 1
        email = mail.outbox[0]
        assert email.to == ["author@example.com"]
        assert sub.submission_id in email.subject
        assert "João Silva" in email.body

    def test_email_in_portuguese(self, submission_with_author):
        from notifications.services import send_submission_confirmation

        sub = submission_with_author
        mail.outbox.clear()
        send_submission_confirmation(sub)
        email = mail.outbox[0]
        assert "recebida" in email.body or "recebimento" in email.body

    def test_no_corresponding_author_no_email(self, db):
        from notifications.services import send_submission_confirmation

        axis = ThematicAxis.objects.create(name="X", order=1)
        user = User.objects.create_user(
            username="noauth", password="p", is_author=True,
            first_name="A", last_name="B", institution="X", country="BR",
        )
        sub = Submission.objects.create(
            title="T", abstract="R.", keywords=["a", "b", "c"],
            thematic_axis=axis, submitter=user,
        )
        mail.outbox.clear()
        send_submission_confirmation(sub)
        assert len(mail.outbox) == 0
