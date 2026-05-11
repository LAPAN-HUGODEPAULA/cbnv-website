# Tasks: Add Program Speakers and Venue Models

## 1. OpenSpec

- [x] 1.1 Create `openspec/changes/add-program-speakers-and-venue-models/`.
- [x] 1.2 Add `proposal.md`.
- [x] 1.3 Add `design.md`.
- [x] 1.4 Add delta spec `specs/program/spec.md`.
- [x] 1.5 Add new capability spec `specs/venue/spec.md`.
- [x] 1.6 Run `openspec validate add-program-speakers-and-venue-models --strict`.

## 2. Model Audit

- [x] 2.1 Inspect existing `program` models, migrations, admin panels and seed command.
- [x] 2.2 Inspect existing venue-related fields in `core.CoreSettings`.
- [x] 2.3 Confirm venue remains settings-backed in `CoreSettings` for the MVP; do not create a `Venue` snippet in this proposal.
- [x] 2.4 Document the canonical source for venue data in implementation notes or docs.

## 3. Program Data Models

- [x] 3.1 Confirm `ProgramDay`, `ProgramSession`, `ProgramTalk` and `Speaker` have required fields for the public program contract.
- [x] 3.2 Add any missing fields for deterministic ordering, public status, room/location and admin labels.
- [x] 3.3 Preserve relational integrity between days, sessions, talks and speakers.
- [x] 3.4 Add or update Wagtail panels/snippet registration for single-admin editing.
- [x] 3.5 Create incremental migrations for all model changes.

## 4. Public Query Behavior

- [x] 4.1 Add query helpers or managers for public program sessions grouped by day.
- [x] 4.2 Ensure public program queries exclude draft, pending and cancelled sessions.
- [x] 4.3 Ensure pending and hidden speaker details are not exposed by public query helpers.
- [x] 4.4 Ensure confirmed speakers linked to public activities can be returned for speaker index usage.
- [x] 4.5 Ensure ordering is deterministic by date, configured order and start time.
- [x] 4.6 Move public program filtering/grouping out of `ProgramPage.get_context()` into `program` query helpers or managers.
- [x] 4.7 Update `ProgramPage` to consume the program-domain helper.

## 5. Venue Data

- [x] 5.1 Implement the selected canonical venue storage approach.
- [x] 5.2 Store official venue name and short name.
- [x] 5.3 Store full official address.
- [x] 5.4 Store Google Maps URL.
- [x] 5.5 Add optional access instructions without hardcoding page copy.
- [x] 5.6 Provide a helper or documented access pattern for public pages to read canonical venue data.
- [x] 5.7 Add `venue_address` to `CoreSettings`.
- [x] 5.8 Add optional `venue_access_notes` to `CoreSettings`.
- [x] 5.9 Update `seed_canonical_event_content` to populate `venue_address` instead of overloading `location` with the full address.
- [x] 5.10 Keep `location` as a short display summary or backward-compatible field.
- [x] 5.11 Ensure missing optional venue fields are omitted cleanly by consumers.

## 6. Seed Data

- [x] 6.1 Review the existing `seed_program` command.
- [x] 6.2 Make the program seed idempotent if it is not already.
- [x] 6.3 Seed only canonical confirmed program/speaker data.
- [x] 6.4 Avoid placeholder `#` links and unconfirmed public speaker claims.
- [x] 6.5 Ensure canonical CAD-1/UFMG venue data is preserved by the seed flow where the relevant fields exist.
- [x] 6.6 Add command output summarizing created, updated and skipped records.

## 7. Documentation

- [x] 7.1 Create or update documentation for program model ownership.
- [x] 7.2 Document `populate_cbnv` as legacy/dev-only and identify `seed_canonical_event_content` + `seed_program` as the canonical seed path.
- [x] 7.3 Document speaker and activity status meanings.
- [x] 7.4 Document where canonical venue data lives.
- [x] 7.5 Document how later public pages should consume program and venue data.
- [x] 7.6 Document what remains out of scope for public page implementation.

## 8. Tests

- [x] 8.1 Add model tests for program relationships.
- [x] 8.2 Add tests for public program ordering and grouping.
- [x] 8.3 Add tests that draft, pending and cancelled sessions are excluded from public queries.
- [x] 8.4 Add tests that pending and hidden speaker details are not exposed publicly.
- [x] 8.5 Add tests for confirmed speaker retrieval.
- [x] 8.6 Add tests for canonical venue fields and fallback behavior.
- [x] 8.7 Add tests for `seed_program` idempotence where the command is implemented.

## 9. Validation

- [x] 9.1 Run `openspec validate add-program-speakers-and-venue-models --strict`.
- [x] 9.2 Run `uv run python manage.py check`.
- [x] 9.3 Run `uv run python manage.py makemigrations --check --dry-run`.
- [x] 9.4 Run `uv run pytest`.

## 10. PR Checklist

- [x] 10.1 Branch is `change/add-program-speakers-and-venue-models`.
- [x] 10.2 PR title starts with `[add-program-speakers-and-venue-models]`.
- [x] 10.3 PR body includes linked issue or planning note.
- [x] 10.4 PR body includes validation checklist.
- [x] 10.5 No final public pages, submissions, reviews, payments, certificates or QR code flows were implemented.
