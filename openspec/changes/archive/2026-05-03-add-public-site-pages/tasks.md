## 1. i18n & Core Blocks Setup

- [x] 1.1 Enable Wagtail Internationalization and configure `LANGUAGES` (PT, EN) in `settings`.
- [x] 1.2 Implement `BentoGridBlock`, `StatBlock`, and `TimelineBlock` in `core/blocks.py`.
- [x] 1.3 Update `src/input.css` with the high-contrast OKLCH palette (5.5:1 ratio).

## 2. CMS Models & Migrations

- [x] 2.1 Refactor `pages/models.py` to use `StreamField` for `AboutPage` and `NewsArticlePage`.
- [x] 2.2 Implement `RegistrationPage` and `SubmissionsPage` with `status` state-tracking.
- [x] 2.3 Implement `SponsorsPage` and `VideoGalleryPage`.
- [x] 2.4 Update `SponsorTier` snippet with grid weight logic.
- [x] 2.5 Ensure all models inherit from `TranslatableMixin` or equivalent.
- [x] 2.6 Generate and apply migrations.

## 3. Hybrid Navigation & Layout

- [x] 3.1 Refine `templates/layouts/public.html` with HTMX-aware header.
- [x] 3.2 Implement `SiteMenu` snippet or setting to manage dynamic navigation.
- [x] 3.3 Refactor `header.html` to support smooth-scroll or direct-link behavior.

## 4. Page Templates

- [x] 4.1 Update `home_page.html` to act as a hub, including sections from child pages.
- [x] 4.2 Implement `submissions_page.html` with 2-phase workflow visualization.
- [x] 4.3 Implement `sponsors_page.html` with weight-based grid rendering.
- [x] 4.4 Implement `video_gallery_page.html` and `registration_page.html`.

## 5. Testing & Verification

- [x] 5.1 Verify contrast ratios across all pages using accessibility tools (target 5.5:1).
- [x] 5.2 Validate i18n switching and language-specific URLs.
- [x] 5.3 Test hybrid navigation (smooth scroll vs. deep link).
- [x] 5.4 Smoke test all 200 OK responses for public routes.
