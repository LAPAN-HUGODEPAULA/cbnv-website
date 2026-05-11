# Site Público (public-site)

## Purpose
Definir como as páginas públicas passam a consumir conteúdo dinâmico do CMS mantendo consistência visual com os shells e componentes do design system.

## Requirements

### Requirement: Layout consistency
As páginas do site público SHALL usar o layout `templates/layouts/public.html` para garantir consistência visual e navegação institucional uniforme. Metadados dinâmicos (títulos de página, descrição SEO) SHALL ser extraídos dos modelos de página do CMS.

#### Scenario: Uniform navigation across pages
- **WHEN** um usuário navega entre "Home" e "Sobre"
- **THEN** SHALL encontrar o mesmo header e footer em ambas as páginas

### Requirement: Program page with timeline
O sistema SHALL implementar `ProgramPage` que exibe a programação completa usando o componente `timeline.html` existente.

#### Scenario: Navigating to program timeline
- **WHEN** um usuário acessa a ProgramPage
- **THEN** SHALL exibir a timeline filtrável por dia com todos os talks confirmados

### Requirement: Public component integration
A `ProgramPage` SHALL usar os partials do Design System (`timeline.html`, `badge.html`) para renderizar a programação.

#### Scenario: Timeline rendering on program page
- **WHEN** a página de programação é carregada
- **THEN** SHALL usar o componente timeline existente para exibir horários, títulos, tipos e palestrantes
- **AND** SHALL omitir inteiramente itens não confirmados

### Requirement: Home Page Content
A página Home SHALL exibir informações de alto impacto, incluindo data do evento, local, chamada para ação (CTA) principal e destaques do congresso.

#### Scenario: Visitor lands on Home
- **WHEN** o visitante acessa a URL raiz
- **THEN** SHALL ver a seção hero with details chave do evento e um botão "Inscreva-se Agora"

### Requirement: Registration Informational Page
A página de Inscrição SHALL fornecer informações sobre preços, datas e instruções, direcionando o usuário para uma plataforma externa ou exibindo uma mensagem de "Em breve".

#### Scenario: Visitor views registration info
- **WHEN** o visitante navega para a página de Inscrição
- **THEN** SHALL ver a tabela de preços e um link para o sistema externo de inscrição

### Requirement: Submissions Informational Page
A página de Submissões SHALL exibir as regras, datas importantes e categorias de submissão, sem fornecer o formulário de submissão nesta fase.

#### Scenario: Visitor views submission rules
- **WHEN** o visitante navega para a página de Submissões
- **THEN** SHALL ver a lista de requisitos e uma mensagem "Submissões abertas em [Data]"

### Requirement: Proceedings public page
O sistema SHALL fornecer uma página pública em `/anais/` listando todos os trabalhos publicados nos anais do congresso.

#### Scenario: Visitor accesses proceedings page
- **WHEN** um visitante acessa `/anais/`
- **THEN** SHALL ver a listagem de trabalhos publicados com título, autores, modalidade, eixo temático e resumo

#### Scenario: Filtering proceedings by modality
- **WHEN** o visitante seleciona o filtro "Oral" na página de anais
- **THEN** SHALL ver apenas trabalhos com modalidade oral

#### Scenario: Filtering proceedings by thematic axis
- **WHEN** o visitante seleciona um eixo temático no filtro
- **THEN** SHALL ver apenas trabalhos daquele eixo temático

### Requirement: Proceedings detail with embedded video
Trabalhos publicados com vídeo associado SHALL exibir um player YouTube incorporado na página de detalhes ou na listagem.

#### Scenario: Viewing published work with video
- **GIVEN** um trabalho publicado com `video_url` preenchido
- **WHEN** o visitante visualiza o trabalho nos anais
- **THEN** SHALL ver un player YouTube incorporado junto com os metadados do trabalho

#### Scenario: Viewing published work without video
- **GIVEN** um trabalho publicado sem `video_url`
- **WHEN** o visitante visualiza o trabalho nos anais
- **THEN** SHALL ver os metadados e download do PDF, sem player de vídeo

### Requirement: Proceedings PDF download
Trabalhos publicados SHALL ter seu PDF final disponível para download público.

#### Scenario: Downloading proceedings PDF
- **WHEN** o visitante clica no botão de download do PDF de um trabalho publicado
- **THEN** o PDF final SHALL ser baixado diretamente

#### Scenario: PDF not available for unpublished work
- **GIVEN** um trabalho que não está publicado nos anais
- **WHEN** alguém tenta acessar diretamente o URL do PDF
- **THEN** o sistema SHALL negar o acesso (403)

### Requirement: Accessibility Landmarks
The public site layouts SHALL include ARIA landmarks (`<header>`, `<nav>`, `<main>`, `<footer>`) to facilitate navigation for screen reader users.

