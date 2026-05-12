# Tasks: Produce Public Site Content Round 1

## OpenSpec

- [x] Create `openspec/changes/produce-public-site-content-round-1/`.
- [x] Add `proposal.md`.
- [x] Add `design.md`.
- [x] Add `tasks.md`.
- [x] Add delta spec `specs/content/spec.md`.
- [x] Add delta spec `specs/public-site/spec.md`.
- [x] Add delta spec `specs/cms/spec.md`.
- [x] Add delta spec `specs/editorial/spec.md`.
- [x] Add delta spec `specs/qa/spec.md`.
- [x] Run `openspec validate produce-public-site-content-round-1 --strict`.

## Inputs

- [x] Read source-of-truth requirements document.
- [x] Read `docs/CBNV2026_OpenSpec_Plano_Implementacao_v2.md`.
- [x] Read `docs/reviews/public-site-ui-ux-round-1.md`.
- [x] Read `docs/reviews/public-site-ui-ux-round-1-backlog.md`.
- [x] Review current page structure and available CMS fields.
- [x] Review current program/speaker/venue data.
- [x] Review canonical seeded event content.

## Create output docs

- [x] Create `docs/content/` if missing.
- [x] Create `docs/content/public-site-content-round-1.md`.
- [x] Create `docs/content/public-site-copy-map-round-1.md`.
- [x] Create `docs/content/public-site-editorial-guidelines.md`.
- [x] Optionally create `docs/content/public-site-content-decisions-round-1.md`.
- [x] Optionally create `docs/content/public-site-open-questions-round-1.md`.

## Editorial guidelines

- [x] Define voice and tone.
- [x] Define terms to use.
- [x] Define terms to avoid.
- [x] Define rules for confirmed vs pending content.
- [x] Define CTA language.
- [x] Define “em breve” language.
- [x] Define previous-edition archive language.
- [x] Define institutional acknowledgement language.

## Page copy

- [x] Write Home content.
- [x] Write About content.
- [x] Write Program content.
- [x] Write Speakers content.
- [x] Write Submissions content.
- [x] Write Registration content.
- [x] Write Sponsorship content.
- [x] Write Previous Editions content.
- [x] Write Contact content.
- [x] Write Footer and shared microcopy.

## Specific content requirements

- [x] Avoid inflated claims.
- [x] Avoid unsupported “largest event” language.
- [x] Avoid workshop references unless confirmed.
- [x] Explicitly state video is not required in initial submission.
- [x] Explain registration/certificates/QR are external.
- [x] Use current CAD-1/UFMG venue/address.
- [x] Frame previous editions as archive/history.
- [x] Mark unavailable links as “em breve”.

## Copy map

- [x] Map each content block to page/section.
- [x] Identify target CMS field/template/seed location.
- [x] Mark status: ready, provisional, needs-data or defer.
- [x] Identify source/rationale for each block.
- [x] Identify blocks that should not yet be implemented.

## Implementation, if appropriate

- [x] Update CMS seed/fixtures if content storage mechanism is defined. Not applied in this round; copy map identifies targets and defers unstable storage points.
- [x] Update page body/default content only where safe. Not applied in this round; produced docs define safe field targets for later application.
- [x] Update template text only if it is clearly placeholder copy and no CMS field exists. Not applied in this round; no template edits were needed.
- [x] Do not make layout changes.
- [x] Do not add migrations unless separately justified.

## Handoff

- [x] Add handoff to `verify-cross-page-content-consistency`.
- [x] Add handoff to `implement-public-site-polish-round-1`.
- [x] Add list of unresolved factual questions.
- [x] Add list of content that remains provisional.

## Validation

- [x] Run `openspec validate produce-public-site-content-round-1 --strict`.
- [x] If implementation files changed, run `uv run python manage.py check`. Not applicable; no implementation files changed.
- [x] If implementation files changed, run `uv run python manage.py makemigrations --check --dry-run`. Not applicable; no implementation files changed.
- [x] If implementation files changed, run `uv run pytest`. Ran full suite anyway: 233 passed.
- [x] If templates/CSS changed, run `npm run build`. Not applicable; no templates/CSS changed.

## PR checklist

- [x] Branch is `change/produce-public-site-content-round-1`.
- [x] PR title starts with `[produce-public-site-content-round-1]`.
- [x] PR body includes `Closes #8`.
- [x] PR includes required content docs.
- [x] PR does not implement layout redesign.
- [x] PR does not add unapproved models or migrations.
