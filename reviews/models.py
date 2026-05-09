from django.conf import settings
from django.db import models

from submissions.models import Submission
from reviews.managers import ReviewerAssignmentManager, ReviewManager


class ReviewerAssignment(models.Model):
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="review_assignments",
        verbose_name="Revisor",
        limit_choices_to={"profile__is_reviewer": True},
    )
    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE,
        related_name="reviewer_assignments",
        verbose_name="Submissão",
    )
    assigned_at = models.DateTimeField("Atribuído em", auto_now_add=True)
    accepted_at = models.DateTimeField("Aceito em", null=True, blank=True)
    declined_at = models.DateTimeField("Recusado em", null=True, blank=True)

    objects = ReviewerAssignmentManager()

    class Meta:
        unique_together = ("reviewer", "submission")
        ordering = ["assigned_at"]
        verbose_name = "Atribuição de revisor"
        verbose_name_plural = "Atribuições de revisores"

    def __str__(self):
        return f"{self.reviewer.get_full_name()} → {self.submission.submission_id}"


RECOMMENDATION_CHOICES = [
    ("accept", "Aceitar"),
    ("reject", "Rejeitar"),
    ("corrections", "Aceitar com correções"),
]


class Review(models.Model):
    assignment = models.OneToOneField(
        ReviewerAssignment,
        on_delete=models.CASCADE,
        related_name="review",
        verbose_name="Atribuição",
    )
    recommendation = models.CharField(
        "Recomendação", max_length=20, choices=RECOMMENDATION_CHOICES
    )
    score = models.IntegerField(
        "Nota (1-5)",
        choices=[(i, str(i)) for i in range(1, 6)],
        null=True,
        blank=True,
        help_text="1 = Ruim, 5 = Excelente",
    )
    comments = models.TextField("Comentários para o autor", blank=True)
    confidential_notes = models.TextField(
        "Notas confidenciais para a comissão", blank=True
    )
    submitted_at = models.DateTimeField("Enviado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)

    objects = ReviewManager()

    class Meta:
        ordering = ["submitted_at"]
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

    def __str__(self):
        return (
            f"Avaliação de {self.assignment.reviewer.get_full_name()} "
            f"({self.get_recommendation_display()})"
        )

    @property
    def reviewer_name(self):
        return self.assignment.reviewer.get_full_name()

    @property
    def submission(self):
        return self.assignment.submission
