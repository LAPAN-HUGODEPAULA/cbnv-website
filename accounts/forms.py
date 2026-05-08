from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


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
        self.instance.is_author = True
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_author = True
        user.institution = self.cleaned_data["institution"]
        user.country = self.cleaned_data["country"]
        user.position = self.cleaned_data["position"]
        user.consent_privacy = self.cleaned_data["consent_privacy"]
        user.consent_image = self.cleaned_data["consent_image"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "institution", "country", "position")
