# Proposal: Verify Cross-Page Content Consistency

## Change ID

`verify-cross-page-content-consistency`

## Why

The repository now contains more than the public-site MVP. It includes public pages, central event settings, account/profile dashboards, author submissions, review and decision workflows, final materials, proceedings, video resources, notifications, reports, exports and indicators.

That wider surface creates consistency risk. The same fact, status, instruction or label can now appear in public pages, author dashboards, reviewer dashboards, chair dashboards, forms, e-mails, reports, exports, proceedings, video gallery pages, SEO metadata and non-visual labels. A mismatch can mislead users, expose private information, cause premature workflow actions, or let previous-edition facts leak into the current CBNV 2026 experience.

This change creates a structured verification pass for cross-page and cross-workflow consistency after the major submission, review, final-materials, proceedings, videos and reporting modules have been implemented.

## What Changes

This change adds a verification framework, not a broad implementation pass.

It MUST produce review documents, matrices, inventories and a prioritized correction backlog. It MUST NOT become a mixed feature/polish change.

The verification MUST cover:

1. canonical event facts from central settings;
2. public pages and SEO metadata;
3. author, reviewer and chair dashboards;
4. submission, review, decision, final-material and proceedings workflows;
5. notification copy and notification triggers;
6. video URLs and public video-resource promotion;
7. report/export/indicator labels and privacy boundaries;
8. translation and terminology consistency;
9. non-visual content such as alt text and ARIA labels;
10. legacy ghost facts from previous editions;
11. candidates for automated consistency checks.

## OpenSpec Delta Scope

The delta specs in this change define verification requirements. They do not define broad new product behavior.

Findings discovered during the audit MUST be recorded in review documents and routed to the appropriate implementation proposal unless a correction is trivial, low-risk and explicitly documented.

## Required Output Documents

The change MUST create or update:

```text
docs/reviews/public-site-content-consistency-round-1.md
docs/reviews/public-site-content-consistency-matrix-round-1.md
docs/reviews/public-site-content-consistency-backlog-round-1.md
docs/reviews/persona-status-map-round-1.md
docs/reviews/legacy-ghost-facts-inventory-round-1.md
docs/reviews/consistency-automation-candidates-round-1.md
docs/reviews/notification-trigger-consistency-round-1.md
```

Optional supporting outputs:

```text
docs/reviews/non-visual-content-consistency-round-1.md
docs/reviews/translation-terminology-consistency-round-1.md
```

## Required Data Profiles

The audit MUST use at least two data profiles.

### Empty/default profile

This profile MUST test fallback behavior:

- default or minimally configured site settings;
- missing optional links;
- missing optional logos/images;
- no or minimal announcements;
- no confirmed speakers where applicable;
- no or minimal workflow data.

### Populated/custom profile

This profile MUST test real workflow behavior:

- current CBNV 2026 event facts;
- customized central settings;
- submissions in multiple workflow states;
- review assignments and decisions;
- final materials with and without publication authorization;
- proceedings-ready or published items;
- video URLs and public video resources;
- report/export data;
- sponsor/supporting-entity data.

Each finding MUST record which profile exposed the issue.

## Persona Status Map

The audit MUST produce a persona status map comparing internal workflow states with labels shown to:

- public visitors;
- authors;
- reviewers;
- chair/scientific committee users;
- admin/staff users.

The map MUST cover submission, review, decision, final-material, proceedings, notification and report/export status labels. Different labels are acceptable only when the asymmetry is intentional, documented and not misleading.

## Legacy Ghost Facts Inventory

The audit MUST create an inventory of previous-edition facts that must not appear as current CBNV 2026 content. This includes old dates, venues, addresses, themes, sponsors, program/workshop references, registration links, submission links, videos and proceedings links.

Legacy facts MAY appear only in archive or previous-edition contexts.

## Notification Trigger Consistency

The audit MUST verify not only notification copy, but also notification timing. For each notification type, the audit MUST check triggering event, expected recipient, state before sending, state after sending, dashboard state after sending, subject/body terminology and duplicate-send risk.

## Automated Consistency Checks

The audit MUST identify checks that can be automated. Examples include canonical event facts in metadata, absence of legacy dates outside archive contexts, status-label assertions, e-mail-template variable use, CTA link-state checks and protected-file URL checks in public pages or exports.

Automation does not need to be fully implemented in this change, but candidates MUST be documented and prioritized.

## Finding Severity

Every actionable finding MUST use one severity:

- `P0` - factual error, privacy leak, trust-breaking contradiction or critical workflow misinstruction;
- `P1` - significant inconsistency likely to confuse users or create support burden;
- `P2` - moderate inconsistency that should be corrected before launch;
- `P3` - wording polish or low-risk standardization.

## Finding Categories

Findings MUST use one or more categories:

- `fact-mismatch`
- `label-mismatch`
- `status-mismatch`
- `persona-status-mismatch`
- `date-mismatch`
- `venue-mismatch`
- `workflow-trigger-mismatch`
- `notification-mismatch`
- `program-mismatch`
- `speaker-status-mismatch`
- `cta-mismatch`
- `entity-taxonomy-mismatch`
- `legacy-contamination`
- `duplicate-content`
- `copy-tone-drift`
- `cms-source-mismatch`
- `translation-mismatch`
- `non-visual-content-mismatch`
- `accessibility-label-mismatch`
- `export-header-mismatch`
- `privacy-risk`
- `automation-candidate`

## Correction Routing

Findings MUST be routed to an appropriate target:

- copy correction;
- template rendering correction;
- domain/model correction;
- workflow trigger correction;
- notification correction;
- export/report correction;
- accessibility correction;
- unresolved factual question.

## Acceptance Criteria

1. Required review documents exist.
2. The audit covers public pages and implemented workflow surfaces.
3. The audit uses empty/default and populated/custom data profiles.
4. Canonical event facts are checked across pages, dashboards, notifications and exports.
5. Submission, review, decision, final-material and proceedings statuses are mapped by persona.
6. Translation and terminology consistency is checked.
7. Non-visual content consistency is checked.
8. Legacy ghost facts are inventoried and searched.
9. Notification trigger consistency is checked.
10. Reports, exports and indicators are checked for terminology, privacy and protected-file exposure.
11. Findings include severity, category, expected value, observed value, data profile, recommendation and target proposal.
12. Automation candidates are documented.
13. The change passes:

```bash
openspec validate verify-cross-page-content-consistency --strict
```
