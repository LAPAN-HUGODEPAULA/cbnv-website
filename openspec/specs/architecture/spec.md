# Arquitetura (architecture)

## Requirements

### Requirement: Django project structure
O sistema SHALL ser um projeto Django 5.x com módulo de settings dividido em `settings/base.py`, `settings/development.py`, `settings/test.py` e `settings/production.py`. O `manage.py` SHALL usar `DJANGO_SETTINGS_MODULE` para selecionar o ambiente.

#### Scenario: Project created with correct structure
- **WHEN** um desenvolvedor clona o repositório e inspeciona a estrutura
- **THEN** SHALL existir `cbnv/settings/` com `__init__.py`, `base.py`, `development.py`, `test.py`, `production.py` e `cbnv/wsgi.py`, `cbnv/asgi.py`, `cbnv/urls.py`

### Requirement: Wagtail integration
O projeto SHALL integrar Wagtail CMS com rota de admin em `/admin/`. O `INSTALLED_APPS` SHALL incluir `wagtail` e dependências necessárias. O `ROOT_URLCONF` SHALL incluir `wagtail.admin.urls` via `include`.

#### Scenario: Wagtail admin accessible
- **WHEN** o servidor está rodando e um usuário acessa `/admin/`
- **THEN** SHALL ser exibida a tela de login do Wagtail

### Requirement: Modular Django apps
O projeto SHALL conter apps Django vazios (sem models além do custom user) para cada domínio: `core`, `pages`, `program`, `submissions`, `reviews`, `proceedings`, `videos`, `sponsors`, `accounts`, `reports`, `notifications`. Cada app SHALL ter `apps.py`, `__init__.py` e estar registrado em `INSTALLED_APPS`.

#### Scenario: All domain apps registered
- **WHEN** `python manage.py check` é executado
- **THEN** SHALL reportar que todos os apps estão registrados sem erros

### Requirement: PostgreSQL database
O sistema SHALL usar PostgreSQL como banco de dados. A conexão SHALL ser configurada via variável de ambiente `DATABASE_URL` com fallback para credenciais individuais.

#### Scenario: PostgreSQL connection works
- **WHEN** `python manage.py migrate` é executado com PostgreSQL disponível
- **THEN** SHALL criar todas as tabelas sem erro

### Requirement: Docker Compose environment
O projeto SHALL fornecer `docker-compose.yml` (e `docker-compose.override.yml` opcional para desenvolvimento) com serviços `web` e `db`. O serviço `db` SHALL usar imagem oficial PostgreSQL com healthcheck. O serviço `web` SHALL expor a porta 8000 e depender de `db`.

#### Scenario: Docker Compose starts all services
- **WHEN** `docker compose up` é executado
- **THEN** SHALL iniciar os serviços `web` e `db` e a aplicação responder em `http://localhost:8000`

### Requirement: Custom user model before domain models
O sistema SHALL definir um custom user model `cbnv.User` (ou `accounts.User`) em `AUTH_USER_MODEL` ANTES de criar qualquer migration de domínio. O model SHALL herdar de `AbstractUser` e ser definido no app `accounts`.

#### Scenario: Custom user is the auth model
- **WHEN** `python manage.py makemigrations` é executado após criação do model
- **THEN** SHALL gerar migration de User sem conflito with `auth.User`

#### Scenario: No domain migrations depend on auth.User
- **WHEN** migrations de domínio são criadas posteriormente
- **THEN** SHALL referenciar `settings.AUTH_USER_MODEL` (string) em ForeignKey, não `auth.User`
