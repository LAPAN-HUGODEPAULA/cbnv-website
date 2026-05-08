import os
import sys
import django
import json

sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cbnv.settings.development")
django.setup()

from wagtail.models import Page
from pages.models import HomePage, AboutPage

def populate_about():
    home = HomePage.objects.first()
    if not home:
        print("Home Page not found.")
        return

    about = AboutPage.objects.first()
    title = "Sobre o Congresso"
    
    body_data = [
        {
            'type': 'text',
            'value': '<h2>O Evento</h2>'
                     '<p>O <strong>Congresso Brasileiro de Neurociências da Visão (CBNV)</strong> é um evento técnico-científico consolidado, de abrangência nacional, dedicado à disseminação de avanços na compreensão da função visual e de suas interfaces com saúde, tecnologia, educação e sociedade.</p>'
                     '<p>Em sua <strong>12ª edição</strong>, a ser realizada em Belo Horizonte em 2026, o evento adotará como eixo integrador a <strong>neurovisão translacional e a inteligência artificial responsável</strong>, articulando pesquisa básica, investigação clínica, métodos computacionais, biomarcadores visuais, avaliação funcional da visão e inovação em saúde.</p>'
        },
        {
            'type': 'bento_grid',
            'value': {
                'title': 'Eixos Integradores',
                'items': [
                    {
                        'title': 'Investigação Básica',
                        'text': '<p>Estudo dos processos perceptuais e mecanismos neurais da função visual.</p>',
                        'size': '1x1'
                    },
                    {
                        'title': 'Aplicação Clínica',
                        'text': '<p>Integração com oftalmologia, neurologia, psiquiatria e reabilitação visual.</p>',
                        'size': '1x1'
                    },
                    {
                        'title': 'Tecnologias Digitais e IA',
                        'text': '<p>Desenvolvimento de abordagens computacionais, Inteligência Artificial responsável e suporte à decisão clínica.</p>',
                        'size': '2x1'
                    }
                ]
            }
        },
        {
            'type': 'text',
            'value': '<h2>Objetivos</h2>'
                     '<p>A proposta visa reunir pesquisadores, docentes, estudantes, profissionais da saúde e especialistas em tecnologia para:</p>'
                     '<ul>'
                     '<li>Integrar conhecimentos de neurociência visual, oftalmologia e ciência de dados;</li>'
                     '<li>Promover o diálogo entre pesquisa básica e prática clínica;</li>'
                     '<li>Estimular redes de colaboração interinstitucionais em âmbito nacional;</li>'
                     '<li>Contribuir para a formação de recursos humanos e popularização da ciência.</li>'
                     '</ul>'
        },
        {
            'type': 'timeline',
            'value': {
                'title': 'Histórico Recente',
                'items': [
                    {'date': '2021', 'title': '9ª Edição', 'description': 'Foco em rastreamento ocular e percepção visual (Online).'},
                    {'date': '2022', 'title': '10ª Edição', 'description': 'Consolidação de interfaces clínicas e pesquisa translacional.'},
                    {'date': '2024', 'title': '11ª Edição', 'description': 'Neurociência, psicologia e aplicações de IA na UFMG.'},
                    {'date': '2026', 'title': '12ª Edição', 'description': 'Neurovisão na Era da Inteligência Artificial.'}
                ]
            }
        }
    ]

    if not about:
        about = AboutPage(
            title=title,
            slug="sobre",
            body=json.dumps(body_data)
        )
        home.add_child(instance=about)
        print("Created new AboutPage.")
    else:
        about.title = title
        about.body = json.dumps(body_data)
        print("Updating existing AboutPage.")

    about.save_revision().publish()
    print("AboutPage published successfully.")

if __name__ == "__main__":
    populate_about()
