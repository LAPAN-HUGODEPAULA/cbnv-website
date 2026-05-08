# Proposal: Add Design System and Layout Shells

## Change ID

`add-design-system-and-layout-shells`

## Linked issue

GitHub issue: `OpenSpec: add design system and layout shells`  
Expected issue number: `#2`

## Problem

The project needs a stable frontend foundation before implementing the public pages. The current visual direction exists as Stitch/v0-style prototype output and high-level design guidance, but it is not yet expressed as a maintainable Django/Wagtail/Tailwind design system.

Without a formal design-system layer, each page implementation may duplicate layout, navigation, footer, card styles, CTAs, form markup and responsive behavior. That would increase rework when Home, About, Program, Speakers, Submissions, Registration, Sponsorship and Contact pages are implemented.

## Proposed Change

Create a reusable design-system and layout-shell foundation for the public website using Django templates, Tailwind CSS 4, semantic HTML and small progressive-enhancement hooks for HTMX/Alpine only when needed.

This change will implement source-level design tokens, base templates, reusable template partials and accessible public layout shells. It will not implement full page content or domain-specific CMS models.

## Goals

1. Convert the approved visual direction into implementable source files.
2. Establish design tokens for color, typography, spacing, radius, shadows, borders and layout.
3. Provide reusable template partials for header, footer, navigation, CTA buttons, cards, badges, sections, forms and timeline shells.
4. Ensure the design system is usable by later Wagtail page templates.
5. Preserve accessibility, responsiveness and maintainability from the start.
6. Reduce future rework in public pages and authenticated dashboards.

## Non-goals

This change SHALL NOT:

1. implement final Home/About/Program/Submission pages;
2. implement CMS content models;
3. implement program/speaker/venue models;
4. implement submission or review flows;
5. implement final editorial copy;
6. add complex JavaScript or SPA behavior;
7. introduce React, Next.js, Strapi or a component framework outside Django templates;
8. hardcode event content that should later come from CMS/settings.

## Scope

In scope:

- Tailwind CSS 4 source design tokens.
- Public base template.
- Partial templates for layout primitives.
- Header and navigation shell.
- Footer shell.
- Mobile navigation shell.
- Button/CTA partials.
- Card partials.
- Badge partials.
- Section heading partial.
- Timeline shell partial.
- Form field shell partial.
- Alert and empty-state partials.
- Basic accessibility helpers: skip link, focus-visible styles, semantic landmarks, reduced-motion handling.
- Documentation for component usage.
- Tests/checks only where practical at this foundation level.

Out of scope:

- Full Wagtail page models.
- Real news/program/speaker content.
- Final image assets.
- Production deployment.
- Authenticated dashboards.
- Dynamic HTMX behavior except minimal placeholders if necessary.

## Design Direction

The design direction remains:

- dark-mode first;
- deep navy base;
- electric blue primary action color;
- neuro-green accent;
- scientific/institutional tone;
- moderated glassmorphism;
- high readability;
- no excessive neon;
- no animation-heavy interface;
- responsive by default;
- WCAG 2.2 AA as the target.

The system should feel modern and scientific without turning into a generic startup landing page.

## Implementation Strategy

1. Keep the design system source-driven.
2. Avoid relying on generated CSS as the source of truth.
3. Put reusable visual decisions in `src/input.css`, Tailwind tokens and documented template partials.
4. Keep template partials small and composable.
5. Use semantic HTML before JavaScript.
6. Use HTMX/Alpine only if interaction cannot be handled cleanly with HTML/CSS.
7. Keep content placeholders neutral and clearly temporary.
8. Do not hardcode claims or factual content that will be supplied by CMS in later proposals.

## Proposed File Structure

```text
src/
  input.css

templates/
  base.html
  partials/
    layout/
      skip_link.html
      header.html
      mobile_nav.html
      footer.html
      page_shell.html
    components/
      button.html
      card.html
      badge.html
      section_heading.html
      timeline_shell.html
      form_field.html
      alert.html
      empty_state.html
      icon_link.html

docs/
  design-system.md
```

If the project already has a different template convention, the implementation MAY adapt names while preserving the separation between layout partials and reusable components.

## Accessibility Requirements

The change must include:

1. visible focus styles;
2. semantic landmarks: `header`, `nav`, `main`, `footer`;
3. skip link to main content;
4. no interactive element implemented as a non-interactive tag;
5. accessible mobile menu labels;
6. `aria-label` for icon-only links;
7. reduced-motion handling;
8. contrast-aware foreground/background token pairs;
9. support for keyboard navigation.

## Risks

### Risk: overfitting to prototype output

Mitigation: treat Stitch/v0 screens as inspiration, not implementation architecture.

### Risk: hardcoding content too early

Mitigation: use neutral placeholders and reserve event content for CMS/content proposals.

### Risk: excessive visual complexity

Mitigation: keep glassmorphism moderate and prioritize readability.

### Risk: too many component abstractions

Mitigation: create only primitives needed by the public site MVP.

## Acceptance Criteria

1. The project has a documented design-system foundation.
2. Public templates can use a shared base layout.
3. Header, footer and mobile navigation are reusable and responsive.
4. Source CSS contains explicit design tokens.
5. Reusable partials exist for core UI primitives.
6. Components support accessible names, keyboard use and visible focus.
7. The change passes:
   - `openspec validate add-design-system-and-layout-shells --strict`
   - `npm run build`
   - `uv run python manage.py check`
   - `uv run pytest`
8. No final public page content or domain feature is implemented outside this proposal.
