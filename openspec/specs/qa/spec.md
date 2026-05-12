# Review QA (qa)

## Purpose
Define quality gates for diagnostic review changes, including scope control, finding routing and severity classification.
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
- **THEN** `openspec validate add-accounts-profiles-and-dashboards --strict`, `uv run python manage.py check`, `uv run python manage.py makemigrations --check --dry-run` e `uv run pytest` SHALL passar.


