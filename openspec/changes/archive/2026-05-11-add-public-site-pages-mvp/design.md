# Design: Add Public Site Pages MVP

## Overview

This change implements the first complete public-facing website experience for CBNV 2026. It should be functional, navigable and coherent, but not treated as final editorial polish.

It becomes the baseline for:

- `review-public-site-ui-ux-round-1`
- `produce-public-site-content-round-1`
- `verify-cross-page-content-consistency`

## Principles

### Use the design system

All pages should use shared layout partials, section headings, cards, badges, buttons and timeline primitives. Avoid one-off page styling unless necessary.

### Prefer CMS/domain data

Repeated facts such as event name, dates, venue, social links, FAPEMIG acknowledgement, program data and sponsors should come from CMS/domain models.

### Use sober placeholder copy

MVP copy can be provisional, but must not be misleading or inflated. Avoid “maior evento da América Latina”, “fronteira do conhecimento” and workshop claims unless later approved.

### Make review easy

The implementation should expose clear sections and data-driven blocks so the UI/UX and content review proposals can audit them without structural refactoring.

## Page Structure Recommendations

### Home

Recommended sections:

1. Hero: event name, theme, dates, venue, format and CTAs.
2. Quick facts.
3. Program preview.
4. Latest announcements/news.
5. Submissions/registration CTA area.
6. Supporting entities.
7. Footer.

### About

Recommended sections:

1. What CBNV is.
2. 2026 theme context.
3. Institutions and organization.
4. Committee/team area if data exists.
5. Local/access summary or link to Contact.

Avoid duplicating a generic “O que esperar?” block if Home already uses that concept.

### Program

Use day-based layout:

- day/date heading;
- session card;
- time range;
- activity badge;
- talk list;
- speaker display only when visible/confirmed;
- pending participant text where appropriate.

### Speakers

Use responsive cards/grid. Hidden speakers must not appear.

### Submissions

Explain public rules and status. Do not implement actual workflow.

### Registration

Use status-aware external-link pattern. If unavailable, render “em breve”.

### Sponsorship

Group sponsors/supporting entities by tier/category where available.

### Previous editions

Frame as archive/history.

### Contact

Make current venue and contact channels easy to find.

## Template Strategy

Use Wagtail naming conventions already present in the project. Likely paths include:

```text
templates/pages/home_page.html
templates/pages/about_page.html
templates/pages/program_page.html
templates/pages/speakers_page.html
templates/pages/submissions_page.html
templates/pages/registration_page.html
templates/pages/sponsors_page.html
templates/pages/previous_editions_page.html
templates/pages/contact_page.html
```

Actual implementation may adapt paths to current project conventions.

## Context Strategy

- Home: settings, featured announcements, program preview, supporting entities.
- Program: published sessions, visible/confirmed talks, prefetched speakers.
- Speakers: visible speakers only.
- Sponsorship: active sponsor tiers/entities.
- Contact: settings contacts and venue fields.
- Registration: settings registration link/status.
- Submissions: status and public explanation.

Avoid heavy repeated queries when prefetching is simple.

## Accessibility Strategy

1. Use semantic landmarks from base layout.
2. Keep a single `h1` per page.
3. Keep heading levels ordered.
4. Do not make card content available only on hover.
5. Ensure CTA focus is visible.
6. Ensure schedule is readable without horizontal scroll.
7. Ensure status badges include text.

## Testing Strategy

Minimum tests:

1. required pages render;
2. Home context includes settings/news/program/sponsors where available;
3. Program excludes draft/cancelled sessions;
4. Speakers excludes hidden speakers;
5. Registration coming-soon state does not render broken URL;
6. Submissions page includes initial-video-not-required text;
7. Contact renders current venue/address from settings.
