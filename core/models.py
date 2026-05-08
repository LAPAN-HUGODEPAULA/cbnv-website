from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.models import TranslatableMixin
from wagtail.fields import StreamField
from wagtail import blocks


@register_setting
class CoreSettings(TranslatableMixin, BaseSiteSetting):
    event_name = models.CharField("Nome do Evento", max_length=255, default="CBNV 2026")
    edition = models.CharField("Edição", max_length=10, default="XII")
    theme = models.CharField("Tema", max_length=255, default="Neurovisão na Era da Inteligência Artificial")
    dates = models.CharField("Datas", max_length=255, default="11 a 13 de novembro de 2026")
    location = models.CharField("Local", max_length=255, default="CAD-1 — UFMG, Belo Horizonte, MG")
    contact_email = models.EmailField("E-mail de Contato", blank=True)
    registration_link = models.URLField("Link de Inscrição", blank=True)
    livestream_link = models.URLField("Link de Transmissão", blank=True)
    fapemig_text = models.TextField("Texto FAPEMIG", blank=True)
    instagram_url = models.URLField("Instagram", blank=True)
    youtube_url = models.URLField("YouTube", blank=True)
    twitter_url = models.URLField("X / Twitter", blank=True)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Logotipo"
    )

    panels = [
        FieldPanel("event_name"),
        FieldPanel("edition"),
        FieldPanel("theme"),
        FieldPanel("dates"),
        FieldPanel("location"),
        FieldPanel("logo"),
        FieldPanel("contact_email"),
        FieldPanel("registration_link"),
        FieldPanel("livestream_link"),
        FieldPanel("fapemig_text"),
        FieldPanel("instagram_url"),
        FieldPanel("youtube_url"),
        FieldPanel("twitter_url"),
    ]

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
