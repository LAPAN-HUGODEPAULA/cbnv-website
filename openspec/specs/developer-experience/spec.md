# Experiência do Desenvolvedor (developer-experience)

## Purpose
Fornecer ferramentas, pipelines de build e documentação para otimizar o fluxo de desenvolvimento e testes.

## Requirements

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

### Requirement: pytest configuration
O projeto SHALL usar pytest como framework de testes. SHALL existir `pytest.ini` ou `pyproject.toml` com configuração `DJANGO_SETTINGS_MODULE = cbnv.settings.test` e `django_db` habilitado. SHALL existir arquivo `conftest.py` global com fixtures para `db` e `client`.

#### Scenario: Tests run with pytest
- **WHEN** `pytest` é executado no diretório raiz do projeto
- **THEN** SHALL descobrir e executar testes sem erros de configuração

#### Scenario: Database fixture available
- **WHEN** um teste usa a fixture `db` do pytest-django
- **THEN** SHALL ter acesso a um banco de dados de teste limpo

### Requirement: Base templates
O projeto SHALL fornecer templates base mínimos: `base.html` (layout HTML5 com `<head>`, `<body>`, blocos `{% block title %}`, `{% block content %}`, `{% block scripts %}`) e `base_admin.html` (herda de `base.html` com navegação admin). Os templates SHALL carregar Tailwind CSS.

#### Scenario: Base template renders
- **WHEN** uma view renderiza usando `base.html`
- **THEN** SHALL produzir HTML válido com Tailwind CSS carregado e blocos substituíveis

### Requirement: Healthcheck endpoint
O sistema SHALL fornecer endpoint `/health/` que retorne HTTP 200 com JSON `{"status": "ok"}` quando o banco de dados está acessível. SHALL retornar HTTP 503 quando o banco está indisponível.

#### Scenario: Healthcheck with database available
- **WHEN** `GET /health/` é chamado e PostgreSQL está acessível
- **THEN** SHALL retornar HTTP 200 com `{"status": "ok"}`

#### Scenario: Healthcheck with database unavailable
- **WHEN** `GET /health/` é chamado e PostgreSQL não está acessível
- **THEN** SHALL retornar HTTP 503

### Requirement: Environment variables documentation
O projeto SHALL fornecer `.env.example` com todas as variáveis de ambiente necessárias documentadas. SHALL fornecer `README.md` com instruções de setup, desenvolvimento e testes. O `.env.example` SHALL ser organizado em seções: Geral, Banco de Dados, SMTP/Email, SSL/TLS, Rate Limiting, Backups. Cada variável SHALL ter comentário com descrição, valor de exemplo e indicação se é obrigatória ou opcional.

#### Scenario: Developer can set up environment
- **WHEN** um desenvolvedor copia `.env.example` para `.env` e preenche os valores
- **THEN** SHALL poder iniciar o projeto com `docker compose up` ou `python manage.py runserver`

#### Scenario: Variable categories are clear
- **WHEN** um desenvolvedor abre `.env.example`
- **THEN** SHALL encontrar variáveis agrupadas por categoria com comentários explicativos

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

### Requirement: Automated Accessibility Auditing
The project SHALL integrate `axe-core` or a similar tool for automated accessibility auditing in the CI/CD pipeline or local test suite.

#### Scenario: Running accessibility tests
- **WHEN** the test suite is executed
- **THEN** it SHALL include automated checks for ARIA compliance, contrast, and labels

### Requirement: Performance Budgeting
The project SHALL define and enforce a performance budget for the public site, targeting a Lighthouse Performance score of 90+ and LCP under 2.5s.

#### Scenario: Performance audit passes
- **WHEN** a production build is audited with Lighthouse
- **THEN** it SHALL meet the performance budget criteria for Largest Contentful Paint (LCP) and Total Blocking Time (TBT)

### Requirement: E2E QA Coverage for User Journeys
The project SHALL include End-to-End (E2E) tests covering the primary journeys for all user roles (Visitor, Author, Reviewer, Chair).

#### Scenario: Visitor journey E2E
- **WHEN** the visitor E2E test runs
- **THEN** it SHALL verify navigation from Home to Program to Submissions rules without errors

#### Scenario: Author journey E2E
- **WHEN** the author E2E test runs
- **THEN** it SHALL verify login, submission creation, and dashboard status updates

### Requirement: Production environment variables documentation
O `.env.example` SHALL documentar todas as variáveis de ambiente necessárias para produção, incluindo: `SMTP_HOST`, `SMTP_PORT`, `SMTP_USE_TLS`, `SMTP_USER`, `SMTP_PASSWORD`, `DEFAULT_FROM_EMAIL`, `SSL_CERT_PATH`, `SSL_KEY_PATH`, `GUNICORN_WORKERS`, `AXES_FAILURE_LIMIT`, `AXES_COOLOFF_TIME`, `AXES_LOCKOUT_PARAMETERS`, `NGINX_RATE_LIMIT`, `NGINX_BURST`, `BACKUP_RETENTION_DAYS`.

#### Scenario: Developer configures production environment
- **WHEN** um desenvolvedor copia `.env.example` para `.env` e preenche os valores de produção
- **THEN** SHALL ter todas as variáveis necessárias documentadas com valores de exemplo seguros

### Requirement: Restore playbook
O documento `docs/implementation/SETUP_DEPLOY.md` SHALL incluir seção de restore com passos para: (1) identificar o backup mais recente, (2) executar `scripts/restore.sh`, (3) verificar integridade dos dados restaurados, (4) checklist de validação pós-restore.

#### Scenario: Operator restores from backup
- **WHEN** um operador segue o playbook de restore em `SETUP_DEPLOY.md`
- **THEN** SHALL conseguir restaurar o banco e verificar integridade usando apenas os comandos documentados

### Requirement: Health check for all services
O `docker-compose.yml` SHALL incluir `healthcheck` para todos os serviços (`db`, `web`, `nginx`). O health check do `web` SHALL usar `curl` para `/health/`. O health check do `nginx` SHALL verificar que a porta 443 está respondendo.

#### Scenario: Nginx health check passes
- **WHEN** o serviço `nginx` está ativo e respondendo HTTPS
- **THEN** o healthcheck SHALL retornar sucesso

#### Scenario: Unhealthy service stops dependents
- **WHEN** o serviço `web` falha o healthcheck
- **THEN** o Docker SHALL marcar o serviço como unhealthy e dependências SHALL parar de enviar tráfego
