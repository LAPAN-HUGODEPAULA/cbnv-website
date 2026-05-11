from django.core.exceptions import ValidationError
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import TranslatableMixin
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


class SponsorQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status=Sponsor.Status.ACTIVE)

    def for_home(self):
        return self.active().filter(show_on_home=True)

    def for_footer(self):
        return self.active().filter(show_in_footer=True)

    def for_about(self):
        return self.active().filter(show_on_about=True)

    def for_sponsorship(self):
        return self.active().filter(show_on_sponsorship=True)


@register_snippet
class Sponsor(TranslatableMixin, models.Model):
    class Category(models.TextChoices):
        INSTITUTIONAL_PARTNER = "institutional_partner", "Parceiro institucional"
        FUNDING_AGENCY = "funding_agency", "Agência de fomento"
        SCIENTIFIC_PARTNER = "scientific_partner", "Parceiro científico"
        SUPPORT = "support", "Apoio"
        SPONSOR = "sponsor", "Patrocinador"
        ORGANIZING_INSTITUTION = "organizing_institution", "Instituição organizadora"

    class Status(models.TextChoices):
        ACTIVE = "active", "Ativo"
        HIDDEN = "hidden", "Oculto"
        ARCHIVED = "archived", "Arquivado"

    name = models.CharField("Nome", max_length=255)
    category = models.CharField(
        "Categoria",
        max_length=40,
        choices=Category.choices,
        default=Category.SPONSOR,
    )
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
    description = models.TextField("Descrição", blank=True)
    status = models.CharField(
        "Status",
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
    show_on_home = models.BooleanField("Exibir na Home", default=False)
    show_in_footer = models.BooleanField("Exibir no rodapé", default=False)
    show_on_about = models.BooleanField("Exibir em Sobre", default=False)
    show_on_sponsorship = models.BooleanField("Exibir em Patrocínio", default=True)
    sort_order = models.IntegerField("Ordem de exibição", default=0)
    logo_alt_text = models.CharField(
        "Texto alternativo do logotipo",
        max_length=255,
        blank=True,
        help_text="Descreva o logotipo para tecnologias assistivas quando houver imagem.",
    )

    objects = SponsorQuerySet.as_manager()

    panels = [
        FieldPanel("name"),
        FieldPanel("category"),
        FieldPanel("tier"),
        FieldPanel("logo"),
        FieldPanel("logo_alt_text"),
        FieldPanel("url"),
        FieldPanel("description"),
        FieldPanel("status"),
        FieldPanel("show_on_home"),
        FieldPanel("show_in_footer"),
        FieldPanel("show_on_about"),
        FieldPanel("show_on_sponsorship"),
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

    def clean(self):
        super().clean()
        if self.logo_id and not self.logo_alt_text:
            raise ValidationError({"logo_alt_text": "Informe o texto alternativo quando houver logotipo."})
