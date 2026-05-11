# Conteúdo CMS (content-cms)

## Purpose
Definir a fundação editorial Wagtail para metadados globais, páginas estruturadas, fluxo administrativo simples e propriedade dos modelos por domínio.

## Requirements

### Requirement: SiteSettings for global metadata
O sistema SHALL implementar `SiteSettings` do Wagtail para gerenciar dados globais. Os campos MUST incluir: Nome do Evento, Edição, Tema, Datas, Local, E-mail de Contato, Redes Sociais, Link Externo de Inscrição, Link de Transmissão e Texto de Menção FAPEMIG.

#### Scenario: Registration link configuration
- **GIVEN** que o admin acessa as configurações do site no Wagtail
- **WHEN** altera o "Link Externo de Inscrição"
- **THEN** o novo link SHALL refletir automaticamente nos botões de CTA do site público

### Requirement: Structured Page Models
O sistema SHALL fornecer modelos de página Wagtail para a estrutura principal: `HomePage`, `AboutPage`, `NewsIndexPage`, `NewsArticlePage`, `PreviousEditionsPage`, `ProgramPage`, `SpeakerIndexPage`, `SponsorsPage` e `VideoGalleryPage`.

#### Scenario: Program page setup
- **WHEN** um admin cria uma `ProgramPage` no Wagtail
- **THEN** ela SHALL servir como base para renderizar a timeline de programação usando o componente `timeline.html` do design system

#### Scenario: Speaker index page setup
- **WHEN** um admin cria uma `SpeakerIndexPage` no Wagtail
- **THEN** ela SHALL listar todos os palestrantes confirmados cadastrados no sistema

### Requirement: Sponsors Page Models
O sistema SHALL fornecer um modelo `SponsorsPage` para exibir a lista de patrocinadores agrupados por seus respectivos níveis (tiers).

#### Scenario: Admin configures sponsors page
- **WHEN** o administrador cria uma `SponsorsPage`
- **THEN** o sistema SHALL buscar automaticamente todos os patrocinadores ativos dos snippets e exibi-los por nível

### Requirement: Video Gallery Page Models
O sistema SHALL fornecer um modelo `VideoGalleryPage` para agregar e exibir recursos de vídeo vinculados a plataformas externas.

#### Scenario: Admin creates video gallery
- **WHEN** o administrador cria uma `VideoGalleryPage`
- **THEN** ele SHALL poder selecionar categorias de vídeo ou vídeos individuais para exibir na galeria

### Requirement: Single Admin Workflow
O sistema SHALL ser configurado para um fluxo de trabalho de administrador editorial único, simplificando as permissões e ocultando recursos de multi-perfil desnecessários para o MVP.

#### Scenario: Editorial content management
- **WHEN** o administrador único faz login no `/admin/`
- **THEN** SHALL ter acesso total a todas as funções editoriais (páginas, snippets, configurações) sem barreiras de RBAC complexo

### Requirement: Domain app ownership
O sistema SHALL manter modelos editoriais nos apps de domínio correspondentes. `CoreSettings` SHALL ficar em `core`, páginas Wagtail em `pages`, patrocinadores em `sponsors`, vídeos em `videos`, edições anteriores/acervo em `proceedings` e modelos de programação (`Speaker`, `ProgramDay`, `ProgramSession`, `ProgramTalk`) em `program`.

#### Scenario: Developer locates program models
- **WHEN** um desenvolvedor precisa alterar o modelo de palestrante
- **THEN** SHALL encontrar `Speaker` em `program/models.py`

### Requirement: Clear admin labels
CMS fields SHALL use clear Portuguese labels and help text where needed.

#### Scenario: Admin edits a public link
- **WHEN** the admin edits an external link field
- **THEN** the label and help text SHALL make clear where the link appears or what it controls

### Requirement: Visibility controls
CMS editorial models SHALL include simple visibility controls.

#### Scenario: Admin hides content
- **WHEN** a news item or supporting entity should not appear publicly
- **AND** the admin marks it as draft, hidden or inactive
- **THEN** later public queries SHALL exclude it

### Requirement: External public links
The platform SHALL centralize external public links used across the site.

#### Scenario: Registration link is configured
- **GIVEN** the registration platform is external
- **WHEN** the admin sets a registration URL and status
- **THEN** public templates SHALL be able to render either the configured link or a clear "em breve" state

