# Proposal: Review Public Site UI/UX Round 1

## Change ID

`review-public-site-ui-ux-round-1`

## Linked issue

GitHub issue: `OpenSpec: review public site UI/UX round 1`
Expected issue number: `#7`

## Problem

The public-site MVP establishes the first navigable version of the CBNV 2026 website. Before producing polished public copy or applying visual refinements, the team needs a structured diagnostic review of the implemented experience.

Without this review, later proposals may spend effort writing copy for sections that should be removed, polishing layouts that should be reorganized, or fixing inconsistencies after content has already been inserted.

This proposal exists to evaluate the public MVP as a product experience: structure, usability, navigation, layout, accessibility, responsiveness, content placement, information hierarchy and readiness for the next content-production pass.

## Proposed Change

Perform a formal UI/UX review of the implemented public site and store the results in versioned documentation.

This is a diagnostic change. It should produce review artifacts and a prioritized backlog. It should not implement UI changes, rewrite final copy, remodel data, or make page-level fixes. Those changes belong to later proposals.

## Required Output Documents

Yes, review results SHALL be stored in `docs/`.

The implementation of this proposal MUST create:

```text
docs/reviews/public-site-ui-ux-round-1.md
docs/reviews/public-site-ui-ux-round-1-backlog.md
```

Optional but recommended:

```text
docs/reviews/public-site-ui-ux-round-1-checklist.md
```

If screenshots are useful but large, do not commit large binary files unless repository policy allows it. Instead, record screenshot filenames, viewport notes or external/local artifact paths in the report.

## Goals

1. Review the implemented public-site MVP before content production.
2. Identify structural, navigational, visual, accessibility and responsive issues.
3. Identify copy/content gaps without writing final copy.
4. Decide which sections should be kept, removed, merged, moved or rewritten.
5. Produce a prioritized backlog for subsequent proposals.
6. Provide direct input to:
   - `produce-public-site-content-round-1`
   - `verify-cross-page-content-consistency`
   - `implement-public-site-polish-round-1`

## Non-goals

This change SHALL NOT:

1. rewrite final public copy;
2. implement layout fixes;
3. change CSS/components/templates except for review documentation artifacts;
4. change models, migrations or CMS schemas;
5. add new pages;
6. modify seeded canonical data;
7. implement accessibility fixes;
8. implement content consistency fixes;
9. create authenticated flows;
10. archive unrelated changes.

## Review Inputs

The review SHALL use, at minimum:

1. the current public-site MVP implementation;
2. the current source-of-truth requirements document;
3. `docs/CBNV2026_OpenSpec_Plano_Implementacao_v2.md`;
4. design-system documentation if available;
5. canonical event content seeded in the CMS;
6. current program/speaker/venue data;
7. known user feedback and previously identified UI/content concerns.

If a local running site is used, record:

- commit SHA;
- branch name;
- date/time of review;
- viewport sizes tested;
- browser(s);
- whether seeded data was loaded.

## Review Method

The review must inspect the public site at multiple levels:

1. user journeys;
2. information architecture;
3. page-by-page layout;
4. content placement;
5. navigation and CTAs;
6. responsiveness;
7. accessibility baseline;
8. visual hierarchy;
9. consistency of repeated elements;
10. readiness for content production.

The reviewer should treat the current content as provisional. The question is not whether every sentence is final, but whether the page structure is sound enough to receive final content.

## Core User Journeys

The review SHALL evaluate these journeys:

### General visitor

1. lands on Home;
2. understands what CBNV 2026 is;
3. identifies date, location and theme;
4. finds program;
5. finds registration status;
6. finds contact/location.

### Potential author

1. lands on Home or Submissions;
2. understands whether submissions are open;
3. understands that initial submission does not require video;
4. understands future modalities;
5. finds next action or coming-soon state.

### Potential participant

1. finds dates/location quickly;
2. reviews program;
3. understands registration is external;
4. finds venue/access information.

### Potential sponsor/supporter

1. finds sponsorship page;
2. understands support opportunity at a high level;
3. finds contact path.

### Returning visitor

1. finds latest news/announcements;
2. finds program updates;
3. distinguishes current content from previous-edition archive.

## Page Review Scope

### Home

