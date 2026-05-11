# Tasks: Add Public Site Pages MVP

## OpenSpec

- [ ] Create `openspec/changes/add-public-site-pages-mvp/`.
- [ ] Add `proposal.md`.
- [ ] Add `design.md`.
- [ ] Add `tasks.md`.
- [ ] Add delta spec `specs/public-site/spec.md`.
- [ ] Add delta spec `specs/content/spec.md`.
- [ ] Add delta spec `specs/program/spec.md`.
- [ ] Add delta spec `specs/cms/spec.md`.
- [ ] Add delta spec `specs/accessibility/spec.md`.
- [ ] Run `openspec validate add-public-site-pages-mvp --strict`.

## Pre-implementation audit

- [ ] Confirm prerequisite proposals are complete.
- [ ] Review current `pages.models`.
- [ ] Review current templates.
- [ ] Identify missing page types, especially Speakers and Contact.
- [ ] Confirm current navigation/menu approach.

## Wagtail page types

- [ ] Reuse existing page types where implemented.
- [ ] Add missing speakers page type if absent.
- [ ] Add missing contact page type if absent.
- [ ] Confirm parent/subpage rules allow required public navigation.
- [ ] Avoid fields duplicating `CoreSettings`.

## Templates

- [ ] Implement Home template.
- [ ] Implement About template.
- [ ] Implement Program template.
- [ ] Implement Speakers template.
- [ ] Implement Submissions template.
- [ ] Implement Registration template.
- [ ] Implement Sponsorship template.
- [ ] Implement Previous Editions template.
- [ ] Implement Contact template.
- [ ] Reuse design-system partials consistently.

## Home

- [ ] Render event name/theme/dates/location/format from settings.
- [ ] Render primary CTAs.
- [ ] Render quick facts.
- [ ] Render featured announcements/news.
- [ ] Render program preview.
- [ ] Render submissions/registration status.
- [ ] Render supporting entities.
- [ ] Avoid exaggerated claims.

## About

- [ ] Render institutional/scientific description.
- [ ] Render 2026 theme context.
- [ ] Render organizing/supporting institutions.
- [ ] Render committee/team section only if data source exists.
- [ ] Avoid redundant or inconsistent “O que esperar?” content.

## Program

- [ ] Render days.
- [ ] Render published sessions only.
- [ ] Render time ranges.
- [ ] Render activity badges.
- [ ] Render confirmed/visible talks.
- [ ] Handle pending participants safely.
- [ ] Ensure mobile-friendly layout.

## Speakers

- [ ] Render confirmed/visible speakers.
- [ ] Exclude hidden speakers.
- [ ] Provide photo fallback.
- [ ] Show institution/country when available.
- [ ] Link to related talks/sessions if feasible.

## Submissions

- [ ] Render status.
- [ ] Explain initial submission does not require video.
- [ ] Explain possible final modalities.
- [ ] Render CTA or coming-soon state.
- [ ] Do not implement submission workflow.

## Registration

- [ ] Render external-registration explanation.
- [ ] Use `registration_status`.
- [ ] Render “em breve” if unavailable.
- [ ] Do not imply internal payment/certificate/QR implementation.

## Sponsorship

- [ ] Render sponsor/supporting entity groups.
- [ ] Render sponsorship contact path if available.
- [ ] Avoid unconfirmed sponsorship claims.

## Previous editions

- [ ] Render existing edition/fallback data.
- [ ] Clearly label content as archive/history.
- [ ] Link to proceedings/videos only when available.

## Contact

- [ ] Render general contact email if available.
- [ ] Render submissions contact if available.
- [ ] Render sponsorship contact if available.
- [ ] Render current venue/address/map link.
- [ ] Do not render inherited previous-edition venue.

## Page model gaps

- [ ] Add `SpeakerIndexPage` or `SpeakersPage` if absent.
- [ ] Add `ContactPage` if absent.
- [ ] Add both to `HomePage.subpage_types` or the appropriate Wagtail page hierarchy.
- [ ] Ensure main navigation can link to both pages.

## Home/About data source cleanup

- [ ] Refactor Home to prefer `CoreSettings`, `Announcement`, `Sponsor`, and program models.
- [ ] Refactor About to prefer `CoreSettings` and Sponsor/supporting-entity models.
- [ ] Keep `pages.content` constants only as temporary fallback if needed.
- [ ] Do not introduce new hardcoded repeated event facts.

## Committee/team data

- [ ] Do not add `is_committee` or `is_speaker` flags to `Speaker` in this proposal.
- [ ] If structured committee modeling is needed, document a follow-up proposal.

## Navigation and SEO

- [ ] Ensure main navigation links to required pages.
- [ ] Ensure mobile navigation works.
- [ ] Add breadcrumbs where appropriate.
- [ ] Add meaningful page titles.
- [ ] Add search descriptions or defaults.

## Accessibility

- [ ] Each page has a single clear `h1`.
- [ ] Heading levels are ordered.
- [ ] CTAs have accessible names.
- [ ] Cards do not hide content behind hover-only behavior.
- [ ] Status badges include text.
- [ ] Program schedule remains readable on mobile.

## Tests and validation

- [ ] Add smoke tests for public page rendering.
- [ ] Add Home context test.
- [ ] Add Program filtering test.
- [ ] Add Speaker hidden-status filtering test.
- [ ] Add Registration coming-soon test.
- [ ] Add Contact venue/address test if ContactPage exists.
- [ ] Run `openspec validate add-public-site-pages-mvp --strict`.
- [ ] Run `npm run build`.
- [ ] Run `uv run python manage.py check`.
- [ ] Run `uv run python manage.py makemigrations --check --dry-run`.
- [ ] Run `uv run pytest`.

## PR checklist

- [ ] Branch is `change/add-public-site-pages-mvp`.
- [ ] PR title starts with `[add-public-site-pages-mvp]`.
- [ ] PR body includes `Closes #6`.
- [ ] No authenticated submissions/review workflows were implemented.


