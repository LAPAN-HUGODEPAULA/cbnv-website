## MODIFIED Requirements

### Requirement: Custom user model
O sistema SHALL definir `accounts.User` como custom user model via `AUTH_USER_MODEL = "accounts.User"`. O model SHALL herdar de `AbstractUser` e utilizar os campos nativos `first_name` e `last_name` do Django em vez de um campo `full_name` redundante. Campos customizados:
- `first_name` (herdado do Django, Nome)
- `last_name` (herdado do Django, Sobrenome)
- `institution` (CharField, Instituição)
- `country` (CharField, País com choices ISO)
- `position` (CharField, Vínculo/Cargo)
- `is_author` (BooleanField, Default=False)
- `is_reviewer` (BooleanField, Default=False)
- `is_chair` (BooleanField, Default=False)
- `consent_privacy` (BooleanField, Default=False)
- `consent_image` (BooleanField, Default=False)

O método `__str__` SHALL retornar `self.get_full_name()` ou `self.username` como fallback.
Para saudações personalizadas (ex: "Olá, Hugo!"), SHALL ser utilizado `self.first_name`.

#### Scenario: User creation with profile fields
- **GIVEN** que o sistema está configurado com `accounts.User`
- **WHEN** um usuário é criado via formulário ou `createsuperuser`
- **THEN** SHALL ser possível preencher `first_name`, `last_name`, `institution`, `country` e `position`

#### Scenario: User with multiple scientific roles
- **GIVEN** um usuário existente no sistema
- **WHEN** o admin marca simultaneamente `is_author=True` e `is_reviewer=True`
- **THEN** o usuário SHALL possuir ambos os papéis sem necessidade de contas separadas

#### Scenario: Personalized greeting
- **GIVEN** um usuário com `first_name="Hugo"` e `last_name="de Paula"`
- **WHEN** o sistema exibe uma saudação
- **THEN** SHALL exibir "Olá, Hugo!" (usando `first_name`)
- **WHEN** o sistema exibe o nome completo
- **THEN** SHALL exibir "Hugo de Paula" (usando `get_full_name()`)

### Requirement: Mandatory role enforcement
Todo usuário SHALL possuir pelo menos um papel ativo entre os papéis transacionais (`is_author`, `is_reviewer`, `is_chair`) OU ser staff/superuser (`is_staff`, `is_superuser`). Esta validação SHALL ser implementada no método `User.clean()` e SHALL impedir a criação de usuários sem função no sistema.

#### Scenario: Admin creates user without any role
- **WHEN** um administrador tenta salvar um usuário sem marcar nenhum papel (is_author, is_reviewer, is_chair) e sem is_staff/is_superuser
- **THEN** o sistema SHALL rejeitar com um erro de validação: "Todo usuário deve ter pelo menos um papel atribuído."

#### Scenario: Registration auto-assigns Author role
- **WHEN** um visitante completa o registro
- **THEN** o usuário SHALL ser criado com `is_author=True`, satisfazendo automaticamente a validação de papel.

#### Scenario: Superuser bypasses role requirement
- **WHEN** `createsuperuser` é executado
- **THEN** `is_superuser=True` e `is_staff=True` satisfazem a validação, sem necessidade de papel transacional.

### Requirement: Role-based filtering capability
O custom user SHALL permitir filtragem eficiente de papéis via flags booleanas para uso futuro em submissões e revisões.

#### Scenario: Filtering for reviewers
- **WHEN** o sistema busca usuários para atribuição de revisão
- **THEN** SHALL ser possível filtrar via `User.objects.filter(is_reviewer=True)`

### Requirement: Wagtail admin user compatibility
O custom user model SHALL ser compatível com Wagtail admin. Superusuários SHALL ter acesso ao Wagtail admin. Campos customizados de perfil e flags de papéis SHALL ser editáveis via interface administrativa.

#### Scenario: Superuser can access Wagtail admin
- **WHEN** um superusuário faz login em `/admin/`
- **THEN** SHALL acessar o painel do Wagtail sem erro e visualizar os campos customizados no perfil do usuário

