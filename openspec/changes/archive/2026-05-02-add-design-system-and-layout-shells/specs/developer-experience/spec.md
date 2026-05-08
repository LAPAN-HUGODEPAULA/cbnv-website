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

## MODIFIED Requirements

### Requirement: Tailwind CSS build pipeline
O projeto SHALL integrar Tailwind CSS `4.2.4` via pipeline de build com os pacotes npm `tailwindcss` e `@tailwindcss/cli`. O projeto SHALL usar configuração CSS-first em `src/input.css` com `@import "tailwindcss";`, `@source` explícito para templates Django e `@theme` para tokens de design. O projeto SHALL NOT exigir `tailwind.config.js` por padrão. O build SHALL gerar CSS compilado em `static/css/output.css`. O `manage.py collectstatic` SHALL incluir o CSS compilado.

#### Scenario: Tailwind CSS builds successfully
- **WHEN** `npm run build` é executado
- **THEN** SHALL gerar `static/css/output.css` com classes Tailwind compiladas

#### Scenario: Tailwind classes available in templates
- **WHEN** um template Django usa classes utilitárias do Tailwind como `bg-cbnv-blue-600` e `text-white`
- **THEN** os estilos SHALL ser aplicados corretamente no HTML renderizado

#### Scenario: Django template sources are scanned
- **WHEN** o build Tailwind é executado
- **THEN** `src/input.css` SHALL declarar `@source` para os diretórios de templates Django usados pelo projeto
