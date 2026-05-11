from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.models import Page, TranslatableMixin
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from core.blocks import BentoGridBlock, StatBlock, TimelineBlock
from pages.content import (
    ABOUT_CONTENT,
    ORGANIZATIONS,
    ORGANIZING_COMMITTEE,
    PREVIOUS_EDITIONS_FALLBACK,
    dedupe_editions,
)


class AnnouncementQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=Announcement.Status.PUBLISHED, published_at__lte=timezone.now())

    def featured(self):
        return self.published().filter(featured_on_home=True)

    def recent(self):
        return self.published().order_by("-pinned", "-published_at", "title")


@register_snippet
class Announcement(TranslatableMixin, models.Model):
    class Category(models.TextChoices):
        GENERAL = "general", "Geral"
        REGISTRATION = "registration", "Inscrições"
        SUBMISSIONS = "submissions", "Submissões"
        PROGRAM = "program", "Programação"
        INSTITUTIONAL = "institutional", "Institucional"

    class Status(models.TextChoices):
        DRAFT = "draft", "Rascunho"
        PUBLISHED = "published", "Publicado"
        ARCHIVED = "archived", "Arquivado"

    title = models.CharField("Título", max_length=255)
    slug = models.SlugField("Slug", max_length=255, unique=True, blank=True)
    summary = models.CharField("Resumo", max_length=300, blank=True)
    body = RichTextField("Corpo", blank=True)
    category = models.CharField(
        "Categoria",
        max_length=32,
        choices=Category.choices,
        default=Category.GENERAL,
    )
    published_at = models.DateTimeField("Data de publicação", null=True, blank=True)
    status = models.CharField(
        "Status",
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    featured_on_home = models.BooleanField("Destaque na Home", default=False)
    pinned = models.BooleanField("Fixar no topo", default=False)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Imagem",
    )
    external_url = models.URLField("URL externa", blank=True)
    seo_title = models.CharField("Título SEO", max_length=255, blank=True)
    seo_description = models.TextField("Descrição SEO", blank=True)

    objects = AnnouncementQuerySet.as_manager()

    panels = [
        FieldPanel("title"),
        FieldPanel("slug"),
        FieldPanel("summary"),
        FieldPanel("body"),
        MultiFieldPanel(
            [
                FieldPanel("category"),
                FieldPanel("status"),
                FieldPanel("published_at"),
                FieldPanel("featured_on_home"),
                FieldPanel("pinned"),
            ],
            heading="Publicação e destaque",
        ),
        FieldPanel("image"),
        FieldPanel("external_url"),
        MultiFieldPanel(
            [
                FieldPanel("seo_title"),
                FieldPanel("seo_description"),
            ],
            heading="SEO",
        ),
    ]

    class Meta:
        ordering = ["-pinned", "-published_at", "title"]
        verbose_name = "Notícia ou comunicado"
        verbose_name_plural = "Notícias e comunicados"
        constraints = [
            models.UniqueConstraint(
                fields=("translation_key", "locale"),
                name="unique_translation_key_locale_pages_announcement",
            )
        ]

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if self.status == self.Status.PUBLISHED and not self.published_at:
            raise ValidationError({"published_at": "Informe a data de publicação para conteúdo publicado."})
        slug = self.slug or slugify(self.title)
        if slug:
            qs = Announcement.objects.filter(slug=slug)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            if qs.exists():
                raise ValidationError({"slug": "Já existe um comunicado com este slug."})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class HomePage(Page):
    intro = models.TextField("Introdução", blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Imagem de Destaque"
    )
    cta_text = models.CharField("Texto do CTA", max_length=255, blank=True, default="Inscreva-se")
    cta_link = models.URLField("Link do CTA", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("hero_image"),
        MultiFieldPanel(
            [FieldPanel("cta_text"), FieldPanel("cta_link")],
            heading="Call to Action",
        ),
    ]

    class Meta:
        verbose_name = "Página Inicial"

    parent_page_types = []
    subpage_types = [
        "pages.AboutPage",
        "pages.NewsIndexPage",
        "pages.PreviousEditionsPage",
        "pages.ProgramPage",
        "pages.RegistrationPage",
        "pages.SubmissionsPage",
        "pages.SponsorsPage",
        "pages.VideoGalleryPage",
    ]

    def get_context(self, request, *args, **kwargs):
        ctx = super().get_context(request, *args, **kwargs)

        # Child pages for hub
        ctx["about_page"] = self.get_children().live().type(AboutPage).first()
        ctx["program_page"] = self.get_children().live().type(ProgramPage).first()
        ctx["submissions_page"] = self.get_children().live().type(SubmissionsPage).first()
        ctx["registration_page"] = self.get_children().live().type(RegistrationPage).first()
        ctx["sponsors_page"] = self.get_children().live().type(SponsorsPage).first()
        ctx["organizations"] = ORGANIZATIONS
        
        # Featured news
        news_index = NewsIndexPage.objects.live().first()
        if news_index:
            ctx["featured_news"] = news_index.get_children().live().order_by("-first_published_at")[:3]
            
        return ctx