#### Scenario: Social and media links are configured
- **GIVEN** YouTube or Instagram links are available
- **WHEN** the admin edits global settings
- **THEN** those links SHALL be stored centrally and reusable by public templates

### Requirement: Institutional acknowledgement
The platform SHALL provide a central CMS-backed field or slot for FAPEMIG acknowledgement.

#### Scenario: Footer needs FAPEMIG acknowledgement
- **WHEN** the footer or public page needs to show institutional support
- **THEN** it SHALL be able to obtain the FAPEMIG acknowledgement from the central CMS-backed source

### Requirement: News and announcements
The platform SHALL provide CMS-backed news or announcement entries.

#### Scenario: Admin creates announcement
- **GIVEN** the admin creates a news or announcement entry
- **WHEN** the entry is published
- **THEN** it SHALL become available for later public-page rendering

#### Scenario: Home can select featured news
- **GIVEN** multiple news or announcement entries exist
- **WHEN** one or more are marked as featured
- **THEN** later Home rendering SHALL be able to retrieve featured entries

#### Scenario: Draft news is hidden
- **GIVEN** a news or announcement entry has draft status
- **WHEN** public content queries are used
- **THEN** the draft entry SHALL NOT be returned as publicly visible
### Requirement: Idempotent CMS seed
The platform SHALL provide an idempotent seed mechanism for canonical CMS content.

#### Scenario: Seed can run twice
- **GIVEN** the seed command or fixture has been executed once
- **WHEN** it is executed again
- **THEN** it SHALL complete successfully without creating duplicate global settings or supporting entities.

#### Scenario: Seed reports results
- **GIVEN** the seed command is executed
- **WHEN** it completes
- **THEN** it SHOULD report created, updated or skipped records in a readable summary.

### Requirement: Manual edits are protected where appropriate
The seed mechanism SHALL document whether it overwrites existing values or only creates missing content.

#### Scenario: Idempotence behavior is documented
- **GIVEN** a developer reads the seed documentation
- **WHEN** they inspect how existing records are handled
- **THEN** they SHALL know which fields are authoritative and which fields are preserved after manual edits.

### Requirement: Pending external links are represented safely
The seed SHALL represent unknown external links with an explicit pending state rather than broken placeholder URLs.

#### Scenario: Unknown registration URL
- **GIVEN** the registration URL is not known
- **WHEN** canonical content is seeded
- **THEN** registration status SHALL be stored as coming soon or equivalent
- **AND** the seed SHALL NOT store `#` as the registration URL.

### Requirement: Canonical event identity seed
The platform SHALL provide a seed mechanism for canonical CBNV 2026 event identity.

#### Scenario: Seed event identity
- **GIVEN** the CMS global settings model exists
- **WHEN** the canonical content seed is executed
- **THEN** the formal event name, short name, edition, theme, dates, format, city, state and country SHALL be created or updated in the central settings model.

### Requirement: Canonical venue seed
The platform SHALL seed the official CBNV 2026 venue and address.

#### Scenario: Seed official venue
- **GIVEN** the canonical content seed is executed
- **WHEN** venue fields exist in the global settings model
- **THEN** the venue SHALL be set to CAD-1/UFMG with the official full address and Google Maps URL.

#### Scenario: Previous edition venue is not used
- **GIVEN** the seed is executed
- **WHEN** venue data is created or updated
- **THEN** it SHALL NOT use venue data inherited from previous CBNV editions.

### Requirement: Canonical supporting entities seed
The platform SHALL seed known institutional/support entities.

#### Scenario: Seed supporting entities
- **GIVEN** supporting-entity models exist
- **WHEN** the seed is executed
- **THEN** known entities such as UFMG, FUNDEP, FAPEMIG, Sociedade Brasileira de Neurovisão, HOLHOS, UFRJ, USP, UFRN and UEMG SHALL be created or updated.

#### Scenario: Supporting entities are not duplicated
- **GIVEN** the seed has already been executed once
- **WHEN** the seed is executed again
- **THEN** duplicate supporting entities SHALL NOT be created.

### Requirement: Conservative seeded content
Seeded content SHALL avoid unverified claims and final promotional copy.

#### Scenario: Seed avoids inflated claims
- **GIVEN** the seed creates default text or announcements
- **WHEN** the content is inspected
- **THEN** it SHALL NOT claim that the event is the largest in Latin America or use similarly unverified promotional claims.
