## ADDED Requirements

### Requirement: Template and partial organization
A estrutura de templates SHALL ser organizada para facilitar a reutilização:
- `templates/base.html` (estrutura base)
- `templates/layouts/` (shells específicos como public e dashboard)
- `templates/components/` (biblioteca de partials reutilizáveis)

#### Scenario: Developer finds component easily
- **WHEN** um desenvolvedor precisa adicionar um botão
- **THEN** SHALL encontrar o partial em `templates/components/button.html`

### Requirement: Design documentation access
O projeto SHALL incluir um arquivo `DESIGN.md` resumindo como aplicar os tokens e componentes para novos desenvolvedores.

#### Scenario: New dev onboarding for UI
- **WHEN** um novo membro da equipe inicia no projeto
- **THEN** SHALL consultar o `DESIGN.md` para entender o uso das classes Tailwind customizadas
