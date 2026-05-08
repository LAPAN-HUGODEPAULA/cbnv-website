import pytest
from django.core.files import File
from wagtail.images.models import Image
from wagtail.models import Page, Site

from core.models import SiteMenu
from pages.models import AboutPage, HomePage, NewsArticlePage, NewsIndexPage, PreviousEditionsPage, ProgramPage
from proceedings.models import Edition


@pytest.mark.django_db
class TestLegacyContentPages:
    def setup_method(self):
        self.root = Page.objects.get(id=1)
        for child in self.root.get_children():
            child.delete()
        self.root.refresh_from_db()

        self.home = HomePage(title="Home", slug="home")
        self.root.add_child(instance=self.home)
        self.home.refresh_from_db()

        Site.objects.create(
            hostname="localhost",
            port=80,
            root_page=self.home,
            is_default_site=True,
        )

        self.about = AboutPage(title="Sobre", slug="sobre")
        self.home.add_child(instance=self.about)

        self.program = ProgramPage(title="Programação", slug="programacao", intro="Confira a agenda completa.")
        self.home.add_child(instance=self.program)

        site = Site.objects.first()
        menu = SiteMenu.for_site(site)
        menu.menu_items = [
            ("link", {"label": "Sobre", "page": self.about}),
            ("link", {"label": "Programação", "page": self.program}),
        ]
        menu.save()

        self.news_index = NewsIndexPage(title="Notícias", slug="noticias", intro="Atualizações do congresso.")
        self.home.add_child(instance=self.news_index)

        self.previous_editions = PreviousEditionsPage(title="Edições Anteriores", slug="edicoes-anteriores", intro="Histórico do congresso.")
        self.home.add_child(instance=self.previous_editions)

        with open("_legacy/save-the-date.jpg", "rb") as image_file:
            save_the_date = Image(title="Save the Date", file=File(image_file, name="save-the-date.jpg"))
            save_the_date.save()

        self.article = NewsArticlePage(
            title="Save the Date: XII CBNV 2026 em Belo Horizonte!",
            slug="save-the-date-xii-cbnv-2026-em-belo-horizonte",
            summary="Reserve a data do XII CBNV 2026 em Belo Horizonte.",
            featured=True,
            body=[
                ("image", save_the_date),
                ("text", "O XII Congresso Brasileiro de Neurociências da Visão será realizado em Belo Horizonte."),
            ],
        )
        self.news_index.add_child(instance=self.article)
        self.article.save_revision().publish()

    def test_home_and_about_show_organizations_and_footer(self, client):
        home_response = client.get(self.home.url)
        about_response = client.get(self.about.url)

        for response in (home_response, about_response):
            html = response.content.decode()
            assert "fapemig-logo.svg" in html
            assert "https://www.instagram.com/cbnvufmg/" in html
            assert "Universidade Federal de Minas Gerais" in html
            assert "Laboratório de Pesquisa Aplicada à Neurociências da Visão" in html
            assert "LAboratório de Neurodinâmica da Visão" in html
            assert "https://www.ufmg.br/" in html
            assert "https://lapan.com.br/" in html

    def test_header_menu_uses_normal_navigation(self, client):
        response = client.get(self.home.url)
        html = response.content.decode()

        assert 'hx-boost="false"' in html
        assert 'href="/sobre/"' in html
        assert 'document.querySelector' not in html

    def test_about_page_sections_and_maps(self, client):
        response = client.get(self.about.url)
        html = response.content.decode()

        for heading in [
            "Bem vindos",
            "O evento",
            "Objetivos",
            "O que esperar",
            "Local e acessibilidade",
            "Comissão organizadora",
            "Organização",
        ]:
            assert heading in html

        assert "google.com/maps" in html
        assert "eventos recentes" not in html

    def test_committee_cards_use_compact_four_column_layout(self, client):
        response = client.get(self.about.url)
        html = response.content.decode()

        assert "xl:grid-cols-4" in html
        assert "aspect-[3/4]" in html

    def test_news_article_renders_save_the_date_image(self, client):
        response = client.get(self.article.url)
        html = response.content.decode()

        assert "Save the Date: XII CBNV 2026 em Belo Horizonte!" in html
        assert "<img" in html
        assert "media/images/save-the-date_" in html

    def test_previous_editions_deduplicate_entries_and_use_local_metadata(self):
        Edition.objects.create(
            edition_number=11,
            year=2024,
            theme="Duplicate 11th edition",
            dates="20 a 22 de novembro de 2024",
            location="UFMG — Belo Horizonte, MG",
            proceedings_url="",
            playlist_url="",
        )

        context = self.previous_editions.get_context(None)
        editions = context["editions"]

        assert sum(1 for edition in editions if edition["edition_number"] == 11) == 1
        assert any(edition["edition_number"] == 6 and edition["proceedings_url"] for edition in editions)
