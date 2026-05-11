# Proposal: Add Public Site Pages MVP

## Change ID

`add-public-site-pages-mvp`

## Linked issue

GitHub issue: `OpenSpec: add public site pages MVP`  
Expected issue number: `#6`

## Problem

The project now has the foundation needed for a navigable public website: design-system/layout shells, core CMS content models, canonical event seed data, and program/speaker/venue models. The repository already includes `CoreSettings`, `SiteMenu`, `Announcement`, `Sponsor`, program models and several page models. The next step is to connect these pieces into the first complete public-site MVP.

Without this change, the project has models and content infrastructure but not a coherent public user journey for visitors, potential participants, authors, sponsors and institutional stakeholders.

## Proposed Change

Implement the main public pages of the CBNV 2026 website using Wagtail page types, Django templates, shared layout components, CMS settings, announcements, program models and supporting-entity/sponsor models.

The result should be navigable, responsive, accessible and ready for the next formal review cycle: UI/UX review, content production review and cross-page consistency verification.

## Goals

1. Implement a navigable public website MVP.
2. Reuse design-system/layout-shell components.
3. Consume `CoreSettings` and global CMS settings.
4. Consume news/announcements.
5. Consume `ProgramDay`, `ProgramSession`, `ProgramTalk` and `Speaker`.
6. Consume sponsor/supporting-entity models.
7. Render safe “em breve” states for unavailable external links.
8. Provide basic SEO metadata.
9. Avoid hardcoded repeated factual content.
10. Create a stable baseline for UI/UX and editorial review.

## Non-goals

This change SHALL NOT:

1. implement authenticated submission workflow;
2. implement author/reviewer/chair dashboards;
3. implement review, decision, proceedings or reports;
4. implement production deployment;
5. add a SPA or separate frontend app;
6. host videos directly;
7. implement payment, certificates or QR-code functionality;
8. claim final editorial polish is complete.

This change SHALL NOT remodel the organizing committee or expand `Speaker` into a generic person/team model. Committee/team modeling is deferred to a later proposal unless strictly required for MVP rendering.

## Required Pages

The public MVP SHALL include:

1. Home
2. About
3. Program
4. Speakers
5. Submissions
6. Registration
7. Sponsorship
8. Previous Editions
9. Contact

If some page classes already exist, this change SHOULD refine templates, context and navigation instead of duplicating models.

The implementation MUST add missing Wagtail page types needed for the public MVP, especially:

- `SpeakerIndexPage` or `SpeakersPage`
- `ContactPage`

Existing page types SHOULD be reused and refined rather than duplicated.

## Current Implementation Context

Use the existing implementation as the starting point:

- `CoreSettings` centralizes event identity, dates, venue fields, link statuses, social links and FAPEMIG fields.
- `SiteMenu` supports configurable menu items.
- `Announcement` exists for news/announcements.
- Several public page classes already exist in `pages.models`.
- Program models exist: `ProgramDay`, `ProgramSession`, `ProgramTalk`, `Speaker`.
- Sponsor models exist: `SponsorTier` and `Sponsor`.
- `templates/base.html` already loads fonts/CSS and defines `main#main-content`.

Avoid creating parallel models that duplicate these responsibilities.

## Page Requirements

### Home

Home SHALL render event identity, theme, dates, venue/location, format, primary CTAs, featured announcements, program preview, submission/registration states and supporting entities.

### About

About SHALL provide institutional/scientific context, 2026 theme framing, organizations/supporting entities and committee/team content when available.

### Program

Program SHALL render published program sessions grouped by day, with time ranges, activity labels, visible/confirmed talks and safe handling of pending participants.

### Speakers

Speakers SHALL render public speaker data while hiding hidden speakers and avoiding representation of pending speakers as confirmed.

### Submissions

Submissions SHALL explain the public submission process and explicitly state that video is not required in the initial submission phase. It SHALL NOT implement the submission workflow.

### Registration

Registration SHALL explain external registration, use registration link/status from settings and render “em breve” when unavailable.

### Sponsorship

Sponsorship SHALL render sponsorship/support information and active supporting entities grouped by tier/category when available.

### Previous Editions

Previous Editions SHALL present archive/history content only and must not override current 2026 event facts.

### Contact

Contact SHALL render public contact channels and current CAD-1/UFMG venue/address/map data from settings.

## Data Rules

1. Event identity and global links come from `CoreSettings` or the documented settings mechanism.
2. Announcements/news come from CMS models.
3. Program data comes from program models.
4. Sponsors/supporting entities come from sponsor models.
5. Unknown links must not render as broken `#` links.
6. Pending speaker/participant status must not render as confirmed.
7. Previous-edition content must not appear as current 2026 data.

## Accessibility Requirements

1. Preserve semantic landmarks.
2. Use one clear `h1` per page.
3. Keep heading hierarchy logical.
4. CTAs must have accessible names.
5. Icon-only links must have labels.
6. Program schedule must remain readable on mobile.
7. Keyboard users must be able to navigate header, CTAs and links.
8. Status badges must include text and not rely only on color.

## Acceptance Criteria

1. Public site is navigable from Home to all required pages.
2. Pages use Wagtail/CMS/domain models instead of scattered hardcoded data.
3. Home communicates theme, dates, venue, CTAs, program preview and announcements.
4. Program renders day-based schedule from program models.
5. Speakers page renders visible speaker data and excludes hidden speakers.
6. Registration handles external link and “em breve” state correctly.
7. Submissions states that video is not required initially.
8. Contact uses current CAD-1/UFMG venue data.
9. Header/footer are consistent across pages.
10. Basic SEO metadata is available.
11. Validation commands pass.
12. No authenticated submission/review workflow is implemented.
