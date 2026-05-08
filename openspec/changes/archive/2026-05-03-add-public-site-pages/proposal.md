## Why

The XII Congresso Brasileiro de Neurociências da Visão (CBNV 2026) needs a professional digital presence to inform participants, attract sponsors, and showcase the scientific program. This change implements the public-facing side of the platform, ensuring a high-quality, accessible, and responsive experience for all visitors.

## What Changes

- **Internationalization (i18n)**: Implementation of dual-language support (PT/EN) across all public pages.
- **Hybrid Single-Page Navigation**: A modern navigation system using HTMX to provide smooth scrolling on the Home page while maintaining unique URLs and standalone rendering for deep links.
- **High-Contrast Design**: Application of a 5.5:1 contrast ratio palette using OKLCH colors, ensuring WCAG 2.2 AA compliance while maintaining the "NeuroVision AI" aesthetic.
- **Home Page**: Implementation of a high-impact landing page that serves as a hub for all congress information.
- **Informational Pages**: Creation of dedicated pages for Registration, Submissions (informational only), Program, Sponsors, and Videos using flexible StreamField blocks.
- **CMS Integration**: Leveraging Wagtail to manage dynamic content across the site.
- **Design System Application**: Applying the updated design system (Tailwind CSS v4 + OKLCH) to all public templates.

## Capabilities

### New Capabilities
- `program`: Management and display of the congress scientific program, including sessions and speakers.
- `i18n`: Global support for multi-language content translation.

### Modified Capabilities
- `public-site`: Expanding to include a hybrid single-page structure and modern navigation.
- `content-cms`: Configuring models and settings for flexible "Bento Grid" and "State-Aware" content.
- `sponsors`: Implementation of weight-based grid logic for tiered visual hierarchy.
- `videos`: Setup of video gallery pages linked to external platforms.

## Impact

- **Apps**: `pages`, `core`, `program`, `sponsors`, `videos`.
- **UI**: Global layout, hybrid navigation, and accessible OKLCH color system.
- **Data**: New models for Program, Sponsors, and Video content with translation support.
- **CMS**: New Wagtail page types and snippets for administrators.
