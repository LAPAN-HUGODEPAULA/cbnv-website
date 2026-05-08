import os
from datetime import date
from django.core.management.base import BaseCommand
from django.core.files import File
from django.utils.text import slugify
from wagtail.models import Page, Site
from wagtail.images.models import Image
from core.models import CoreSettings, SiteMenu
from pages.models import HomePage, AboutPage, ProgramPage, SubmissionsPage, NewsIndexPage, NewsArticlePage, SponsorsPage, PreviousEditionsPage
from program.models import Speaker, ProgramDay
from proceedings.models import Edition

class Command(BaseCommand):
    help = "Populates the database with XII CBNV 2026 content"

    def handle(self, *args, **options):
        self.stdout.write("Populating XII CBNV 2026 content...")

        # 1. Setup Site and HomePage
        root = Page.objects.get(id=1)
        
        # Remove existing home page if it exists
        home = HomePage.objects.first()
        if not home:
            # Try to find any child of root and delete it to start fresh
            root.get_children().delete()
            home = HomePage(
                title="XII CBNV 2026",
                slug="home",
                intro="O Congresso Brasileiro de Neurociências da Visão (CBNV) é um evento técnico-científico consolidado, dedicado à disseminação de avanços na compreensão da função visual e de suas interfaces com saúde, tecnologia, educação e sociedade.",
                cta_text="Inscreva-se",
                cta_link="https://inscricoes.cbnv.org.br"
            )
            root.add_child(instance=home)
            home.save_revision().publish()
        else:
            home.title = "XII CBNV 2026"
            home.intro = "O Congresso Brasileiro de Neurociências da Visão (CBNV) é um evento técnico-científico consolidado, dedicado à disseminação de avanços na compreensão da função visual e de suas interfaces com saúde, tecnologia, educação e sociedade."
            home.save()
            home.save_revision().publish()
        
        # Set as default site
        site = Site.objects.first()
        if site:
            site.root_page = home
            site.save()
        else:
            site = Site.objects.create(hostname="localhost", port=8000, root_page=home, is_default_site=True)

        # 2. Import Images
        logo_path = "_legacy/mirror/CBNV-alternativo-com-legenda-multicolorido.png"
        hero_path = "_legacy/12-CBNV.avif"
        
        logo_img = self.import_image(logo_path, "CBNV Logo")
        hero_img = self.import_image(hero_path, "XII CBNV Hero")
        
        if hero_img:
            home.hero_image = hero_img
            home.save()
            home.save_revision().publish()

        # 3. Core Settings
        settings = CoreSettings.for_site(site)
        settings.event_name = "XII CBNV 2026"
        settings.edition = "XII"
        settings.theme = "Neurovisão translacional e inteligência artificial responsável"
        settings.dates = "11 a 13 de novembro de 2026"
        settings.location = "CAD-1 — UFMG, Belo Horizonte, MG"
        settings.contact_email = "jerome.baron.ufmg@gmail.com"
        settings.registration_link = "https://inscricoes.cbnv.org.br"
        settings.instagram_url = "https://www.instagram.com/cbnvufmg/"
        settings.logo = logo_img
        settings.fapemig_text = "Apoio: FAPEMIG — Fundação de Amparo à Pesquisa do Estado de Minas Gerais. Processo OET-00394-26."
        settings.save()

        # 4. Create Child Pages
        pages_to_create = [
            (AboutPage, "Sobre o Congresso", "sobre", {'body': [('text', 'O Congresso Brasileiro de Neurociências da Visão (CBNV), em sua 12ª edição, tem como objetivo consolidar um espaço nacional qualificado para a divulgação de resultados recentes de pesquisa...')]} ),
            (ProgramPage, "Programação", "programacao", {'intro': "Confira a agenda completa do XII CBNV 2026."}),
            (SubmissionsPage, "Submissões", "submissoes", {'status': "open", 'intro': "Abertas as submissões de trabalhos para o XII CBNV 2026."}),
            (NewsIndexPage, "Notícias", "noticias", {'intro': "Fique por dentro das novidades do congresso."}),
            (SponsorsPage, "Patrocinadores", "patrocinadores", {'intro': "Nossos parceiros e apoiadores."}),
            (PreviousEditionsPage, "Edições Anteriores", "edicoes-anteriores", {'intro': "Conheça a história do CBNV."}),
        ]
        
        created_pages = {}
        for model, title, slug, extra in pages_to_create:
            p = model.objects.filter(slug=slug).first()
            if not p:
                p = model(title=title, slug=slug, **extra)
                home.add_child(instance=p)
            else:
                for k, v in extra.items():
                    setattr(p, k, v)
                p.save()
            p.save_revision().publish()
            created_pages[slug] = p

        save_the_date = self.import_image("_legacy/save-the-date.jpg", "Save the Date - XII CBNV 2026")
        if save_the_date:
            save_the_date_article = NewsArticlePage(
                title="Save the Date: XII CBNV 2026 em Belo Horizonte!",
                slug="save-the-date-xii-cbnv-2026-em-belo-horizonte",
                summary="Reserve a data do XII CBNV 2026 em Belo Horizonte.",
                featured=True,
                body=[
                    ("image", save_the_date),
                    ("text", "O XII Congresso Brasileiro de Neurociências da Visão será realizado em Belo Horizonte."),
                    ("text", "Acompanhe os canais oficiais do congresso para atualizações sobre programação e inscrições."),
                ],
            )
            created_pages["noticias"].add_child(instance=save_the_date_article)
            save_the_date_article.save_revision().publish()

        # 5. Populate Site Menu
        menu = SiteMenu.for_site(site)
        menu.menu_items = [
            ('link', {'label': 'Início', 'anchor': '#hero'}),
            ('link', {'label': 'Sobre', 'page': created_pages['sobre'], 'anchor': '#sobre'}),
            ('link', {'label': 'Programação', 'page': created_pages['programacao']}),
            ('link', {'label': 'Submissões', 'page': created_pages['submissoes']}),
            ('link', {'label': 'Notícias', 'page': created_pages['noticias']}),
            ('link', {'label': 'Edições Anteriores', 'page': created_pages['edicoes-anteriores']}),
        ]
        menu.save()

        # 6. Populate Speakers
        speakers_data = [
            {"name": "Kerstin Schmidt", "institution": "UFRN", "title": "Profa. Dra."},
            {"name": "Gustavo Rohenkohl", "institution": "USP", "title": "Prof. Dr."},
            {"name": "Bruss Lima", "institution": "UFRJ", "title": "Prof. Dr."},
            {"name": "Sergio Neuenschwander", "institution": "UFRN", "title": "Prof. Dr."},
            {"name": "Ricardo Gattass", "institution": "UFRJ", "title": "Prof. Dr."},
            {"name": "Michael Jackson Oliveira de Andrade", "institution": "UEMG Divinópolis", "title": "Prof. Dr."},
            {"name": "João Dallyson Sousa de Almeida", "institution": "UFMA", "title": "Prof. Dr."},
        ]
        for s_data in speakers_data:
            Speaker.objects.create(**s_data, status="confirmed")

        # 7. Populate Program Days
        d1 = ProgramDay.objects.create(date=date(2026, 11, 11), title="Dia 1", subtitle="Abertura e Fundamentos", sort_order=1)
        d2 = ProgramDay.objects.create(date=date(2026, 11, 12), title="Dia 2", subtitle="Clínica e Translacional", sort_order=2)
        d3 = ProgramDay.objects.create(date=date(2026, 11, 13), title="Dia 3", subtitle="IA e Tecnologias", sort_order=3)

        # 8. Populate Sessions and Talks
        from program.models import ProgramSession, ProgramTalk, KEYNOTE, ROUNDTABLE, THEMATIC_SESSION, CONFIRMED, PUBLISHED
        
        # Day 1 Sessions
        s1 = ProgramSession.objects.create(day=d1, start_time="09:00", end_time="10:00", title="Conferência Magna: Neurovisão e IA Responsável", activity_type=KEYNOTE, status=PUBLISHED)
        ProgramTalk.objects.create(session=s1, title="Desafios e Oportunidades na Neurovisão", status=CONFIRMED)
        
        s2 = ProgramSession.objects.create(day=d1, start_time="10:30", end_time="12:30", title="Mesa Redonda: Percepção Visual e Processamento Cromático", activity_type=ROUNDTABLE, status=PUBLISHED)
        ProgramTalk.objects.create(session=s2, title="Mecanismos Neurais da Percepção de Cores", status=CONFIRMED)
        
        # Day 2 Sessions
        s3 = ProgramSession.objects.create(day=d2, start_time="09:00", end_time="11:00", title="Sessão Temática: Biomarcadores Visuais em Condições Neurológicas", activity_type=THEMATIC_SESSION, status=PUBLISHED)
        ProgramTalk.objects.create(session=s3, title="Novos Biomarcadores em Oftalmologia", status=CONFIRMED)
        
        # 9. Populate Previous Editions
        Edition.objects.create(edition_number=11, year=2024, theme="Interfaces Cérebro-Máquina e Percepção", location="UFMG, Belo Horizonte")
        Edition.objects.create(edition_number=10, year=2022, theme="Neurovisão e Sociedade", location="Online")
        Edition.objects.create(edition_number=9, year=2021, theme="Avanços na Neurociência da Visão", location="Online")

        self.stdout.write(self.style.SUCCESS("Successfully populated XII CBNV 2026 content!"))

    def import_image(self, path, title):
        if os.path.exists(path):
            with open(path, 'rb') as f:
                img = Image(title=title, file=File(f, name=os.path.basename(path)))
                img.save()
                return img
        return None
