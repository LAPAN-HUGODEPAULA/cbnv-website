from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="Usuário",
    )
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
        if not (
            self.is_author
            or self.is_reviewer
            or self.is_chair
            or self.user.is_staff
            or self.user.is_superuser
        ):
            raise ValidationError(
                "Todo usuário deve ter pelo menos um papel atribuído "
                "(autor, revisor, comissão científica, staff ou superuser)."
            )

    class Meta:
        verbose_name = "Perfil de usuário"
        verbose_name_plural = "Perfis de usuários"

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    @property
    def has_complete_author_profile(self):
        return bool(
            self.user.first_name.strip()
            and self.user.last_name.strip()
            and self.institution.strip()
            and self.country.strip()
        )


def get_or_create_profile(user):
    if not getattr(user, "is_authenticated", False):
        return None
    if not user.pk:
        return UserProfile(user=user)
    try:
        return user.profile
    except ObjectDoesNotExist:
        profile, _ = UserProfile.objects.get_or_create(user=user)
        return profile


def user_has_role(user, role):
    profile = get_or_create_profile(user)
    return bool(profile and getattr(profile, role, False))


def user_has_complete_author_profile(user):
    profile = get_or_create_profile(user)
    return bool(profile and profile.has_complete_author_profile)


def _profile_property(name):
    def getter(user):
        profile = get_or_create_profile(user)
        return getattr(profile, name) if profile else False

    def setter(user, value):
        profile = get_or_create_profile(user)
        setattr(profile, name, value)
        if user.pk:
            profile.save(update_fields=[name])

    return property(getter, setter)


for _profile_field in (
    "institution",
    "country",
    "position",
    "is_author",
    "is_reviewer",
    "is_chair",
    "consent_privacy",
    "consent_image",
):
    if not hasattr(User, _profile_field):
        setattr(User, _profile_field, _profile_property(_profile_field))

if not hasattr(User, "has_complete_author_profile"):
    User.has_complete_author_profile = property(user_has_complete_author_profile)
