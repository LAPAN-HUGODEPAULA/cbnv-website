import pytest
from django.urls import reverse
from wagtail.models import Page, Site
from pages.models import HomePage, AboutPage, ProgramPage, RegistrationPage, SubmissionsPage, SponsorsPage, VideoGalleryPage, NewsIndexPage, PreviousEditionsPage

@pytest.mark.django_db
class TestPublicRoutes:
    def setup_method(self):
        self.root = Page.objects.get(id=1)
        # Clear existing children to avoid slug conflicts
        for child in self.root.get_children():
            child.delete()
        self.root.refresh_from_db()

        self.home = HomePage(title="Home", slug="home")
        self.root.add_child(instance=self.home)
        self.home.refresh_from_db()
        # Set up a Site for the home page
        Site.objects.create(
            hostname='localhost',
            port=80,
            root_page=self.home,
            is_default_site=True
        )

        self.about = AboutPage(title="Sobre", slug="sobre")
        self.home.add_child(instance=self.about)

        self.program = ProgramPage(title="Programação", slug="programacao")
        self.home.add_child(instance=self.program)
        
        self.registration = RegistrationPage(title="Inscrição", slug="inscricao")
        self.home.add_child(instance=self.registration)
        
        self.submissions = SubmissionsPage(title="Submissões", slug="submissoes")
        self.home.add_child(instance=self.submissions)

        self.news_index = NewsIndexPage(title="Notícias", slug="noticias")
        self.home.add_child(instance=self.news_index)

        self.previous_editions = PreviousEditionsPage(title="Edições Anteriores", slug="edicoes-anteriores")
        self.home.add_child(instance=self.previous_editions)
        
        self.sponsors = SponsorsPage(title="Patrocinadores", slug="patrocinadores")
        self.home.add_child(instance=self.sponsors)
        
        self.videos = VideoGalleryPage(title="Vídeos", slug="videos")
        self.home.add_child(instance=self.videos)

    def test_routes_return_200(self, client):
        pages = [
            self.home,
            self.about,
            self.program,
            self.registration,
            self.submissions,
            self.news_index,
            self.previous_editions,
            self.sponsors,
            self.videos
        ]
        
        for page in pages:
            url = page.get_url()
            response = client.get(url)
            assert response.status_code == 200, f"Page {page.title} returned {response.status_code} at {url}"

    def test_i18n_routes_return_200(self, client):
        # Test default language (no prefix)
        response = client.get('/')
        assert response.status_code == 200
        
        # Test EN prefix
        response = client.get('/en/')
        assert response.status_code == 200

    def test_header_menu_falls_back_to_core_public_pages(self, client):
        response = client.get(self.home.url)
        html = response.content.decode()

        assert 'href="/"' in html
        assert 'href="/sobre/"' in html
        assert 'href="/programacao/"' in html
        assert 'href="/submissoes/"' in html
        assert 'href="/edicoes-anteriores/"' in html
        assert 'hx-boost="false"' in html
