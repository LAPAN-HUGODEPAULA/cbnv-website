## ADDED Requirements

### Requirement: Environment-based settings
Os settings SHALL ser divididos em `settings/base.py` (configuração comum), `settings/development.py` (DEBUG=True, ferramentas de dev), `settings/test.py` (banco em memória, settings mínimos), `settings/production.py` (DEBUG=False, segurança restritiva). Cada ambiente SHALL poder sobrescrever variáveis do base.

#### Scenario: Development settings activate
- **WHEN** `DJANGO_SETTINGS_MODULE=cbnv.settings.development` está definido
- **THEN** `DEBUG` SHALL ser `True` e `ALLOWED_HOSTS` SHALL incluir `localhost` e `127.0.0.1`

#### Scenario: Test settings use in-memory database
- **WHEN** `DJANGO_SETTINGS_MODULE=cbnv.settings.test` está definido e pytest executa
- **THEN** SHALL usar SQLite em memória (`:memory:`) sem necessidade de PostgreSQL

### Requirement: Security headers
Os settings de produção SHALL configurar `SECURE_SSL_REDIRECT=True`, `SESSION_COOKIE_SECURE=True`, `CSRF_COOKIE_SECURE=True`, `SECURE_HSTS_SECONDS`, `SECURE_BROWSER_XSS_FILTER=True`, `SECURE_CONTENT_TYPE_NOSNIFF=True`, `X_FRAME_OPTIONS='DENY'`. Headers SHALL ser aplicados via `SecurityMiddleware`.

#### Scenario: Security headers present in production
- **WHEN** uma requisição HTTP é feita ao servidor em produção
- **THEN** SHALL incluir headers `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`

### Requirement: Sensitive data via environment
`SECRET_KEY`, `DATABASE_URL`, credenciais de email e outras variáveis sensíveis SHALL ser lidas de variáveis de ambiente. Nenhum segredo SHALL estar hardcoded no código-fonte. O `.env` SHALL estar listado em `.gitignore`.

#### Scenario: Secrets loaded from environment
- **WHEN** o servidor inicia com `SECRET_KEY` definido como variável de ambiente
- **THEN** SHALL usar esse valor sem fallback para string hardcoded

#### Scenario: .env not in git
- **WHEN** `git status` é verificado
- **THEN** `.env` SHALL aparecer em `.gitignore` e não SHALL ser rastreado

### Requirement: Docker secrets support
O `docker-compose.yml` SHALL suportar passagem de variáveis sensíveis via `env_file` ou Docker secrets. O `docker-compose.yml` SHALL referenciar `.env` file para desenvolvimento.

#### Scenario: Docker Compose loads environment
- **WHEN** `docker compose up` é executado com `.env` presente
- **THEN** SHALL carregar variáveis de ambiente para os serviços `web` e `db`
