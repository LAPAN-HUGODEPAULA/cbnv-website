## ADDED Requirements

### Requirement: Layout consistency
As páginas do site público SHALL usar o layout `base_public.html` para garantir consistência visual e navegação institucional uniforme.

#### Scenario: Uniform navigation across pages
- **WHEN** um usuário navega entre "Home" e "Sobre"
- **THEN** SHALL encontrar o mesmo header e footer em ambas as páginas

### Requirement: Public component integration
Componentes como `scientific_card` e `timeline` SHALL ser usados para renderizar destaques da programação e palestrantes na área pública.

#### Scenario: Timeline rendering on public page
- **WHEN** a página de programação é carregada
- **THEN** SHALL usar os partials do Design System para exibir a grade de horários
