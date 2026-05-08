from django import forms
from django.core.exceptions import ValidationError

from .models import Submission, SubmissionAuthor


class AuthorForm(forms.ModelForm):
    class Meta:
        model = SubmissionAuthor
        fields = ("first_name", "last_name", "email", "institution")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-input"}),
            "last_name": forms.TextInput(attrs={"class": "form-input"}),
            "email": forms.EmailInput(attrs={"class": "form-input"}),
            "institution": forms.TextInput(attrs={"class": "form-input"}),
        }


AuthorFormSet = forms.inlineformset_factory(
    Submission,
    SubmissionAuthor,
    form=AuthorForm,
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True,
)


class SubmissionMetadataForm(forms.ModelForm):
    keywords_input = forms.CharField(
        label="Palavras-chave",
        help_text="Separe as palavras-chave por vírgula (mín. 3, máx. 5).",
        required=True,
    )

    class Meta:
        model = Submission
        fields = ("title", "abstract", "thematic_axis")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Título do trabalho",
                }
            ),
            "abstract": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 8,
                    "maxlength": 2500,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["keywords_input"].initial = ", ".join(
                self.instance.keywords or []
            )

    def clean_keywords_input(self):
        raw = self.cleaned_data["keywords_input"]
        keywords = [k.strip() for k in raw.split(",") if k.strip()]
        if len(keywords) < 3 or len(keywords) > 5:
            raise ValidationError(
                "A submissão deve ter entre 3 e 5 palavras-chave."
            )
        return keywords

    def clean_abstract(self):
        abstract = self.cleaned_data["abstract"]
        if len(abstract) > 2500:
            raise ValidationError("O resumo não pode ultrapassar 2500 caracteres.")
        return abstract

    def _post_clean(self):
        if "keywords_input" in self.cleaned_data:
            self.instance.keywords = self.cleaned_data["keywords_input"]
        super()._post_clean()


class SubmissionFileForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ()

    file = forms.FileField(
        label="Arquivo PDF",
        help_text="Envie o arquivo em formato PDF (máx. 10 MB).",
        required=False,
    )

    def clean_file(self):
        f = self.cleaned_data.get("file")
        if not f:
            return None
        if not f.name.lower().endswith(".pdf"):
            raise ValidationError("Apenas arquivos PDF são aceitos.")
        if f.size > 10 * 1024 * 1024:
            raise ValidationError("O arquivo não pode ultrapassar 10 MB.")
        return f
