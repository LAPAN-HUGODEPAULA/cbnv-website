from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from core.storage import ProtectedMediaStorage
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

from proceedings.managers import FinalMaterialManager

protected_storage = ProtectedMediaStorage()


class FinalMaterial(models.Model):
    submission = models.OneToOneField(
        "submissions.Submission",
        on_delete=models.CASCADE,
        related_name="final_material",
        verbose_name="Submissão",
    )
    final_pdf = models.FileField(
        "PDF final", storage=protected_storage, blank=True
    )
    presentation_file = models.FileField(
        "Apresentação", storage=protected_storage, blank=True
    )
    video_url = models.URLField("Link do vídeo (YouTube)", blank=True)
    received_at = models.DateTimeField("Recebido em", null=True, blank=True)
    validated_at = models.DateTimeField("Validado em", null=True, blank=True)
    validated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Validado por",
    )
    notes = models.TextField("Notas internas", blank=True)

    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    objects = FinalMaterialManager()

    class Meta:
        verbose_name = "Material final"
        verbose_name_plural = "Materiais finais"

    def __str__(self):
        return f"Materiais finais — {self.submission.submission_id}"

    def clean(self):
        super().clean()

        if self.final_pdf:
            if not self.final_pdf.name.lower().endswith(".pdf"):
                raise ValidationError({"final_pdf": "Apenas arquivos PDF são aceitos para o PDF final."})
            if self.final_pdf.size > 10 * 1024 * 1024:
                raise ValidationError({"final_pdf": "O PDF final não pode ultrapassar 10 MB."})

        if self.presentation_file:
            ext = self.presentation_file.name.lower().split(".")[-1]
            if ext not in ("pdf", "pptx"):
                raise ValidationError({"presentation_file": "Apenas arquivos PDF ou PPTX são aceitos para a apresentação."})
            if self.presentation_file.size > 50 * 1024 * 1024:
                raise ValidationError({"presentation_file": "A apresentação não pode ultrapassar 50 MB."})

        if self.video_url:
            from videos.models import parse_youtube_url

            parsed = parse_youtube_url(self.video_url)
            if not parsed.get("type"):
                raise ValidationError({"video_url": "Informe uma URL válida do YouTube."})

    @property
    def has_files(self):
        return bool(self.final_pdf or self.presentation_file or self.video_url)


@register_snippet
class Edition(models.Model):
    edition_number = models.PositiveIntegerField("Número da Edição")
    year = models.PositiveIntegerField("Ano")
    theme = models.CharField("Tema", max_length=255)
    dates = models.CharField("Datas", max_length=255, blank=True)
    location = models.CharField("Local", max_length=255, blank=True)
    proceedings_url = models.URLField("Link dos Anais", blank=True, help_text="URL externa para os anais em PDF")
    playlist_url = models.URLField("Link da Playlist (YouTube)", blank=True)

    panels = [
        FieldPanel("edition_number"),
        FieldPanel("year"),
        FieldPanel("theme"),
        FieldPanel("dates"),
        FieldPanel("location"),
        FieldPanel("proceedings_url"),
        FieldPanel("playlist_url"),
    ]

    class Meta:
        ordering = ["-year"]
        verbose_name = "Edição Anterior"
        verbose_name_plural = "Edições Anteriores"

    def __str__(self):
        return f"{self.edition_number}ª CBNV — {self.year}"
