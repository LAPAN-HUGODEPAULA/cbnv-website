# Site Público (public-site)

## Purpose
Definir a página de programação no site público.

## ADDED Requirements

### Requirement: Program page with timeline
O sistema SHALL implementar `ProgramPage` que exibe a programação completa usando o componente `timeline.html` existente.

#### Scenario: Navigating to program timeline
- **WHEN** um usuário acessa a ProgramPage
- **THEN** SHALL exibir a timeline filtrável por dia com todos os talks confirmados

## MODIFIED Requirements

### Requirement: Public component integration
A `ProgramPage` SHALL usar os partials do Design System (`timeline.html`, `badge.html`) para renderizar a programação.

#### Scenario: Timeline rendering on program page
- **WHEN** a página de programação é carregada
- **THEN** SHALL usar o componente timeline existente para exibir horários, títulos, tipos e palestrantes
- **AND** SHALL omitir inteiramente itens não confirmados
