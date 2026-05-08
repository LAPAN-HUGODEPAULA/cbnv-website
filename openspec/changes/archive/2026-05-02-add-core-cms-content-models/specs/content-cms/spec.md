# Conteúdo CMS (content-cms)

## Purpose
Definir a fundação editorial Wagtail para metadados globais, páginas estruturadas, fluxo administrativo simples e propriedade dos modelos por domínio.

## ADDED Requirements

### Requirement: SiteSettings for global metadata
O sistema SHALL implementar `SiteSettings` do Wagtail para gerenciar dados globais. Os campos MUST incluir: Nome do Evento, Edição, Tema, Datas, Local, E-mail de Contato, Redes Sociais, Link Externo de Inscrição, Link de Transmissão e Texto de Menção FAPEMIG.

#### Scenario: Registration link configuration
- **GIVEN** que o admin acessa as configurações do site no Wagtail
- **WHEN** altera o "Link Externo de Inscrição"
- **THEN** o novo link SHALL refletir automaticamente nos botões de CTA do site público

### Requirement: Structured Page Models
O sistema SHALL fornecer modelos de página Wagtail para a estrutura principal: `HomePage`, `AboutPage`, `NewsIndexPage`, `NewsArticlePage` e `PreviousEditionsPage`.

#### Scenario: News article publication
- **WHEN** um admin publica uma `NewsArticlePage` sob o `NewsIndexPage`
- **THEN** ela SHALL aparecer automaticamente na lista de notícias e, se marcada como destaque, na Home

### Requirement: Single Admin Workflow
O sistema SHALL ser configurado para um fluxo de trabalho de administrador editorial único, simplificando as permissões e ocultando recursos de multi-perfil desnecessários para o MVP.

#### Scenario: Editorial content management
- **WHEN** o administrador único faz login no `/admin/`
- **THEN** SHALL ter acesso total a todas as funções editoriais (páginas, snippets, configurações) sem barreiras de RBAC complexo

### Requirement: Domain app ownership
O sistema SHALL manter modelos editoriais nos apps de domínio correspondentes. `CoreSettings` SHALL ficar em `core`, páginas Wagtail em `pages`, patrocinadores em `sponsors`, vídeos em `videos` e edições anteriores/acervo em `proceedings`.

#### Scenario: Developer locates editorial models by domain
- **WHEN** um desenvolvedor precisa alterar o modelo de vídeo
- **THEN** SHALL encontrar `VideoResource` em `videos/models.py`
