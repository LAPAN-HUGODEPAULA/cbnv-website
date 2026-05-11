# Proposal: Seed Canonical Event Content

## Change ID

`seed-canonical-event-content`

## Linked issue

GitHub issue: `OpenSpec: seed canonical event content`  
Expected issue number: `#4`

## Problem

The core CMS models provide editable structures for global settings, news/announcements and supporting entities, but the site still needs a canonical initial content dataset. Without a controlled seed, developers and agents may hardcode event facts into templates or create inconsistent placeholder data across Home, About, footer, venue sections and future public pages.

This proposal creates the canonical initial content layer for CBNV 2026 so later public-page proposals can consume consistent data from the CMS instead of duplicating facts manually.

## Proposed Change

Add an idempotent seeding mechanism that populates the CMS with the minimum canonical CBNV 2026 event content required by the public site foundation.

The seed should populate global event settings, venue/address/link information, institutional/support entities, social/media links, institutional acknowledgement fields and initial placeholder states for unavailable external links.

## Goals

1. Provide a single canonical source for event identity and core event facts.
2. Seed global settings required by Home, About, footer, registration, contact and future pages.
3. Seed the official venue name, address and Google Maps URL.
4. Seed known institutional/support entities.
5. Seed FAPEMIG acknowledgement fields and/or logo slot if the CMS model supports it.
6. Seed external links in a safe “coming soon” state when unknown.
7. Make the seed idempotent and safe to run multiple times.
8. Avoid hardcoded factual content in templates.

## Non-goals

This change SHALL NOT:

1. implement public pages;
2. implement final Home/About copy;
3. implement program/speaker/venue domain models beyond global setting fields already available;
4. seed the detailed scientific program;
5. seed speaker biographies;
6. implement submission, review, proceedings or reports;
7. create production secrets;
8. connect to external APIs;
9. scrape or re-import Wix/Notion content.

## Canonical Content

### Event identity

- Formal name: `XII Congresso Brasileiro de Neurociências da Visão`
- Short name: `CBNV 2026`
- Theme: `Neurovisão na Era da Inteligência Artificial`
- Format: `Presencial com transmissão híbrida`
- Dates: `11 a 13 de novembro de 2026`
- Start date: `2026-11-11`
- End date: `2026-11-13`
- City: `Belo Horizonte`
- State: `Minas Gerais`
- Country: `Brasil`

### Venue

- Venue name: `Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha`
- Venue short name: `CAD-1/UFMG`
- Address:

```text
Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha.
R. Prof. Baeta Viana, s/n - Pampulha, Belo Horizonte - MG, 31270-901
```

- Google Maps URL:

```text
https://maps.app.goo.gl/xzqJ2LCAHVP4hsFp6
```

### Institutional/support entities

Seed known entities as supporting entities, using conservative categories and visibility defaults:

- UFMG
- FUNDEP
- FAPEMIG
- Sociedade Brasileira de Neurovisão
- Hospital de Olhos de Minas Gerais / HOLHOS
- UFRJ
- USP
- UFRN
- UEMG

Categories may be adjusted to the model choices implemented in `add-core-cms-content-models`, but the seed must avoid implying sponsorship if the relationship is only institutional/scientific support.

### External links

If real links are unknown, seed status as `coming_soon` or equivalent:

- registration URL: empty / coming soon
- livestream URL: empty / coming soon
- YouTube channel URL: empty unless known
- YouTube playlist URL: empty unless known
- Instagram URL: empty unless known
- sponsorship/contact links: use configured email/contact if known, otherwise leave empty

### Initial news/announcements

This proposal MAY seed minimal neutral draft/published announcements only if the news model exists and the team wants initial placeholders. Suggested entries:

- `Programação preliminar em preparação`
- `Submissões em breve`
- `Inscrições em breve`

These should avoid final claims and may be draft by default.

## Implementation Strategy

Implement one of these patterns:

### Preferred

Create an idempotent Django management command:

```text
python manage.py seed_canonical_event_content
```

Recommended path:

```text
core/management/commands/seed_canonical_event_content.py
```

or another app path that matches the implemented model ownership.

### Acceptable

Create Wagtail/Django fixtures if they are reliable and easy to maintain.

### Required behavior

The seed must be idempotent:

1. running once creates missing objects;
2. running again updates canonical fields or leaves existing intentional edits untouched according to documented behavior;
3. it does not create duplicate sponsors/entities/news;
4. it does not overwrite user-edited long-form content unless explicitly intended.

The implementation must document whether the seed is:

- **authoritative update mode**: updates canonical fields each run; or
- **create-only mode**: creates missing objects but avoids overwriting existing values.

For this project, prefer a hybrid:

- canonical event facts may be updated;
- manually edited rich text should not be overwritten after initial creation;
- supporting entities should be upserted by stable slug/name.

## Data Ownership

After this proposal:

- event identity is owned by CMS global settings;
- venue/address/map are owned by CMS global settings until the venue model proposal refines this;
- supporting entities are owned by the supporting-entity/sponsor model;
- external public links are owned by CMS global settings;
- final page copy is still owned by later content-production proposal.

## Acceptance Criteria

1. A developer can seed canonical content with a documented command or fixture.
2. The seed creates/updates global event settings.
3. The seed creates/updates the official venue/address/Google Maps URL.
4. The seed creates/updates known institutional/support entities.
5. The seed sets unknown external links to a safe coming-soon/unavailable state.
6. Running the seed twice does not create duplicates.
7. The seed does not implement public pages.
8. The seed does not add final promotional copy.
9. The change passes:
   - `openspec validate seed-canonical-event-content --strict`
   - `uv run python manage.py check`
   - `uv run python manage.py makemigrations --check --dry-run`
   - `uv run pytest`
