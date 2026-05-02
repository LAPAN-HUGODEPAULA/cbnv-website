from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField("Nome completo", max_length=255, blank=True)
    institution = models.CharField("Instituição", max_length=255, blank=True)
    country = models.CharField("País", max_length=2, blank=True)
    position = models.CharField("Vínculo/Cargo", max_length=255, blank=True)
    is_author = models.BooleanField("Autor", default=False)
    is_reviewer = models.BooleanField("Revisor", default=False)
    is_chair = models.BooleanField("Comissão Científica", default=False)
    consent_privacy = models.BooleanField("Consentimento de privacidade", default=False)
    consent_image = models.BooleanField("Consentimento de uso de imagem", default=False)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.full_name or self.username