Review hero clarity, event identity visibility, date/location/theme visibility, primary CTA hierarchy, latest-news/announcement placement, the usefulness of the “Híbrido” card, venue card content, program preview, “O que esperar?” placement, partner/supporting-entity grid, and footer redundancy.

### About

Review institutional copy depth, relationship with Home content, redundancy of “O que esperar?”, heading hierarchy, committee/team presentation, organization/support sections, local/access section, and whether fallback/static data should be replaced by CMS data.

### Program

Review day-based structure, session readability, time hierarchy, activity labels, pending participant handling, mobile timeline/card layout, desktop scanability, and alignment between Home program preview and full Program page.

### Speakers

Review page reachability, card/grid readability, confirmed/hidden/pending speaker handling, photo fallback, institutional affiliation display, and relationship to Program page.

### Submissions

Review submission status clarity, visibility of the no-video-in-initial-submission rule, final modality explanation, CTA/coming-soon state, and whether the page avoids overpromising workflow functionality.

### Registration

Review external registration explanation, coming-soon state, CTA clarity, and whether the page avoids implying internal payment/certificate/QR functionality.

### Sponsorship

Review usefulness of copy, contact path, sponsor/supporting-entity grouping, and distinction between sponsor, partner, support and funding agency.

### Previous Editions

Review archive framing, separation from current 2026 facts, and discoverability from navigation.

### Contact

Review current CAD-1/UFMG address visibility, map/link quality, contact email clarity, separation of general/submission/sponsorship contacts, and absence of previous-edition location data.

## Severity Scale

Each issue in the backlog SHALL use:

- `P0` — blocks trust, correctness or critical navigation;
- `P1` — significantly harms usability, comprehension, accessibility or consistency;
- `P2` — moderate issue, should be fixed before public launch;
- `P3` — polish, nice-to-have or later refinement.

## Issue Categories

Each finding SHALL be categorized as one or more of:

- `information-architecture`
- `navigation`
- `layout`
- `visual-hierarchy`
- `responsiveness`
- `accessibility`
- `content-placement`
- `copy-gap`
- `copy-risk`
- `consistency`
- `cms-data-source`
- `performance-risk`
- `trust-risk`

## Required Decisions

The review MUST produce decisions for major sections using one of:

- `keep`
- `remove`
- `merge`
- `move`
- `rewrite`
- `defer`
- `needs-data`

Examples:

- Home “Híbrido” card: keep/remove/replace?
- Home latest news: where should it appear?
- Home/About “O que esperar?” duplication: merge/move/remove?
- About committee section: keep as fallback or defer until structured committee model?
- Footer long event text: keep/remove/simplify?
- Partner/support grids: consolidate or separate?

## Output Format

### `docs/reviews/public-site-ui-ux-round-1.md`

The main report SHALL include:

1. title and metadata;
2. reviewed commit/branch;
3. environment and viewport matrix;
4. executive summary;
5. user-journey findings;
6. page-by-page findings;
7. accessibility observations;
8. responsive behavior observations;
9. content-placement observations;
10. section decisions;
11. risks for later content production;
12. recommended next steps.

### `docs/reviews/public-site-ui-ux-round-1-backlog.md`

The backlog SHALL include a table with:

- ID;
- severity;
- category;
- page/section;
- finding;
- rationale;
- recommendation;
- proposed target proposal;
- status.

Suggested target proposals:

- `produce-public-site-content-round-1`
- `verify-cross-page-content-consistency`
- `implement-public-site-polish-round-1`
- future model/content proposal, if outside current plan.

## Acceptance Criteria

1. Review report exists in `docs/reviews/public-site-ui-ux-round-1.md`.
2. Prioritized backlog exists in `docs/reviews/public-site-ui-ux-round-1-backlog.md`.
3. Review covers all required public pages.
4. Review covers core user journeys.
5. Review classifies findings by severity and category.
6. Review includes keep/remove/merge/move/rewrite/defer decisions for major ambiguous sections.
7. Review identifies content gaps for the next content-production proposal.
8. Review does not implement UI/layout/content fixes.
9. Validation passes:
   - `openspec validate review-public-site-ui-ux-round-1 --strict`
10. If code is not changed, Django/npm checks are optional but recommended as sanity checks.