class AboutPage(Page):
    body = StreamField([
        ('text', blocks.RichTextBlock()),
        ('bento_grid', BentoGridBlock()),
        ('stats', blocks.ListBlock(StatBlock())),
        ('timeline', TimelineBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Página Sobre"

    parent_page_types = ["pages.HomePage"]
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        ctx = super().get_context(request, *args, **kwargs)
        ctx["about_content"] = ABOUT_CONTENT
        ctx["organizations"] = ORGANIZATIONS
        ctx["committee_members"] = ORGANIZING_COMMITTEE
        return ctx


class NewsIndexPage(Page):
    intro = models.TextField("Introdução", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    class Meta:
        verbose_name = "Índice de Notícias"

    parent_page_types = ["pages.HomePage"]
    subpage_types = ["pages.NewsArticlePage"]

    def get_context(self, request, *args, **kwargs):
        ctx = super().get_context(request, *args, **kwargs)
        all_articles = self.get_children().live().order_by("-first_published_at")
        paginator = Paginator(all_articles, 10)
        page = request.GET.get("page")
        try:
            ctx["articles"] = paginator.page(page)
        except (PageNotAnInteger, EmptyPage):
            ctx["articles"] = paginator.page(1)
        return ctx


class NewsArticlePage(Page):
    summary = models.CharField("Resumo", max_length=255, blank=True)
    body = StreamField([
        ('text', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('video', blocks.URLBlock(help_text="YouTube link", required=False)),
    ], use_json_field=True, blank=True)
    featured = models.BooleanField("Destaque na Home", default=False)

    content_panels = Page.content_panels + [
        FieldPanel("summary"),
        FieldPanel("body"),
        FieldPanel("featured"),
    ]

    class Meta:
        verbose_name = "Notícia"

    parent_page_types = ["pages.NewsIndexPage"]
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        ctx = super().get_context(request, *args, **kwargs)
        ctx["news_index"] = self.get_parent()
        return ctx


class RegistrationPage(Page):
    STATUS_CHOICES = [
        ('coming_soon', 'Em breve'),
        ('open', 'Inscrições Abertas'),
        ('closed', 'Inscrições Encerradas'),
    ]
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default='coming_soon')
    intro = models.TextField("Introdução", blank=True)
    body = StreamField([
        ('text', blocks.RichTextBlock()),
        ('bento_grid', BentoGridBlock()),
    ], use_json_field=True, blank=True, verbose_name="Corpo")
    external_registration_url = models.URLField("URL Externa de Inscrição", blank=True, help_text="Link para a plataforma externa de inscrições")

    content_panels = Page.content_panels + [
        FieldPanel("status"),
        FieldPanel("intro"),
        FieldPanel("body"),
        FieldPanel("external_registration_url"),
    ]

    class Meta:
        verbose_name = "Página de Inscrição"

    parent_page_types = ["pages.HomePage"]
    subpage_types = []


class SubmissionsPage(Page):
    STATUS_CHOICES = [
        ('coming_soon', 'Em breve'),
        ('open', 'Submissões Abertas'),
        ('closed', 'Submissões Encerradas'),
    ]
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default='coming_soon')
    intro = models.TextField("Introdução", blank=True)
    body = StreamField([
        ('text', blocks.RichTextBlock()),
        ('bento_grid', BentoGridBlock()),
        ('timeline', TimelineBlock()),
    ], use_json_field=True, blank=True, verbose_name="Corpo")

    content_panels = Page.content_panels + [
        FieldPanel("status"),
        FieldPanel("intro"),
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Página de Submissão"

    parent_page_types = ["pages.HomePage"]
    subpage_types = []


class SponsorsPage(Page):
    intro = models.TextField("Introdução", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    class Meta:
        verbose_name = "Página de Patrocinadores"

    parent_page_types = ["pages.HomePage"]
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        from sponsors.models import SponsorTier
        ctx = super().get_context(request, *args, **kwargs)
        tiers = SponsorTier.objects.prefetch_related("sponsors").all()
        ctx["tiers"] = tiers
        return ctx


class VideoGalleryPage(Page):
    intro = models.TextField("Introdução", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    class Meta:
        verbose_name = "Galeria de Vídeos"

    parent_page_types = ["pages.HomePage"]
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        from videos.models import VideoResource, PUBLIC
        ctx = super().get_context(request, *args, **kwargs)
        ctx["videos"] = VideoResource.objects.filter(status=PUBLIC)
        return ctx


class PreviousEditionsPage(Page):
    intro = models.TextField("Introdução", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    class Meta:
        verbose_name = "Edições Anteriores"

    parent_page_types = ["pages.HomePage"]
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        from proceedings.models import Edition

        ctx = super().get_context(request, *args, **kwargs)
        ctx["editions"] = dedupe_editions(list(Edition.objects.all()) + PREVIOUS_EDITIONS_FALLBACK)
        return ctx


class ProgramPage(Page):
    intro = models.TextField("Introdução", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    class Meta:
        verbose_name = "Programação"

    parent_page_types = ["pages.HomePage"]
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        from program.models import get_public_program_by_day

        ctx = super().get_context(request, *args, **kwargs)
        ctx["program_data"] = get_public_program_by_day()
        return ctx
