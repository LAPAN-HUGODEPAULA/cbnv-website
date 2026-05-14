# Design: Verify Cross-Page Content Consistency

## Overview

This change is a verification and documentation pass. It evaluates whether the implemented system communicates one coherent set of facts, statuses, labels and workflow expectations across public pages, dashboards, notifications, proceedings, videos, reports and exports.

It does not perform broad implementation work. Its main output is actionable evidence: matrices, inventories, status maps and a prioritized backlog.

## Review Principles

### 1. Treat consistency as product safety

Incorrect dates, venues, statuses, publication states or privacy-bearing export fields can cause practical harm. The audit must prioritize correctness.

### 2. Separate canonical truth from presentation

The same internal state may have different labels for different personas. That is acceptable when intentional. The audit must document the mapping instead of forcing all labels to be identical.

### 3. Test fallback and real-data paths

Many consistency problems appear only when optional data is missing or when real workflow data exists. The audit must use both empty/default and populated/custom profiles.

### 4. Include non-visual content

Alt text, ARIA labels, form labels, icon-only labels and export headers are user-facing content. They must be audited.

### 5. Route findings instead of sprawling

The audit must route corrections to the proper follow-up proposal. It must not become a large mixed implementation PR.

## Required Matrices

### Cross-surface consistency matrix

Rows represent canonical facts and repeated labels. Columns represent surfaces: public pages, author dashboard, reviewer dashboard, chair dashboard, submission forms, review screens, decision screens, final material screens, proceedings, video gallery, notifications, reports/exports, SEO and non-visual content.

### Persona status map

Rows represent internal workflow states. Columns represent public visitor, author, reviewer, chair/scientific committee and admin/staff.

### Notification trigger matrix

Rows represent notification types. Columns include trigger, pre-state, post-state, recipient, subject terminology, body terminology, dashboard state after trigger and duplicate-send risk.

### Legacy ghost facts inventory

Rows include legacy fact, pattern, allowed archive context, forbidden current context, result and action.

### Automation candidate matrix

Rows include check name, risk addressed, suggested mechanism, current feasibility, target proposal and priority.

## Output Document Templates

### Consistency report

```markdown
# Cross-Page Content Consistency Review - Round 1

## Metadata
## Data profiles
## Sources reviewed
## Executive summary
## P0/P1 findings
## Domain findings
## Persona status summary
## Notification trigger summary
## Translation and terminology findings
## Non-visual content findings
## Legacy contamination findings
## Reports/exports/privacy findings
## Automation candidates summary
## Handoff
```

### Consistency matrix

```markdown
| Domain | Canonical source | Expected value/rule | Public pages | Author dashboard | Reviewer dashboard | Chair dashboard | Notifications | Reports/exports | Non-visual content | Status |
|---|---|---|---|---|---|---|---|---|---|---|
```

### Backlog

```markdown
| ID | Severity | Category | Surface | Persona | Data profile | Expected | Observed | Recommendation | Target proposal | Status |
|---|---|---|---|---|---|---|---|---|---|---|
```

### Persona status map

```markdown
| Internal state | Public visitor | Author | Reviewer | Chair | Admin/staff | Intended asymmetry? | Notes |
|---|---|---|---|---|---|---|---|
```

### Legacy inventory

```markdown
| Legacy fact | Pattern | Allowed context | Forbidden context | Found? | Action |
|---|---|---|---|---|---|
```

### Automation candidates

```markdown
| Check | Risk | Suggested mechanism | Priority | Target proposal |
|---|---|---|---|---|
```

## Boundary

This change may add documentation and small smoke checks if low-risk. It must not apply broad fixes to templates, models, dashboards, notifications or exports.