#### Scenario: Landmarks present on homepage
- **WHEN** the homepage is loaded
- **THEN** a screen reader SHALL identify the banner, navigation, main content, and footer regions

### Requirement: Skip to Content Link
The `public.html` layout SHALL include a "Skip to Content" link as the first focusable element on every page.

#### Scenario: Skipping navigation
- **WHEN** a keyboard user presses TAB on page load
- **THEN** a "Skip to Content" link SHALL become visible
- **AND** clicking it SHALL move focus to the `<main>` element

### Requirement: Image Optimization for Performance
The public site SHALL serve images in modern formats (WebP/AVIF) with appropriate `srcset` attributes for responsive delivery.

#### Scenario: Responsive images served
- **WHEN** a user accesses the site from a mobile device
- **THEN** the system SHALL serve a lower-resolution version of the hero image to save bandwidth

### Requirement: Mobile Touch Targets
All interactive elements on mobile views SHALL have a minimum touch target size of 44x44 pixels.

#### Scenario: Buttons are easy to tap
- **WHEN** viewed on a mobile screen
- **THEN** all links and buttons SHALL meet the 44px minimum touch target size requirement

### Requirement: Footer FAPEMIG acknowledgement
O rodape publico SHALL exibir o logotipo da FAPEMIG originado de `_legacy/fapemig-logo.svg` juntamente com o nome "FAPEMIG" ou "Fundacao de Amparo a Pesquisa do Estado de Minas Gerais".

#### Scenario: Footer shows FAPEMIG
- **WHEN** qualquer pagina publica renderiza o rodape
- **THEN** o rodape SHALL exibir o logotipo da FAPEMIG com texto alternativo acessivel
- **AND** SHALL exibir o nome da FAPEMIG junto ao logotipo

### Requirement: Organization section on Home and About
A Home e a pagina Sobre SHALL exibir uma secao "Organizacao" com os logotipos das entidades organizadoras do XII CBNV.

#### Scenario: Home organization section
- **WHEN** o visitante acessa a Home
- **THEN** SHALL ver uma secao "Organizacao" ao final do conteudo principal com os logotipos das entidades organizadoras

#### Scenario: About organization section with names and links
- **WHEN** o visitante acessa a pagina Sobre
- **THEN** SHALL ver uma secao "Organizacao" com logotipos, nomes das entidades e links externos para as entidades que possuem URL cadastrada
- **AND** entidades sem URL SHALL aparecer sem link externo

### Requirement: About page editorial structure
A pagina Sobre SHALL ser reestruturada com base factual no conteudo legado do CBNV anterior e layout inspirado em `docs/stitch_cbnv_2026_digital_platform/sobre_e_local_xii_cbnv_2026/`, mantendo o estilo do site atual.

#### Scenario: About page sections
- **WHEN** o visitante acessa a pagina Sobre
- **THEN** SHALL ver as secoes "Bem vindos", "O evento", "Objetivos", "O que esperar", "Local e acessibilidade", "Comissao organizadora" e "Organizacao"
- **AND** SHALL NOT ver a secao "eventos recentes"

#### Scenario: About page tone
- **WHEN** a secao "O evento" e renderizada
- **THEN** o texto SHALL usar tom institucional e factual
- **AND** SHALL evitar linguagem sensacionalista ou promessas exageradas

### Requirement: About location and accessibility
A pagina Sobre SHALL apresentar uma secao "Local e acessibilidade" com informacoes do local do evento e um Google Maps incorporado inline.

#### Scenario: Inline map is available
- **WHEN** o visitante acessa a secao "Local e acessibilidade"
- **THEN** SHALL ver informacoes textuais do local do evento
- **AND** SHALL ver um iframe do Google Maps com titulo acessivel e carregamento lazy

### Requirement: About organizing committee
A pagina Sobre SHALL exibir a comissao organizadora copiada do 11o CBNV e incluir Hugo de Paula como Subcoordenador do Congresso, Pos-Doutorado em Neurociencias (UFMG).

#### Scenario: Organizer cards include photos
- **WHEN** o visitante acessa a secao "Comissao organizadora"
- **THEN** cada integrante com foto disponivel SHALL aparecer com nome, funcao, afiliacao ou descricao e imagem
- **AND** os arquivos de fotos copiados SHALL usar nomes normalizados baseados nos nomes dos integrantes

#### Scenario: Hugo de Paula is included
- **WHEN** a comissao organizadora e renderizada
- **THEN** SHALL incluir "Hugo de Paula" como "Subcoordenador do Congresso"
- **AND** SHALL exibir a descricao "Pos-Doutorado em Neurociencias (UFMG)"

