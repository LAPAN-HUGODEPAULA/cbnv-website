# Public Site Copy Map - Round 1

## Metadata

- Change ID: `produce-public-site-content-round-1`
- Purpose: map produced copy to implementation targets
- Status meanings: `ready`, `provisional`, `needs-data`, `needs-field`, `defer`

## Copy Map

| Page | Section | Content key | Proposed copy | Target location | Source/rationale | Status |
|---|---|---|---|---|---|---|
| Home | Hero eyebrow | `home.hero_eyebrow` | XII Congresso Brasileiro de Neurociências da Visão | Template/current settings composition | Requirements event name and edition | ready |
| Home | Hero title | `CoreSettings.short_event_name` | CBNV 2026 | `CoreSettings.short_event_name`; `home_page.html` | Canonical settings | ready |
| Home | Hero subtitle | `CoreSettings.theme` | Neurovisão na Era da Inteligência Artificial | `CoreSettings.theme` | Canonical settings | ready |
| Home | Hero description | `HomePage.intro` | Encontro técnico-científico presencial em Belo Horizonte para discutir neurociências da visão, prática clínica, pesquisa translacional e aplicações responsáveis de inteligência artificial em saúde visual. | Wagtail `HomePage.intro` or page seed when canonical page seed exists | UI review asks Home copy to be less generic | ready |
| Home | Dates fact | `CoreSettings.dates` | 11 a 13 de novembro de 2026 | `CoreSettings.dates` seeded by `seed_canonical_event_content` | Canonical settings | ready |
| Home | Venue fact | `CoreSettings.location` | CAD-1/UFMG, Belo Horizonte, MG | `CoreSettings.location` | Canonical venue data | ready |
| Home | Format fact | `CoreSettings.format_label` | Presencial, com transmissão on-line quando confirmada pela organização | `CoreSettings.format_label` after format wording confirmation | UI backlog UXR1-008; current wording differs across docs | provisional |
| Home | Registration status | `CoreSettings.registration_status` | Em breve | `CoreSettings.registration_status` | Pending link policy | ready |
| Home | Livestream status | `CoreSettings.livestream_status` | Em breve | `CoreSettings.livestream_status` | Pending link policy | ready |
| Home | Program preview intro | `home.program_preview_intro` | A programação preliminar organiza três dias de atividades sobre fundamentos da neurociência da visão, neurovisão clínica e translacional, inteligência artificial e inovação em saúde. | Template text or future Home content block | Program seed and UI review | needs-field |
| Home | Announcements intro | `home.announcements_intro` | Comunicados oficiais sobre programação, inscrições, submissões e informações de participação serão publicados nesta área. | Template text or future Home content block | UI review UXR1-003 | needs-field |
| Home | Submissions teaser | `home.submissions_teaser` | Autores devem acompanhar os canais oficiais. A submissão inicial não exige vídeo. | Template text or future Home content block | Mandatory video rule | needs-field |
| Home | Supporting entities intro | `home.supporting_entities_intro` | A realização envolve instituições organizadoras, agência de fomento e parceiros institucionais e científicos. | Template section intro | Support taxonomy not final | provisional |
| Home | "O que esperar?" | `home.expectations` | Do not add separate block in this round. | Defer; do not implement | UI backlog UXR1-004 | defer |
| About | Page intro | `about.page_intro` | O CBNV 2026 reúne pesquisadores, estudantes, profissionais da saúde e instituições científicas para discutir a visão como fenômeno biológico, clínico, tecnológico e social. | `pages.content.ABOUT_CONTENT` or Wagtail `AboutPage.body` | UI backlog UXR1-005 | ready |
| About | What CBNV is | `about.what_is_cbnv` | O Congresso Brasileiro de Neurociências da Visão é um encontro técnico-científico dedicado ao estudo da visão, do cérebro e do comportamento visual. | `pages.content.ABOUT_CONTENT` or Wagtail `AboutPage.body` | Requirements positioning | ready |
| About | Theme context | `about.theme_context` | Com o tema Neurovisão na Era da Inteligência Artificial, o CBNV 2026 propõe uma discussão cuidadosa sobre métodos computacionais e ferramentas de IA na pesquisa e na clínica. | `pages.content.ABOUT_CONTENT` or Wagtail `AboutPage.body` | Requirements scientific positioning | ready |
| About | Audience | `about.audience` | Pesquisadores, estudantes, profissionais de saúde, docentes, equipes clínicas e representantes institucionais. | `pages.content.ABOUT_CONTENT` or Wagtail `AboutPage.body` | Requirements user journeys | ready |
| About | Organization support | `about.organization_support` | A UFMG é instituição proponente; a FUNDEP atua como instituição gestora; demais entidades devem seguir taxonomia validada. | `pages.content.ABOUT_CONTENT`; sponsors taxonomy | Requirements and canonical seed | provisional |
| About | Local access | `CoreSettings.canonical_venue` | CAD-1/UFMG and official address | `CoreSettings` venue fields | Canonical venue data | ready |
| About | Committee intro | `about.committee_intro` | A composição da comissão organizadora deve ser tratada como informação institucional em validação. | `pages.content.ABOUT_CONTENT.committee_intro` | UI review says committee is provisional | provisional |
| Program | Intro | `ProgramPage.intro` | A programação preliminar do CBNV 2026 está organizada em três dias temáticos, com conferências, palestras, sessões temáticas, apresentações orais e sessões de pôsteres. | Wagtail `ProgramPage.intro` or seed when canonical page seed exists | `seed_program` data | ready |
| Program | Status note | `program.status_note` | Programação preliminar, sujeita a atualização. | Template text or future field | Program status policy | needs-field |
| Program | Pending participants | `program.pending_participants_note` | O site exibe apenas informações liberadas para publicação. | Template text or future field | Program helper hides pending details | needs-field |
| Program | Workshops | `program.workshops` | Do not mention workshops unless official program data confirms them. | Editorial guideline only | Mandatory rule | defer |
| Speakers | Intro | `SpeakerIndexPage.intro` | Esta página apresenta palestrantes e participantes confirmados com presença pública na programação do CBNV 2026. | Wagtail `SpeakerIndexPage.intro` | Speaker visibility rules | ready |
| Speakers | Empty state | `speakers.empty_state` | Palestrantes confirmados serão publicados quando estiverem disponíveis na programação oficial. | Existing `speaker_index_page.html` text | Current template already close | ready |
| Speakers | Photo fallback | `speakers.photo_fallback` | Foto em atualização | Template alt/helper if needed | Accessibility/content fallback | needs-field |
| Speakers | Bio fallback | `speakers.bio_fallback` | Mini-bio em atualização. Consulte a programação para o tema da participação confirmada. | Template fallback if needed | Speaker cards | needs-field |
| Submissions | Intro | `SubmissionsPage.intro` | As submissões científicas do CBNV 2026 seguirão um fluxo em duas fases: submissão inicial para avaliação e materiais finais para trabalhos aprovados. | Wagtail `SubmissionsPage.intro` | Requirements submission flow | ready |
| Submissions | Status | `SubmissionsPage.status` | Submissões em breve | Wagtail `SubmissionsPage.status` | Pending operational channel | ready |
| Submissions | Initial requirements | `submissions.initial_requirements` | Metadados, autores e afiliações, resumo, eixo temático, palavras-chave, PDF e ciência das regras. | Template text or Wagtail body | Requirements phase 1 | ready |
| Submissions | Video rule | `submissions.video_rule` | Video não é exigido na submissão inicial. | Existing template text or Wagtail body | Mandatory rule | ready |
| Submissions | Final materials | `submissions.final_materials` | PDF final, arte de pôster, link de video e autorizações podem ser solicitados depois da aprovação. | Existing template text or Wagtail body | Requirements phase 2 | ready |
| Submissions | CTA | `submissions.cta_pending` | Canal oficial a definir | Existing template disabled state | UI backlog UXR1-010 | provisional |
| Registration | Intro | `RegistrationPage.intro` | As inscrições do CBNV 2026 serão realizadas por plataforma externa oficial. | Wagtail `RegistrationPage.intro` | Requirements external registration | ready |
| Registration | External process | `registration.external_process` | O site não processa pagamento, não emite certificados e não gera QR code de credenciamento. | Existing template text or Wagtail body | Mandatory rule | ready |
| Registration | Coming soon | `registration.coming_soon` | Inscrições em breve. Valores, categorias e link oficial serão publicados após confirmação. | Template pending state | Pending link policy | ready |
| Registration | CTA available | `registration.cta_available` | Acessar inscrições | Template CTA | External registration | ready |
| Registration | CTA pending | `registration.cta_pending` | Link em breve | Template pending state | Pending link policy | ready |
| Sponsorship | Intro | `SponsorsPage.intro` | O CBNV 2026 conta com apoio institucional e científico para realizar uma programação qualificada e manter o acesso público a informações do congresso. | Wagtail `SponsorsPage.intro` | UI review taxonomy issue | provisional |
| Sponsorship | Support value | `sponsorship.support_value` | O apoio institucional contribui para a organização científica, infraestrutura, divulgação e aproximação entre universidades, serviços de saúde, pesquisadores e estudantes. | Template or Wagtail body if field exists later | Sponsor page content gap | needs-field |
| Sponsorship | Taxonomy | `sponsorship.taxonomy` | instituições organizadoras; agência de fomento; parceiros institucionais e científicos; patrocinadores | Editorial guideline and consistency proposal | UXR1-006 target is consistency review | provisional |
| Sponsorship | Contact | `sponsorship.contact` | Propostas de apoio institucional, parceria ou patrocínio devem ser encaminhadas pelo canal indicado. | Existing template contact block | Current contact behavior | ready |
| Previous Editions | Intro | `PreviousEditionsPage.intro` | As edições anteriores compõem o acervo histórico do Congresso Brasileiro de Neurociências da Visão. | Wagtail `PreviousEditionsPage.intro` | Archive framing requirement | ready |
| Previous Editions | Archive note | `previous_editions.archive_note` | Datas, locais e temas de edições anteriores são registros históricos. | Template text or future field | UXR1-013 | needs-field |
| Previous Editions | Proceedings label | `previous_editions.proceedings_label` | Anais da edição | Template link label | Archive clarity | ready |
| Previous Editions | Playlist label | `previous_editions.playlist_label` | Playlist da edição | Template link label | YouTube link policy | ready |
| Contact | Intro | `ContactPage.intro` | Use esta página para falar com a organização, encaminhar dúvidas sobre participação, submissões ou apoio institucional, e consultar o local. | Wagtail `ContactPage.intro` | Contact journey | ready |
| Contact | Categories | `contact.categories` | Contato geral; Submissões; Apoio institucional e patrocínio | Existing template labels | Contact model fields | ready |
| Contact | Venue | `CoreSettings.canonical_venue` | CAD-1/UFMG and official address | `CoreSettings` venue fields | Canonical venue source | ready |
| Contact | Access note | `CoreSettings.venue_access_notes` | Orientações detalhadas de acesso e mobilidade serão publicadas quando confirmadas. | `CoreSettings.venue_access_notes` if blank or future body copy | Optional venue field | needs-data |
| Footer | Event identity | `footer.event_identity` | CBNV 2026 - XII Congresso Brasileiro de Neurociências da Visão | Footer template using settings | Footer should be concise | ready |
| Footer | Concise description | `footer.description` | 11 a 13 de novembro de 2026, no CAD-1/UFMG, em Belo Horizonte. | Footer template using settings | Reduce redundancy | ready |
| Footer | FAPEMIG acknowledgement | `CoreSettings.fapemig_text` | Apoio institucional: FAPEMIG - Fundacao de Amparo a Pesquisa do Estado de Minas Gerais. | `CoreSettings.fapemig_text` protected seed field | Canonical seed | provisional |
| Footer | Instagram label | `footer.instagram_label` | CBNV no Instagram | Existing icon link label | Social link clarity | ready |
| Footer | YouTube label | `footer.youtube_label` | Canal do CBNV no YouTube | Existing icon link label | Video policy | ready |

## Blocks Not To Implement Yet

- A separate Home/About "O que esperar?" block, unless a later polish proposal gives it a distinct role.
- Workshop copy, because no workshop activity is confirmed in current program data.
- Final registration categories, values and capacity rules.
- Final submission dates, edital details and official submission channel.
- Final sponsor package language.
- Final committee roles and biographies.
- Any new CMS fields or migrations for this round.
