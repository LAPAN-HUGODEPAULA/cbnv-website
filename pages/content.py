from copy import deepcopy


ORGANIZATIONS = [
    {
        "name": "Universidade Federal de Minas Gerais",
        "url": "https://www.ufmg.br/",
        "logo": "images/organizations/ufmg-logo.svg",
        "alt": "Logo da Universidade Federal de Minas Gerais",
        "order": 1,
    },
    {
        "name": "Laboratório de Pesquisa Aplicada à Neurociências da Visão",
        "url": "https://lapan.com.br/",
        "logo": "images/organizations/logo-lapan-branco.png",
        "alt": "Logo do LAPAN",
        "order": 2,
    },
    {
        "name": "LAboratório de Neurodinâmica da Visão",
        "url": "",
        "logo": "images/organizations/logo-lanev-em-branco-com-legenda.png",
        "alt": "Logo do LANEV",
        "order": 3,
    },
    {
        "name": "Programa de Pós-Graduação em Neurociências",
        "url": "https://neurociencias.icb.ufmg.br/",
        "logo": "images/organizations/logo-neuro.png",
        "alt": "Logo do Programa de Pós-Graduação em Neurociências",
        "order": 4,
    },
    {
        "name": "Laboratório de Fisiologia Sensorial e Comportamental",
        "url": "",
        "logo": "images/organizations/logo-lafisc.png",
        "alt": "Logo do LAFISC",
        "order": 5,
    },
    {
        "name": "Hospital de Olhos de Minas Gerais",
        "url": "https://holhos.com.br",
        "logo": "images/organizations/logo-holhos.png",
        "alt": "Logo do Hospital de Olhos de Minas Gerais",
        "order": 6,
    },
    {
        "name": "Fundação Hospital de Olhos",
        "url": "https://fundacaoholhos.com.br/",
        "logo": "images/organizations/logo-fundaco-hospital-dos-olhos.png",
        "alt": "Logo da Fundação Hospital de Olhos",
        "order": 7,
    },
]


ABOUT_CONTENT = {
    "welcome_title": "Bem vindos",
    "welcome": [
        "Sejam todas e todos bem-vindos ao XII Congresso Brasileiro de Neurociências da Visão (CBNV 2026).",
        "O congresso reúne pesquisa, prática clínica e diálogo institucional em torno dos mecanismos visuais, da neurociência e de suas aplicações na saúde e na tecnologia.",
    ],
    "event_title": "O evento",
    "event": [
        "O CBNV é um encontro científico dedicado a aproximar pesquisadores, estudantes e profissionais que trabalham com visão, cérebro e comportamento.",
        "A proposta desta edição é manter o foco em conteúdo técnico consistente, colaboração interdisciplinar e discussão de evidências, em um formato presencial com apoio digital quando necessário.",
    ],
    "objectives_title": "Objetivos",
    "objectives": [
        "Compartilhar pesquisas recentes em neurociências da visão com base em evidências.",
        "Estimular a integração entre áreas clínicas, básicas e tecnológicas.",
        "Fortalecer a formação de estudantes e pesquisadores em um ambiente de troca acadêmica.",
        "Aproximar o conhecimento científico da sociedade e dos serviços de saúde.",
    ],
    "expectations_title": "O que esperar",
    "expectations": [
        "Palestras e mesas com pesquisadores convidados e integrantes da rede acadêmica do congresso.",
        "Sessões para apresentação de trabalhos e discussão metodológica.",
        "Espaços para diálogo entre instituições parceiras, docentes e estudantes.",
    ],
    "location_title": "Local e acessibilidade",
    "location_intro": "Auditório da Escola de Engenharia da UFMG, Av. Pres. Antônio Carlos, 6627 - Pampulha, Belo Horizonte - MG, 31270-901.",
    "map_url": "https://www.google.com/maps?q=Audit%C3%B3rio%20da%20Escola%20de%20Engenharia%20UFMG%20Belo%20Horizonte&output=embed",
    "map_link": "https://www.google.com/maps/search/?api=1&query=Audit%C3%B3rio+da+Escola+de+Engenharia+UFMG+Belo+Horizonte",
    "committee_title": "Comissão organizadora",
    "committee_intro": "A comissão organizadora do 11o CBNV foi mantida como referência histórica e recebeu a inclusão de Hugo de Paula para a edição de 2026.",
}


