from django.core import mail
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from accounts.tests.factories import create_user_with_profile
from proceedings.models import FinalMaterial
from submissions.models import Submission, SubmissionAuthor, ThematicAxis


class NotificationTest(TestCase):
    def setUp(self):
        self.chair = create_user_with_profile(
            username="chair", password="pass", is_chair=True,
        )
        self.author = create_user_with_profile(
            username="author", password="pass", is_author=True,
            first_name="João", last_name="Silva",
            institution="UFMG", country="BR",
        )
        self.axis = ThematicAxis.objects.create(name="Neurofisiologia")

    def _create_submission(self, status="accepted_oral"):
        sub = Submission.objects.create(
            title="Trabalho teste", abstract="Resumo" * 20,
            keywords=["a", "b", "c"], thematic_axis=self.axis,
            submitter=self.author, status=status, final_modality="oral",
        )
        SubmissionAuthor.objects.create(
            submission=sub, first_name="João", last_name="Silva",
            email="joao@example.com", institution="UFMG", order=1, is_corresponding=True,
        )
        return sub

    def test_materials_requested_sends_email(self):
        sub = self._create_submission()
        self.client.login(username="chair", password="pass")
        self.client.post(reverse("proceedings:request_materials", args=[sub.pk]))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("materiais finais solicitados", mail.outbox[0].subject.lower())

    def test_materials_received_sends_email(self):
        sub = self._create_submission(status="final_materials_pending")
        self.client.login(username="author", password="pass")
        self.client.post(
            reverse("proceedings:author_upload", args=[sub.pk]),
            {
                "final_pdf": SimpleUploadedFile("doc.pdf", b"%PDF-1.4", content_type="application/pdf"),
                "presentation_file": SimpleUploadedFile("s.pptx", b"PK", content_type="application/vnd.openxmlformats-officedocument.presentationml.presentation"),
            },
            format="multipart",
        )
        self.assertTrue(any("recebidos" in m.subject.lower() for m in mail.outbox))

    def test_materials_validated_sends_email(self):
        sub = self._create_submission(status="final_materials_pending")
        FinalMaterial.objects.create(
            submission=sub,
            final_pdf=SimpleUploadedFile("doc.pdf", b"%PDF-1.4", content_type="application/pdf"),
        )
        self.client.login(username="chair", password="pass")
        mail.outbox.clear()
        self.client.post(
            reverse("proceedings:validate_materials", args=[sub.pk]),
            {"notes": "OK"},
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("validados", mail.outbox[0].subject.lower())

    def test_proceedings_published_sends_email(self):
        sub = self._create_submission(status="ready_for_proceedings")
        self.client.login(username="chair", password="pass")
        self.client.post(reverse("proceedings:publish_proceedings", args=[sub.pk]))
        self.assertTrue(any("publicado" in m.subject.lower() for m in mail.outbox))

    def test_no_email_without_corresponding_author(self):
        sub = self._create_submission()
        sub.authors.filter(is_corresponding=True).delete()
        self.client.login(username="chair", password="pass")
        mail.outbox.clear()
        self.client.post(reverse("proceedings:request_materials", args=[sub.pk]))
        self.assertEqual(len(mail.outbox), 0)
