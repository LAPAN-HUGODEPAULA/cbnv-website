from django import forms


class ContactForm(forms.Form):
    SUBJECT_CHOICES = [
        ("geral", "Contato geral"),
        ("submissoes", "Submissões"),
        ("patrocinio", "Patrocínio"),
    ]

    name = forms.CharField(
        label="Nome",
        max_length=255,
        widget=forms.TextInput(attrs={"class": "w-full rounded-lg border border-white/10 bg-cbnv-navy-950 px-4 py-3 text-white placeholder:text-cbnv-text-muted focus:border-cbnv-green-400 focus:outline-none focus:ring-1 focus:ring-cbnv-green-400"}),
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={"class": "w-full rounded-lg border border-white/10 bg-cbnv-navy-950 px-4 py-3 text-white placeholder:text-cbnv-text-muted focus:border-cbnv-green-400 focus:outline-none focus:ring-1 focus:ring-cbnv-green-400"}),
    )
    subject = forms.ChoiceField(
        label="Assunto",
        choices=SUBJECT_CHOICES,
        widget=forms.Select(attrs={"class": "w-full rounded-lg border border-white/10 bg-cbnv-navy-950 px-4 py-3 text-white focus:border-cbnv-green-400 focus:outline-none focus:ring-1 focus:ring-cbnv-green-400"}),
    )
    message = forms.CharField(
        label="Mensagem",
        widget=forms.Textarea(attrs={"rows": 5, "class": "w-full rounded-lg border border-white/10 bg-cbnv-navy-950 px-4 py-3 text-white placeholder:text-cbnv-text-muted focus:border-cbnv-green-400 focus:outline-none focus:ring-1 focus:ring-cbnv-green-400"}),
    )
