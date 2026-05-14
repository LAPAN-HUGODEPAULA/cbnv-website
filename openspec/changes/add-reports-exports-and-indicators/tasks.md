# Tasks: Add Reports, Exports and Indicators

## OpenSpec hygiene

- [x] Create `openspec/changes/add-reports-exports-and-indicators/`.
- [x] Add `proposal.md`.
- [x] Add `design.md`.
- [x] Add `tasks.md`.
- [x] Add delta spec `specs/reports/spec.md`.
- [x] Add delta spec `specs/exports/spec.md`.
- [x] Add delta spec `specs/indicators/spec.md`.
- [x] Add delta spec `specs/submissions/spec.md`.
- [x] Add delta spec `specs/reviews/spec.md`.
- [x] Add delta spec `specs/proceedings/spec.md`.
- [x] Add delta spec `specs/dashboards/spec.md`.
- [x] Add delta spec `specs/security/spec.md`.
- [x] Add delta spec `specs/qa/spec.md`.
- [x] Ensure every delta spec starts with `# <capability-name>`.
- [x] Ensure every delta spec includes `## Purpose`.
- [x] Ensure every requirement uses `MUST`.
- [x] Ensure every requirement has at least one `#### Scenario:` block.
- [x] Run `openspec validate add-reports-exports-and-indicators --strict`.

## Pre-implementation audit

- [x] Review submission models and statuses.
- [x] Review author models.
- [x] Review review assignment/review/decision models.
- [x] Review final material/proceedings models.
- [x] Review account role flags.
- [x] Review chair dashboard routes/templates.
- [x] Decide report app/module placement.
- [x] Decide CSV-only vs CSV/XLSX support.
- [x] Decide export field list and privacy classification.

## Reports app/module

- [x] Create reports app or module if missing.
- [x] Add report services.
- [x] Add export builders.
- [x] Add report views.
- [x] Add report URLs.
- [x] Add templates for report index/dashboard.
- [x] Add permission helpers.
- [x] Add documentation.

## Indicators

- [x] Implement total submissions count.
- [x] Implement submissions by status.
- [x] Implement submissions by thematic axis.
- [x] Implement submissions by final modality.
- [x] Implement submissions by date range if feasible.
- [x] Implement review assignments by status.
- [x] Implement completed/pending reviews.
- [x] Implement decision outcome counts.
- [x] Implement accepted submissions count.
- [x] Implement final materials pending/received/validated counts.
- [x] Implement ready-for-proceedings count.
- [x] Implement published-in-proceedings count.
- [x] Implement works with video URL count.
- [x] Implement videos promoted to gallery count if association exists.
- [x] Implement institutions count.
- [x] Implement authors count where data allows.
- [x] Implement state/country counts where data allows.

## Filters

- [x] Add status filter.
- [x] Add thematic axis filter.
- [x] Add final modality filter.
- [x] Add date range filter.
- [x] Add institution filter if feasible.
- [x] Add country/state filter if feasible.
- [x] Add final-material/proceedings status filter if feasible.
- [x] Apply filters to indicators where practical.
- [x] Apply filters to exports where practical.

## CSV exports

- [x] Implement submissions CSV export.
- [x] Implement authors CSV export.
- [x] Implement institutions CSV export.
- [x] Implement proceedings CSV export.
- [x] Implement reviews/decisions CSV export with permission controls.
- [x] Use UTF-8 encoding.
- [x] Use deterministic column order.
- [x] Avoid protected file URLs.
- [x] Avoid unauthorized sensitive fields.

## XLSX exports

- [x] Decide whether XLSX is implemented in this change.
- [x] If implemented, add submissions XLSX export.
- [x] If implemented, add authors XLSX export.
- [x] If implemented, add institutions XLSX export.
- [x] If implemented, add proceedings XLSX export.
- [x] If implemented, add reviews/decisions XLSX export with permissions.
- [x] Use deterministic sheet names.
- [x] Use deterministic column order.
- [x] If not implemented, document CSV-only limitation.

## Submission export fields

- [x] Include submission code.
- [x] Include title.
- [x] Include thematic axis.
- [x] Include status.
- [x] Include final modality.
- [x] Include submitter or corresponding author.
- [x] Include created/submitted timestamps.
- [x] Include decision status if available.
- [x] Include final-material/proceedings status if available.

## Author and institution exports

- [x] Include submission code.
- [x] Include author order.
- [x] Include full name.
- [x] Include e-mail only when permitted.
- [x] Include institution.
- [x] Include country/state/city if available.
- [x] Include corresponding author flag.
- [x] Include presenting author flag.
- [x] Aggregate institutions and counts.

## Review/decision exports

- [x] Include assignment status.
- [x] Include review status.
- [x] Include decision status.
- [x] Include final modality.
- [x] Include timestamps.
- [x] Include reviewer identity only for privileged users.
- [x] Exclude review text unless explicitly permitted.
- [x] Exclude internal notes unless explicitly permitted.

## Proceedings exports

- [x] Include submission code.
- [x] Include title.
- [x] Include authors.
- [x] Include affiliations.
- [x] Include abstract.
- [x] Include keywords.
- [x] Include thematic axis.
- [x] Include final modality.
- [x] Include publication authorization status.
- [x] Include final-material validation status.
- [x] Include video URL only when permitted.
- [x] Include proceedings publication status.

## Dashboard integration

- [x] Add reports/exports link to chair dashboard.
- [x] Add report cards to reports index.
- [x] Add export buttons to reports index.
- [x] Add empty states.
- [x] Add permission-denied handling.

## Security and privacy

- [x] Require chair/scientific committee role for report access.
- [x] Require privileged access for review/decision exports.
- [x] Prevent authors from accessing global exports.
- [x] Prevent reviewers from accessing global exports unless explicitly allowed.
- [x] Avoid protected file URLs in exports.
- [x] Classify sensitive fields.
- [x] Add tests for unauthorized access.

## Documentation

- [x] Create or update `docs/reports-exports-and-indicators.md`.
- [x] Document available indicators.
- [x] Document available exports.
- [x] Document export columns.
- [x] Document filters.
- [x] Document permissions.
- [x] Document privacy limitations.
- [x] Document CSV/XLSX support status.

## Tests

- [x] Test reports dashboard requires authorization.
- [x] Test chair user can access reports dashboard.
- [x] Test unauthorized user cannot access reports dashboard.
- [x] Test submission indicator counts.
- [x] Test final modality indicator counts.
- [x] Test final-material/proceedings indicator counts.
- [x] Test CSV headers and rows.
- [x] Test CSV uses deterministic columns.
- [x] Test XLSX sheets if implemented.
- [x] Test review export permissions.
- [x] Test exports do not include protected file URLs.
- [x] Test filters affect exported rows if filters are implemented.

## Validation

- [x] Run `openspec validate add-reports-exports-and-indicators --strict`.
- [x] Run `uv run python manage.py check`.
- [x] Run `uv run python manage.py makemigrations --check --dry-run`.
- [x] Run `uv run pytest`.
- [x] Run `npm run build` if templates/CSS changed.

## PR checklist

- [x] Branch is `change/add-reports-exports-and-indicators`.
- [ ] PR title starts with `[add-reports-exports-and-indicators]`.
- [ ] PR body includes `Closes #15`.
- [x] PR includes tests for reports and exports.
- [x] PR includes privacy-aware export behavior.
- [x] PR does not expose protected file URLs.
- [x] PR does not implement unrelated certificate/check-in/payment features.