ORGANIZING_COMMITTEE = [
    {
        "name": "Anderson Rodrigues",
        "role": "Biólogo (UFMG), mestrando no PPG Neurociências (UFMG)",
        "photo": "images/committee/anderson-rodrigues.jpg",
    },
    {
        "name": "Clara Amaral",
        "role": "Bióloga (UFMG), mestre em Fisiologia e Farmacologia (UFMG), doutoranda do PPG FisFar (UFMG)",
        "photo": "images/committee/clara-amaral.jpg",
    },
    {
        "name": "Geovana de Fátima",
        "role": "Graduanda em Ciências Biológicas (UFMG)",
        "photo": "images/committee/geovana-de-fatima.jpg",
    },
    {
        "name": "Jerome Baron",
        "role": "Coordenador do Congresso, Professor Associado do Dep. de Fisiologia e Biofísica (UFMG)",
        "photo": "images/committee/jerome-baron.jpg",
    },
    {
        "name": "Hugo de Paula",
        "role": "Subcoordenador do Congresso, Pós-Doutorado em Neurociências (UFMG)",
        "photo": "images/committee/hugo-de-paula.jpg",
    },
    {
        "name": "Letícia de Senna",
        "role": "Graduanda em Fisioterapia (UFMG)",
        "photo": "images/committee/leticia-de-senna.jpg",
    },
    {
        "name": "Lívia Stemler",
        "role": "Bióloga (UFMG), mestranda no PPG FisFar (UFMG)",
        "photo": "images/committee/livia-stemler.jpg",
    },
    {
        "name": "Luiza Furtado",
        "role": "Graduanda em Ciências Biológicas (UFMG)",
        "photo": "images/committee/luiza-furtado.jpg",
    },
    {
        "name": "Maria Lucia",
        "role": "Professora Titular do Dep. de Engenharia Mecânica da Escola de Engenharia",
        "photo": "images/committee/maria-lucia.jpg",
    },
    {
        "name": "Pedro Brandão",
        "role": "Engenheiro da Computação (CEFET-MG), mestrando no PPG Neurociências (UFMG)",
        "photo": "images/committee/pedro-brandao.jpg",
    },
    {
        "name": "Tiago Lopes",
        "role": "Graduando em Ciências Biológicas (UFMG)",
        "photo": "images/committee/tiago-lopes.jpg",
    },
    {
        "name": "Victor Cesar",
        "role": "Biólogo (Una), Especialista em Psicobiologia (FAMEESP), mestrando no PPG Neurociências (UFMG)",
        "photo": "images/committee/victor-cesar.jpg",
    },
    {
        "name": "Victor Soares",
        "role": "Graduando em Ciências Biológicas (UFMG)",
        "photo": "images/committee/victor-soares.jpg",
    },
    {
        "name": "Vinicius Borges",
        "role": "Graduando em Ciências Biológicas (UFMG)",
        "photo": "images/committee/vinicius-borges.jpg",
    },
    {
        "name": "Carla Neves",
        "role": "Veterinária Oncologista, Mestre em Saúde Pública",
        "photo": "images/committee/carla-neves.jpg",
    },
]


PREVIOUS_EDITIONS_FALLBACK = [
    {
        "edition_number": 11,
        "year": 2024,
        "theme": "Neurociência da Visão: Da Biologia à Clínica",
        "dates": "20 a 22 de novembro de 2024",
        "location": "UFMG — Belo Horizonte, MG",
        "proceedings_url": "",
        "playlist_url": "https://www.youtube.com/@congressoneurovis%C3%A3o",
    },
    {
        "edition_number": 10,
        "year": 2022,
        "theme": "Uma década de Congresso Brasileiro de Neurociências da Visão",
        "dates": "25 de novembro de 2022",
        "location": "UFMG — Belo Horizonte, MG",
        "proceedings_url": "https://www.researchgate.net/publication/365981155_Livro_de_publicacoes_do_10_Congresso_Brasileiro_de_Neurovisao",
        "playlist_url": "",
    },
    {
        "edition_number": 9,
        "year": 2021,
        "theme": "Neurovisão e interfaces internacionais",
        "dates": "10 a 12 de novembro de 2021",
        "location": "Online / UFMG",
        "proceedings_url": "https://www.researchgate.net/publication/356083448_Livro_de_publicacoes_do_9_Congresso_Brasileiro_de_Neurovisao",
        "playlist_url": "",
    },
    {
        "edition_number": 7,
        "year": 2019,
        "theme": "Neurovisão e percepção visual",
        "dates": "2019",
        "location": "Belo Horizonte, MG",
        "proceedings_url": "https://www.researchgate.net/publication/335787521_Livro_de_publicacoes_do_7_Congresso_Brasileiro_de_Neurovisao",
        "playlist_url": "",
    },
    {
        "edition_number": 6,
        "year": 2018,
        "theme": "Neurovisão, leitura e estresse visual",
        "dates": "2018",
        "location": "Belo Horizonte, MG",
        "proceedings_url": "https://www.researchgate.net/publication/327944145_Livro_de_publicacoes_do_6_Congresso_Brasileiro_de_Neurovisao",
        "playlist_url": "",
    },
    {
        "edition_number": 5,
        "year": 2017,
        "theme": "Neurovisão e educação visual",
        "dates": "2017",
        "location": "Belo Horizonte, MG",
        "proceedings_url": "https://www.researchgate.net/publication/319944508_Livro_de_publicacoes_do_5_Congresso_Brasileiro_de_Neurovisao",
        "playlist_url": "",
    },
]


def dedupe_editions(editions):
    seen = set()
    output = []
    for edition in editions:
        if isinstance(edition, dict):
            data = deepcopy(edition)
        else:
            data = {
                "edition_number": edition.edition_number,
                "year": edition.year,
                "theme": edition.theme,
                "dates": edition.dates,
                "location": edition.location,
                "proceedings_url": edition.proceedings_url,
                "playlist_url": edition.playlist_url,
            }
        key = (data["edition_number"], data["year"])
        if key in seen:
            continue
        seen.add(key)
        output.append(data)
    output.sort(key=lambda item: (item["year"], item["edition_number"]), reverse=True)
    return output
