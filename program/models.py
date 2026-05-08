from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import TranslatableMixin
from wagtail.snippets.models import register_snippet

# --- Choices ---

RECEPTION = "reception"
OPENING_CEREMONY = "opening_ceremony"
KEYNOTE = "keynote"
TALK = "talk"
THEMATIC_SESSION = "thematic_session"
POSTER = "poster"
ORAL = "oral"
ROUNDTABLE = "roundtable"
BREAK = "break"
CLOSING_CEREMONY = "closing_ceremony"
AWARDS = "awards"

ACTIVITY_TYPE_CHOICES = [
    (RECEPTION, "Recepção"),
    (OPENING_CEREMONY, "Mesa Solene"),
    (KEYNOTE, "Conferência Plenária"),
    (TALK, "Palestra"),
    (THEMATIC_SESSION, "Sessão Temática"),
    (POSTER, "Sessão de Pôsteres"),
    (ORAL, "Apresentação Oral"),
    (ROUNDTABLE, "Mesa-Redonda"),
    (BREAK, "Intervalo"),
    (CLOSING_CEREMONY, "Encerramento"),
    (AWARDS, "Premiação"),
]

IN_PERSON = "in_person"
HYBRID = "hybrid"
ONLINE = "online"

FORMAT_CHOICES = [
    (IN_PERSON, "Presencial"),
    (HYBRID, "Híbrido"),
    (ONLINE, "Online"),
]

DRAFT = "draft"
PUBLISHED = "published"
PENDING = "pending"
CANCELLED = "cancelled"

SESSION_STATUS_CHOICES = [
    (DRAFT, "Rascunho"),
    (PUBLISHED, "Publicado"),
    (PENDING, "Pendente"),
    (CANCELLED, "Cancelado"),
]

CONFIRMED = "confirmed"
INVITED = "invited"
HIDDEN = "hidden"

SPEAKER_STATUS_CHOICES = [
    (CONFIRMED, "Confirmado"),
    (INVITED, "Convidado"),
    (PENDING, "Pendente"),
    (HIDDEN, "Oculto"),
]

# --- Badge variant mapping per activity type ---

ACTIVITY_BADGE_VARIANT = {
    KEYNOTE: "confirmed",
    TALK: "info",
    THEMATIC_SESSION: "info",
    POSTER: "pending",
    ORAL: "draft",
    ROUNDTABLE: "review",
    RECEPTION: "draft",
    OPENING_CEREMONY: "confirmed",
    CLOSING_CEREMONY: "confirmed",
    AWARDS: "confirmed",
    BREAK: "draft",
}


@register_snippet
class Speaker(TranslatableMixin, models.Model):
    name = models.CharField("Nome", max_length=255)
    display_name = models.CharField("Nome de exibição", max_length=255, blank=True)
    title = models.CharField("Título", max_length=50, blank=True, help_text="Ex: Prof., Dr., Profa. Dra.")
    institution = models.CharField("Instituição", max_length=255, blank=True)
    country = models.CharField("País", max_length=2, blank=True)
    bio = models.TextField("Mini-bio", blank=True)
    photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Foto",
    )
    lattes_url = models.URLField("Lattes", blank=True)
    status = models.CharField("Status", max_length=15, choices=SPEAKER_STATUS_CHOICES, default=PENDING)
    sort_order = models.IntegerField("Ordem", default=0)

    panels = [
        FieldPanel("name"),
        FieldPanel("display_name"),
        FieldPanel("title"),
        FieldPanel("institution"),
        FieldPanel("country"),
        FieldPanel("bio"),
        FieldPanel("photo"),
        FieldPanel("lattes_url"),
        FieldPanel("status"),
        FieldPanel("sort_order"),
    ]

    class Meta:
        ordering = ["sort_order", "name"]
        verbose_name = "Palestrante"
        verbose_name_plural = "Palestrantes"
        constraints = [
            models.UniqueConstraint(
                fields=("translation_key", "locale"),
                name="unique_translation_key_locale_program_speaker",
            )
        ]

    def __str__(self):
        parts = []
        if self.title:
            parts.append(self.title)
        parts.append(self.display_name or self.name)
        return " ".join(parts)

    def display_institution(self):
        if self.institution:
            parts = [self.institution]
            if self.country:
                parts.append(self.country.upper())
            return " — ".join(parts)
        return ""


