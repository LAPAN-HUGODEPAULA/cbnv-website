from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.models import TranslatableMixin
from wagtail.fields import StreamField
from wagtail import blocks


@register_setting
class CoreSettings(TranslatableMixin, BaseSiteSetting):
    class LinkStatus(models.TextChoices):
        AVAILABLE = "available", "Disponível"
        COMING_SOON = "coming_soon", "Em breve"
        UNAVAILABLE = "unavailable", "Indisponível"

    event_name = models.CharField("Nome do Evento", max_length=255, default="CBNV 2026")
    short_event_name = models.CharField("Nome curto", max_length=80, blank=True, default="CBNV 2026")
    edition = models.CharField("Edição", max_length=10, default="XII")
    theme = models.CharField("Tema", max_length=255, default="Neurovisão na Era da Inteligência Artificial")
    dates = models.CharField("Datas", max_length=255, default="11 a 13 de novembro de 2026")
    start_date = models.DateField("Data de início", null=True, blank=True)
    end_date = models.DateField("Data de término", null=True, blank=True)
    location = models.CharField("Local", max_length=255, default="CAD-1 — UFMG, Belo Horizonte, MG")
    city = models.CharField("Cidade", max_length=120, blank=True, default="Belo Horizonte")
    state = models.CharField("Estado", max_length=80, blank=True, default="Minas Gerais")
    country = models.CharField("País", max_length=80, blank=True, default="Brasil")
    venue_name = models.CharField("Nome do local", max_length=255, blank=True)
    venue_short_name = models.CharField("Nome curto do local", max_length=120, blank=True)
    venue_address = models.TextField("Endereço oficial do local", blank=True)
    venue_access_notes = models.TextField("Orientações de acesso", blank=True)
    format_label = models.CharField("Formato", max_length=80, blank=True, default="Presencial")
    contact_email = models.EmailField("E-mail de Contato", blank=True)
    submissions_contact_email = models.EmailField("E-mail para submissões", blank=True)
    sponsorship_contact_email = models.EmailField("E-mail para patrocínios", blank=True)
    registration_link = models.URLField("Link de Inscrição", blank=True)
    registration_status = models.CharField(
        "Status das inscrições",
        max_length=20,
        choices=LinkStatus.choices,
        default=LinkStatus.COMING_SOON,
        help_text="Controla se o CTA de inscrição deve aparecer como link ativo ou como 'em breve'.",
    )
    registration_early_bird_deadline = models.DateField(
        "Prazo lote 1 (early bird)",
        null=True,
        blank=True,
        help_text="Data limite para o lote 1 de inscrição.",
    )
    registration_early_bird_label = models.CharField(
        "Rótulo lote 1",
        max_length=60,
        blank=True,
        default="Lote 1",
    )
    registration_late_label = models.CharField(
        "Rótulo lote 2",
        max_length=60,
        blank=True,
        default="Lote 2",
    )
    registration_notes = models.TextField(
        "Observações sobre inscrição",
        blank=True,
        help_text="Informações adicionais exibidas na página de inscrição.",
    )
    livestream_link = models.URLField("Link de Transmissão", blank=True)
    livestream_status = models.CharField(
        "Status da transmissão",
        max_length=20,
        choices=LinkStatus.choices,
        default=LinkStatus.COMING_SOON,
        help_text="Controla se a transmissão deve aparecer como link ativo, em breve ou indisponível.",
    )
    fapemig_text = models.TextField("Texto FAPEMIG", blank=True)
    fapemig_logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Logotipo FAPEMIG",
    )
    instagram_url = models.URLField("Instagram", blank=True)
    youtube_url = models.URLField("YouTube", blank=True)
    youtube_channel_url = models.URLField("Canal do YouTube", blank=True)
    youtube_playlist_url = models.URLField("Playlist do YouTube", blank=True)
    twitter_url = models.URLField("X / Twitter", blank=True)
    google_maps_url = models.URLField("Google Maps", blank=True)
    default_seo_title = models.CharField("Título SEO padrão", max_length=255, blank=True)
    default_seo_description = models.TextField("Descrição SEO padrão", blank=True)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Logotipo"
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("event_name"),
                FieldPanel("short_event_name"),
                FieldPanel("edition"),
                FieldPanel("theme"),
                FieldPanel("logo"),
            ],
            heading="Identidade do evento",
        ),
        MultiFieldPanel(
            [
                FieldPanel("dates"),
                FieldPanel("start_date"),
                FieldPanel("end_date"),
                FieldPanel("format_label"),
                FieldPanel("location"),
                FieldPanel("city"),
                FieldPanel("state"),
                FieldPanel("country"),
                FieldPanel("venue_name"),
                FieldPanel("venue_short_name"),
                FieldPanel("venue_address"),
                FieldPanel("venue_access_notes"),
                FieldPanel("google_maps_url"),
            ],
            heading="Datas, formato e local",
        ),
        MultiFieldPanel(
            [
                FieldPanel("contact_email"),
                FieldPanel("submissions_contact_email"),
                FieldPanel("sponsorship_contact_email"),
            ],
            heading="Contatos",
        ),
        MultiFieldPanel(
            [
                FieldPanel("registration_status"),
                FieldPanel("registration_link"),
                FieldPanel("registration_early_bird_deadline"),
                FieldPanel("registration_early_bird_label"),
                FieldPanel("registration_late_label"),
                FieldPanel("registration_notes"),
                FieldPanel("livestream_status"),
                FieldPanel("livestream_link"),
                FieldPanel("instagram_url"),
                FieldPanel("youtube_url"),
                FieldPanel("youtube_channel_url"),
                FieldPanel("youtube_playlist_url"),
                FieldPanel("twitter_url"),
            ],
            heading="Links públicos",
        ),
        MultiFieldPanel(
            [
                FieldPanel("fapemig_text"),
                FieldPanel("fapemig_logo"),
            ],
            heading="Apoio institucional",
        ),
        MultiFieldPanel(
            [
                FieldPanel("default_seo_title"),
                FieldPanel("default_seo_description"),
            ],
            heading="SEO padrão",
        ),
    ]

    class Meta:
        verbose_name = "Configurações centrais do site"
        constraints = [
            models.UniqueConstraint(
                fields=("translation_key", "locale"),
                name="unique_translation_key_locale_core_coresettings",
            )
        ]

    @property
    def registration_is_available(self):
        return self.registration_status == self.LinkStatus.AVAILABLE and bool(self.registration_link)

    @property
    def livestream_is_available(self):
        return self.livestream_status == self.LinkStatus.AVAILABLE and bool(self.livestream_link)

    @property
    def primary_youtube_url(self):
        return self.youtube_channel_url or self.youtube_url

    @property
    def canonical_venue(self):
        data = {
            "name": self.venue_name,
            "short_name": self.venue_short_name,
            "address": self.venue_address,
            "location": self.location,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "google_maps_url": self.google_maps_url,
            "access_notes": self.venue_access_notes,
        }
        return {key: value for key, value in data.items() if value}

@register_setting
class SiteMenu(TranslatableMixin, BaseSiteSetting):
    menu_items = StreamField([
        ('link', blocks.StructBlock([
            ('label', blocks.CharBlock(label="Rótulo")),
            ('page', blocks.PageChooserBlock(required=False, label="Página")),
            ('url', blocks.URLBlock(required=False, label="URL Externa")),
            ('anchor', blocks.CharBlock(required=False, label="Âncora", help_text="Ex: #sobre")),
        ]))
    ], use_json_field=True, verbose_name="Itens do Menu")

    panels = [
        FieldPanel("menu_items"),
    ]

    class Meta:
        verbose_name = "Menu do Site"
        constraints = [
            models.UniqueConstraint(
                fields=("translation_key", "locale"),
                name="unique_translation_key_locale_core_sitemenu",
            )
        ]
