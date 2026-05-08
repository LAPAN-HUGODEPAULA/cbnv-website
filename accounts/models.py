from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    institution = models.CharField("Instituição", max_length=255, blank=True)
    country = models.CharField("País", max_length=2, blank=True)
    position = models.CharField("Vínculo/Cargo", max_length=255, blank=True)
    is_author = models.BooleanField("Autor", default=False)
    is_reviewer = models.BooleanField("Revisor", default=False)
    is_chair = models.BooleanField("Comissão Científica", default=False)
    consent_privacy = models.BooleanField("Consentimento de privacidade", default=False)
    consent_image = models.BooleanField("Consentimento de uso de imagem", default=False)

    def clean(self):
        super().clean()
        if not (self.is_author or self.is_reviewer or self.is_chair
                or self.is_staff or self.is_superuser):
            from django.core.exceptions import ValidationError
            raise ValidationError(
                "Todo usuário deve ter pelo menos um papel atribuído "
                "(autor, revisor, comissão científica, staff ou superuser)."
            )

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.get_full_name() or self.username

    @property
    def has_complete_author_profile(self):
        return bool(
            self.first_name.strip()
            and self.last_name.strip()
            and self.institution.strip()
            and self.country.strip()
        )
