# Design System (design-system)

## Purpose
Padronizar a identidade visual, tokens de design e componentes reutilizáveis acessíveis.

## Requirements

### Requirement: Design tokens implementation
O sistema SHALL implementar tokens de design baseados na referência visual do Stitch (dark-mode first, azul-marinho profundo, azul elétrico, verde neuro). Os tokens MUST incluir paleta de cores, tipografia (serif para títulos, sans para corpo) e escalas de espaçamento integradas ao Tailwind CSS `4.2.4` por meio de configuração CSS-first em `src/input.css` usando `@theme`.

#### Scenario: Tailwind CSS-first theme updated with tokens
- **WHEN** o comando de build do Tailwind é executado
- **THEN** SHALL gerar classes utilitárias para as cores `#081426` (marinho), `#214BFF` (azul elétrico) e `#2FEA8B` (verde neuro)
- **AND** SHALL NOT require a `tailwind.config.js` file for tokens or template scanning

### Requirement: Reusable layout shells
O sistema SHALL fornecer shells de layout reutilizáveis em templates Django: `templates/layouts/public.html` (para visitantes, com header/footer institucional) e `templates/layouts/dashboard.html` (para áreas autenticadas, com sidebar/topbar).

#### Scenario: Public layout includes main components
- **WHEN** uma página herda de `templates/layouts/public.html`
- **THEN** SHALL renderizar automaticamente o header responsivo e o footer com menção à FAPEMIG

#### Scenario: Dashboard layout provides sidebar
- **WHEN** uma página herda de `templates/layouts/dashboard.html`
- **THEN** SHALL renderizar o menu lateral de navegação para as áreas científicas

### Requirement: Accessible component library
O projeto SHALL conter uma biblioteca de partials (includes) Django para componentes comuns: `header`, `footer`, `scientific_card`, `timeline_item`, `status_badge`, `accessible_input`, `primary_button`. Todos os componentes MUST seguir as diretrizes WCAG 2.2 AA (contraste, foco visível, labels).

#### Scenario: Header is responsive
- **WHEN** acessado em dispositivo mobile
- **THEN** SHALL exibir menu hambúrguer com interações Alpine.js ou CSS puro

#### Scenario: Components are keyboard accessible
- **WHEN** um usuário navega via tecla TAB
- **THEN** todos os elementos interativos (botões, links) SHALL exibir um contorno de foco (focus ring) visível

### Requirement: Empty and error states
O sistema SHALL fornecer componentes para estados de interface: `loading_spinner`, `empty_state` (com ilustração/placeholder), `error_state` (com mensagem de feedback e CTA de retorno).

#### Scenario: Empty state display
- **WHEN** uma lista (ex: submissões) não possui itens
- **THEN** SHALL exibir o componente de empty state com texto explicativo

### Requirement: WCAG 2.2 AA Contrast and Legibility
The system SHALL ensure a minimum contrast ratio of 4.5:1 for normal text and 3:1 for large text across all components. High-contrast mode compatibility SHALL be maintained.

#### Scenario: Visual elements pass contrast check
- **WHEN** components are rendered in the UI
- **THEN** an automated contrast check SHALL verify all text meets WCAG 2.2 AA minimum ratios

### Requirement: Focus States and Keyboard Navigation
All interactive elements MUST have a visible, high-contrast focus ring when navigated via keyboard. The tab order SHALL follow the logical visual layout.

#### Scenario: Focus ring is visible
- **WHEN** a user navigates via TAB key to a button or link
- **THEN** a 2px outline with high contrast relative to the background SHALL appear around the element

### Requirement: Reduced Motion Support
The system SHALL respect the `prefers-reduced-motion` media query by disabling non-essential animations and transitions.

#### Scenario: Animations are disabled
- **WHEN** the user's OS preference is set to reduced motion
- **THEN** Tailwind's `motion-safe` utilities SHALL ensure animations are suppressed

### Requirement: Semantic Heading Hierarchy
Templates SHALL use a strictly sequential heading hierarchy (H1 -> H2 -> H3) without skipping levels to ensure screen reader compatibility.

#### Scenario: Heading structure is valid
- **WHEN** a page is rendered
- **THEN** the first heading SHALL be an H1 and subsequent sub-headings SHALL be H2, H3, etc., in order

### Requirement: Design system usage documentation
The project SHALL maintain documentation for design-system primitives, including tokens, shared partials, and accessibility expectations, to support consistent template implementation.

#### Scenario: Developer consults design-system documentation
- **WHEN** a developer needs to create or update a public template
- **THEN** they SHALL find documented token names, component usage examples, and accessibility rules in project documentation

### Requirement: Typography roles
The platform SHALL define explicit typography roles for display text, body text and technical labels via source-level font tokens with readable system fallbacks.

#### Scenario: Font fallback is available
- **WHEN** custom fonts fail to load or are not yet configured
- **THEN** the site SHALL render with readable system fallback fonts

### Requirement: Responsive layout primitives
The design system SHALL provide mobile-first layout primitives (content containers, cards, navigation) that remain usable without horizontal scrolling on narrow viewports.

#### Scenario: Layout works on mobile
- **WHEN** a visitor opens the site on a narrow viewport
- **THEN** core navigation, content containers and cards SHALL remain usable without horizontal scrolling
