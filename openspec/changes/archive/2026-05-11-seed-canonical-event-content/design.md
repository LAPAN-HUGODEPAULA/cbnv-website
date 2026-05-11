# Design: Seed Canonical Event Content

## Overview

This proposal adds the first controlled content dataset to the CBNV 2026 platform. It sits between the core CMS models and public-page implementation.

The seed should make later public pages deterministic: every repeated event fact should come from CMS-backed canonical data, not from scattered templates.

## Design Principles

### 1. Canonical facts must be centralized

Event name, theme, dates, venue, address and global links must have one source.

### 2. Seed data should be conservative

The seed must not introduce inflated claims, unconfirmed speakers, unconfirmed sponsors or final editorial copy.

### 3. Idempotence is mandatory

The seed must be safe to run during local development, staging and test setup without duplicating objects.

### 4. Use stable identifiers

Where possible, use stable slugs or keys for upserts:

- `ufmg`
- `fundep`
- `fapemig`
- `sociedade-brasileira-de-neurovisao`
- `holhos`
- `ufrj`
- `usp`
- `ufrn`
- `uemg`

### 5. Do not overwrite human-edited content unnecessarily

The seed should avoid destroying editorial work after initial creation.

## Recommended Implementation

### Management command

Implement:

```bash
uv run python manage.py seed_canonical_event_content
```

Options may include:

```bash
uv run python manage.py seed_canonical_event_content --dry-run
uv run python manage.py seed_canonical_event_content --force
```

`--dry-run` is recommended but not strictly required for MVP.

`--force` may update canonical fields if the implementation chooses to protect manual edits by default.

### Upsert strategy

Recommended:

1. locate the current Wagtail site;
2. locate or create global settings for that site;
3. upsert canonical global fields;
4. upsert supporting entities by slug or normalized name;
5. create minimal announcement placeholders only if this is explicitly useful;
6. report created/updated/skipped counts.

### Logging/output

The command should print a short summary:

```text
Seed canonical event content
Settings: updated
Supporting entities: 9 created, 0 updated, 0 skipped
Announcements: skipped
Done
```

## Canonical Data

### Global settings fields

Map fields to the model created in `add-core-cms-content-models`.

If a field does not exist, do not invent unrelated storage. Either:

1. skip with a clear comment/output; or
2. add the missing field only if it clearly belongs to the core settings model and does not expand scope.

### Venue and map

Use exactly:

```text
Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha.
R. Prof. Baeta Viana, s/n - Pampulha, Belo Horizonte - MG, 31270-901
```

Google Maps URL:

```text
https://maps.app.goo.gl/xzqJ2LCAHVP4hsFp6
```

Do not use venue data from previous CBNV editions.

### Supporting entities

Use neutral categories. If model choices differ, choose the closest accurate category.

FAPEMIG should be categorized as funding agency/support institution, not as a generic commercial sponsor.

### External links

Unknown links should not become `#` links in public rendering. They should be represented by an explicit status such as `coming_soon`.

## Test Strategy

Minimum tests:

1. command creates settings when missing;
2. command upserts settings when already present;
3. command creates supporting entities once;
4. command is idempotent on second run;
5. unknown links are stored as coming-soon/unavailable;
6. no duplicate entities are created.

## Documentation

Update or create:

```text
docs/canonical-content-seed.md
```

Document:

- how to run the seed;
- what it creates;
- what it intentionally does not create;
- how idempotence works;
- how to update canonical content later.

## Interaction with Future Proposals

### Used by `add-public-site-pages-mvp`

Public pages will consume seeded settings/entities.

### Refined by `add-program-speakers-and-venue-models`

That proposal may move venue into a richer model, but it must preserve canonical address consistency.

### Checked by `verify-cross-page-content-consistency`

The consistency proposal should use seeded canonical values as the expected baseline.
