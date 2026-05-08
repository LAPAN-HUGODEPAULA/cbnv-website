# Tasks: Stabilize Platform Foundation

## Version baseline

- [x] Restore direct dependencies required by project settings/templates: django-widget-tweaks, django-axes, django-countries.
- [x] Run Django system checks.
- [x] Verify migrations are clean.
- [x] Run test suite successfully.
- [ ] Define approved baseline as Python 3.14.x, Django 6.0.x, Wagtail 7.4.x LTS, PostgreSQL 18.3, Tailwind CSS 4.x.
- [ ] Update `README.md` to reflect the approved baseline.
- [ ] Update `openspec/project.md` to reflect the approved baseline.
- [ ] Update `docs/CBNV2026_Requisitos_Arquitetura_v1.md` to reflect the approved baseline.
- [ ] Update any implementation plan docs that still mention older versions.

## Python dependencies

- [ ] Update `requires-python` to allow Python 3.14.
- [ ] Pin Django to the latest validated 6.0.x patch.
- [ ] Pin Wagtail to the latest validated 7.4.x LTS patch.
- [ ] Run `uv sync --upgrade`.
- [ ] Commit updated `pyproject.toml` and `uv.lock`.
- [ ] Run `uv run python -m django --version`.
- [ ] Run `uv run python manage.py check`.

## Docker

- [ ] Update Python base image to Python 3.14.x.
- [ ] Update PostgreSQL image to `postgres:18.3` or `postgres:18.3-trixie`.
- [ ] Ensure `DB_HOST=db` is set for the `web` service in `docker-compose.yml`.
- [ ] Add `.dockerignore`.
- [ ] Remove silent `collectstatic` failure or split dev/prod Docker behavior.
- [ ] Run `docker compose build --no-cache`.
- [ ] Run `docker compose up`.

## Accounts

- [ ] Remove custom `accounts.User` model if no real data depends on it.
- [ ] Remove `AUTH_USER_MODEL = "accounts.User"`.
- [ ] Add `accounts.UserProfile` linked to Django default User.
- [ ] Move `institution`, `country`, `position`, role flags, and consent fields to `UserProfile`.
- [ ] Use Django standard `first_name`, `last_name`, and `email` fields.
- [ ] Regenerate initial project-owned migrations.
- [ ] Add admin registration for `UserProfile`.
- [ ] Add tests for default User and UserProfile.

## Routing and settings

- [ ] Add `/admin/` for Wagtail Admin.
- [ ] Add `/django-admin/` for Django Admin.
- [ ] Add Wagtail public routing at `/`.
- [ ] Add Wagtail documents route if documents are enabled.
- [ ] Update settings for Django/Wagtail current-template conventions.
- [ ] Ensure production settings fail if `DJANGO_SECRET_KEY` is missing.
- [ ] Add `CSRF_TRUSTED_ORIGINS` parsing.

## Validation

- [ ] Run `openspec validate stabilize-platform-foundation --strict`.
- [ ] Run `uv run pytest`.
- [ ] Run `uv run python manage.py check`.
- [ ] Run `uv run python manage.py makemigrations --check --dry-run`.
- [ ] Run `docker compose up --build`.