### Requirement: Dashboard shell for authenticated areas
As telas de área do autor e revisor SHALL herdar de `templates/layouts/dashboard.html`, fornecendo uma interface de navegação focada em tarefas, separada do site institucional. O dashboard SHALL exibir estados vazios (Empty States) amigáveis quando o usuário não possuir submissões ou revisões pendentes.

#### Scenario: Author dashboard layout
- **WHEN** um autor faz login e acessa seu painel
- **THEN** SHALL ser apresentado com o shell de dashboard contendo navegação lateral para suas submissões e um estado vazio se não houver submissões.

#### Scenario: Role-based Dashboard Access
- **WHEN** um usuário com apenas `is_author=True` tenta acessar o dashboard de revisor
- **THEN** o sistema SHALL redirecionar para o dashboard de autor ou exibir uma página de acesso negado (403).

### Requirement: Dynamic sidebar navigation
A navegação lateral do dashboard SHALL exibir links condicionalmente baseados nos papéis do usuário autenticado. Todos os usuários veem "Painel"; seções adicionais aparecem apenas se o usuário tiver o papel correspondente.

#### Scenario: Author sees only relevant links
- **WHEN** um usuário com `is_author=True` (mas não is_reviewer/is_chair) acessa o dashboard
- **THEN** a sidebar SHALL exibir apenas "Painel" e "Submissões". "Revisões" e "Indicadores" SHALL ser ocultos.

#### Scenario: Chair sees all sections
- **WHEN** um usuário com `is_chair=True` acessa o dashboard
- **THEN** a sidebar SHALL exibir todas as seções: "Painel", "Submissões", "Revisões" e "Indicadores".

### Requirement: Mobile-responsive dashboard
O shell do dashboard SHALL ser totalmente responsivo em dispositivos móveis. SHALL incluir um menu hamburger usando Alpine.js para alternar a visibilidade da navegação lateral, seguindo o mesmo padrão estabelecido em `templates/components/header.html` (x-data toggle, x-show, x-transition, escape para fechar).

#### Scenario: Mobile navigation toggle
- **WHEN** um usuário acessa o dashboard em um dispositivo móvel (< lg breakpoint)
- **THEN** a sidebar SHALL estar oculta por padrão e SHALL ser revelada ao tocar no botão hamburger.
- **THEN** o menu SHALL fechar ao pressionar Escape ou ao clicar em um link.

## ADDED Requirements

### Requirement: Participant Registration Flow
The system SHALL provide a public registration flow where users can create an account and automatically gain the 'Author' role (`is_author=True`). Registration SHALL NOT require email verification — users are logged in immediately upon successful registration.

#### Scenario: Successful Registration
- **WHEN** a visitor completes the registration form with valid data and mandatory consents
- **THEN** a new user account is created with `is_author=True`, they are logged in, and redirected to the Author Dashboard.

#### Scenario: Registration form collects first and last name
- **WHEN** the registration form is displayed
- **THEN** it SHALL present separate fields for `first_name` and `last_name` (not a combined full_name field).

### Requirement: Authentication Views
The system SHALL provide standard authentication views including Login, Logout, and Password Reset, styled according to the Design System.

#### Scenario: User Login
- **WHEN** a registered user provides correct credentials
- **THEN** they are redirected to their primary dashboard based on their highest role (Chair > Reviewer > Author).

#### Scenario: Password Reset
- **WHEN** a user requests a password reset
- **THEN** they receive an email with a secure link to set a new password, following Django's built-in password reset flow.

### Requirement: Profile and submission form styling
Componentes de formulário (`accessible_input`, `primary_button`) SHALL ser usados em todas as telas de autenticação e perfil para manter a consistência visual.

#### Scenario: Profile editing form consistency
- **WHEN** um usuário edita seu perfil
- **THEN** os inputs SHALL seguir o padrão visual definido no Design System

#### Scenario: Profile editing uses first_name/last_name
- **WHEN** um usuário edita seu perfil
- **THEN** SHALL editar `first_name` e `last_name` separadamente, não um campo combinado.
