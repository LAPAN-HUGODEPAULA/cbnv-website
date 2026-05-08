## Context

The XII CBNV 2026 platform is being built as a monolithic modular Django application using Wagtail CMS. This change focuses on implementing the complete public-facing website using a modern hybrid single-page architecture, ensuring it aligns with the "NeuroVision AI" aesthetic while enforcing a strict 5.5:1 contrast ratio for accessibility.

## Goals / Non-Goals

**Goals:**
- Implement a responsive, high-contrast (5.5:1 ratio) public website using OKLCH colors.
- Support full internationalization (PT/EN) using Wagtail's i18n features.
- Create a hybrid navigation system (Smooth scroll on Home + Standalone deep links via HTMX).
- Implement flexible Wagtail models for Home, Program, Registration, Submissions, Sponsors, and Video Gallery.
- Ensure all informational pages (Registration/Submissions) are "Phase 2 ready" using state-aware logic.
- Integrate the scientific program and tiered sponsorship grid into the CMS.

**Non-Goals:**
- Implementation of the actual submission form/workflow (Phase 2).
- Native video hosting (YouTube embed only).
- Authenticated user dashboards (handled in separate changes).

## Decisions

- **Hybrid Navigation**: Navigation links will use HTMX to detect if the target section is present on the current page. If so, it performs a smooth scroll; otherwise, it navigates to the standalone URL.
- **Accessibility & Color**: We will use a custom OKLCH palette in Tailwind v4 to ensure a 5.5:1 contrast ratio against the deep navy background, avoiding problematic "frosted" transparency in favor of solid tonal elevation.
- **StreamField "Bento" Strategy**: The `AboutPage` and `SubmissionsPage` will use a shared `BentoGridBlock` in `core/blocks.py` to allow editors to create high-impact, non-linear layouts.
- **State-Aware Modules**: `RegistrationPage` and `SubmissionsPage` will include a `status` field (e.g., `COMING_SOON`, `OPEN`, `CLOSED`) to swap UI states without template refactoring in the future.
- **Sponsor Weight Logic**: The `SponsorTier` snippet will define visual "weights" (Diamond=1, Support=4) to automatically scale logos in a responsive grid.
- **Wagtail i18n**: Use `wagtail-localize` or core Wagtail i18n to manage translations for all fields and snippets.

## Risks / Trade-offs

- **[Risk] i18n Complexity** → **[Mitigation]** Standardize all template strings and model fields for translation from the start.
- **[Risk] Contrast vs. Aesthetic** → **[Mitigation]** Use OKLCH to find the precise balance between neon vibrancy and required luminance ratios.
- **[Trade-off] Single-Page vs. SEO** → **[Rationale]** The hybrid model provides the smooth UX of a single-page app while maintaining the full SEO benefit of unique, crawlable URLs for each section.
