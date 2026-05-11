# Tasks: Add Public Site Pages MVP

## OpenSpec

- [x] Create `openspec/changes/add-public-site-pages-mvp/`.
- [x] Add `proposal.md`.
- [x] Add `design.md`.
- [x] Add `tasks.md`.
- [x] Add delta spec `specs/public-site/spec.md`.
- [x] Add delta spec `specs/content/spec.md`.
- [x] Add delta spec `specs/program/spec.md`.
- [x] Add delta spec `specs/cms/spec.md`.
- [x] Add delta spec `specs/accessibility/spec.md`.
- [x] Run `openspec validate add-public-site-pages-mvp --strict`.

## Pre-implementation audit

- [x] Confirm prerequisite proposals are complete.
- [x] Review current `pages.models`.
- [x] Review current templates.
- [x] Identify missing page types, especially Speakers and Contact.
- [x] Confirm current navigation/menu approach.

## Wagtail page types

- [x] Reuse existing page types where implemented.
- [x] Add missing speakers page type if absent.
- [x] Add missing contact page type if absent.
- [x] Confirm parent/subpage rules allow required public navigation.
- [x] Avoid fields duplicating `CoreSettings`.

## Templates

- [x] Implement Home template.
- [x] Implement About template.
- [x] Implement Program template.
- [x] Implement Speakers template.
- [x] Implement Submissions template.
- [x] Implement Registration template.
- [x] Implement Sponsorship template.
- [x] Implement Previous Editions template.
- [x] Implement Contact template.
- [x] Reuse design-system partials consistently.

## Home

- [x] Render event name/theme/dates/location/format from settings.
- [x] Render primary CTAs.
- [x] Render quick facts.
- [x] Render featured announcements/news.
- [x] Render program preview.
- [x] Render submissions/registration status.
- [x] Render supporting entities.
- [x] Avoid exaggerated claims.

## About

- [x] Render institutional/scientific description.
- [x] Render 2026 theme context.
- [x] Render organizing/supporting institutions.
- [x] Render committee/team section only if data source exists.
- [x] Avoid redundant or inconsistent “O que esperar?” content.

## Program

- [x] Render days.
- [x] Render published sessions only.
- [x] Render time ranges.
- [x] Render activity badges.
- [x] Render confirmed/visible talks.
- [x] Handle pending participants safely.
- [x] Ensure mobile-friendly layout.

## Speakers

- [x] Render confirmed/visible speakers.
- [x] Exclude hidden speakers.
- [x] Provide photo fallback.
- [x] Show institution/country when available.
- [x] Link to related talks/sessions if feasible.

## Submissions

- [x] Render status.
- [x] Explain initial submission does not require video.
- [x] Explain possible final modalities.
- [x] Render CTA or coming-soon state.
- [x] Do not implement submission workflow.

## Registration

- [x] Render external-registration explanation.
- [x] Use `registration_status`.
- [x] Render “em breve” if unavailable.
- [x] Do not imply internal payment/certificate/QR implementation.

## Sponsorship

- [x] Render sponsor/supporting entity groups.
- [x] Render sponsorship contact path if available.
- [x] Avoid unconfirmed sponsorship claims.

## Previous editions

- [x] Render existing edition/fallback data.
- [x] Clearly label content as archive/history.
- [x] Link to proceedings/videos only when available.

## Contact

- [x] Render general contact email if available.
- [x] Render submissions contact if available.
- [x] Render sponsorship contact if available.
- [x] Render current venue/address/map link.
- [x] Do not render inherited previous-edition venue.

## Page model gaps

- [x] Add `SpeakerIndexPage` or `SpeakersPage` if absent.
- [x] Add `ContactPage` if absent.
- [x] Add both to `HomePage.subpage_types` or the appropriate Wagtail page hierarchy.
- [x] Ensure main navigation can link to both pages.

## Home/About data source cleanup

- [x] Refactor Home to prefer `CoreSettings`, `Announcement`, `Sponsor`, and program models.
- [x] Refactor About to prefer `CoreSettings` and Sponsor/supporting-entity models.
- [x] Keep `pages.content` constants only as temporary fallback if needed.
- [x] Do not introduce new hardcoded repeated event facts.

## Committee/team data

- [x] Do not add `is_committee` or `is_speaker` flags to `Speaker` in this proposal.
- [x] If structured committee modeling is needed, document a follow-up proposal.

## Navigation and SEO

- [x] Ensure main navigation links to required pages.
- [x] Ensure mobile navigation works.
- [x] Add breadcrumbs where appropriate.
- [x] Add meaningful page titles.
- [x] Add search descriptions or defaults.

## Accessibility

- [x] Each page has a single clear `h1`.
- [x] Heading levels are ordered.
- [x] CTAs have accessible names.
- [x] Cards do not hide content behind hover-only behavior.
- [x] Status badges include text.
- [x] Program schedule remains readable on mobile.

## Tests and validation

- [x] Add smoke tests for public page rendering.
- [x] Add Home context test.
- [x] Add Program filtering test.
- [x] Add Speaker hidden-status filtering test.
- [x] Add Registration coming-soon test.
- [x] Add Contact venue/address test if ContactPage exists.
- [x] Run `openspec validate add-public-site-pages-mvp --strict`.
- [x] Run `npm run build`.
- [x] Run `uv run python manage.py check`.
- [x] Run `uv run python manage.py makemigrations --check --dry-run`.
- [x] Run `uv run pytest`.

## PR checklist

- [x] Branch is `change/add-public-site-pages-mvp`.
- [ ] PR title starts with `[add-public-site-pages-mvp]`.
- [ ] PR body includes `Closes #6`.
- [x] No authenticated submissions/review workflows were implemented.