@register_snippet
class ProgramDay(TranslatableMixin, models.Model):
    date = models.DateField("Data")
    title = models.CharField("Título", max_length=255)
    subtitle = models.CharField("Subtítulo", max_length=255, blank=True)
    description = models.TextField("Descrição", blank=True)
    sort_order = models.IntegerField("Ordem", default=0)

    panels = [
        FieldPanel("date"),
        FieldPanel("title"),
        FieldPanel("subtitle"),
        FieldPanel("description"),
        FieldPanel("sort_order"),
    ]

    class Meta:
        ordering = ["sort_order", "date"]
        verbose_name = "Dia do Programa"
        verbose_name_plural = "Dias do Programa"
        constraints = [
            models.UniqueConstraint(
                fields=("translation_key", "locale"),
                name="unique_translation_key_locale_program_programday",
            )
        ]

    def __str__(self):
        return f"{self.date.strftime('%d/%m')} — {self.title}"


@register_snippet
class ProgramSession(TranslatableMixin, models.Model):
    day = models.ForeignKey(ProgramDay, on_delete=models.CASCADE, related_name="sessions", verbose_name="Dia")
    start_time = models.TimeField("Horário início")
    end_time = models.TimeField("Horário fim")
    title = models.CharField("Título", max_length=255)
    activity_type = models.CharField("Tipo de atividade", max_length=20, choices=ACTIVITY_TYPE_CHOICES)
    description = models.TextField("Descrição", blank=True)
    room = models.CharField("Sala/Local", max_length=100, blank=True)
    format = models.CharField("Formato", max_length=15, choices=FORMAT_CHOICES, default=IN_PERSON)
    thematic_axis = models.CharField("Eixo temático", max_length=255, blank=True)
    status = models.CharField("Status", max_length=15, choices=SESSION_STATUS_CHOICES, default=DRAFT)
    sort_order = models.IntegerField("Ordem", default=0)

    panels = [
        FieldPanel("day"),
        FieldPanel("start_time"),
        FieldPanel("end_time"),
        FieldPanel("title"),
        FieldPanel("activity_type"),
        FieldPanel("description"),
        FieldPanel("room"),
        FieldPanel("format"),
        FieldPanel("thematic_axis"),
        FieldPanel("status"),
        FieldPanel("sort_order"),
    ]

    class Meta:
        ordering = ["day", "sort_order", "start_time"]
        verbose_name = "Sessão"
        verbose_name_plural = "Sessões"
        constraints = [
            models.UniqueConstraint(
                fields=("translation_key", "locale"),
                name="unique_translation_key_locale_program_programsession",
            )
        ]

    def __str__(self):
        return f"{self.start_time.strftime('%H:%M')} {self.title}"

    @property
    def badge_variant(self):
        return ACTIVITY_BADGE_VARIANT.get(self.activity_type, "info")

    @property
    def time_range(self):
        return f"{self.start_time.strftime('%H:%M')} – {self.end_time.strftime('%H:%M')}"


@register_snippet
class ProgramTalk(TranslatableMixin, models.Model):
    session = models.ForeignKey(ProgramSession, on_delete=models.CASCADE, related_name="talks", verbose_name="Sessão")
    speaker = models.ForeignKey(
        Speaker,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="talks",
        verbose_name="Palestrante",
    )
    title = models.CharField("Título", max_length=255)
    description = models.TextField("Descrição", blank=True)
    status = models.CharField("Status do palestrante", max_length=15, choices=SPEAKER_STATUS_CHOICES, default=PENDING)
    sort_order = models.IntegerField("Ordem", default=0)

    panels = [
        FieldPanel("session"),
        FieldPanel("speaker"),
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("status"),
        FieldPanel("sort_order"),
    ]

    class Meta:
        ordering = ["session", "sort_order"]
        verbose_name = "Fala/Apresentação"
        verbose_name_plural = "Falas/Apresentações"
        constraints = [
            models.UniqueConstraint(
                fields=("translation_key", "locale"),
                name="unique_translation_key_locale_program_programtalk",
            )
        ]

    def __str__(self):
        return self.title

    @property
    def is_visible(self):
        return self.status == CONFIRMED
