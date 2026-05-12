from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import UserProfile, get_or_create_profile

User = get_user_model()


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nome",
        max_length=150,
        widget=forms.TextInput(attrs={"autofocus": True}),
    )
    last_name = forms.CharField(
        label="Sobrenome",
        max_length=150,
    )
    institution = forms.CharField(
        label="Instituição",
        max_length=255,
        required=True,
    )
    country = forms.ChoiceField(
        label="País",
        required=True,
    )
    position = forms.CharField(
        label="Vínculo/Cargo",
        max_length=255,
        required=True,
    )
    consent_privacy = forms.BooleanField(
        label="Li e concordo com a Política de Privacidade.",
        required=True,
    )
    consent_image = forms.BooleanField(
        label="Autorizo o uso de minha imagem para divulgação do evento.",
        required=False,
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"autofocus": False})
        self.fields["email"].required = True
        self.fields["country"].choices = self._get_country_choices()

    @staticmethod
    def _get_country_choices():
        from django_countries import countries

        return [("", "Selecione...")] + list(countries)

    def clean(self):
        cleaned = super().clean()
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.update_or_create(
                user=user,
                defaults={
                    "institution": self.cleaned_data["institution"],
                    "country": self.cleaned_data["country"],
                    "position": self.cleaned_data["position"],
                    "is_author": True,
                    "consent_privacy": self.cleaned_data["consent_privacy"],
                    "consent_image": self.cleaned_data["consent_image"],
                },
            )
        return user

    @property
    def role_fields(self):
        return ("is_author",)


class ProfileForm(forms.Form):
    first_name = forms.CharField(label="Nome", max_length=150, required=True)
    last_name = forms.CharField(label="Sobrenome", max_length=150, required=True)
    email = forms.EmailField(label="E-mail", required=True)
    institution = forms.CharField(label="Instituição", max_length=255, required=True)
    country = forms.ChoiceField(label="País", required=True)
    position = forms.CharField(label="Vínculo/Cargo", max_length=255, required=True)

    def __init__(self, *args, instance=None, **kwargs):
        self.instance = instance
        initial = kwargs.pop("initial", {})
        if instance is not None:
            profile = get_or_create_profile(instance)
            initial = {
                **initial,
                "first_name": instance.first_name,
                "last_name": instance.last_name,
                "email": instance.email,
                "institution": profile.institution if profile else "",
                "country": profile.country if profile else "",
                "position": profile.position if profile else "",
            }
        super().__init__(*args, initial=initial, **kwargs)
        self.fields["country"].choices = RegistrationForm._get_country_choices()

    def save(self):
        user = self.instance
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.save(update_fields=["first_name", "last_name", "email"])
        profile = get_or_create_profile(user)
        profile.institution = self.cleaned_data["institution"]
        profile.country = self.cleaned_data["country"]
        profile.position = self.cleaned_data["position"]
        profile.save(update_fields=["institution", "country", "position"])
        return user
