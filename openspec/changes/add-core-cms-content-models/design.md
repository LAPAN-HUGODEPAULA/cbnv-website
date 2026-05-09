# Design: Add Core CMS Content Models

## Overview

This change introduces the core editable content layer for the CBNV 2026 website. It should provide stable CMS models that later public pages can consume.

The design priority is separation of responsibility:

- global event and site configuration belongs in settings;
- editorial updates belong in news/announcement models;
- institutional/support entities belong in sponsor/support models;
- program, speakers and venue details belong to the later program-domain proposal;
- final page copy belongs to the later content-production proposal.

## Domain Boundaries

### Core/global settings

Use for information that is global, reused and expected to appear in multiple pages or layout areas.

Examples:

- event name;
- event theme;
- dates;
- city;
- format;
- contact email;
- registration link;
- YouTube link;
- Instagram link;
- FAPEMIG acknowledgement;
- default SEO fields.

### News/announcements

Use for dated public updates.

Examples:

- “Submissões abertas em breve”;
- “Programação preliminar publicada”;
- “Inscrições em breve”;
- “Chamada de trabalhos publicada”.

### Supporting entities/sponsors

Use for institutions, partners, supporters and sponsors that may appear in Home, footer, About or Sponsorship pages.

Examples:

- UFMG;
- FUNDEP;
- FAPEMIG;
- HOLHOS;
- Sociedade Brasileira de Neurovisão;
- other confirmed entities.

### Program/speaker/venue domain

Do not implement here, except for generic global placeholders if strictly needed.

The detailed venue, Google Maps embed, program days, sessions, talks and speaker status should be handled in:

`add-program-speakers-and-venue-models`

## Wagtail Usage

Prefer Wagtail-native editing patterns:

- settings for global singleton-like configuration;
- snippets for reusable entities such as sponsors;
- pages or plain Django models for news depending on the project’s final Wagtail structure.

Recommended:

- `@register_setting` for `SiteSettings`;
- `@register_snippet` for `Sponsor` or `SupportingEntity`;
- Wagtail admin panels with clear Portuguese labels;
- `help_text` for fields that affect public display.

## Model Design

### SiteSettings

Recommended behavior:

- one object per Wagtail site;
- provides global context to base template and public pages;
- stores external links and status flags;
- should not contain long page copy;
- should not contain program details.

Recommended status choices:

```python
class LinkStatus(models.TextChoices):
    AVAILABLE = "available", "Disponível"
    COMING_SOON = "coming_soon", "Em breve"
    UNAVAILABLE = "unavailable", "Indisponível"
```

These can be implemented as repeated fields or a simpler first iteration.

### NewsArticle / Announcement

Recommended fields:

- `title`;
- `slug`;
- `summary`;
- `body`;
- `category`;
- `status`;
- `published_at`;
- `featured_on_home`;
- `pinned`;
- `image`;
- `external_url`;
- `seo_title`;
- `seo_description`.

Recommended status choices:

- draft;
- published;
- archived.

Queries needed later:

- published;
- featured;
- recent;
- pinned first.

### Sponsor / SupportingEntity

Recommended fields:

- `name`;
- `category`;
- `logo`;
- `url`;
- `description`;
- `status`;
- `show_on_home`;
- `show_in_footer`;
- `show_on_about`;
- `show_on_sponsorship`;
- `sort_order`;
- `logo_alt_text`.

Recommended categories:

- institutional partner;
- funding agency;
- scientific partner;
- support;
- sponsor;
- organizing institution.

Use Portuguese labels in the admin, but keep stable internal values.

## Admin Ergonomics

The admin should make common updates obvious:

- registration URL and status;
- livestream URL and status;
- social links;
- contact email;
- news/announcement visibility;
- partner/supporter visibility;
- FAPEMIG acknowledgement.

Avoid deeply nested panels unless necessary.

## Validation Rules

Suggested validation:

1. URL fields must be valid URLs when present.
2. `published_at` should be set when status is published.
3. display flags should not matter when status is hidden/archived.
4. logo alt text should be available when logo is present.
5. `sort_order` should support deterministic display.

## Template Context Strategy

Later public templates need access to global settings. This change may add:

- a context processor;
- template tag;
- Wagtail settings context usage;
- lightweight helper functions.

Choose the simplest Wagtail-idiomatic approach.

## Migration Strategy

Create migrations normally. This change should not require data migration if no previous CMS content exists.

If placeholder data is needed, keep it minimal and do not hardcode final claims.

Full canonical seed belongs to:

`seed-canonical-event-content`

## Testing Strategy

Minimum tests:

1. model creation tests;
2. status/filter manager tests if managers exist;
3. settings availability test;
4. admin import/system check test;
5. migration dry-run check.

Avoid brittle tests that assert final copy.

## Documentation

Create or update documentation explaining:

- where global event data lives;
- where news lives;
- where sponsors/supporting entities live;
- what should not be stored in these models;
- how later pages should consume the models.
