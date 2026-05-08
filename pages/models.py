from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.models import Page, TranslatableMixin
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from core.blocks import BentoGridBlock, StatBlock, TimelineBlock
from pages.content import (
    ABOUT_CONTENT,
    ORGANIZATIONS,
    ORGANIZING_COMMITTEE,
    PREVIOUS_EDITIONS_FALLBACK,
    dedupe_editions,
)


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
        from program.models import ProgramDay, ProgramSession, ProgramTalk, CONFIRMED

        ctx = super().get_context(request, *args, **kwargs)
        days = ProgramDay.objects.prefetch_related("sessions__talks__speaker").order_by("sort_order", "date")

        program_data = []
        for day in days:
            sessions = []
            for session in day.sessions.filter(status="published").order_by("start_time"):
                talks = session.talks.filter(status=CONFIRMED).order_by("sort_order")
                if talks or session.activity_type in ("break", "reception", "closing_ceremony", "awards"):
                    sessions.append({"session": session, "talks": list(talks)})
            if sessions:
                program_data.append({"day": day, "sessions": sessions})

        ctx["program_data"] = program_data
        return ctx
