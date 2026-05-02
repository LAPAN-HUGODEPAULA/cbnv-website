# Contas e Autenticação (accounts-auth)

## Requirements

### Requirement: Custom user model
O sistema SHALL definir `accounts.User` como custom user model via `AUTH_USER_MODEL = "accounts.User"`. O model SHALL herdar de `AbstractUser` e conter campos:
- `full_name` (CharField, Nome completo)
- `institution` (CharField, Instituição)
- `country` (CharField, País com choices ISO)
- `position` (CharField, Vínculo/Cargo)
- `is_author` (BooleanField, Default=False)
- `is_reviewer` (BooleanField, Default=False)
- `is_chair` (BooleanField, Default=False)
- `consent_privacy` (BooleanField, Default=False)
- `consent_image` (BooleanField, Default=False)

#### Scenario: User creation with profile fields
- **GIVEN** que o sistema está configurado com `accounts.User`
- **WHEN** um usuário é criado via formulário ou `createsuperuser`
- **THEN** SHALL ser possível preencher `full_name`, `institution`, `country` e `position`

#### Scenario: User with multiple scientific roles
- **GIVEN** um usuário existente no sistema
- **WHEN** o admin marca simultaneamente `is_author=True` e `is_reviewer=True`
- **THEN** o usuário SHALL possuir ambos os papéis sem necessidade de contas separadas

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
