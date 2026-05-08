from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel
from wagtail.models import Orderable, TranslatableMixin
from wagtail.snippets.models import register_snippet


@register_snippet
class SponsorTier(TranslatableMixin, models.Model):
    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField(unique=True)
    weight = models.PositiveIntegerField(
        default=2, 
        help_text="Peso visual no grid (ex: 1=Diamante/Grande, 4=Apoio/Pequeno)"
    )
    sort_order = models.PositiveIntegerField(default=0)

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
        FieldPanel("weight"),
        FieldPanel("sort_order"),
    ]

    class Meta:
        ordering = ["sort_order"]
        verbose_name = "Nível de Patrocínio"
        verbose_name_plural = "Níveis de Patrocínio"
        constraints = [
            models.UniqueConstraint(
                fields=("translation_key", "locale"),
                name="unique_translation_key_locale_sponsors_sponsortier",
            )
        ]

    def __str__(self):
        return self.name


@register_snippet
class Sponsor(TranslatableMixin, models.Model):
# ... (omitting for brevity, but I will provide full replacement for Sponsor class)
    name = models.CharField("Nome", max_length=255)
    tier = models.ForeignKey(
        SponsorTier, 
        on_delete=models.PROTECT, 
        related_name="sponsors", 
        verbose_name="Nível",
        null=True,
        blank=True
    )
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Logotipo",
    )
    url = models.URLField("URL", blank=True)
    sort_order = models.IntegerField("Ordem de exibição", default=0)

    panels = [
        FieldPanel("name"),
        FieldPanel("tier"),
        FieldPanel("logo"),
        FieldPanel("url"),
        FieldPanel("sort_order"),
    ]

    class Meta:
        ordering = ["tier__sort_order", "sort_order", "name"]
        verbose_name = "Patrocinador"
        verbose_name_plural = "Patrocinadores"
        constraints = [
            models.UniqueConstraint(
                fields=("translation_key", "locale"),
                name="unique_translation_key_locale_sponsors_sponsor",
            )
        ]

    def __str__(self):
        return self.name
