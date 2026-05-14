# Cross-Page Content Consistency Review - Round 1

## Metadata

- Change: `verify-cross-page-content-consistency`
- Branch: `change/verify-cross-page-content-consistency`
- Reviewed commit: `d3044e5`
- Review date: 2026-05-14
- Reviewer: Codex
- Validation mode: source/template/static review.
- Runtime constraint: local PostgreSQL on `localhost:5432` was not reachable, so live browser checks and database-backed profile execution could not be completed in this session.

## Data Profiles

### Empty/default profile

- Source basis: model defaults, fallback content in `pages/content.py`, templates with missing optional links/logos/images, and empty queryset branches.
- Database state: not available locally because PostgreSQL refused connection.
- Purpose: detect stale fallback facts, missing optional-link behavior, empty dashboard states and non-visual fallback labels.

### Populated/custom profile

- Source basis: `seed_canonical_event_content`, public content docs, fixtures, workflow models, notification templates, reports/export views, and proceedings/video tests.
- Canonical facts: CBNV 2026, XII edition, 11 a 13 de novembro de 2026, CAD-1/UFMG, official address, Belo Horizonte, Minas Gerais, Brasil.
- Database state: not available locally because PostgreSQL refused connection.
- Purpose: detect real workflow drift across submissions, reviews, final materials, proceedings, videos, reports and notifications.

## Sources Reviewed

- `core/models.py`, `core/management/commands/seed_canonical_event_content.py`, `core/fixtures/initial_cms_data.json`
- `pages/content.py`, `pages/templates/pages/*.html`, `templates/components/footer.html`
- `templates/dashboard/*.html`, `templates/accounts/*.html`
- `submissions/models.py`, `submissions/views.py`, `templates/submissions/**/*.html`
- `reviews/models.py`, `reviews/views.py`, `templates/reviews/*.html`
- `proceedings/models.py`, `proceedings/views.py`, `templates/proceedings/**/*.html`
- `notifications/services.py`, `templates/notifications/email/*`
- `reports/views.py`, `templates/reports/*.html`
- `videos/models.py`, public video/proceedings test coverage references

## Executive Summary

The current implementation has a strong central source for 2026 event identity and venue facts in `CoreSettings`, and many public templates correctly read those settings. The highest consistency risk is not missing source data; it is duplicated presentation logic around fallback copy, notifications, reports and proceedings publication boundaries.

No P0 issue was confirmed from source review. The round produced nine actionable findings and one terminology-polish finding. The most important issues are old venue fallback copy, public proceedings including internally ready items, raw workflow codes in reports/exports, and hardcoded notification event facts.

## P0/P1 Findings

- `CCR1-001` (P1): About fallback content contains an old Engineering Auditorium venue instead of canonical CAD-1/UFMG data.
- `CCR1-005` (P1): public proceedings pages include `ready_for_proceedings` items while copy presents the page as published works.
- `CCR1-006` (P1): report/indicator surfaces expose raw machine statuses instead of approved status labels or code+label pairs.

## Domain Findings

- Canonical event name, short name, edition, theme and populated venue data are represented in `CoreSettings` and the seed command.
- Public Home/About/Contact generally read event and venue values from settings.
- Fallback About copy still carries old venue and committee framing.
- Submission initial-video messaging is consistent across upload and submission confirmation copy.
- Registration/submission CTAs appear status-gated in source review, but browser confirmation is still needed because the local database was unavailable.

## Persona Status Summary

The author-facing status map is coherent in `AUTHOR_STATUS_LABELS`, especially the collapse of review states into `Em avaliação`. The chair-facing screens need a separate label strategy because they currently reuse author-facing labels in places where operational terms are clearer. Reports and exports need either user-facing labels or explicit code+label output.

See `docs/reviews/persona-status-map-round-1.md`.

## Notification Trigger Summary

Notification timing is mostly tied to workflow transitions, but the templates hardcode event facts and duplicate-send boundaries are not durable. The final-material received notification can be resent on every valid replacement upload.

See `docs/reviews/notification-trigger-consistency-round-1.md`.

## Translation and Terminology Findings

Preferred terms:

| Concept | Preferred Portuguese | English/internal equivalent | Notes |
|---|---|---|---|
| Current event | CBNV 2026 | CBNV 2026 | Use full event name on first mention. |
| Submissions | Submissões | submissions | Avoid mixing `trabalhos` and `submissões` in controls unless context demands it. |
| Reviews | Avaliações | reviews | Reviewer-facing action can be `Avaliar`. |
| Decision | Decisão | decision | Author result can be `Aprovado`/`Rejeitado`; chair action can be `Aceitar`/`Rejeitar`. |
| Final materials | Materiais finais | final materials | Use lowercase in prose; title case only in headings if needed. |
| Proceedings | Anais | proceedings | Prefer `anais` in public/author copy; use `proceedings` only in code/export filenames when technical. |
| Video link | Link do vídeo (YouTube) | YouTube URL | Public gallery item should be `Vídeo` or `Recurso de vídeo`. |

## Non-Visual Content Findings

Image alt text is generally present for logos and committee photos. The footer uses `Logotipo FAPEMIG`, while sponsor cards prefer sponsor logo alt text or sponsor name. Icon-only buttons such as remove-author controls include ARIA labels, but many decorative SVGs and status badges are not covered by automated tests. Add focused checks before launch.

## Legacy Contamination Findings

Previous-edition facts are mostly isolated in previous-edition fallback data, fixtures and prototype docs. The current contamination risk is `pages/content.py` fallback About content, which includes the old Engineering Auditorium venue and 11th-edition committee framing.

See `docs/reviews/legacy-ghost-facts-inventory-round-1.md`.

## Reports/Exports/Privacy Findings

Protected direct file URLs were not observed in reports or exports during source review. Proceedings export includes `video_url`, which is acceptable for chair/admin export but should remain role-protected. Reports and indicator exports need label normalization because raw status codes leak into user-facing CSV/JSON and dashboards.

## Automation Candidates Summary

The highest-value future checks are canonical event fact rendering, legacy fact allowlisting, report/export status labels, proceedings publication boundary and protected-file URL absence.

See `docs/reviews/consistency-automation-candidates-round-1.md`.

## Handoff

Use `docs/reviews/public-site-content-consistency-backlog-round-1.md` as the correction backlog. This change intentionally does not apply broad template/model fixes; it routes follow-up work by category and target proposal.