### Requirement: Save the Date news image
A noticia "Save the Date: XII CBNV 2026 em Belo Horizonte!" SHALL exibir a imagem `_legacy/save-the-date.jpg`.

#### Scenario: Save the Date article renders image
- **WHEN** o visitante acessa a noticia "Save the Date: XII CBNV 2026 em Belo Horizonte!"
- **THEN** SHALL ver a imagem de Save the Date com texto alternativo descritivo

### Requirement: Congress Instagram link
O site publico SHALL exibir link para o Instagram oficial do congresso em local de navegacao social persistente.

#### Scenario: Instagram link is available
- **WHEN** o visitante acessa o rodape ou outra area persistente de redes sociais
- **THEN** SHALL ver um link para `https://www.instagram.com/cbnvufmg/`
- **AND** o link SHALL abrir de forma segura com `rel="noopener noreferrer"` quando usar nova aba

### Requirement: Responsive public header shell
O layout base publico SHALL incluir header responsivo com identidade do site, navegacao primaria e area reservada para CTA.

#### Scenario: Desktop header navigation
- **WHEN** uma pagina publica e renderizada em viewport desktop
- **THEN** a navegacao primaria SHALL estar visivel e utilizavel sem interacoes adicionais

#### Scenario: Mobile header navigation
- **WHEN** uma pagina publica e renderizada em viewport mobile
- **THEN** o padrao de navegacao mobile SHALL estar disponivel e acessivel por teclado

### Requirement: Public footer shell slots
O layout base publico SHALL incluir footer reutilizavel com links essenciais e area institucional para reconhecimento de apoio.

#### Scenario: Footer exposes essential navigation
- **WHEN** o visitante alcanca o rodape de qualquer pagina publica
- **THEN** o footer SHALL exibir links essenciais de navegacao

#### Scenario: Footer includes institutional acknowledgement slot
- **WHEN** houver necessidade de exibicao de apoio institucional
- **THEN** o footer SHALL fornecer area dedicada para FAPEMIG ou equivalente

### Requirement: Layout shell editorial neutrality
Antes da aprovacao editorial final no CMS, o layout shell publico SHALL usar placeholders neutros e SHALL NOT incluir afirmacoes promocionais nao verificadas no proprio shell.

#### Scenario: Placeholder usage in layout shell
- **WHEN** o shell de layout precisar de conteudo temporario
- **THEN** o texto SHALL usar placeholders neutros e delegar afirmacoes editoriais para blocos/conteudos gerenciados

### Requirement: Public layout consumes CMS-backed globals
The public layout SHALL be able to consume CMS-backed global values instead of hardcoded repeated values.

#### Scenario: Footer consumes global settings
- **WHEN** the footer needs event identity, social links or institutional acknowledgement
- **THEN** it SHALL use CMS-backed global settings where available

#### Scenario: Header consumes global link state
- **WHEN** the header needs a registration CTA and registration is not yet available
- **THEN** the header SHALL be able to render a clear "em breve" state instead of a broken link

### Requirement: Public pages can query featured content
Public pages SHALL be able to query featured news/announcements and supporting entities.

#### Scenario: Home requests featured news
- **WHEN** the Home page queries CMS content
- **THEN** it SHALL be able to retrieve published featured or recent news entries

#### Scenario: Footer requests supporting entities
- **WHEN** the footer queries CMS content
- **THEN** it SHALL be able to retrieve active entities marked for footer display
### Requirement: Public pages use seeded canonical values
Future public pages SHALL use seeded canonical values for repeated event facts.

#### Scenario: Page needs event dates
- **GIVEN** a public page needs the event dates
- **WHEN** it renders after the canonical seed exists
- **THEN** it SHALL use the CMS-backed canonical dates rather than hardcoded template text.

#### Scenario: Page needs venue address
- **GIVEN** a public page needs the event address
- **WHEN** it renders after the canonical seed exists
- **THEN** it SHALL use the CMS-backed CAD-1/UFMG address rather than hardcoded or inherited previous-edition location.

### Requirement: Coming-soon link states
Future public pages SHALL render unknown external links as clear coming-soon states.

#### Scenario: Registration URL is pending
- **GIVEN** registration status is coming soon
- **WHEN** a public CTA requests registration
- **THEN** the UI SHALL render an accessible “em breve” state instead of a broken link.

### Requirement: Institutional support data is reusable
Future public pages and footer SHALL reuse seeded institutional support data.

#### Scenario: Footer needs FAPEMIG acknowledgement
- **GIVEN** the canonical seed includes FAPEMIG support data
- **WHEN** the footer later renders institutional acknowledgement
- **THEN** it SHALL use CMS-backed support data rather than duplicating hardcoded text.
