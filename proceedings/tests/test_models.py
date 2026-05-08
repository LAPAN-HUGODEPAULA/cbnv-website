from django.core.exceptions import ValidationError
from django.test import TestCase
from io import BytesIO

from accounts.models import User
from accounts.tests.factories import create_user_with_profile
from proceedings.models import FinalMaterial
from submissions.models import Submission, SubmissionAuthor, ThematicAxis


class FinalMaterialModelTest(TestCase):
    def setUp(self):
        self.axis = ThematicAxis.objects.create(name="Neurofisiologia")
        self.author = create_user_with_profile(
            username="author", password="pass", is_author=True,
            first_name="João", last_name="Silva",
            institution="UFMG", country="BR",
        )
        self.submission = Submission.objects.create(
            title="Trabalho de teste",
            abstract="Resumo de teste para o trabalho.",
            keywords=["neuro", "visão", "teste"],
            thematic_axis=self.axis,
            submitter=self.author,
            status="accepted_oral",
            final_modality="oral",
        )
        SubmissionAuthor.objects.create(
            submission=self.submission,
            first_name="João", last_name="Silva",
            email="joao@example.com", institution="UFMG",
            order=1, is_corresponding=True,
        )

    def test_create_final_material(self):
        material = FinalMaterial.objects.create(submission=self.submission)
        self.assertEqual(str(material), f"Materiais finais — {self.submission.submission_id}")
        self.assertFalse(material.has_files)

    def test_one_to_one_constraint(self):
        FinalMaterial.objects.create(submission=self.submission)
        with self.assertRaises(Exception):
            FinalMaterial.objects.create(submission=self.submission)

    def test_has_files_with_pdf(self):
        material = FinalMaterial.objects.create(submission=self.submission)
        material.final_pdf = self._fake_file("doc.pdf", b"%PDF-1.4")
        self.assertTrue(material.has_files)

    def test_has_files_with_video_url(self):
        material = FinalMaterial.objects.create(submission=self.submission, video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        self.assertTrue(material.has_files)

    def test_invalid_pdf_extension(self):
        material = FinalMaterial(submission=self.submission)
        material.final_pdf = self._fake_file("doc.docx", b"content")
        with self.assertRaises(ValidationError) as ctx:
            material.clean()
        self.assertIn("final_pdf", ctx.exception.message_dict)

    def test_oversized_pdf(self):
        material = FinalMaterial(submission=self.submission)
        material.final_pdf = self._fake_file("big.pdf", b"X" * (10 * 1024 * 1024 + 1))
        with self.assertRaises(ValidationError) as ctx:
            material.clean()
        self.assertIn("final_pdf", ctx.exception.message_dict)

    def test_invalid_presentation_extension(self):
        material = FinalMaterial(submission=self.submission)
        material.presentation_file = self._fake_file("slides.key", b"content")
        with self.assertRaises(ValidationError) as ctx:
            material.clean()
        self.assertIn("presentation_file", ctx.exception.message_dict)

    def test_oversized_presentation(self):
        material = FinalMaterial(submission=self.submission)
        material.presentation_file = self._fake_file("big.pptx", b"X" * (50 * 1024 * 1024 + 1))
        with self.assertRaises(ValidationError) as ctx:
            material.clean()
        self.assertIn("presentation_file", ctx.exception.message_dict)

    def test_valid_youtube_url(self):
        material = FinalMaterial(
            submission=self.submission,
            video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        )
        material.clean()

    def test_valid_youtube_short_url(self):
        material = FinalMaterial(
            submission=self.submission,
            video_url="https://youtu.be/dQw4w9WgXcQ",
        )
        material.clean()

    def test_invalid_youtube_url(self):
        material = FinalMaterial(
            submission=self.submission,
            video_url="https://vimeo.com/123456",
        )
        with self.assertRaises(ValidationError) as ctx:
            material.clean()
        self.assertIn("video_url", ctx.exception.message_dict)

    def test_blank_video_url_is_valid(self):
        material = FinalMaterial(submission=self.submission, video_url="")
        material.clean()

    def _fake_file(self, name, content):
        from django.core.files.base import File
        return File(BytesIO(content), name=name)
