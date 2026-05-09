# Proposal: Stabilize Platform Foundation

## Problem

Early implementation drifted across documentation, dependency declarations, Docker configuration, settings, migrations, and authentication assumptions. The project needs one stable technical baseline before CMS pages, program models, submissions, review workflow, proceedings, and reporting continue to expand.

## Proposed Change

Align the repository around the approved foundation:

- Python 3.14.x, Django 6.0.x, Wagtail 7.4.x LTS, PostgreSQL 18.3, Tailwind CSS 4.x, and Node.js 24 LTS when Node is required.
- Django default `auth.User` for authentication.
- `accounts.UserProfile` for institution, country, position, scientific roles, and consent fields.
- Wagtail Admin at `/admin/`, Django Admin at `/django-admin/`, documents at `/documents/`, healthcheck at `/health/`, and Wagtail public pages at `/`.
- Docker Compose using the `db` service hostname for the web container.
- Safe environment examples, untracked local `.env`, and visible Docker build failures.
- Foundation tests for settings, healthcheck, routing, user/profile behavior, and migration consistency.

## Scope

- Update active code, tests, migrations, Docker, and docs needed for this baseline.
- Regenerate project-owned migrations where the pre-production baseline reset requires it.
- Preserve direct dependencies already confirmed as project requirements: `django-widget-tweaks`, `django-axes`, and `django-countries`.
- Keep changes limited to this foundation stabilization.

## Out of Scope

- Public CMS page model expansion.
- Program/speaker feature work.
- Submission/review/proceedings/reporting feature expansion beyond compatibility fixes.
- Final visual design.
- Production deployment hardening beyond the foundation settings required here.

## Decision: direct dependency retention

During dependency cleanup, `django-widget-tweaks`, `django-axes`, and `django-countries` were confirmed as direct project dependencies. They must remain declared in `pyproject.toml` rather than being treated as Wagtail/Django transitives.
