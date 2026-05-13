from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from accounts.models import User
from accounts.tests.factories import create_user_with_profile
from proceedings.models import FinalMaterial
from submissions.models import Submission, SubmissionAuthor, ThematicAxis
from videos.models import PUBLIC, VideoResource


class _SubmissionMixin:
    def _create_submission(self, status="accepted_oral", modality="oral", **kwargs):
        axis = kwargs.pop("axis", None) or ThematicAxis.objects.get_or_create(name="Neurofisiologia")[0]
        author = kwargs.pop("author", None) or self.author
        title = kwargs.pop("title", "Trabalho teste")
        sub = Submission.objects.create(
            title=title,
            abstract="Resumo teste" * 10,
            keywords=["neuro", "visão", "teste"],
            thematic_axis=axis,
            submitter=author,
            status=status,
            final_modality=modality,
        )
        SubmissionAuthor.objects.create(
            submission=sub, first_name="João", last_name="Silva",
            email="joao@example.com", institution="UFMG",
            order=1, is_corresponding=True,
        )
        return sub

    def _pdf_file(self, name="doc.pdf"):
        return SimpleUploadedFile(name, b"%PDF-1.4 fake content", content_type="application/pdf")

    def _pptx_file(self, name="slides.pptx"):
        return SimpleUploadedFile(name, b"PK fake pptx content", content_type="application/vnd.openxmlformats-officedocument.presentationml.presentation")


