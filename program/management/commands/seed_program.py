from datetime import date, time

from django.core.management.base import BaseCommand

from program.models import (
    BREAK, CLOSING_CEREMONY, CONFIRMED, KEYNOTE, PUBLISHED, RECEPTION,
    ROUNDTABLE, TALK, THEMATIC_SESSION, OPENING_CEREMONY, POSTER, ORAL,
    AWARDS, HYBRID, IN_PERSON,
    ProgramDay, ProgramSession, ProgramTalk, Speaker,
)


def _time(h, m):
    return time(h, m)


def _s(day, start, end, title, atype, status=PUBLISHED, fmt=IN_PERSON, room="", desc="", sort=0):
    return {
        "start_time": start, "end_time": end, "title": title, "activity_type": atype,
        "status": status, "format": fmt, "room": room, "description": desc, "sort_order": sort,
    }


def _t(session_title, speaker_name, title, status=CONFIRMED, desc="", sort=0):
    return {
        "session_title": session_title, "speaker_name": speaker_name,
        "title": title, "status": status, "description": desc, "sort_order": sort,
    }


class Command(BaseCommand):
    help = "Seed full preliminary program data for XII CBNV 2026."

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Clear existing program data before seeding.",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            self.stdout.write("Clearing existing program data...")
            ProgramTalk.objects.all().delete()
            ProgramSession.objects.all().delete()
            ProgramDay.objects.all().delete()
            # We keep speakers but they will be updated if they exist
        elif ProgramDay.objects.exists():
            self.stdout.write(self.style.WARNING("Program data already exists. Use --clear to overwrite."))
            return

        speakers = self._create_speakers()
        self._create_days_and_sessions(speakers)
        self.stdout.write(self.style.SUCCESS("Program seed complete."))

    def _create_speakers(self):
        # (Full Name, Display Name, Title, Institution, Country, Bio, Lattes)
        data = [
            ("Alessandro Fernandes Moreira", "Alessandro Fernandes Moreira", "Prof. Dr.", "UFMG", "BR", "Reitor da UFMG.", ""),
            ("Grace Schenatto Pereira Moraes", "Grace Schenatto Pereira Moraes", "Profa. Dra.", "UFMG", "BR", "Coordenadora do PPG em Neurociências da UFMG.", ""),
            ("Ricardo Guimarães", "Ricardo Guimarães", "Dr.", "Hospital de Olhos de Minas Gerais", "BR", "Diretor do Hospital de Olhos de Minas Gerais.", ""),
            ("Jerome Baron", "Jerome Baron", "Prof. Dr.", "UFMG", "BR", "Coordenador do 12º CBNV. Pesquisador em neurofisiologia da percepção visual.", "http://lattes.cnpq.br/7044465149117355"),
            ("Hugo Bastos de Paula", "Hugo Bastos de Paula", "Prof. Dr.", "PUC Minas", "BR", "Sub-coordenador do 12º CBNV. Coordenador do LAPAN.", "http://lattes.cnpq.br/0010858860721392"),
            ("Sergio Neuenschwander", "Sergio Neuenschwander", "Prof. Dr.", "UFRN", "BR", "Pesquisador do Instituto do Cérebro da UFRN.", ""),
            ("Bruss Lima", "Bruss Lima", "Prof. Dr.", "UFRJ", "BR", "Pesquisador da UFRJ.", ""),
            ("Anderson Rodrigues de Oliveira", "Anderson Rodrigues de Oliveira", "", "UFMG", "BR", "Mestrado pelo PPG em Neurociências, UFMG.", ""),
            ("Kerstin Schmidt", "Kerstin Schmidt", "Profa. Dra.", "UFRN", "BR", "Diretora do Instituto do Cérebro, UFRN.", ""),
            ("Danilo Barbosa Melges", "Danilo Barbosa Melges", "Prof. Dr.", "UFMG", "BR", "Departamento de Engenharia Elétrica, UFMG.", ""),
            ("Jan Kremers", "Jan Kremers", "Prof. Dr.", "Hospital Universitário de Erlangen", "DE", "University Hospital Erlangen, Germany.", ""),
            ("Mirella Telles Salgueiro Barboni", "Mirella Telles Salgueiro Barboni", "Profa. Dra.", "Semmelweis University", "HU", "Department of Ophthalmology, Semmelweis University, Hungary.", ""),
            ("Márcia Guimarães", "Márcia Guimarães", "Dra.", "Hospital de Olhos de Minas Gerais", "BR", "Hospital de Olhos de Minas Gerais.", ""),
            ("Michael Jackson Oliveira de Andrade", "Michael Jackson Oliveira de Andrade", "Prof. Dr.", "UEMG", "BR", "PPg Biociências e Saúde Humana, UEMG.", ""),
            ("Guilherme Menezes Lage", "Guilherme Menezes Lage", "Prof. Dr.", "UFMG", "BR", "Departamento de Educação Física (EEF/UFMG).", ""),
            ("Julia Beatriz Lopes Silva", "Julia Beatriz Lopes Silva", "Profa. Dra.", "UFMG", "BR", "Departamento de Psicologia (FAFICH/UFMG).", ""),
            ("Gustavo Rohenkohl", "Gustavo Rohenkohl", "Prof. Dr.", "USP", "BR", "Max Planck Tandem Research Group no Instituto de Biociências (USP).", ""),
            ("João Dallyson Sousa de Almeida", "João Dallyson Sousa de Almeida", "Prof. Dr.", "UFMA", "BR", "Professor da UFMA.", ""),
            ("Antônio de Pádua Braga", "Antônio de Pádua Braga", "Prof. Dr.", "UFMG", "BR", "Departamento de Engenharia Eletrônica, UFMG.", ""),
            ("Wagner Meira Júnior", "Wagner Meira Júnior", "Prof. Dr.", "UFMG", "BR", "Diretor do Centro de Inovação em Inteligência Artificial para Saúde (CI-IA-Saúde), UFMG.", ""),
            ("Nikolaus Kriegeskorte", "Nikolaus Kriegeskorte", "Prof. Dr.", "Columbia University", "US", "Visual Inference Lab., Columbia University, United States.", ""),
            ("Ricardo Gattass", "Ricardo Gattass", "Prof. Dr.", "UFRJ", "BR", "Membro da Academia Brasileira de Ciências e Superintendente da FINEP.", ""),
        ]
        speakers = {}
        for full_name, display, title, inst, country, bio, lattes in data:
            s, _ = Speaker.objects.update_or_create(
                name=full_name,
                defaults={
                    "display_name": display, "title": title,
                    "institution": inst, "country": country,
                    "bio": bio, "lattes_url": lattes, "status": CONFIRMED,
                },
            )
            speakers[full_name] = s
        self.stdout.write(f"Processed {len(speakers)} speakers.")
        return speakers

    def _create_days_and_sessions(self, speakers):
        days_data = [
            {
                "date": date(2026, 11, 11),
                "title": "Dia 1 — Fundamentos e Fronteiras da Neurociência da Visão",
                "subtitle": "Base conceitual: retina, circuitos visuais, percepção e cognição",
                "sort": 1,
                "day_sessions": [
                    _s(None, "10:00", "10:30", "Recepção e credenciamento dos participantes", RECEPTION, sort=1),
                    _s(None, "10:30", "11:00", "Mesa solene de abertura", OPENING_CEREMONY, sort=2),
                    _s(None, "11:00", "12:00", "Conferência plenária de abertura", KEYNOTE, sort=3),
                    _s(None, "12:30", "14:00", "Almoço", BREAK, sort=4),
                    _s(None, "14:00", "15:00", "Palestra: Sincronização Neuronal", TALK, sort=5),
                    _s(None, "15:00", "16:00", "Palestra: Núcleo Pulvinar", TALK, sort=6),
                    _s(None, "16:00", "17:00", "Intervalo e Sessão de pôsteres", POSTER, sort=7),
                    _s(None, "17:00", "18:00", "Palestra: Movimento Visual em Aves", TALK, sort=8),
                    _s(None, "18:00", "19:00", "Palestra: Movimento Visual Reverso", TALK, sort=9),
                ],
                "talks": [
                    _t("Conferência plenária de abertura", "Ricardo Guimarães", "Da neurobiologia da visão à prática clínica: novos caminhos na era da inteligência artificial?"),
                    _t("Palestra: Sincronização Neuronal", "Sergio Neuenschwander", "Mecanismos de sincronização neuronal na retina"),
                    _t("Palestra: Núcleo Pulvinar", "Bruss Lima", "O núcleo pulvinar como um centro integrativo: topografia visuotópica e propriedades eletrofisiológicas"),
                    _t("Palestra: Movimento Visual em Aves", "Jerome Baron", "Resolução temporal e processamento do movimento visual em aves adaptadas a ambientes de baixa luminosidade"),
                    _t("Palestra: Movimento Visual Reverso", "Anderson Rodrigues de Oliveira", "Percepção de movimento visual reverso: casos raros ou janela para novos mecanismos?"),
                ],
            },
            {
                "date": date(2026, 11, 12),
                "title": "Dia 2 — Neurovisão Clínica e Translacional",
                "subtitle": "Aplicações clínicas, eletrofisiologia, biomarcadores e condições neurológicas",
                "sort": 2,
                "day_sessions": [
                    _s(None, "09:00", "10:00", "Palestra: Alzheimer e Córtex Visual", TALK, sort=1),
                    _s(None, "10:00", "10:30", "Intervalo", BREAK, sort=2),
                    _s(None, "10:30", "12:30", "Sessão temática – ERG clínica", THEMATIC_SESSION, sort=3),
                    _s(None, "12:30", "14:00", "Almoço", BREAK, sort=4),
                    _s(None, "14:00", "16:00", "Sessão temática – Biomarcadores", THEMATIC_SESSION, sort=5),
                    _s(None, "16:00", "17:00", "Intervalo e Sessão de pôsteres", POSTER, sort=6),
                    _s(None, "17:00", "18:00", "Palestra: Rastreamento Ocular", TALK, sort=7),
                    _s(None, "18:00", "19:00", "Sessões paralelas de apresentação oral", ORAL, sort=8),
                ],
                "talks": [
                    _t("Palestra: Alzheimer e Córtex Visual", "Kerstin Schmidt", "Alterações na atividade neuronal do córtex visual na doença de Alzheimer"),
                    _t("Sessão temática – ERG clínica", "Danilo Barbosa Melges", "Tema 1: ERG: princípios de aquisição, processamento e interpretação do sinal", sort=1),
                    _t("Sessão temática – ERG clínica", "Jan Kremers", "Tema 2: Caracterização das vias magnocelular e parvocelular", sort=2),
                    _t("Sessão temática – ERG clínica", "Mirella Telles Salgueiro Barboni", "Tema 3: ERG e distrofia muscular de Duchenne", sort=3),
                    _t("Sessão temática – Biomarcadores", "Márcia Guimarães", "Painelista", sort=1),
                    _t("Sessão temática – Biomarcadores", "Michael Jackson Oliveira de Andrade", "Painelista", sort=2),
                    _t("Sessão temática – Biomarcadores", "Guilherme Menezes Lage", "Painelista", sort=3),
                    _t("Sessão temática – Biomarcadores", "Julia Beatriz Lopes Silva", "Painelista", sort=4),
                    _t("Palestra: Rastreamento Ocular", "Gustavo Rohenkohl", "Rastreamento ocular: princípios técnicos e aplicações na avaliação da função visual"),
                ],
            },
            {
                "date": date(2026, 11, 13),
                "title": "Dia 3 — Neurovisão, Inteligência Artificial e Inovação em Saúde",
                "subtitle": "IA, ciência de dados e tecnologias digitais em neurovisão",
                "sort": 3,
                "day_sessions": [
                    _s(None, "09:00", "10:00", "Palestra: IA no Diagnóstico Ocular", TALK, sort=1),
                    _s(None, "10:00", "10:30", "Intervalo", BREAK, sort=2),
                    _s(None, "10:30", "12:30", "Sessão temática – IA: Oportunidades Institucionais", THEMATIC_SESSION, sort=3),
                    _s(None, "12:30", "14:00", "Almoço", BREAK, sort=4),
                    _s(None, "14:00", "15:00", "Palestra: Modelos de Redes Neurais", TALK, fmt=HYBRID, sort=5),
                    _s(None, "15:00", "16:00", "Mesa redonda: Confiança em Modelos de IA", ROUNDTABLE, sort=6),
                    _s(None, "16:00", "17:00", "Conferência plenária de Encerramento", KEYNOTE, sort=7),
                    _s(None, "17:00", "18:00", "Encerramento oficial", CLOSING_CEREMONY, sort=8),
                ],
                "talks": [
                    _t("Palestra: IA no Diagnóstico Ocular", "João Dallyson Sousa de Almeida", "IA no diagnóstico e triagem de doenças oculares"),
                    _t("Sessão temática – IA: Oportunidades Institucionais", "Antônio de Pádua Braga", "IA no contexto institucional brasileiro", sort=1),
                    _t("Sessão temática – IA: Oportunidades Institucionais", "Wagner Meira Júnior", "Inovação em IA para Saúde", sort=2),
                    _t("Palestra: Modelos de Redes Neurais", "Nikolaus Kriegeskorte", "Desenvolver modelos de redes neurais que reproduzam desafios computacionais da visão biológica"),
                    _t("Conferência plenária de Encerramento", "Ricardo Gattass", "Além dos mapas corticais: codificação de características multidimensionais complexas"),
                ],
            },
        ]

        for day_data in days_data:
            talks_map = day_data.pop("talks")
            day_sessions = day_data.pop("day_sessions")
            sort_order = day_data.pop("sort")
            day = ProgramDay.objects.create(**day_data, sort_order=sort_order)
            session_objs = {}
            for s in day_sessions:
                s["day"] = day
                sess = ProgramSession.objects.create(**s)
                session_objs[sess.title] = sess
            for t in talks_map:
                sess = session_objs.get(t["session_title"])
                if not sess:
                    self.stderr.write(f"  WARNING: session '{t['session_title']}' not found for talk '{t['title']}'")
                    continue
                speaker = speakers.get(t["speaker_name"])
                ProgramTalk.objects.create(
                    session=sess,
                    speaker=speaker,
                    title=t["title"],
                    description=t.get("description", ""),
                    status=t["status"],
                    sort_order=t.get("sort_order", 0),
                )

        total = ProgramSession.objects.count()
        total_talks = ProgramTalk.objects.count()
        self.stdout.write(f"Created 3 days, {total} sessions, {total_talks} talks.")
