# Tasks: Add Core CMS Content Models

## OpenSpec

- [x] Create `openspec/changes/add-core-cms-content-models/`.
- [x] Add `proposal.md`.
- [x] Add `design.md`.
- [x] Add `tasks.md`.
- [x] Add delta spec `specs/content/spec.md`.
- [x] Add delta spec `specs/public-site/spec.md`.
- [x] Add delta spec `specs/cms/spec.md`.
- [x] Run `openspec validate add-core-cms-content-models --strict`.

## Model design

- [x] Review current app structure: `core`, `pages`, `sponsors`.
- [x] Decide exact app placement for:
  - [x] `SiteSettings`;
  - [x] `NewsArticle` or `Announcement`;
  - [x] `Sponsor` or `SupportingEntity`.
- [x] Confirm naming conventions before writing migrations.

## Global settings

- [x] Implement Wagtail `SiteSettings` or equivalent global settings model.
- [x] Add event identity fields.
- [x] Add event date/format fields.
- [x] Add global contact fields.
- [x] Add external link fields.
- [x] Add registration status.
- [x] Add livestream status.
- [x] Add YouTube/Instagram fields.
- [x] Add FAPEMIG acknowledgement field.
- [x] Add FAPEMIG logo/image slot if image integration is ready.
- [x] Add default SEO fields.
- [x] Configure Wagtail admin panels.

## News/announcements

- [x] Implement news/announcement model.
- [x] Add title, slug, summary, body.
- [x] Add category.
- [x] Add publication date.
- [x] Add status.
- [x] Add featured/pinned flags.
- [x] Add image field if media integration is ready.
- [x] Add optional external URL.
- [x] Add SEO fields.
- [x] Add published/recent/featured query helpers if useful.
- [x] Configure admin panels.

## Sponsors/supporting entities

- [x] Implement sponsor/supporting-entity model.
- [x] Add name.
- [x] Add category.
- [x] Add logo.
- [x] Add URL.
- [x] Add description.
- [x] Add status.
- [x] Add display flags:
  - [x] show on Home;
  - [x] show in Footer;
  - [x] show on About;
  - [x] show on Sponsorship.
- [x] Add sort order.
- [x] Add logo alt text.
- [x] Configure admin/snippet panels.

## Public-site integration foundation

- [x] Provide a simple way for templates to access global settings.
- [x] Ensure layout shell can later render:
  - [x] registration link or “em breve”;
  - [x] YouTube link;
  - [x] Instagram link;
  - [x] FAPEMIG acknowledgement;
  - [x] supporting entities for footer.
- [x] Do not implement final public pages in this change.

## Documentation

- [x] Create or update `docs/cms-content-models.md`.
- [x] Explain where global settings live.
- [x] Explain where news/announcements live.
- [x] Explain where supporting entities live.
- [x] Explain what belongs to later proposals.
- [x] Document expected usage by later page templates.

## Tests

- [x] Add model tests for global settings if practical.
- [x] Add model tests for news/announcements.
- [x] Add model tests for sponsors/supporting entities.
- [x] Add query helper tests if helpers exist.
- [x] Add admin/import smoke tests if useful.

## Validation

- [x] Run `openspec validate add-core-cms-content-models --strict`.
- [x] Run `uv run python manage.py check`.
- [x] Run `uv run python manage.py makemigrations --check --dry-run`.
- [x] Run `uv run pytest`.

## PR checklist

- [x] Branch is `change/add-core-cms-content-models`.
- [x] PR title starts with `[add-core-cms-content-models]`.
- [x] PR body includes `Closes #3`.
- [x] PR body includes validation checklist.
- [x] No public pages, program models or submission flows were implemented.
