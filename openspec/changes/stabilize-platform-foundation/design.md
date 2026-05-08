# Design: Stabilize Platform Foundation

## Version baseline

The project shall standardize around:

- Python 3.14
- Django 6.x, fixed to the latest validated patch in the lockfile
- Wagtail 7.3.x, fixed to the latest validated patch in the lockfile
- PostgreSQL 18.3
- Tailwind CSS 4.x
- Node.js: 24 LTS, if necessary to align with Wagtail/Tailwind

The exact patch versions must be declared consistently in:

- `pyproject.toml`
- `uv.lock`
- `README.md`
- `openspec/project.md`
- architecture docs
- Docker configuration

## Authentication strategy

Use Django's default `User` model.

Do not set `AUTH_USER_MODEL = "accounts.User"`.

Congress-specific fields belong to `accounts.UserProfile`:

- institution
- country
- position
- is_author
- is_reviewer
- is_chair
- consent_privacy
- consent_image

Rationale:

- avoids custom UserManager/forms early in the project;
- improves compatibility with Django Admin and Wagtail;
- reduces implementation burden for AI-assisted coding;
- preserves enough flexibility for scientific roles.

## Public login UX

The internal authentication model may use Django's standard username field.

Public-facing forms may label the username field as “E-mail” and store the e-mail in both `username` and `email`, if the implementation chooses email-like login without custom User.

This behavior must be documented if adopted.

## Routing

Use:

- `/admin/` for Wagtail Admin
- `/django-admin/` for Django Admin
- `/documents/` for Wagtail documents
- `/health/` for healthcheck
- `/` for Wagtail public pages

## Docker

Docker Compose must set `DB_HOST=db` for the web container.

`.env.example` must remain safe and must not contain secrets.

The `.env` file must remain untracked.

## Migrations

Because this is a pre-production baseline reset, project-owned migrations may be regenerated.

Do not delete Django/Wagtail third-party migrations.

## Tests

Add tests for:

- healthcheck;
- URL routing;
- default User model;
- UserProfile creation/access;
- settings import;
- production settings requiring safe configuration where applicable.