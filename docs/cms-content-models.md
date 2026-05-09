# Core CMS Content Models

## Purpose

This document explains where reusable CMS content for the CBNV 2026 site lives and what later public-page templates should consume.

## Global Settings

Global event and site metadata lives in the Wagtail settings model `core.CoreSettings`.

Use it for repeated values such as:

- formal and short event names;
- edition and theme;
- event dates, city, venue labels and format;
- contact, submission and sponsorship emails;
- registration, livestream, Instagram, YouTube and Google Maps links;
- FAPEMIG acknowledgement text and logo slot;
- default SEO title and description.

Public templates can access this through the existing Wagtail settings context as `settings.core.CoreSettings`. The model also exposes helper properties for link availability, such as `registration_is_available`, `livestream_is_available` and `primary_youtube_url`.

## News And Announcements

Dated editorial updates live in `pages.Announcement`, registered as a Wagtail snippet.

Use announcements for public updates such as registration notices, submission notices, program updates and institutional news. The model includes category, status, publication date, feature and pin flags, optional image, external URL and SEO fields.

Public-page code should use query helpers:

- `Announcement.objects.published()`
- `Announcement.objects.featured()`
- `Announcement.objects.recent()`

Draft, archived and future-dated entries are excluded from public queries.

## Supporting Entities

Partners, supporters, sponsors, funding agencies and organizing institutions live in `sponsors.Sponsor`, registered as a Wagtail snippet. Existing sponsor tiers remain available through `sponsors.SponsorTier`.

Use supporting entities for organizations that may appear on the Home page, footer, About page or Sponsorship page. The model includes category, logo, URL, description, status, display flags, sort order and logo alt text.

Public-page code should use query helpers:

- `Sponsor.objects.for_home()`
- `Sponsor.objects.for_footer()`
- `Sponsor.objects.for_about()`
- `Sponsor.objects.for_sponsorship()`

Hidden and archived entities are excluded from public queries.

## Later Proposals

Do not store program sessions, speakers, detailed venue data, submissions, review workflow data, payment information, certificates or final public-page copy in these core CMS models.

Those belong to later proposals such as program/speaker/venue modeling, submission/review workflows and public-site content production.
