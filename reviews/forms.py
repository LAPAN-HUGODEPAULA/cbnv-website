from django import forms

from .models import RECOMMENDATION_CHOICES, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["recommendation", "score", "comments", "confidential_notes"]
        widgets = {
            "comments": forms.Textarea(attrs={"rows": 6}),
            "confidential_notes": forms.Textarea(attrs={"rows": 4}),
        }
