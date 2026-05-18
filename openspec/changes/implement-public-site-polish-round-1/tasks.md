# Tasks: Implement Public Site Polish Round 1

## OpenSpec hygiene

- [ ] Create `openspec/changes/implement-public-site-polish-round-1/`.
- [ ] Add `proposal.md`.
- [ ] Add `design.md`.
- [ ] Add `tasks.md`.
- [ ] Add delta specs for all relevant capabilities.
- [ ] Ensure `proposal.md` includes `## Why` and `## What Changes`.
- [ ] Ensure every delta spec starts with `# <capability-name>`.
- [ ] Ensure every delta spec includes `## Purpose`.
- [ ] Ensure every requirement uses `MUST`.
- [ ] Ensure every requirement has at least one `#### Scenario:` block.
- [ ] Run `openspec validate implement-public-site-polish-round-1 --strict`.

## Required inputs

- [ ] Read `docs/reviews/public-site-content-consistency-round-1.md`.
- [ ] Read `docs/reviews/public-site-content-consistency-matrix-round-1.md`.
- [ ] Read `docs/reviews/public-site-content-consistency-backlog-round-1.md`.
- [ ] Read `docs/reviews/persona-status-map-round-1.md`.
- [ ] Read `docs/reviews/legacy-ghost-facts-inventory-round-1.md`.
- [ ] Read `docs/reviews/consistency-automation-candidates-round-1.md`.
- [ ] Read `docs/reviews/notification-trigger-consistency-round-1.md`.
- [ ] If required input is missing, document the limitation and do not proceed as broad polish.

## Implementation report

- [ ] Create `docs/reviews/public-site-polish-round-1-implementation-report.md`.
- [ ] Record branch and commit.
- [ ] Record reviewed input documents.
- [ ] Record resolved findings.
- [ ] Record deferred findings.
- [ ] Record files changed.
- [ ] Record validation commands and results.
- [ ] Record residual risks.

## Finding triage

- [ ] Extract all P0 findings.
- [ ] Extract all P1 findings.
- [ ] Extract low-risk P2 findings.
- [ ] Identify P3 findings that are trivial.
- [ ] Map each finding to a target surface.
- [ ] Mark findings requiring deferral.
- [ ] Create implementation checklist.

## Canonical public-page fixes

- [ ] Fix event name inconsistencies.
- [ ] Fix event date inconsistencies.
- [ ] Fix venue/address/map inconsistencies.
- [ ] Fix theme inconsistencies.
- [ ] Fix contact e-mail inconsistencies.
- [ ] Fix registration status and CTA inconsistencies.
- [ ] Fix submission status and CTA inconsistencies.
- [ ] Fix livestream/video link inconsistencies.
- [ ] Remove forbidden legacy facts from current pages.
- [ ] Preserve allowed archive facts on previous-edition pages.

## Persona status fixes

- [ ] Apply author-facing status labels from persona status map.
- [ ] Apply reviewer-facing status labels from persona status map.
- [ ] Apply chair-facing status labels from persona status map.
- [ ] Apply admin/staff labels where relevant.
- [ ] Centralize status mappings where feasible.
- [ ] Update dashboard labels.
- [ ] Update report/export status labels.
- [ ] Update notification status labels.

## Workflow fixes

- [ ] Align public submission copy with actual workflow.
- [ ] Align author dashboard submission states.
- [ ] Align reviewer dashboard review states.
- [ ] Align chair dashboard review/decision states.
- [ ] Correct any initial-video-rule inconsistency.
- [ ] Correct accepted modality labels.
- [ ] Correct decision labels and messages.
- [ ] Preserve reviewer privacy.
- [ ] Align final-material request labels.
- [ ] Align final-material upload instructions.
- [ ] Align publication authorization wording.
- [ ] Align proceedings readiness labels.
- [ ] Align published-in-proceedings labels.
- [ ] Align YouTube/video terminology.

## Notification fixes

- [ ] Correct submission confirmation wording if needed.
- [ ] Correct reviewer assignment wording if needed.
- [ ] Correct decision notification wording if needed.
- [ ] Correct final-material request wording if needed.
- [ ] Correct final-material received wording if needed.
- [ ] Correct final-material validation wording if needed.
- [ ] Correct proceedings publication wording if needed.
- [ ] Fix low-risk trigger drift if documented.
- [ ] Defer high-risk workflow trigger redesigns.

## Translation and non-visual content

- [ ] Standardize Portuguese terms.
- [ ] Standardize English terms where present.
- [ ] Standardize navigation labels.
- [ ] Standardize CTA labels.
- [ ] Standardize dashboard labels.
- [ ] Standardize export headers.
- [ ] Fix image and logo alt text inconsistencies.
- [ ] Fix ARIA label inconsistencies.
- [ ] Fix icon-only link labels.
- [ ] Fix form labels.
- [ ] Fix status badge accessible names.

## Reports, exports and indicators fixes

- [ ] Fix report label inconsistencies.
- [ ] Fix indicator label inconsistencies.
- [ ] Fix export header inconsistencies.
- [ ] Fix status values in exports.
- [ ] Ensure protected file URLs are not exported.
- [ ] Ensure reviewer identity is not exposed to unauthorized users.
- [ ] Align proceedings export terminology.
- [ ] Add tests for export headers where feasible.

## Automation

- [ ] Review automation candidates.
- [ ] Add selected high-value smoke tests.
- [ ] Add selected status mapping tests.
- [ ] Add selected export header tests.
- [ ] Add selected protected-file exposure tests.
- [ ] Add selected legacy ghost fact checks if feasible.
- [ ] Document deferred automation candidates.

## Security and privacy

- [ ] Verify no protected file URLs were introduced.
- [ ] Verify no unauthorized reviewer identity exposure was introduced.
- [ ] Verify no unauthorized personal data exposure in exports was introduced.
- [ ] Verify public pages do not expose private workflow information.
- [ ] Verify notifications do not leak private notes.

## Tests and validation

- [ ] Run `openspec validate implement-public-site-polish-round-1 --strict`.
- [ ] Run `uv run python manage.py check`.
- [ ] Run `uv run python manage.py makemigrations --check --dry-run`.
- [ ] Run `uv run pytest`.
- [ ] Run `npm run build` if templates or frontend assets changed.
- [ ] Manually smoke-test public pages.
- [ ] Manually smoke-test author dashboard.
- [ ] Manually smoke-test reviewer dashboard.
- [ ] Manually smoke-test chair dashboard.
- [ ] Manually smoke-test reports/exports if changed.

## PR checklist

- [ ] Branch is `change/implement-public-site-polish-round-1`.
- [ ] PR title starts with `[implement-public-site-polish-round-1]`.
- [ ] PR body references the consistency verification outputs.
- [ ] PR includes implementation report.
- [ ] PR maps changes to source findings.
- [ ] PR does not include broad unrelated redesign.
- [ ] PR does not include new unapproved workflow features.
