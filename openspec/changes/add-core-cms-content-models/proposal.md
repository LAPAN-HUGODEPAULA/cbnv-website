# Proposal: Add Core CMS Content Models

## Change ID

`add-core-cms-content-models`

## Linked issue

GitHub issue: `OpenSpec: add core CMS content models`
Expected issue number: `#3`

## Problem

The public site needs a CMS-backed content foundation before implementing full public pages. Without central models for global event settings, news, announcements, supporting entities, links, institutional acknowledgements and reusable content blocks, templates will drift into hardcoded content.

That drift would make later UI/UX and editorial consistency work harder, especially for repeated information such as event dates, venue, external registration link, YouTube link, FAPEMIG acknowledgement, sponsors/partners and Home highlights.

## Proposed Change

Create the core Wagtail/Django CMS models that centralize global site content and recurring editorial entities.

This proposal should implement the data and admin foundation only. It should not build the final public pages, program/speaker models, submissions, review workflow or final copy.

## Goals

1. Centralize global CBNV 2026 metadata in editable settings.
2. Create CMS-backed models for news/announcements.
3. Create CMS-backed models for sponsors, partners and supporting entities.
4. Centralize external links used by the public site.
5. Provide reusable editorial structures for later Home/About/Public-page proposals.
6. Prepare the CMS for a single admin/editorial operator.
7. Reduce hardcoded content in templates and future pages.

## Non-goals

This change SHALL NOT:

1. implement final public pages;
2. implement program/speaker/venue domain models;
3. implement author/reviewer/chair dashboards;
4. implement submission or review workflows;
5. implement final editorial copy;
6. implement payment, certificates, QR code, or video hosting;
7. create complex editorial RBAC;
8. add automated integration with Sympla, UFMG, FUNDEP, YouTube or Instagram APIs.

## Scope

In scope:

- Wagtail settings for global site/event configuration.
- News/announcement model.
- Sponsor/supporting-entity model.
- External link fields and “coming soon” states.
- Institutional acknowledgement fields, including FAPEMIG support.
- Basic editorial status fields.
- Admin panels/snippets for a single admin workflow.
- Minimal model tests.
- Documentation of CMS model responsibilities.

Out of scope:

- Full Wagtail page templates.
- Program and speaker data.
- Venue/map model if handled later in `add-program-speakers-and-venue-models`.
- Submission files.
- Review forms.
- Reports and indicators.

## Proposed Model Responsibilities

### SiteSettings

Global editable site/event configuration.

Recommended fields:

- formal event name;
- short event name;
- edition;
- theme;
- start date;
- end date;
- city;
- state;
- country;
- venue name;
- venue short name;
- format label;
- primary contact email;
- submissions contact email;
- sponsorship contact email;
- Instagram URL;
- YouTube channel URL;
- YouTube playlist URL;
- registration URL;
- registration status;
- livestream URL;
- livestream status;
- Google Maps URL;
- FAPEMIG acknowledgement text;
- FAPEMIG logo/image slot;
- primary institutional logos;
- default SEO title;
- default SEO description.

### NewsArticle or Announcement

Editorial updates and notices shown on public pages.

Recommended fields:

- title;
- slug;
- summary;
- body;
- category;
- publication date/time;
- status;
- featured on Home;
- pinned;
- image;
- external URL optional;
- SEO title;
- SEO description.

### SupportingEntity / Sponsor

Organizations shown in partner/support areas.

Recommended fields:

- name;
- category;
- logo;
- URL;
- description;
- status;
- display on Home;
- display in Footer;
- display on Sponsorship/About pages;
- order;
- accessibility alt text.

### Reusable editorial structures

If useful, the implementation may add small reusable blocks or helpers for:

- CTA configuration;
- highlight cards;
- link lists;
- social links;
- institutional acknowledgement.

The implementation should avoid over-modeling and only add reusable structures that are necessary for the next public-site proposals.

## Admin Workflow

The admin workflow should be simple:

1. one central admin/editor updates global settings;
2. the same admin creates/updates news and announcements;
3. the same admin manages supporting entities/sponsors;
4. content can be hidden, drafted or published without code changes;
5. final public pages consume these models later.

No complex editorial RBAC should be introduced.

## Implementation Strategy

1. Keep global settings in `core` or the project’s chosen settings app.
2. Keep news/content entities in `pages` or `content` depending on existing structure.
3. Keep sponsors/supporting entities in `sponsors`.
4. Use Wagtail snippets/settings where this improves editor ergonomics.
5. Add model-level choices for statuses and categories.
6. Add query helpers/managers only if they simplify public-page rendering.
7. Add migrations and tests in the same proposal.
8. Document where each piece of content should live.

## Data Consistency Rules

1. Event name, dates, theme and global links should come from `SiteSettings`.
2. Repeated partner/support logos should come from supporting-entity/sponsor models.
3. News shown on the Home should be selected from news/announcement models.
4. FAPEMIG acknowledgement should be editable from CMS/settings, not hardcoded in multiple templates.
5. Missing external links should render later as “em breve” rather than broken links.

## Risks

### Risk: over-modeling before public pages exist

Mitigation: implement only models needed by the public-site MVP and known requirements.

### Risk: mixing domain program data into generic CMS models

Mitigation: keep program/speaker/venue models for the next domain proposal.

### Risk: hardcoding copy while creating models

Mitigation: use neutral defaults and leave final copy to `produce-public-site-content-round-1`.

### Risk: making admin too complex

Mitigation: optimize for a single editorial admin and avoid RBAC/editorial workflow complexity.

## Acceptance Criteria

1. Global event/site settings are editable in Wagtail.
2. News/announcements can be created, hidden and featured.
3. Supporting entities/sponsors can be created, categorized, ordered and hidden.
4. External public links can be configured centrally.
5. FAPEMIG acknowledgement has a central CMS-backed field/slot.
6. The implementation avoids hardcoded repeated content in layout templates where possible.
7. The change passes:
   - `openspec validate add-core-cms-content-models --strict`
   - `uv run python manage.py check`
   - `uv run python manage.py makemigrations --check --dry-run`
   - `uv run pytest`
8. Public pages are not fully implemented in this change.
