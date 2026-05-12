# Design: Review Public Site UI/UX Round 1

## Overview

This is a diagnostic review proposal. It should not produce final copy or implement fixes. Its function is to determine whether the public-site MVP has a sound structure before content production and polish work begin.

The review must be concrete enough that the next proposals can act on it without re-litigating page structure.

## Why this comes before content production

Final content should not be written for sections that may be removed, merged or moved. This review decides whether the current public-site structure is good enough to receive polished content.

The review still considers content. It should identify where content is missing, weak, redundant or misleading. But it should not write final copy.

## Review Philosophy

### 1. Diagnose structure before rewriting

Focus on information architecture, flow, hierarchy and section purpose.

### 2. Evaluate content placement, not final prose

Ask whether content belongs in that location, what job it should perform and whether the section is needed.

### 3. Prioritize user journeys

Review from the perspective of visitors, authors, participants, sponsors and returning users.

### 4. Prefer actionable findings

Every issue should include a recommendation and target follow-up proposal.

### 5. Avoid implementation creep

Do not fix the site during review.

## Review Evidence

The report should record evidence:

- URL or local command used;
- commit SHA;
- branch name;
- review date;
- viewport sizes;
- browser;
- seeded data state;
- screenshots if useful.

Recommended viewport matrix:

```text
mobile: 390x844
large mobile: 430x932
tablet: 768x1024
desktop: 1366x768
wide desktop: 1440x1000 or larger
```

## Recommended Report Structure

```markdown
# Public Site UI/UX Review — Round 1

## Metadata

- Change ID:
- Reviewer:
- Date:
- Branch:
- Commit:
- Environment:
- Browser:
- Viewports:
- Seed data state:

## Executive Summary

## Top Findings

## User Journey Review

### General visitor
### Potential author
### Potential participant
### Potential sponsor/supporter
### Returning visitor

## Page-by-Page Review

### Home
### About
### Program
### Speakers
### Submissions
### Registration
### Sponsorship
### Previous Editions
### Contact

## Accessibility Observations

## Responsive Observations

## Content Placement and Copy Risks

## Section Decisions

| Section | Decision | Rationale | Target proposal |
|---|---|---|---|

## Backlog Summary

## Risks for Next Proposal

## Recommended Next Steps
```

## Recommended Backlog Structure

```markdown
# Public Site UI/UX Review — Round 1 Backlog

| ID | Severity | Category | Page/Section | Finding | Rationale | Recommendation | Target proposal | Status |
|---|---|---|---|---|---|---|---|---|
```

Issue IDs should be stable, for example:

```text
UXR1-001
UXR1-002
UXR1-003
```

## Review Heuristics

### Home

Check whether a first-time visitor can identify in five seconds:

1. what the event is;
2. when it happens;
3. where it happens;
4. what the theme is;
5. what the next useful action is.

### About

Check whether the page answers:

1. what CBNV is;
2. why the 2026 edition exists;
3. what the theme means in this context;
4. who organizes/supports it;
5. where it happens.

### Program

Check whether users can scan days, times, activity type, session title and confirmed vs pending participants.

### Submissions

Check whether authors can understand whether submissions are open, what they need initially, that video is not initially required, what happens after approval and where to act next.

### Registration

Check whether users understand registration is external, may not be open yet, certificates and QR/check-in are outside this site, and there is no broken CTA.

### Sponsorship

Check whether a supporter knows why support matters, what contact path to use and which institutions are partners/supporters vs sponsors.

### Contact

Check whether the current venue and contact channels are obvious.

## Accessibility Heuristics

This is not a full WCAG audit, but must identify obvious issues:

- heading order;
- keyboard navigation;
- focus visibility;
- contrast concerns;
- icon-only links;
- link purpose;
- card semantics;
- schedule readability;
- image alt-text risks;
- mobile navigation accessibility.

## Content Handoff

The review must produce a content handoff section for `produce-public-site-content-round-1`.

That section should include:

1. pages needing new copy;
2. sections needing shorter copy;
3. sections needing longer explanatory copy;
4. claims to avoid;
5. terminology decisions;
6. content gaps that require factual input;
7. content that should remain provisional.

## Consistency Handoff

The review must produce a consistency handoff section for `verify-cross-page-content-consistency`.

That section should list repeated facts to check, repeated labels to standardize, duplicated sections, conflicting CTAs and cross-page terminology risks.

## Implementation Handoff

The review must produce an implementation handoff section for `implement-public-site-polish-round-1`.

That section should list layout/visual fixes that are not copywriting tasks.
