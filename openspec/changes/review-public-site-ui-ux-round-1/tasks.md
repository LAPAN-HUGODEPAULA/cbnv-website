# Tasks: Review Public Site UI/UX Round 1

## OpenSpec

- [x] Create `openspec/changes/review-public-site-ui-ux-round-1/`.
- [x] Add `proposal.md`.
- [x] Add `design.md`.
- [x] Add `tasks.md`.
- [x] Add delta spec `specs/ui-ux/spec.md`.
- [x] Add delta spec `specs/public-site/spec.md`.
- [x] Add delta spec `specs/content/spec.md`.
- [x] Add delta spec `specs/accessibility/spec.md`.
- [x] Add delta spec `specs/qa/spec.md`.
- [x] Run `openspec validate review-public-site-ui-ux-round-1 --strict`.

## Review setup

- [x] Confirm `add-public-site-pages-mvp` is implemented and merged.
- [x] Record branch and commit SHA.
- [x] Run or access the public site.
- [x] Confirm seeded canonical content is loaded.
- [x] Identify available pages and URLs.
- [x] Define viewport matrix.
- [x] Record browser/environment.

## Create documentation targets

- [x] Create `docs/reviews/` if missing.
- [x] Create `docs/reviews/public-site-ui-ux-round-1.md`.
- [x] Create `docs/reviews/public-site-ui-ux-round-1-backlog.md`.
- [x] Optionally create `docs/reviews/public-site-ui-ux-round-1-checklist.md`.
- [x] Optionally document screenshot paths if screenshots are captured.

## User journey review

- [x] Review general visitor journey.
- [x] Review potential author journey.
- [x] Review potential participant journey.
- [x] Review potential sponsor/supporter journey.
- [x] Review returning visitor journey.
- [x] Document blockers and friction points.

## Page-by-page review

- [x] Review Home.
- [x] Review About.
- [x] Review Program.
- [x] Review Speakers.
- [x] Review Submissions.
- [x] Review Registration.
- [x] Review Sponsorship.
- [x] Review Previous Editions.
- [x] Review Contact.

## Specific known concerns

- [x] Evaluate latest-news/announcement placement on Home.
- [x] Evaluate whether the Home “Híbrido” card should remain, move, merge or be replaced.
- [x] Check date/location/theme visibility.
- [x] Check venue/address completeness.
- [x] Check CTA hierarchy.
- [x] Check program preview.
- [x] Check “O que esperar?” consistency and necessity.
- [x] Check supporting-entity grid.
- [x] Check footer visibility and redundancy.
- [x] Evaluate About copy depth and usefulness.
- [x] Evaluate Home/About content overlap.
- [x] Check committee/team display.
- [x] Check local/access section.
- [x] Check contact venue/address/map link.
- [x] Check no previous-edition location appears.

## Accessibility and responsiveness

- [x] Test keyboard navigation superficially.
- [x] Check focus visibility.
- [x] Check heading structure.
- [x] Check contrast concerns.
- [x] Check icon-only labels.
- [x] Check mobile navigation.
- [x] Check mobile program readability.
- [x] Check no horizontal overflow on key pages.

## Backlog production

- [x] Create stable issue IDs: `UXR1-001`, `UXR1-002`, etc.
- [x] Assign severity: P0/P1/P2/P3.
- [x] Assign category.
- [x] Identify page/section.
- [x] Describe finding.
- [x] Explain rationale.
- [x] Recommend action.
- [x] Assign target proposal.
- [x] Mark status.

## Section decisions

- [x] Decide keep/remove/merge/move/rewrite/defer/needs-data for major ambiguous sections.
- [x] Document rationale.
- [x] Assign target follow-up proposal.

## Handoffs

- [x] Add handoff section for `produce-public-site-content-round-1`.
- [x] Add handoff section for `verify-cross-page-content-consistency`.
- [x] Add handoff section for `implement-public-site-polish-round-1`.
- [x] Add any future proposal recommendations if outside current plan.

## Validation

- [x] Run `openspec validate review-public-site-ui-ux-round-1 --strict`.
- [x] If code is unchanged, confirm no migrations are needed.
- [x] If any project files besides docs/OpenSpec changed, run relevant checks.
- [x] Recommended sanity checks:
  - [x] `uv run python manage.py check`
  - [x] `uv run pytest`
  - [x] `npm run build` if templates/assets were touched.

## PR checklist

- [x] Branch is `change/review-public-site-ui-ux-round-1`.
- [ ] PR title starts with `[review-public-site-ui-ux-round-1]`.
- [ ] PR body includes `Closes #7`.
- [x] PR includes review report.
- [x] PR includes prioritized backlog.
- [x] PR does not implement UI/layout/content fixes.