class AuthorUploadTest(_SubmissionMixin, TestCase):
    def setUp(self):
        self.author = create_user_with_profile(
            username="author", password="pass", is_author=True,
            first_name="João", last_name="Silva",
            institution="UFMG", country="BR",
        )

    def test_upload_page_requires_login(self):
        sub = self._create_submission()
        response = self.client.get(reverse("proceedings:author_upload", args=[sub.pk]))
        self.assertEqual(response.status_code, 302)

    def test_upload_page_for_final_materials_pending(self):
        sub = self._create_submission(status="final_materials_pending")
        self.client.login(username="author", password="pass")
        response = self.client.get(reverse("proceedings:author_upload", args=[sub.pk]))
        self.assertEqual(response.status_code, 200)

    def test_upload_page_redirects_for_wrong_status(self):
        sub = self._create_submission(status="accepted_oral")
        self.client.login(username="author", password="pass")
        response = self.client.get(reverse("proceedings:author_upload", args=[sub.pk]))
        self.assertEqual(response.status_code, 302)

    def test_upload_page_denies_other_user(self):
        other = create_user_with_profile(username="other", password="pass", is_author=True)
        sub = self._create_submission(status="final_materials_pending", author=other)
        self.client.login(username="author", password="pass")
        response = self.client.get(reverse("proceedings:author_upload", args=[sub.pk]))
        self.assertEqual(response.status_code, 404)

    def test_valid_upload_creates_material(self):
        sub = self._create_submission(status="final_materials_pending")
        self.client.login(username="author", password="pass")
        response = self.client.post(
            reverse("proceedings:author_upload", args=[sub.pk]),
            {
                "final_pdf": self._pdf_file(),
                "presentation_file": self._pptx_file(),
                "publication_authorized": "on",
            },
            format="multipart",
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        sub.refresh_from_db()
        material = sub.final_material
        self.assertIsNotNone(material)
        self.assertTrue(bool(material.final_pdf))
        self.assertTrue(bool(material.presentation_file))
        self.assertTrue(material.publication_authorized)
        self.assertIsNotNone(material.received_at)

    def test_upload_without_authorization_is_rejected(self):
        sub = self._create_submission(status="final_materials_pending")
        self.client.login(username="author", password="pass")
        response = self.client.post(
            reverse("proceedings:author_upload", args=[sub.pk]),
            {"final_pdf": self._pdf_file()},
            format="multipart",
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A autorização de publicação é obrigatória.")
        self.assertFalse(sub.final_material.publication_authorized)

    def test_invalid_file_type_rejected(self):
        sub = self._create_submission(status="final_materials_pending")
        self.client.login(username="author", password="pass")
        bad_file = SimpleUploadedFile("bad.txt", b"not a pdf", content_type="text/plain")
        response = self.client.post(
            reverse("proceedings:author_upload", args=[sub.pk]),
            {"final_pdf": bad_file},
            format="multipart",
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(sub.final_material.final_pdf if hasattr(sub, 'final_material') else True)

    def test_re_upload_updates_materials(self):
        sub = self._create_submission(status="final_materials_pending")
        self.client.login(username="author", password="pass")
        self.client.post(
            reverse("proceedings:author_upload", args=[sub.pk]),
            {
                "final_pdf": self._pdf_file(),
                "presentation_file": self._pptx_file(),
                "publication_authorized": "on",
            },
            format="multipart",
        )
        first_received = sub.final_material.received_at
        self.client.post(
            reverse("proceedings:author_upload", args=[sub.pk]),
            {
                "final_pdf": self._pdf_file("updated.pdf"),
                "presentation_file": self._pptx_file(),
                "publication_authorized": "on",
            },
            format="multipart",
        )
        sub.refresh_from_db()
        self.assertTrue(sub.final_material.received_at >= first_received)

    def test_video_url_shown_for_oral(self):
        sub = self._create_submission(status="final_materials_pending", modality="oral")
        self.client.login(username="author", password="pass")
        response = self.client.get(reverse("proceedings:author_upload", args=[sub.pk]))
        self.assertContains(response, "video_url")

    def test_video_url_hidden_for_poster(self):
        sub = self._create_submission(status="final_materials_pending", modality="poster")
        self.client.login(username="author", password="pass")
        response = self.client.get(reverse("proceedings:author_upload", args=[sub.pk]))
        self.assertNotContains(response, "video_url")


class CommissionValidationTest(_SubmissionMixin, TestCase):
    def setUp(self):
        self.chair = create_user_with_profile(
            username="chair", password="pass", is_chair=True,
            first_name="Comissão", last_name="Científica",
        )
        self.author = create_user_with_profile(
            username="author", password="pass", is_author=True,
            first_name="João", last_name="Silva",
            institution="UFMG", country="BR",
        )

    def test_request_materials_transitions_status(self):
        sub = self._create_submission(status="accepted_oral")
        self.client.login(username="chair", password="pass")
        response = self.client.post(reverse("proceedings:request_materials", args=[sub.pk]))
        self.assertEqual(response.status_code, 302)
        sub.refresh_from_db()
        self.assertEqual(sub.status, "final_materials_pending")
        self.assertTrue(hasattr(sub, 'final_material'))

    def test_request_materials_rejected_for_non_accepted(self):
        sub = self._create_submission(status="draft")
        self.client.login(username="chair", password="pass")
        response = self.client.post(reverse("proceedings:request_materials", args=[sub.pk]))
        self.assertEqual(response.status_code, 302)
        sub.refresh_from_db()
        self.assertEqual(sub.status, "draft")

    def test_validate_materials_transitions(self):
        sub = self._create_submission(status="final_materials_pending")
        FinalMaterial.objects.create(
            submission=sub,
            final_pdf=self._pdf_file(),
            presentation_file=self._pptx_file(),
            publication_authorized=True,
        )
        self.client.login(username="chair", password="pass")
        response = self.client.post(
            reverse("proceedings:validate_materials", args=[sub.pk]),
            {"notes": "OK"},
        )
        self.assertEqual(response.status_code, 302)
        sub.refresh_from_db()
        self.assertEqual(sub.status, "ready_for_proceedings")
        material = sub.final_material
        self.assertIsNotNone(material.validated_at)
        self.assertEqual(material.validated_by, self.chair)

    def test_validate_materials_requires_publication_authorization(self):
        sub = self._create_submission(status="final_materials_pending")
        FinalMaterial.objects.create(submission=sub, final_pdf=self._pdf_file())
        self.client.login(username="chair", password="pass")
        response = self.client.post(
            reverse("proceedings:validate_materials", args=[sub.pk]),
            {"notes": "OK"},
        )
        self.assertEqual(response.status_code, 302)
        sub.refresh_from_db()
        self.assertEqual(sub.status, "final_materials_pending")

    def test_publish_proceedings_transitions(self):
        sub = self._create_submission(status="ready_for_proceedings")
        self.client.login(username="chair", password="pass")
        response = self.client.post(reverse("proceedings:publish_proceedings", args=[sub.pk]))
        self.assertEqual(response.status_code, 302)
        sub.refresh_from_db()
        self.assertEqual(sub.status, "published_in_proceedings")

    def test_commission_materials_page(self):
        self.client.login(username="chair", password="pass")
        response = self.client.get(reverse("proceedings:commission_materials"))
        self.assertEqual(response.status_code, 200)


class PublicProceedingsTest(_SubmissionMixin, TestCase):
    def setUp(self):
        self.author = create_user_with_profile(
            username="author", password="pass", is_author=True,
            first_name="João", last_name="Silva",
            institution="UFMG", country="BR",
        )
        self.axis = ThematicAxis.objects.create(name="Neurofisiologia")
        self.other_axis = ThematicAxis.objects.create(name="Psicofísica")
        self.published = self._create_submission(status="published_in_proceedings", axis=self.axis, title="Trabalho publicado")
        self.unpublished = self._create_submission(
            status="ready_for_proceedings", axis=self.other_axis, title="Trabalho não publicado",
        )
        self.ready = self._create_submission(
            status="ready_for_proceedings", axis=self.axis, title="Trabalho pronto",
        )
        FinalMaterial.objects.create(
            submission=self.published,
            final_pdf=self._pdf_file(),
            publication_authorized=True,
            validated_at=timezone.now(),
        )
        FinalMaterial.objects.create(
            submission=self.ready,
            final_pdf=self._pdf_file("ready.pdf"),
            publication_authorized=True,
            validated_at=timezone.now(),
        )

    def test_proceedings_list_shows_validated_authorized_items_only(self):
        response = self.client.get("/anais/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.published.title)
        self.assertContains(response, self.ready.title)
        self.assertNotContains(response, self.unpublished.title)

    def test_proceedings_detail_for_published(self):
        response = self.client.get(reverse("proceedings:proceedings_detail", args=[self.published.submission_id]))
        self.assertEqual(response.status_code, 200)

    def test_proceedings_detail_for_ready_material(self):
        response = self.client.get(reverse("proceedings:proceedings_detail", args=[self.ready.submission_id]))
        self.assertEqual(response.status_code, 200)

    def test_proceedings_detail_for_unvalidated_404(self):
        response = self.client.get(reverse("proceedings:proceedings_detail", args=[self.unpublished.submission_id]))
        self.assertEqual(response.status_code, 404)

    def test_pdf_download_for_published(self):
        response = self.client.get(reverse("proceedings:proceedings_download_pdf", args=[self.published.submission_id]))
        self.assertEqual(response.status_code, 200)

    def test_pdf_download_for_unpublished_403(self):
        FinalMaterial.objects.create(submission=self.unpublished, final_pdf=self._pdf_file())
        response = self.client.get(reverse("proceedings:proceedings_download_pdf", args=[self.unpublished.submission_id]))
        self.assertEqual(response.status_code, 403)

    def test_ready_pdf_is_not_downloadable_until_published(self):
        response = self.client.get(reverse("proceedings:proceedings_download_pdf", args=[self.ready.submission_id]))
        self.assertEqual(response.status_code, 403)

    def test_submitted_video_url_does_not_render_without_public_resource(self):
        self.published.final_material.video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        self.published.final_material.save()
        response = self.client.get(reverse("proceedings:proceedings_detail", args=[self.published.submission_id]))
        self.assertNotContains(response, "youtube.com/embed")

    def test_explicit_public_video_resource_renders(self):
        video = VideoResource.objects.create(
            title="Vídeo público",
            youtube_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            status=PUBLIC,
        )
        self.published.final_material.video_url = video.youtube_url
        self.published.final_material.video_resource = video
        self.published.final_material.save()
        response = self.client.get(reverse("proceedings:proceedings_detail", args=[self.published.submission_id]))
        self.assertContains(response, "youtube.com/embed/dQw4w9WgXcQ")

    def test_filter_by_modality(self):
        response = self.client.get("/anais/?modality=oral")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.published.title)

    def test_filter_by_axis(self):
        response = self.client.get(f"/anais/?axis={self.other_axis.pk}")
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.published.title)
