import os
import sys
import django
from django.utils import timezone
import json

# Add the current directory to sys.path to find the cbnv module
sys.path.append(os.getcwd())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cbnv.settings.development")
django.setup()

from wagtail.models import Page
from pages.models import NewsIndexPage, NewsArticlePage

def create_news():
    news_index = NewsIndexPage.objects.first()
    if not news_index:
        print("News Index Page not found.")
        return

    title = "Save the Date: XII CBNV 2026 em Belo Horizonte!"
    slug = "save-the-date-xii-cbnv-2026"
    summary = "Marque em sua agenda: de 18 a 21 de novembro de 2026, nos encontraremos na UFMG para discutir a Neurovisão na Era da Inteligência Artificial."
    
    body_data = [
        {
            'type': 'text',
            'value': '<p>Estamos muito felizes em anunciar as datas oficiais do <strong>XII Congresso Brasileiro de Neurociências da Visão (CBNV 2026)</strong>!</p>'
                     '<p>O evento ocorrerá entre os dias <strong>18 e 21 de novembro de 2026</strong>, no Centro de Atividades Didáticas 1 (CAD-1) da UFMG, em Belo Horizonte.</p>'
                     '<p>Com o tema "Neurovisão na Era da Inteligência Artificial", esta edição promete ser um marco na integração entre as ciências biológicas e as novas fronteiras tecnológicas. Prepare-se para quatro dias intensos de conferências, workshops práticos e networking com os maiores nomes da área.</p>'
                     '<p>Em breve, abriremos o período de submissão de trabalhos e as inscrições com valores promocionais.</p>'
                     '<p>Não perca a chance de fazer parte deste encontro histórico. Nos vemos em BH!</p>'
        }
    ]

    # Delete existing page properly through Wagtail
    existing_page = NewsArticlePage.objects.filter(slug=slug).first()
    if existing_page:
        existing_page.delete()

    article = NewsArticlePage(
        title=title,
        slug=slug,
        summary=summary,
        body=json.dumps(body_data),
        first_published_at=timezone.now(),
        featured=True
    )
    news_index.add_child(instance=article)
    article.save_revision().publish()
    print(f"Successfully created: {title}")

if __name__ == "__main__":
    create_news()
