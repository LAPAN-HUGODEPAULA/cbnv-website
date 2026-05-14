# Tasks: Verify Cross-Page Content Consistency

## OpenSpec hygiene

- [x] Create `openspec/changes/verify-cross-page-content-consistency/`.
- [x] Add `proposal.md`.
- [x] Add `design.md`.
- [x] Add `tasks.md`.
- [x] Add delta specs for all relevant capabilities.
- [x] Ensure `proposal.md` includes `## Why` and `## What Changes`.
- [x] Ensure every delta spec starts with `# <capability-name>`.
- [x] Ensure every delta spec includes `## Purpose`.
- [x] Ensure every requirement uses `MUST`.
- [x] Ensure every requirement has at least one `#### Scenario:` block.
- [x] Run `openspec validate verify-cross-page-content-consistency --strict`.

## Create review documents

- [x] Create `docs/reviews/public-site-content-consistency-round-1.md`.
- [x] Create `docs/reviews/public-site-content-consistency-matrix-round-1.md`.
- [x] Create `docs/reviews/public-site-content-consistency-backlog-round-1.md`.
- [x] Create `docs/reviews/persona-status-map-round-1.md`.
- [x] Create `docs/reviews/legacy-ghost-facts-inventory-round-1.md`.
- [x] Create `docs/reviews/consistency-automation-candidates-round-1.md`.
- [x] Create `docs/reviews/notification-trigger-consistency-round-1.md`.

## Data profiles

- [x] Define empty/default profile.
- [x] Define populated/custom profile.
- [x] Record branch, commit and database state for each profile.
- [x] Run review against empty/default profile.
- [x] Run review against populated/custom profile.
- [x] Record which profile exposes each finding.

## Canonical event facts

- [x] Verify event name, short name, edition and theme.
- [x] Verify dates, venue, address, city, state and country.
- [x] Verify format label and Google Maps URL.
- [x] Verify registration, submission and livestream status/link behavior.
- [x] Verify social links and contact e-mails.

## Public and workflow surfaces

- [x] Verify all public pages and footer.
- [x] Verify author dashboard.
- [x] Verify reviewer dashboard.
- [x] Verify chair dashboard.
- [x] Verify submission forms and upload messages.
- [x] Verify review and decision screens.
- [x] Verify final-material screens.
- [x] Verify proceedings screens.
- [x] Verify video gallery.
- [x] Verify report/export screens.

## Persona status map

- [x] Map submission statuses by persona.
- [x] Map review assignment statuses by persona.
- [x] Map review statuses by persona.
- [x] Map decision statuses by persona.
- [x] Map final-material statuses by persona.
- [x] Map proceedings statuses by persona.
- [x] Mark intentional asymmetries.
- [x] Flag unintentional asymmetries.

## Translation and terminology

- [x] Verify Portuguese labels.
- [x] Verify English labels where present.
- [x] Verify navigation, CTA, dashboard, e-mail and export labels.
- [x] Verify status labels.
- [x] Record preferred terminology.

## Non-visual content

- [x] Verify image alt text.
- [x] Verify logo alt text.
- [x] Verify ARIA labels.
- [x] Verify icon-only link labels.
- [x] Verify form labels.
- [x] Verify status badge accessible names.
- [x] Verify map and social link accessible names.

## Legacy ghost facts

- [x] Inventory old dates, venues, addresses and themes.
- [x] Inventory old sponsor/support labels.
- [x] Inventory old registration and submission links.
- [x] Inventory old program/workshop references.
- [x] Search current-event contexts.
- [x] Mark allowed archive contexts.
- [x] Flag legacy contamination.

## Notification trigger consistency

- [x] Verify submission confirmation trigger.
- [x] Verify reviewer assignment trigger.
- [x] Verify decision notification trigger.
- [x] Verify final-material request trigger.
- [x] Verify final-material received trigger.
- [x] Verify final-material validation trigger.
- [x] Verify proceedings publication trigger if implemented.
- [x] Compare notification copy with dashboard status.
- [x] Flag premature, duplicate or stale notification risks.

## Reports, exports and indicators

- [x] Verify report labels and indicator labels.
- [x] Verify export column labels.
- [x] Verify status values in exports.
- [x] Verify privacy-sensitive fields.
- [x] Verify protected file URLs are not exported.
- [x] Verify indicators use the same status vocabulary.

## Automation candidates

- [x] Identify high-risk repeated facts.
- [x] Identify feasible smoke tests.
- [x] Identify feasible management-command checks.
- [x] Identify feasible grep/static checks.
- [x] Prioritize automation candidates.
- [x] Route candidates to appropriate future proposal.

## Backlog

- [x] Create stable IDs such as `CCR1-001`.
- [x] Assign severity and category.
- [x] Identify surface, persona and data profile.
- [x] Record expected value or rule.
- [x] Record observed value.
- [x] Record recommendation and target proposal.
- [x] Mark status.

## Validation

- [x] Run `openspec validate verify-cross-page-content-consistency --strict`.
- [x] If only docs/OpenSpec changed, Django/npm checks are optional.
- [x] If automated tests/checks are added, run `uv run pytest`.
- [x] If templates or code are touched, run relevant project checks.

## PR checklist

- [x] Branch is `change/verify-cross-page-content-consistency`.
- [x] PR title starts with `[verify-cross-page-content-consistency]`.
- [x] PR body includes `Closes #9` or the correct issue number.
- [x] PR includes required review documents or templates.
- [x] PR does not implement broad unrelated fixes.
