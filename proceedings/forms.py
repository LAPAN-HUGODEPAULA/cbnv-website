from django import forms
from django.core.exceptions import ValidationError

from .models import FinalMaterial


class FinalMaterialForm(forms.ModelForm):
    class Meta:
        model = FinalMaterial
        fields = ("final_pdf", "presentation_file", "video_url")

    def __init__(self, *args, show_video=True, **kwargs):
        super().__init__(*args, **kwargs)
        if not show_video:
            self.fields.pop("video_url")

    def clean_final_pdf(self):
        f = self.cleaned_data.get("final_pdf")
        if not f:
            return f
        if not f.name.lower().endswith(".pdf"):
            raise ValidationError("Apenas arquivos PDF são aceitos.")
        if f.size > 10 * 1024 * 1024:
            raise ValidationError("O PDF final não pode ultrapassar 10 MB.")
        return f

    def clean_presentation_file(self):
        f = self.cleaned_data.get("presentation_file")
        if not f:
            return f
        ext = f.name.lower().split(".")[-1]
        if ext not in ("pdf", "pptx"):
            raise ValidationError("Apenas arquivos PDF ou PPTX são aceitos.")
        if f.size > 50 * 1024 * 1024:
            raise ValidationError("A apresentação não pode ultrapassar 50 MB.")
        return f

    def clean_video_url(self):
        url = self.cleaned_data.get("video_url")
        if not url:
            return url
        from videos.models import parse_youtube_url

        parsed = parse_youtube_url(url)
        if not parsed.get("type"):
            raise ValidationError("Informe uma URL válida do YouTube.")
        return url
