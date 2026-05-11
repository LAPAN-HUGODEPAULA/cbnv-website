# Design: Add Program Speakers and Venue Models

## Context

The current planning sequence places this change after the core CMS content models and canonical event seed. Core settings already centralize broad event facts, while the `program` domain owns program days, sessions, talks and speakers.

The public-site MVP depends on these domain models for Programacao, Palestrantes and local/acesso content. The implementation should therefore provide stable structured data and query behavior, but should not implement the final public pages or final editorial copy.

The seed document defines the canonical venue baseline:

```text
Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha.
R. Prof. Baeta Viana, s/n - Pampulha, Belo Horizonte - MG, 31270-901
https://maps.app.goo.gl/xzqJ2LCAHVP4hsFp6
```

## Goals / Non-Goals

**Goals:**

1. Keep programming data in the `program` domain app.
2. Ensure program days, sessions, talks and speakers are admin-manageable.
3. Preserve explicit status controls for pending, confirmed and hidden speakers or activities.
4. Provide canonical venue/access data for later public pages.
5. Provide deterministic ordering and public query helpers for later page rendering.
6. Add or update tests for visibility, ordering, relationship integrity and seed behavior.

**Non-Goals:**

1. Do not implement the final Programacao or Palestrantes public pages.
2. Do not write final editorial copy for public pages.
3. Do not implement submissions, reviews, payments, certificates, QR code check-in or video hosting.
4. Do not add complex editorial RBAC.
5. Do not integrate with external agenda, maps, registration or streaming APIs.

## Decisions

### Decision 1: Program models remain in `program`

Program days, sessions, talks and speakers should remain in the `program` app, matching the existing domain ownership spec. This keeps scientific schedule behavior separate from generic CMS content.

Alternative considered: put program structures into generic Wagtail page StreamFields. That would make page editing flexible but would weaken relational integrity, status filtering and reuse by Programacao, Palestrantes and consistency checks.

### Decision 2: Use simple status fields and public query helpers

Models should expose clear internal status values and helper/query behavior for public rendering. Public consumers should not duplicate filtering rules in templates.

The key rule is conservative visibility: public program output should include published sessions and confirmed public participants, and omit hidden or pending names unless a deliberate placeholder state is modeled.

Alternative considered: allow templates to inspect raw statuses directly. That increases drift risk across Home, Programacao and Palestrantes.

### Decision 3: Keep venue settings-backed for the MVP

Venue data SHALL remain in `CoreSettings` for the MVP because CBNV 2026 has one official venue. This proposal SHALL NOT create a dedicated `Venue` snippet/model.

The implementation SHALL add explicit structured fields for:
- full venue address;
- optional access instructions.

Existing settings fields remain the canonical source for:
- official venue name;
- short venue name;
- city;
- state;
- country;
- Google Maps URL.

`location` MAY remain as a short display summary, but full-address rendering SHOULD use the dedicated venue address field once added.

A dedicated `Venue` model may be considered later only if the event needs multiple venues, per-room metadata, coordinates, accessibility metadata, or richer map behavior.

### Decision 4: Seed program data with an idempotent command

The preliminary official program should be loadable through `seed_program` or a successor command. The command should be safe to re-run and should avoid creating confirmed speakers or official claims without canonical source data.

Alternative considered: fixtures only. Fixtures are less ergonomic for incremental local/staging updates and do not naturally report skipped/updated records.

### Decision 5: Keep page rendering out of scope

This change prepares model and query contracts. Public pages may add minimal smoke coverage only when necessary to prove data availability, but final page templates and Stitch-aligned rendering belong to `add-public-site-pages-mvp`.



## Risks / Trade-offs

- Risk: Program visibility logic is duplicated across views and templates -> Mitigation: add model managers/query helpers and tests that define public visibility once.
- Risk: Venue data is split between `CoreSettings` and a new venue model -> Mitigation: document the canonical source and add tests or helper methods that make the public source unambiguous.
- Risk: Pending speaker names leak before confirmation -> Mitigation: test that pending/hidden speakers and talks are excluded from public query helpers.
- Risk: Program seed data becomes outdated -> Mitigation: keep the seed idempotent, conservative and clearly documented as preliminary.
- Risk: Over-modeling venue before public pages exist -> Mitigation: implement only fields needed for Programacao, Sobre/local and consistency checks.

## Migration Plan

1. Inspect existing `program` and `core` migrations before adding fields.
2. Add incremental migrations for any new venue fields, venue model fields or program refinements.
3. Preserve existing data where present; avoid destructive renames unless accompanied by data migration.
4. Update or add the program seed command after model changes.
5. Run `uv run python manage.py makemigrations --check --dry-run` after migrations are committed.

Rollback should be a normal Django migration rollback during development. Once real content exists, rollback requires preserving exported program and venue records first.

## Open Questions

1. Should venue live as a dedicated `Venue` snippet or remain in `CoreSettings` for the MVP?
2. What is the canonical source file for the preliminary official program schedule?
3. Should pending activities be omitted entirely from public program queries, or can the admin intentionally publish anonymous placeholders such as "palestrante a confirmar"?
