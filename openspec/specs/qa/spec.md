# Review QA (qa)

## Purpose
Define quality gates for the platform, including authentication, authorization, and scientific workflows.
## Requirements
### Requirement: Testes de conta e dashboard
A base de conta/perfil/dashboard SHALL incluir testes para o comportamento central de autenticação e autorização.

#### Scenario: Teste de registro existe
- **GIVEN** que a suíte de testes executa
- **THEN** ela SHALL verificar que o registro cria um usuário e perfil.

#### Scenario: Teste de autenticação do dashboard existe
- **GIVEN** que a suíte de testes executa
- **THEN** ela SHALL verificar que o acesso ao dashboard não autenticado redireciona para o login.

#### Scenario: Testes de acesso por papel existem
- **GIVEN** que a suíte de testes executa
- **THEN** ela SHALL verificar o acesso ao dashboard específico de papel para os papéis de autor, revisor e chair.

### Requirement: Comandos de validação
A mudança SHALL passar pelos comandos de validação do projeto.

#### Scenario: Validação está completa
- **GIVEN** que a implementação está completa
- **WHEN** a validação é executada
- **THEN** `openspec validate <change-id> --strict`, `uv run python manage.py check`, `uv run python manage.py makemigrations --check --dry-run` e `uv run pytest` SHALL passar.

### Requirement: Account and dashboard tests

The account/profile/dashboard foundation SHALL include tests for core authentication and authorization behavior.

#### Scenario: Registration test exists

Given the test suite runs
Then it SHALL verify that registration creates a user and profile.

#### Scenario: Dashboard auth test exists

Given the test suite runs
Then it SHALL verify that unauthenticated dashboard access redirects to login.

#### Scenario: Role access tests exist

Given the test suite runs
Then it SHALL verify role-specific dashboard access for author, reviewer and chair roles.

### Requirement: Review workflow tests

The initial submission flow SHALL include tests for core workflow behavior.

#### Scenario: Valid submission test

Given the test suite runs  
Then it SHALL verify an authenticated author can create a valid initial submission with PDF.

#### Scenario: Video not required test

Given the test suite runs  
Then it SHALL verify initial submission succeeds without video.

#### Scenario: File validation tests

Given the test suite runs  
Then it SHALL verify non-PDF and oversized files are rejected.

#### Scenario: Permission tests

Given the test suite runs  
Then it SHALL verify users cannot view or download another user's submissions/files.

### Requirement: Review workflow testing

The platform SHALL include automated tests for the full review and decision cycle.

#### Scenario: Review cycle test
- **WHEN** the test suite runs
- **THEN** it SHALL verify that a chair can assign a reviewer, the reviewer can submit an evaluation, and the chair can issue a final decision.

#### Scenario: Review permission test
- **WHEN** the test suite runs
- **THEN** it SHALL verify that unauthorized users cannot perform review or decision actions.

### Requirement: Validation commands


The change SHALL pass project validation commands.

#### Scenario: Validation is complete

Given the implementation is complete  
When validation is run  
Then `openspec validate add-author-submission-initial-flow --strict`, `uv run python manage.py check`, `uv run python manage.py makemigrations --check --dry-run`, and `uv run pytest` SHALL pass.

