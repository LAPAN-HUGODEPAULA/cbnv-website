from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.db import models, transaction
from django.db.models import Max
from wagtail.snippets.models import register_snippet


protected_storage = FileSystemStorage(location=settings.PROTECTED_MEDIA_ROOT)


class IllegalStateTransitionError(ValueError):
    pass


STATUS_CHOICES = [
    ("draft", "Rascunho"),
    ("submitted", "Enviado"),
    ("admin_screening", "Em triagem"),
    ("assigned_to_reviewers", "Atribuído a revisores"),
    ("under_review", "Em revisão"),
    ("reviews_completed", "Revisões concluídas"),
    ("decision_pending", "Decisão pendente"),
    ("accepted_oral", "Aceito — Oral"),
    ("accepted_poster", "Aceito — Pôster"),
    ("accepted_video", "Aceito — Vídeo"),
    ("rejected", "Rejeitado"),
    ("final_materials_pending", "Materiais finais pendentes"),
    ("ready_for_proceedings", "Pronto para anais"),
    ("published_in_proceedings", "Publicado nos anais"),
]

VALID_TRANSITIONS = {
    "draft": ["submitted"],
    "submitted": ["admin_screening", "draft"],
    "admin_screening": ["assigned_to_reviewers", "rejected"],
    "assigned_to_reviewers": ["under_review"],
    "under_review": ["reviews_completed"],
    "reviews_completed": ["decision_pending"],
    "decision_pending": ["accepted_oral", "accepted_poster", "accepted_video", "rejected"],
    "accepted_oral": ["final_materials_pending"],
    "accepted_poster": ["final_materials_pending"],
    "accepted_video": ["final_materials_pending"],
    "rejected": [],
    "final_materials_pending": ["ready_for_proceedings"],
    "ready_for_proceedings": ["published_in_proceedings"],
    "published_in_proceedings": [],
}

AUTHOR_STATUS_LABELS = {
    "draft": "Rascunho",
    "submitted": "Enviado",
    "admin_screening": "Em triagem",
    "assigned_to_reviewers": "Em avaliação",
    "under_review": "Em avaliação",
    "reviews_completed": "Em avaliação",
    "decision_pending": "Em avaliação",
    "accepted_oral": "Aprovado — Oral",
    "accepted_poster": "Aprovado — Pôster",
    "accepted_video": "Aprovado — Vídeo",
    "rejected": "Rejeitado",
    "final_materials_pending": "Materiais finais pendentes",
    "ready_for_proceedings": "Pronto para anais",
    "published_in_proceedings": "Publicado nos anais",
}


@register_snippet
class ThematicAxis(models.Model):
    name = models.CharField("Nome", max_length=255, unique=True)
    order = models.PositiveIntegerField("Ordem", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Eixo temático"
        verbose_name_plural = "Eixos temáticos"

    def __str__(self):
        return self.name


from submissions.managers import SubmissionQuerySet, SubmissionManager


MODALITY_CHOICES = [
    ("oral", "Oral"),
    ("poster", "Pôster"),
    ("video", "Vídeo"),
]


class Submission(models.Model):
    submission_id = models.CharField(
        "ID da submissão", max_length=20, unique=True, editable=False
    )
    title = models.CharField("Título", max_length=500)
    abstract = models.TextField("Resumo", max_length=2500)
    keywords = models.JSONField("Palavras-chave", default=list)
    thematic_axis = models.ForeignKey(
        ThematicAxis,
        on_delete=models.PROTECT,
        verbose_name="Eixo temático",
        related_name="submissions",
    )
    status = models.CharField(
        "Status", max_length=30, choices=STATUS_CHOICES, default="draft"
    )
    submitter = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="submissions",
        verbose_name="Submetedor",
    )
    final_modality = models.CharField(
        "Modalidade final", max_length=10, choices=MODALITY_CHOICES, blank=True
    )
    decision_notes = models.TextField(
        "Notas da decisão (para o autor)", blank=True
    )
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    objects = SubmissionManager()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Submissão"
        verbose_name_plural = "Submissões"

    def __str__(self):
        return f"{self.submission_id} — {self.title}"

    def clean(self):
        super().clean()
        if len(self.keywords) < 3 or len(self.keywords) > 5:
            raise ValidationError(
                {"keywords": "A submissão deve ter entre 3 e 5 palavras-chave."}
            )
        if len(self.abstract) > 2500:
            raise ValidationError(
                {"abstract": "O resumo não pode ultrapassar 2500 caracteres."}
            )

    def save(self, *args, **kwargs):
        if not self.submission_id:
            self.submission_id = self._generate_submission_id()
        super().save(*args, **kwargs)

    def _generate_submission_id(self):
        year = 2026
        with transaction.atomic():
            last = (
                Submission.objects.filter(submission_id__startswith=f"CBNV-{year}-")
                .order_by("-submission_id")
                .first()
            )
            if last:
                last_number = int(last.submission_id.split("-")[-1])
                next_number = last_number + 1
            else:
                next_number = 1
            return f"CBNV-{year}-{next_number:04d}"

    def transition_to(self, new_status):
        allowed = VALID_TRANSITIONS.get(self.status, [])
        if new_status not in allowed:
            raise IllegalStateTransitionError(
                f"Transição inválida: '{self.status}' → '{new_status}'. "
                f"Transições permitidas: {', '.join(allowed) or 'nenhuma'}"
            )
        self.status = new_status
        self.save(update_fields=["status", "updated_at"])

    def submit(self):
        self.transition_to("submitted")

    def withdraw_to_draft(self):
        self.transition_to("draft")

    @property
    def status_label(self):
        return AUTHOR_STATUS_LABELS.get(self.status, self.status)

    def get_corresponding_author(self):
        return self.authors.filter(is_corresponding=True).first()


class SubmissionAuthor(models.Model):
    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE,
        related_name="authors",
        verbose_name="Submissão",
    )
    first_name = models.CharField("Nome", max_length=150)
    last_name = models.CharField("Sobrenome", max_length=150)
    email = models.EmailField("E-mail")
    institution = models.CharField("Instituição", max_length=255)
    order = models.PositiveIntegerField("Ordem", default=0)
    is_corresponding = models.BooleanField("Autor correspondente", default=False)

    class Meta:
        ordering = ["order"]
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class SubmissionFile(models.Model):
    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE,
        related_name="files",
        verbose_name="Submissão",
    )
    file = models.FileField("Arquivo", storage=protected_storage)
    uploaded_at = models.DateTimeField("Enviado em", auto_now_add=True)

    class Meta:
        verbose_name = "Arquivo da submissão"
        verbose_name_plural = "Arquivos da submissão"

    def __str__(self):
        return f"{self.file.name} (submissão {self.submission.submission_id})"

    @property
    def filename(self):
        return self.file.name.split("/")[-1] if self.file.name else ""

    @property
    def filesize(self):
        if self.file and self.file.size:
            size = self.file.size
            if size < 1024:
                return f"{size} B"
            if size < 1024 * 1024:
                return f"{size / 1024:.1f} KB"
            return f"{size / (1024 * 1024):.1f} MB"
        return ""
