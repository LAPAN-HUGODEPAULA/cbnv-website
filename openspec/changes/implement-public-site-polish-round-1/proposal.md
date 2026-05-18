# Proposal: Implement Public Site Polish Round 1

## Change ID

`implement-public-site-polish-round-1`

## Why

The consistency verification pass identifies contradictions, terminology drift, status-label mismatches, legacy contamination, notification drift, non-visual content inconsistencies and automation opportunities across the CBNV 2026 platform. Those findings only improve the system if they are converted into traceable implementation changes.

The platform now includes public pages, accounts, submissions, review/decision workflows, final materials, proceedings, video resources, notifications, dashboards, reports and exports. A generic visual polish pass is insufficient. This change must implement the highest-priority corrections from `verify-cross-page-content-consistency` while preserving the system boundaries already established by prior proposals.

## What Changes

This change implements the first corrective polish pass after `verify-cross-page-content-consistency`.

It MUST consume the consistency review artifacts when present:

```text
docs/reviews/public-site-content-consistency-round-1.md
docs/reviews/public-site-content-consistency-matrix-round-1.md
docs/reviews/public-site-content-consistency-backlog-round-1.md
docs/reviews/persona-status-map-round-1.md
docs/reviews/legacy-ghost-facts-inventory-round-1.md
docs/reviews/consistency-automation-candidates-round-1.md
docs/reviews/notification-trigger-consistency-round-1.md
```

It MUST create an implementation report:

```text
docs/reviews/public-site-polish-round-1-implementation-report.md
```

The change MUST focus on:

1. correcting public-page content inconsistencies;
2. aligning dashboard status labels with the persona status map;
3. correcting notification wording and low-risk trigger drift;
4. removing legacy ghost facts from current-event contexts;
5. standardizing Portuguese/English terminology;
6. fixing alt text, ARIA labels, icon labels and form-label consistency;
7. aligning report/export headers and indicator labels with approved terminology;
8. ensuring CTAs obey `CoreSettings` link and status fields;
9. preventing protected-file URL exposure in public pages and exports;
10. adding selected automated consistency checks where feasible.

## Required Inputs

This change depends on the consistency review outputs. If those documents are missing, this change MUST not proceed as a broad ad hoc polish pass. It may only create scaffolding or explicitly document missing inputs.

## Implementation Priority

The implementation MUST process findings in this order:

1. P0 findings;
2. P1 findings;
3. low-risk P2 findings;
4. trivial P3 findings only if non-disruptive.

Any P0 or P1 finding not implemented MUST be documented as deferred with rationale and target follow-up proposal.

## Scope

In scope:

- public-page template and copy corrections;
- dashboard label and CTA corrections;
- persona-specific status label alignment;
- notification subject/body wording corrections;
- low-risk notification trigger corrections;
- translation and terminology corrections;
- non-visual content corrections;
- report/export header and label corrections;
- safe status-label helper functions or mapping corrections;
- removal of legacy ghost facts from current-event contexts;
- selected automated smoke tests or consistency checks;
- implementation report.

Out of scope:

- broad visual redesign;
- new workflow features;
- large data model redesign;
- new authentication flows;
- external registration integration;
- payment, certificate or QR-code systems;
- automatic YouTube API sync;
- broad report-builder features;
- full accessibility audit;
- broad i18n architecture redesign.

## Traceability Rule

Every non-trivial implementation change MUST map to at least one of:

- a consistency backlog ID;
- a persona status map finding;
- a legacy ghost facts finding;
- a notification trigger finding;
- an automation candidate;
- an explicit acceptance criterion in this proposal.

The implementation report MUST list that mapping.

## Required Implementation Report

The implementation report MUST include:

```markdown
# Public Site Polish Round 1 — Implementation Report

## Metadata
## Inputs reviewed
## Summary
## Resolved findings
## Deferred findings
## Page and workflow changes
## Notification changes
## Translation and terminology changes
## Non-visual content changes
## Report/export changes
## Automation added
## Validation results
## Residual risks
```

Resolved findings table:

```markdown
| Source ID | Severity | Source document | Surface | Action | Files changed | Status |
|---|---|---|---|---|---|---|
```

Deferred findings table:

```markdown
| Source ID | Severity | Reason deferred | Target proposal | Risk |
|---|---|---|---|---|
```

## Acceptance Criteria

1. P0 findings from the consistency backlog are resolved or explicitly deferred with strong rationale.
2. P1 findings from the consistency backlog are resolved or explicitly deferred with rationale.
3. Public pages use canonical event facts consistently.
4. CTAs respect `CoreSettings` link and status fields.
5. Persona-facing status labels align with the persona status map.
6. Current-event pages do not contain forbidden legacy ghost facts.
7. Notification copy and trigger behavior align with the notification-trigger review for implemented fixes.
8. Report/export headers use approved terminology for implemented fixes.
9. Non-visual labels and alt text are corrected for implemented findings.
10. Protected-file URLs are not exposed by implemented public/report/export fixes.
11. Selected automated consistency checks are added or documented as deferred.
12. `docs/reviews/public-site-polish-round-1-implementation-report.md` exists.
13. Validation passes:

```bash
openspec validate implement-public-site-polish-round-1 --strict
uv run python manage.py check
uv run python manage.py makemigrations --check --dry-run
uv run pytest
```

14. `npm run build` passes when templates or frontend assets are changed.
