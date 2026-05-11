# Tasks: Seed Canonical Event Content

## OpenSpec

- [x] Create `openspec/changes/seed-canonical-event-content/`.
- [x] Add `proposal.md`.
- [x] Add `design.md`.
- [x] Add `tasks.md`.
- [x] Add delta spec `specs/content/spec.md`.
- [x] Add delta spec `specs/cms/spec.md`.
- [x] Add delta spec `specs/public-site/spec.md`.
- [x] Add delta spec `specs/data-seeding/spec.md`.
- [x] Run `openspec validate seed-canonical-event-content --strict`.

## Implementation planning

- [x] Inspect models created by `add-core-cms-content-models`.
- [x] Identify exact model names and fields for:
  - [x] global site settings;
  - [x] supporting entities/sponsors;
  - [x] news/announcements;
  - [x] external link statuses.
- [x] Decide whether to implement a management command or fixture.
- [x] Document idempotence behavior before implementation.

## Management command / seed mechanism

- [x] Create `seed_canonical_event_content` management command or equivalent fixture.
- [x] Ensure seed can be run locally.
- [x] Ensure seed can be run in staging.
- [x] Ensure seed prints a useful summary.
- [x] Add optional `--dry-run` if feasible.
- [x] Add optional `--force` if useful.

## Seed global event settings

- [x] Seed formal event name.
- [x] Seed short event name.
- [x] Seed edition.
- [x] Seed theme.
- [x] Seed start date.
- [x] Seed end date.
- [x] Seed format.
- [x] Seed city/state/country.
- [x] Seed venue name.
- [x] Seed venue short name.
- [x] Seed full address.
- [x] Seed Google Maps URL.
- [x] Seed contact fields if known.
- [x] Seed FAPEMIG acknowledgement text/slot.
- [x] Seed default SEO title/description if fields exist.

## Seed external link states

- [x] Registration link status is `coming soon` if URL is unknown.
- [x] Livestream link status is `coming soon` if URL is unknown.
- [x] YouTube channel URL is blank or configured if known.
- [x] YouTube playlist URL is blank or configured if known.
- [x] Instagram URL is blank or configured if known.
- [x] No placeholder `#` links are introduced.

## Seed supporting entities

- [x] Seed UFMG.
- [x] Seed FUNDEP.
- [x] Seed FAPEMIG.
- [x] Seed Sociedade Brasileira de Neurovisão.
- [x] Seed Hospital de Olhos de Minas Gerais / HOLHOS.
- [x] Seed UFRJ.
- [x] Seed USP.
- [x] Seed UFRN.
- [x] Seed UEMG.
- [x] Use stable slugs or normalized names.
- [x] Avoid duplicate entities on repeated runs.
- [x] Use conservative categories.

## Optional announcements

- [x] Decide whether initial announcements should be seeded.
- [x] If yes, create neutral draft/placeholder entries only.
- [x] Avoid final promotional copy.

## Documentation

- [x] Create or update `docs/canonical-content-seed.md`.
- [x] Document command usage.
- [x] Document idempotence behavior.
- [x] Document seeded entities.
- [x] Document known pending links.
- [x] Document what is intentionally not seeded.

## Tests

- [x] Test command creates global settings if missing.
- [x] Test command updates or preserves settings according to documented behavior.
- [x] Test supporting entities are created.
- [x] Test second run does not duplicate entities.
- [x] Test unknown links use coming-soon/unavailable state.
- [x] Test command exits successfully.

## Validation

- [x] Run `openspec validate seed-canonical-event-content --strict`.
- [x] Run `uv run python manage.py check`.
- [x] Run `uv run python manage.py makemigrations --check --dry-run`.
- [x] Run `uv run pytest`.

## PR checklist

- [x] Branch is `change/seed-canonical-event-content`.
- [x] PR title starts with `[seed-canonical-event-content]`.
- [x] PR body includes `Closes #4`.
- [x] PR body includes validation checklist.
- [x] No public pages, program models, submissions or review flows were implemented.
