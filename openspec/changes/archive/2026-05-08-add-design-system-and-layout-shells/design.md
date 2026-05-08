# Design: Add Design System and Layout Shells

## Overview

This change establishes the frontend foundation of the CBNV 2026 platform. It translates the approved visual direction into a maintainable Django-template/Tailwind design system.

The goal is not to make final pages. The goal is to create the reusable visual grammar that future pages will consume.

## Design Principles

### 1. Scientific clarity over spectacle

The interface should look modern and technically sophisticated, but never obscure information. Avoid decorative effects that compete with the content.

### 2. Humble institutional tone

The design should support a credible scientific congress. It should not imply inflated scale or marketing claims.

### 3. Content-first hierarchy

Every component must help users answer:

- What is this event?
- When and where does it happen?
- What can I do now?
- What is confirmed vs pending?
- Where do I go next?

### 4. Accessibility as a baseline

Accessibility is not a final QA patch. It is part of the component contract.

### 5. Reuse before page-specific styling

If a pattern will appear twice, it should likely become a partial or documented utility pattern.

## Visual System

### Color roles

Use semantic roles, not only raw hex names.

Recommended source tokens:

```css
@theme {
  --color-cbnv-navy-950: #04132B;
  --color-cbnv-navy-900: #081426;
  --color-cbnv-navy-800: #0E1E3A;

  --color-cbnv-blue-500: #214BFF;
  --color-cbnv-blue-400: #4E6DFF;

  --color-cbnv-green-400: #2FEA8B;
  --color-cbnv-green-300: #77F5B5;

  --color-cbnv-surface-dark: rgba(255, 255, 255, 0.06);
  --color-cbnv-surface-border: rgba(255, 255, 255, 0.12);

  --color-cbnv-text-primary: #E7ECF7;
  --color-cbnv-text-secondary: #9AA8C7;
  --color-cbnv-text-inverse: #111827;

  --color-cbnv-warning: #F59E0B;
}
```

Implementation may adjust token names to the final Tailwind 4 convention, but the roles must remain explicit.

### Usage rules

- Deep navy is the primary canvas.
- Electric blue is for primary actions and links.
- Neuro green is for accents, active states and scientific/visual motifs.
- Green should not be overused as body text.
- Avoid low-contrast gray-on-navy text.
- Use the warning color sparingly for deadlines and important notices.

## Typography

Recommended roles:

- display/headline: academic or editorial serif if loaded safely;
- body: highly legible sans-serif;
- label: compact technical sans-serif.

If custom fonts are not yet configured, use robust system fallbacks:

```css
@theme {
  --font-cbnv-display: "Newsreader", ui-serif, Georgia, serif;
  --font-cbnv-sans: "Inter", ui-sans-serif, system-ui, sans-serif;
  --font-cbnv-label: "Space Grotesk", "Inter", ui-sans-serif, system-ui, sans-serif;
}
```

Do not block implementation on external font loading. Provide fallbacks.

## Layout System

Use Tailwind breakpoints. Components must be mobile-first.

Create a standard content container pattern:

- small content: max width suitable for prose;
- normal content: site-wide max width;
- wide content: program/timeline/admin-style layouts.

Use consistent vertical rhythm:

- section padding mobile: moderate;
- section padding desktop: larger;
- card padding: comfortable but not bloated;
- avoid cramped dense grids.

## Components

### Header

Requirements:

- site identity;
- primary navigation;
- responsive mobile menu;
- visible CTA slot;
- clear focus states;
- no content overlap on mobile;
- no dependence on JavaScript for basic navigation unless required.

### Footer

Requirements:

- concise event identity;
- essential links;
- institutional/support mention;
- FAPEMIG slot;
- Instagram/icon link with accessible label;
- no redundant long slogan if copyright/branding already communicates identity.

### Button/CTA

Variants:

- primary;
- secondary;
- ghost;
- external link;
- disabled/coming soon.

Requirements:

- accessible focus;
- clear disabled state;
- external links should be visually recognizable when appropriate;
- button text should be action-oriented.

### Card

Variants:

- information card;
- event fact card;
- news card;
- program card;
- partner card;
- person card.

Requirements:

- not too large by default;
- good density on mobile;
- image handling must avoid layout shift;
- cards should not hide critical content behind hover-only interaction.

### Badge

Uses:

- confirmed/pending;
- hybrid/in-person;
- day;
- activity type;
- deadline state.

Requirements:

- never rely on color alone;
- text must carry meaning.

### Section heading

Requirements:

- eyebrow/label optional;
- heading;
- short description;
- optional CTA.

### Timeline shell

Used later by Program.

Requirements:

- supports time, title, type, description, participants;
- mobile vertical layout;
- desktop grouped layout;
- handles pending participants.

### Form field shell

Used later by submissions/auth.

Requirements:

- label;
- help text;
- error text;
- required indicator;
- accessible `id`/`for` pattern.

### Alert

Variants:

- info;
- success;
- warning;
- error.

Requirements:

- role/status semantics as appropriate;
- text not dependent on color.

### Empty state

Used for no news, no program item, no submissions.

Requirements:

- clear title;
- explanatory text;
- optional action.

## Template Strategy

Use Django includes for partials. Keep logic minimal in templates.

Example pattern:

```django
{% include "partials/components/button.html" with href="/programacao/" label="Ver programação" variant="primary" %}
```

Do not require an advanced component library at this stage.

## JavaScript Strategy

Do not introduce a frontend framework.

Allowed:

- minimal Alpine.js for mobile menu state if needed;
- HTMX later for dynamic interactions.

Not allowed:

- React;
- Next.js;
- client-side routing;
- complex global state.

## Responsive Behavior

All layout shells must work at:

- narrow mobile;
- large mobile;
- tablet;
- desktop;
- wide desktop.

Design must not assume that users browse only from desktop.

## Accessibility Details

Required implementation details:

1. `<a class="skip-link" href="#main-content">Pular para o conteúdo principal</a>`.
2. `<main id="main-content">`.
3. focus-visible styles for links/buttons/form controls.
4. aria-label on icon-only links.
5. mobile menu button with `aria-controls` and `aria-expanded`.
6. no inaccessible hover-only content.
7. reduced motion CSS.

## Content Strategy in this Change

Use only neutral placeholders, for example:

- “Ver programação”
- “Submissões”
- “Inscrição em breve”
- “Notícia em destaque”
- “Participantes a confirmar”

Avoid final copy such as:

- “maior evento da América Latina”;
- “fronteira do conhecimento”;
- claims not present in canonical requirements.

Final content belongs to later content proposals.

## Documentation

Create or update:

```text
docs/design-system.md
```

It should explain:

- token roles;
- component partials;
- when to use each component;
- accessibility expectations;
- what is intentionally out of scope.
