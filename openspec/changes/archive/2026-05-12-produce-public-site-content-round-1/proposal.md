# Proposal: Produce Public Site Content Round 1

## Change ID

`produce-public-site-content-round-1`

## Linked issue

GitHub issue: `OpenSpec: produce public site content round 1`  
Expected issue number: `#8`

## Problem

The public-site MVP provides page structure and navigable public routes. The UI/UX review identifies which sections should be kept, moved, merged, removed or rewritten. The next step is to produce coherent public-facing content that fits the approved structure and supports the key visitor journeys.

Without this change, the website may remain visually navigable but editorially weak: generic hero copy, shallow About content, unclear submission/registration explanations, inconsistent “coming soon” states, repeated sections, unsupported claims or copy that does not match the actual program and requirements.

## Proposed Change

Produce the first formal content round for the CBNV 2026 public website.

This change should write and document page-level copy, microcopy, CTA labels, status messages and editorial guidelines. It may also update CMS seed data, fixtures or safe editable content fields if the project already has a defined mechanism for storing public copy.

This is a content-production change, not a layout-redesign change.

## Required Input

This proposal depends on:

1. `add-public-site-pages-mvp`
2. `review-public-site-ui-ux-round-1`
3. the current source-of-truth requirements document
4. canonical event content in CMS/settings
5. current program/speaker/venue data
6. current UI/UX review backlog

The content production pass should explicitly use:

```text
docs/reviews/public-site-ui-ux-round-1.md
docs/reviews/public-site-ui-ux-round-1-backlog.md
```

If those files do not exist yet, this change should not proceed beyond drafting.

## Required Output Documents

The content produced in this proposal SHALL be stored in `docs/content/`.

Required:

```text
docs/content/public-site-content-round-1.md
docs/content/public-site-copy-map-round-1.md
docs/content/public-site-editorial-guidelines.md
```

Optional but recommended:

```text
docs/content/public-site-content-decisions-round-1.md
docs/content/public-site-open-questions-round-1.md
```

## Goals

1. Replace generic or placeholder copy with coherent round-1 public copy.
2. Create a consistent editorial tone for the public site.
3. Improve Home and About content without overclaiming the event’s scale.
4. Clarify Submissions, Registration, Sponsorship and Contact pages.
5. Produce page-level copy that respects current data and pending states.
6. Produce microcopy for CTAs, badges and “em breve” states.
7. Create a copy map that tells implementers where each piece of content belongs.
8. Prepare content for `verify-cross-page-content-consistency`.

## Non-goals

This change SHALL NOT:

1. change the page information architecture unless the review explicitly requires a content-level decision;
2. implement major layout changes;
3. redesign components;
4. create new data models;
5. implement submissions, registration, payment, certificates, QR code or review workflows;
6. invent confirmed speakers, workshops, sponsors or partners;
7. scrape Wix or Notion as current sources of truth;
8. claim final legal/institutional approval of all text;
9. close consistency verification; that belongs to the next proposal.

## Editorial Positioning

The CBNV 2026 site should sound:

- scientific;
- clear;
- institutional;
- sober;
- welcoming;
- precise;
- modest about scale;
- transparent about what is confirmed vs pending.

It should not sound:

- inflated;
- generic;
- sales-heavy;
- startup-like;
- vague;
- sensational;
- overconfident about unconfirmed information.

## Mandatory Editorial Rules

The content SHALL:

1. use Brazilian Portuguese;
2. avoid claiming the event is the largest in Latin America;
3. avoid generic phrases like “fronteira do conhecimento” unless made specific and justified;
4. avoid saying there will be workshops unless the official program contains workshops;
5. distinguish confirmed information from pending information;
6. treat registration, certificates and QR/check-in as external to the site;
7. state that video is not required in the initial submission phase;
8. describe videos as links/YouTube playlist references, not files hosted by the website;
9. use current venue/address data only;
10. frame previous editions as archive/history, not current information;
11. use “em breve” states where links or details are unavailable;
12. avoid hardcoded old-edition facts.

## Page Scope

### Home

Produce copy for hero title/subtitle, short event description, primary CTAs, quick facts labels, program preview intro, announcements/latest news section, submissions/registration teaser, supporting entities intro and footer microcopy if applicable.

Home must quickly communicate what CBNV is, dates, location, theme and what the visitor can do next.

### About

Produce copy for what CBNV is, scientific/institutional context, 2026 theme framing, organization/support context, local/access summary if retained and committee/team intro if that section remains.

About should be more informative than Home and should not duplicate Home CTA sections unnecessarily.

### Program

Produce copy for program intro, provisional/updated-program note if needed, day/session intro labels, pending participant note, no-workshop correction if relevant and “program subject to update” microcopy if appropriate.

### Speakers

Produce copy for page intro, confirmed vs pending explanation if needed, empty state when no confirmed speakers are public and photo/bio fallback microcopy if needed.

### Submissions

Produce copy for page intro, submission status text, initial-submission requirements summary, explicit “video is not required initially” statement, final-materials explanation, modalities, “em breve” CTA/state and short FAQ-style clarifications if helpful.

### Registration

Produce copy for external registration explanation, coming-soon status, what is handled externally, certificates/check-in/QR external note, CTA labels and support/contact path.

### Sponsorship

Produce copy for sponsorship/support intro, why institutional support matters, contact path, sponsor/supporter terminology and display intro for supporting entities.

### Previous Editions

Produce copy for archive framing, explanation that prior editions are historical and links to proceedings/videos where available.

### Contact

Produce copy for general contact intro, venue/address label, map link label, contact categories and access note if content is known.

### Footer

Produce copy/microcopy for concise event identity, institutional acknowledgement, FAPEMIG acknowledgement, Instagram/YouTube labels and copyright.

## Copy Map

The proposal must produce a copy map with:

- page;
- section;
- content key or suggested field;
- proposed copy;
- source/rationale;
- target implementation location;
- status.

Example:

```text
Home | Hero subtitle | home.hero_subtitle | ... | requirements + UI review | CMS/HomePage.intro or template block | ready
```

## Implementation Strategy

Preferred order:

1. read UI/UX review report and backlog;
2. list all pages and sections that survived the review;
3. create content inventory;
4. write page-level copy;
5. write CTA/microcopy;
6. create editorial guidelines;
7. create copy map;
8. update CMS seed/fixtures/editable page fields only if the implementation path is already defined;
9. do not make unrelated layout changes.

If the system stores page copy in Wagtail page fields or seed commands, this proposal MAY update those values. If the system still stores some content in templates or static fallback files, this proposal MAY update text-only content, but must not perform structural template redesign.

## Acceptance Criteria

1. `docs/content/public-site-content-round-1.md` exists.
2. `docs/content/public-site-copy-map-round-1.md` exists.
3. `docs/content/public-site-editorial-guidelines.md` exists.
4. Home copy is no longer generic or inflated.
5. About copy is substantially more informative than the MVP placeholder.
6. Submissions copy explicitly states that video is not required initially.
7. Registration copy clearly states registration/certificates/QR are external.
8. Program copy does not mention workshops unless present in official program data.
9. Contact copy uses current CAD-1/UFMG venue/address data.
10. Previous Editions copy frames legacy content as archive/history.
11. Copy map identifies where each content block should be implemented.
12. Content gaps and open factual questions are documented.
13. The change passes `openspec validate produce-public-site-content-round-1 --strict`.
14. If implementation files are changed, relevant Django/npm checks pass.
