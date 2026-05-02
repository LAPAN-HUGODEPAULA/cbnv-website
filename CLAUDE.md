# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Website and digital platform for **XII Congresso Brasileiro de Neurociências da Visão (CBNV 2026)** — "Neurovisão na Era da Inteligência Artificial", November 11–13, 2026, CAD-1 UFMG, Belo Horizonte, MG. It serves as both public website and administrative infrastructure for the congress (submissions, reviews, proceedings, indicators).

**Language:** Portuguese Brazilian (institutional/scientific tone).

## Single Source of Truth

- **Requirements & Architecture:** `docs/CBNV2026_Requisitos_Arquitetura_v1.md` — read this before any design or development task. It prevails over all other sources.
- **Design reference:** `docs/CBNV2026_DESIGN.md` and `docs/stitch_cbnv_2026_digital_platform/` (visual reference only, NOT functional spec).
- **Implementation plan:** `docs/CBNV2026_OpenSpec_Plano_Implementacao_v1.md` — sequential change proposals via OpenSpec.

**Do NOT** use the legacy Wix site (`_legacy/`) or Notion as scope/design reference.

## Tech Stack

Django + Wagtail CMS + PostgreSQL + Tailwind CSS + HTMX + Alpine.js (optional) + Docker Compose.

No Next.js, no Strapi, no full SPA, no React required.

## Development Commands

```bash
docker compose up                    # Start app + PostgreSQL + dependencies
uv sync                              # Sync Python dependencies
uv add <package>                     # Add a new Python package
uv add --group dev <package>         # Add a dev dependency
uv run python manage.py migrate      # Run migrations
uv run python manage.py createsuperuser  # Create admin user
uv run python manage.py runserver    # Dev server (outside Docker)
uv run python manage.py collectstatic    # Collect static files
uv run pytest                        # Run tests
npm run build                        # Build CSS
npm run watch                        # Watch CSS
```

## OpenSpec Workflow

Implementation follows sequential change proposals. Only one active proposal at a time (except minor independent fixes).

```bash
openspec list
openspec validate <change-id> --strict
openspec archive <change-id> --yes
```

Do not implement code before a proposal is validated and approved. Mark tasks in `tasks.md` as completed after implementation.

### Change Proposal Sequence

01. `bootstrap-django-wagtail-platform` — Django/Wagtail base, custom user, Docker
02. `add-design-system-and-layout-shells` — Tailwind tokens, reusable components
03. `add-core-cms-content-models` — Wagtail editorial models, SiteSettings
04. `add-program-speakers-and-fixtures` — Program, speakers, fixtures
05. `add-public-site-pages` — Public MVP pages
06. `add-accounts-roles-and-dashboards` — Auth, roles, dashboard shells
07. `add-author-submission-initial-flow` — Phase 1 submissions (no video)
08. `add-review-decision-workflow` — Peer review, decisions
09. `add-final-materials-proceedings-videos` — Final materials, proceedings
10. `add-reports-exports-and-indicators` — Metrics and exports
11. `harden-deployment-security-and-backups` — Production hardening
12. `complete-accessibility-performance-and-qa` — QA, a11y, performance

## Architecture

Modular Django monolith with apps per domain:

| App | Purpose |
|---|---|
| `core` | Global settings, utilities |
| `pages` | Wagtail page types |
| `program` | ProgramDay, ProgramSession, ProgramTalk, Speaker |
| `submissions` | Submissions, authors, files |
| `reviews` | ReviewAssignment, Review, Decision |
| `proceedings` | Final materials, proceedings, publications |
| `videos` | VideoResource (YouTube links only — never host video) |
| `sponsors` | Sponsor management |
| `accounts` | Custom user, auth, transactional roles |
| `reports` | Exports, indicators |
| `notifications` | Email templates, transactional emails |

### Submission State Machine

States: draft → submitted → admin_screening → assigned_to_reviewers → under_review → reviews_completed → decision_pending → accepted_oral/accepted_poster/accepted_video/rejected → final_materials_pending → ready_for_proceedings → published_in_proceedings.

Use simple labels for authors (e.g., "em avaliação", "aprovado", "rejeitado") — don't expose internal state names.

### Roles

- **Editorial:** single admin CMS user (no complex RBAC)
- **Transactional:** Author, Reviewer, Chair/Scientific Committee, Admin/Organizer

## Hard Boundaries

These are explicitly out of scope. Do not implement:

- Payment processing
- Certificate generation
- QR code check-in
- Native mobile app
- Full video hosting (YouTube/playlist links only)
- Complex editorial RBAC
- Next.js / Strapi
- Automatic integration with Sympla/UFMG/FUNDEP (link only)

Submission files must NEVER be publicly accessible by direct URL.

## Design System

Dark-mode first. Color tokens:

```
--cbnv-navy-950: #081426    --cbnv-blue-600: #214BFF
--cbnv-green-400: #2FEA8B   --cbnv-text-light: #E7ECF7
--cbnv-text-muted: #9AA8C7  --cbnv-text-dark: #111827
```

Target: WCAG 2.2 AA. Keyboard accessible, visible focus, semantic headings, high contrast, respect `prefers-reduced-motion`.

## Coding Guidelines

- Use **uv** for all Python dependency management. Never use `pip` or `pip install`.
- Django idiomatic patterns, incremental migrations
- Custom user model must be created before any domain models (Proposal 01)
- Templates server-side, readable, no heavy SPA patterns
- HTMX only where there's clear benefit over full page loads
- Tailwind utility classes, reusable components (cards, badges, timeline, tables, forms)
- Write tests for critical flows (submission, upload, review, decision, export)
- Keep components and templates modular — design system before pages
