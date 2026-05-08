# Site Público (public-site)

## Purpose
Definir como as páginas públicas passam a consumir conteúdo dinâmico do CMS mantendo consistência visual com os shells e componentes do design system.

## MODIFIED Requirements

### Requirement: Layout consistency
As páginas do site público SHALL usar o layout `templates/layouts/public.html` para garantir consistência visual e navegação institucional uniforme. Metadados dinâmicos (títulos de página, descrição SEO) SHALL ser extraídos dos modelos de página do CMS.

#### Scenario: Uniform navigation across pages
- **WHEN** um usuário navega entre "Home" e "Sobre"
- **THEN** SHALL encontrar o mesmo header e footer em ambas as páginas

### Requirement: Public component integration
Componentes como `scientific_card` e `timeline` SHALL ser usados para renderizar destaques da programação e palestrantes na área pública. Os dados para esses componentes MUST vir preferencialmente dos Snippets e Páginas do Wagtail.

#### Scenario: Timeline rendering on public page
- **WHEN** a página de programação é carregada
- **THEN** SHALL usar os partials do Design System para exibir a grade de horários
