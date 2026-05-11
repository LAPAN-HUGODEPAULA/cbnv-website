# Program and Venue Data

## Purpose

Document the canonical ownership and consumption rules for CBNV 2026 program, speaker and venue data.

## Requirements

### Requirement: Program ownership

The `program` Django app SHALL own structured program data for days, sessions, talks and speakers.

#### Scenario: Public pages read program data

- **GIVEN** a public page needs the event schedule
- **WHEN** it queries program data
- **THEN** it SHALL use `program.models.get_public_program_by_day()` instead of duplicating status or ordering logic in page code

### Requirement: Canonical seed path

Canonical local or staging setup SHALL use `seed_canonical_event_content` for event settings and `seed_program` for preliminary confirmed program data.

#### Scenario: Developer seeds event data

- **GIVEN** a developer needs canonical CBNV 2026 data
- **WHEN** seed commands are executed
- **THEN** `populate_cbnv` SHALL be treated as legacy/dev-only and the canonical path SHALL be `seed_canonical_event_content` followed by `seed_program`

### Requirement: Speaker and activity status meanings

Program public output SHALL expose only published sessions and confirmed public speaker details.

#### Scenario: Pending details exist

- **GIVEN** a speaker or talk is `pending`, `invited` or `hidden`
- **WHEN** public program or speaker queries run
- **THEN** identifiable speaker details SHALL be omitted from public results

`ProgramSession.status` values:

- `draft`: internal work in progress.
- `pending`: not ready for public display.
- `published`: eligible for public program queries.
- `cancelled`: retained for admin/history, omitted from public program queries.

`Speaker.status` and `ProgramTalk.status` values:

- `confirmed`: eligible for public display.
- `invited` or `pending`: not confirmed, omitted from public helpers.
- `hidden`: intentionally not public.

### Requirement: Venue source

Canonical venue data SHALL remain settings-backed in `core.CoreSettings` for the MVP.

#### Scenario: Public page needs venue data

- **GIVEN** a public page needs local or access information
- **WHEN** it reads the venue data
- **THEN** it SHALL use `CoreSettings.canonical_venue` and omit missing optional fields without placeholder copy

`CoreSettings` is the canonical source for venue name, short name, address, city, state, country, Google Maps URL and optional access notes. No `Venue` snippet is part of this MVP because CBNV 2026 has one official venue.

### Requirement: Public page scope

This implementation SHALL provide data contracts only and SHALL NOT implement final public pages.

#### Scenario: Later proposal renders pages

- **GIVEN** future public Programacao, Palestrantes or local pages are implemented
- **WHEN** they need program or venue content
- **THEN** they SHALL consume the helpers documented here without adding submissions, reviews, payments, certificates or QR code flows in this change
