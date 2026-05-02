## ADDED Requirements

### Requirement: Design tokens implementation
O sistema SHALL implementar tokens de design baseados na referência visual do Stitch (dark-mode first, azul-marinho profundo, azul elétrico, verde neuro). Os tokens MUST incluir paleta de cores, tipografia (serif para títulos, sans para corpo) e escalas de espaçamento integradas ao Tailwind CSS.

#### Scenario: Tailwind configuration updated with tokens
- **WHEN** o comando de build do Tailwind é executado
- **THEN** SHALL gerar classes utilitárias para as cores `#081426` (marinho), `#214BFF` (azul elétrico) e `#2FEA8B` (verde neuro)

### Requirement: Reusable layout shells
O sistema SHALL fornecer shells de layout reutilizáveis em templates Django: `base_public.html` (para visitantes, com header/footer institucional) e `base_dashboard.html` (para áreas autenticadas, com sidebar/topbar).

#### Scenario: Public layout includes main components
- **WHEN** uma página herda de `base_public.html`
- **THEN** SHALL renderizar automaticamente o header responsivo e o footer com menção à FAPEMIG

#### Scenario: Dashboard layout provides sidebar
- **WHEN** uma página herda de `base_dashboard.html`
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
