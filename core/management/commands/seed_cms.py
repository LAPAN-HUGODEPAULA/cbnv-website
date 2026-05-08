import os

from django.core.files import File
from django.core.management.base import BaseCommand
from wagtail.models import Page, Site
from wagtail.images.models import Image


class Command(BaseCommand):
    help = "Seed initial CMS data: HomePage and child pages."

    def handle(self, *args, **options):
        from core.models import CoreSettings
        from pages.models import HomePage, AboutPage, NewsIndexPage, NewsArticlePage, PreviousEditionsPage

        root = Page.get_first_root_node()

        existing = HomePage.objects.first()
        if existing:
            self.stdout.write(self.style.WARNING("HomePage already exists. Skipping."))
            return

        # Remove default Wagtail welcome page (plain Page with slug='home')
        for child in root.get_children():
            if child.content_type.model == "page":
                child.delete()
                self.stdout.write("Removed default Wagtail welcome page.")
                break

        home = HomePage(
            title="Página Inicial",
            slug="home",
            intro="Bem-vindo ao XII Congresso Brasileiro de Neurociências da Visão.",
            cta_text="Inscreva-se",
        )
        root.add_child(instance=home)

        about = AboutPage(
            title="Sobre o Congresso",
            slug="sobre",
            body="O CBNV é o principal congresso brasileiro dedicado à neurociência da visão, reunindo pesquisadores, estudantes e profissionais da área.",
        )
        home.add_child(instance=about)

        news_index = NewsIndexPage(
            title="Notícias",
            slug="noticias",
            intro="Últimas novidades sobre o congresso.",
        )
        home.add_child(instance=news_index)

        save_the_date_img = self.import_image("_legacy/save-the-date.jpg", "Save the Date - XII CBNV 2026")
        if save_the_date_img:
            article = NewsArticlePage(
                title="Save the Date: XII CBNV 2026 em Belo Horizonte!",
                slug="save-the-date-xii-cbnv-2026-em-belo-horizonte",
                summary="Reserve a data do XII CBNV 2026 em Belo Horizonte.",
                featured=True,
                body=[
                    ("image", save_the_date_img),
                    ("text", "O XII Congresso Brasileiro de Neurociências da Visão será realizado em Belo Horizonte."),
                    ("text", "Acompanhe os canais oficiais do congresso para atualizações sobre programação e inscrições."),
                ],
            )
            news_index.add_child(instance=article)
            article.save_revision().publish()

        editions = PreviousEditionsPage(
            title="Edições Anteriores",
            slug="edicoes-anteriores",
            intro="Conheça as edições anteriores do CBNV e acesse os anais.",
        )
        home.add_child(instance=editions)

        site = Site.objects.first()
        if site:
            site.root_page = home
            site.save(update_fields=["root_page"])

            settings = CoreSettings.for_site(site)
            settings.instagram_url = "https://www.instagram.com/cbnvufmg/"
            settings.save()

        self.stdout.write(self.style.SUCCESS(
            "CMS seed complete: created HomePage, AboutPage, NewsIndexPage, PreviousEditionsPage."
        ))

    def import_image(self, path, title):
        if os.path.exists(path):
            with open(path, "rb") as f:
                img = Image(title=title, file=File(f, name=os.path.basename(path)))
                img.save()
                return img
        return None
