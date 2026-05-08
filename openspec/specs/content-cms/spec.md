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
