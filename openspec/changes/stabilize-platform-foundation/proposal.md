# Proposal: Stabilize Platform Foundation

## Intent

Stabilize the technical foundation of the CBNV 2026 platform before implementing CMS pages, program models, submissions, review workflow, proceedings, and reporting.

This change resolves foundation drift introduced during early implementation by aligning documentation, specs, code, Docker, settings, and dependency declarations around the approved current baseline.

## Background

The project must use current versions of Django, Wagtail, PostgreSQL, Python, and Tailwind CSS. During implementation, some files diverged: documentation, Docker configuration, generated migrations, settings, and user model assumptions no longer describe the same baseline.

The project should also avoid unnecessary custom authentication engineering. The platform should use Django's default User model and extend congress-specific metadata via a profile model.

## Scope

In scope:

- Align README, OpenSpec, architecture docs, Docker, dependency files, and settings around the approved current version baseline.
- Use Django default User model for authentication.
- Add a UserProfile model for congress-specific metadata and scientific roles.
- Remove the custom accounts.User model if no real production data exists.
- Regenerate initial migrations for project-owned apps.
- Mount Wagtail public URLs.
- Separate Wagtail Admin and Django Admin routes.
- Make Docker Compose work without manual DB host correction.
- Keep `.env` local-only and `.env.example` safe.
- Remove silent Docker build failures.
- Add foundation tests.

Out of scope:

- Public CMS page models.
- Program/speaker models.
- Submission workflow.
- Review workflow.
- Proceedings.
- Reports.
- Final visual design.
- Production deployment hardening beyond foundation settings.

## Approach

Treat this change as a baseline reset. Since there is no real production data, migrations for project-owned apps may be regenerated.

Prefer Django defaults where they reduce custom code and operational risk. Keep the platform modular but avoid premature abstractions.

## Impact

This change may delete and regenerate early migrations. It should be completed before any user, submission, program, or CMS content data becomes authoritative.

## Decision: direct dependency retention

During dependency cleanup, `django-widget-tweaks`, `django-axes`, and `django-countries` were confirmed as direct project dependencies. They must remain declared in `pyproject.toml` rather than being treated as Wagtail/Django transitives.
