## ADDED Requirements

### Requirement: Dashboard shell for authenticated areas
As telas de área do autor e revisor SHALL herdar de `base_dashboard.html`, fornecendo uma interface de navegação focada em tarefas, separada do site institucional.

#### Scenario: Author dashboard layout
- **WHEN** um autor faz login e acessa seu painel
- **THEN** SHALL ser apresentado com o shell de dashboard contendo navegação lateral para suas submissões

### Requirement: Profile and submission form styling
Componentes de formulário (`accessible_input`, `primary_button`) SHALL ser usados em todas as telas de autenticação e perfil para manter a consistência visual.

#### Scenario: Profile editing form consistency
- **WHEN** um usuário edita seu perfil
- **THEN** os inputs SHALL seguir o padrão visual definido no Design System
