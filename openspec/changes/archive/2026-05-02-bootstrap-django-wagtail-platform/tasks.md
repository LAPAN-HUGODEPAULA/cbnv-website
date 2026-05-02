## 1. Projeto Django e Wagtail

- [x] 1.1 Criar projeto Django com `django-admin startproject cbnv .` (nota final com `.` para não aninhar)
- [x] 1.2 Instalar Wagtail e dependências (`wagtail`, `wagtail[telephone]` se necessário)
- [x] 1.3 Adaptar `INSTALLED_APPS` em settings para incluir `wagtail`, `wagtail.admin`, `wagtail.documents`, `wagtail.images`, `wagtail.sites`, `modelcluster`, `taggit`, `wagtail.contrib.settings`
- [x] 1.4 Configurar `ROOT_URLCONF` com `path('admin/', admin.site.urls)` e `include('wagtail.admin.urls')`
- [x] 1.5 Verificar que `python manage.py migrate` executa sem erro

## 2. Custom User Model

- [x] 2.1 Criar app `accounts` com `python manage.py startapp accounts`
- [x] 2.2 Definir `accounts/models.py` com `User(AbstractUser)` com campos: `full_name`, `institution`, `country`, `position`, `is_author`, `is_reviewer`, `is_chair`, `consent_privacy`, `consent_image`
- [x] 2.3 Configurar `AUTH_USER_MODEL = "accounts.User"` em settings base
- [x] 2.4 Registrar `User` em `accounts/admin.py` com `UserAdmin`
- [x] 2.5 Verificar compatibilidade com Wagtail admin (login de superusuário)
- [x] 2.6 Gerar migration inicial: `python manage.py makemigrations accounts`

## 3. Apps de Domínio

- [x] 3.1 Criar apps: `core`, `pages`, `program`, `submissions`, `reviews`, `proceedings`, `videos`, `sponsors`, `reports`, `notifications` via `startapp`
- [x] 3.2 Registrar todos os apps em `INSTALLED_APPS`
- [x] 3.3 Verificar `python manage.py check` passa sem erros

## 4. Settings Split

- [x] 4.1 Converter `cbnv/settings.py` em pacote `cbnv/settings/` com `__init__.py`
- [x] 4.2 Criar `cbnv/settings/base.py` com toda configuração comum (INSTALLED_APPS, middleware, auth, wagtail, static files, i18n)
- [x] 4.3 Criar `cbnv/settings/development.py` herdando de base, com `DEBUG=True`, `ALLOWED_HOSTS=["*"]`, ferramentas de debug
- [x] 4.4 Criar `cbnv/settings/test.py` herdando de base, com SQLite in-memory, `DEBUG=False`, `PASSWORD_HASHERS` simplificados
- [x] 4.5 Criar `cbnv/settings/production.py` herdando de base, com `DEBUG=False`, security headers, `SECURE_SSL_REDIRECT`, `ALLOWED_HOSTS` via env
- [x] 4.6 Remover `cbnv/settings.py` original e garantir que `manage.py` aponta para `cbnv.settings.development` como padrão

## 5. Docker Compose

- [x] 5.1 Criar `Dockerfile` baseado em Python 3.12 slim com dependências do projeto
- [x] 5.2 Criar `docker-compose.yml` com serviços `web` (Django) e `db` (PostgreSQL 16)
- [x] 5.3 Configurar healthcheck no serviço `db` (`pg_isready`)
- [x] 5.4 Configurar `depends_on` com `condition: service_healthy` no serviço `web`
- [x] 5.5 Configurar volumes para código e media files
- [x] 5.6 Criar `.env` e `.env.example` com `DJANGO_SECRET_KEY`, `DATABASE_URL`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`
- [x] 5.7 Verificar `docker compose up` inicia sem erro

## 6. Tailwind CSS

- [x] 6.1 Inicializar npm: `npm init -y`
- [x] 6.2 Instalar Tailwind CSS: `npm install -D tailwindcss @tailwindcss/cli`
- [x] 6.3 Criar `tailwind.config.js` com content paths apontando para `**/*.html`
- [x] 6.4 Criar `src/input.css` com `@tailwind base; @tailwind components; @tailwind utilities;`
- [x] 6.5 Adicionar npm scripts: `build` (compila minificado) e `watch` (watch mode)
- [x] 6.6 Configurar `STATICFILES_DIRS` para incluir diretório de CSS compilado
- [x] 6.7 Verificar `npx tailwindcss --input src/input.css --output static/css/output.css --minify` gera CSS

## 7. Templates Base

- [x] 7.1 Criar diretório `templates/` na raiz com `base.html` (HTML5, head, body, blocos title/content/scripts, Tailwind CSS link)
- [x] 7.2 Criar `templates/base.html` com meta charset, viewport, carregamento do CSS Tailwind compilado
- [x] 7.3 Verificar que templates renderizam HTML válido

## 8. Healthcheck

- [x] 8.1 Criar view `core/views.py` com endpoint `/health/` que verifica conexão com banco
- [x] 8.2 Registrar URL no `cbnv/urls.py`
- [x] 8.3 Retornar HTTP 200 `{"status": "ok"}` quando DB acessível, HTTP 503 quando não

## 9. pytest

- [x] 9.1 Criar `pytest.ini` ou seção em `pyproject.toml` com `DJANGO_SETTINGS_MODULE = cbnv.settings.test` e `addopts = --ds=cbnv.settings.test`
- [x] 9.2 Criar `conftest.py` na raiz com fixtures básicas (`db`, `client`)
- [x] 9.3 Criar `accounts/tests/test_models.py` com teste de criação de User
- [x] 9.4 Criar `core/tests/test_healthcheck.py` com teste do endpoint `/health/`
- [x] 9.5 Verificar `pytest` executa e todos os testes passam

## 10. Documentação

- [x] 10.1 Criar `.gitignore` com padrões Django/Python (`.env`, `__pycache__`, `*.pyc`, `db.sqlite3`, `node_modules/`, `.venv/`, `static/`, `media/`, `.DS_Store`)
- [x] 10.2 Criar `README.md` com: descrição do projeto, pré-requisitos, setup local, Docker, Tailwind, testes, estrutura de apps
- [x] 10.3 Criar `requirements.txt` (ou `requirements/base.txt`) com Django, Wagtail, psycopg2-binary, pytest, pytest-django

## 11. Validação

- [x] 11.1 Executar `docker compose up` e verificar que `/health/` retorna 200
- [x] 11.2 Executar `python manage.py migrate` sem erro
- [x] 11.3 Acessar `/admin/` e fazer login como superusuário
- [x] 11.4 Executar `pytest` e verificar que todos os testes passam
- [x] 11.5 Executar `openspec validate bootstrap-django-wagtail-platform --strict` e verificar aprovação
