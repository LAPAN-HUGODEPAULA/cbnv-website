# Dashboards

## Purpose

Esta especificação define os requisitos para as áreas internas de dashboard sensíveis ao papel (role-aware) para autores, revisores e membros do comitê científico.
## Requirements
### Requirement: Índice de dashboard autenticado
A plataforma SHALL fornecer um índice de dashboard autenticado.

#### Scenario: Visitante não autenticado abre o dashboard
- **GIVEN** que um visitante não autenticado solicita o dashboard
- **WHEN** a requisição é processada
- **THEN** o visitante SHALL ser redirecionado para o login.

#### Scenario: Usuário autenticado abre o dashboard
- **GIVEN** que um usuário autenticado solicita o dashboard
- **WHEN** a requisição é processada
- **THEN** ele SHALL ver as áreas de dashboard disponíveis baseadas nos papéis do seu perfil.

### Requirement: Shell de dashboard do autor
A plataforma SHALL fornecer um shell de dashboard do autor.

#### Scenario: Autor abre o dashboard do autor
- **GIVEN** que um usuário autenticado possui o papel de autor
- **WHEN** ele abre o dashboard do autor
- **THEN** ele SHALL ver uma área de autor com placeholders para submissões futuras.

#### Scenario: Não-autor abre o dashboard do autor
- **GIVEN** que um usuário autenticado não possui o papel de autor
- **WHEN** ele abre o dashboard do autor
- **THEN** o acesso SHALL ser negado ou redirecionado.

### Requirement: Shell de dashboard do revisor
A plataforma SHALL fornecer um shell de dashboard do revisor.

#### Scenario: Revisor abre o dashboard do revisor
- **GIVEN** que um usuário autenticado possui o papel de revisor
- **WHEN** ele abre o dashboard do revisor
- **THEN** ele SHALL ver uma área de revisor com placeholders para revisões futuras.

### Requirement: Shell de dashboard do chair
A plataforma SHALL fornecer um shell de dashboard do chair/comitê científico.

#### Scenario: Chair abre o dashboard do chair
- **GIVEN** que um usuário autenticado possui o papel de chair
- **WHEN** ele abre o dashboard do chair
- **THEN** ele SHALL ver uma área de comitê com placeholders para fluxos de trabalho futuros.

### Requirement: Shells de dashboard não implementam fluxos de trabalho
Os shells de dashboard SHALL NOT implementar fluxos de trabalho de submissão ou revisão nesta mudança.

#### Scenario: Dashboard do autor renderiza
- **GIVEN** que o dashboard do autor renderiza
- **THEN** ele SHALL NOT fornecer a criação real de submissões a menos que a proposta posterior de fluxo de submissão tenha sido implementada.

### Requirement: Authenticated dashboard index

The platform SHALL provide an authenticated dashboard index.

#### Scenario: Unauthenticated visitor opens dashboard

Given an unauthenticated visitor requests the dashboard
When the request is processed
Then the visitor SHALL be redirected to login.

#### Scenario: Authenticated user opens dashboard

Given an authenticated user requests the dashboard
When the request is processed
Then they SHALL see available dashboard areas based on their profile roles.

### Requirement: Author dashboard shell

The platform SHALL provide an author dashboard shell.

#### Scenario: Author opens author dashboard

Given an authenticated user has author role
When they open the author dashboard
Then they SHALL see an author area with future submission placeholders.

#### Scenario: Non-author opens author dashboard

Given an authenticated user does not have author role
When they open the author dashboard
Then access SHALL be denied or redirected.

### Requirement: Reviewer dashboard shell

The platform SHALL provide a reviewer dashboard shell.

#### Scenario: Reviewer opens reviewer dashboard

Given an authenticated user has reviewer role
When they open the reviewer dashboard
Then they SHALL see a reviewer area with future review placeholders.

### Requirement: Chair dashboard shell

The platform SHALL provide a chair/scientific committee dashboard shell.

#### Scenario: Chair opens chair dashboard

Given an authenticated user has chair role
When they open the chair dashboard
Then they SHALL see a committee area with future workflow placeholders.

### Requirement: Dashboard shells do not implement workflows

Dashboard shells SHALL not implement submission or review workflows in this change.

#### Scenario: Author dashboard renders

Given the author dashboard renders
Then it SHALL NOT provide actual submission creation unless the later submission-flow proposal has been implemented.

### Requirement: Author dashboard submission list

The author dashboard SHALL show the authenticated author's own submissions.

#### Scenario: Author has submissions

Given an authenticated author has one or more submissions  
When they open the author dashboard  
Then their submissions SHALL be listed with title, code, status and relevant date.

#### Scenario: Author has no submissions

Given an authenticated author has no submissions  
When they open the author dashboard  
Then an empty state SHALL explain how to start a submission if submissions are open.

### Requirement: Dashboard shows submission status safely

The author dashboard SHALL show submission status without exposing review workflow not yet implemented.

#### Scenario: Submitted item shown

Given a submission has submitted status  
When the dashboard renders  
Then the status SHALL be shown as submitted/received, not accepted or rejected.

### Requirement: Dashboard links only to owned submissions

The author dashboard SHALL link only to submissions owned by the authenticated user.

#### Scenario: Other user's submission exists

Given another user's submission exists  
When the author dashboard renders  
Then the other user's submission SHALL NOT be listed.

### Requirement: Reviewer dashboard review list

The reviewer dashboard SHALL list all submissions assigned to the current reviewer.

#### Scenario: Reviewer sees assignments
- **WHEN** a reviewer opens their dashboard
- **THEN** they SHALL see a list of assigned submissions with a link to the evaluation form for each.

### Requirement: Chair dashboard submission management

The chair dashboard SHALL provide an interface to manage all submissions and their review status.

#### Scenario: Chair manages submissions
- **WHEN** a chair opens the management interface
- **THEN** they SHALL see all submissions and be able to access assignment and decision tools for each.

