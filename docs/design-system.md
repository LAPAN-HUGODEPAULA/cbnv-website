# CBNV 2026 Design System

Foundation layer for the XII Congresso Brasileiro de Neurociências da Visão platform.

## Design Tokens

All tokens are defined in `src/input.css` using Tailwind CSS 4 `@theme` blocks.

### Colors

| Token | Role | Usage |
|---|---|---|
| `cbnv-navy-950` | Deep background | Page backgrounds, cards |
| `cbnv-navy-900` | Elevated background | Subtle elevation layers |
| `cbnv-navy-800` | Surface background | Hover states, elevated panels |
| `cbnv-blue-600` | Primary action | CTAs, links, focus rings |
| `cbnv-blue-500` | Primary hover | Hover state for blue-600 |
| `cbnv-blue-400` | Primary light | Accents on dark backgrounds |
| `cbnv-green-400` | Accent | Active states, identity highlight |
| `cbnv-green-300` | Accent light | Subtle green accents |
| `cbnv-green-500` | Accent solid | Green on lighter backgrounds |
| `cbnv-text-primary` | Primary text | Headings, important text on dark |
| `cbnv-text-secondary` | Secondary text | Body text, descriptions on dark |
| `cbnv-text-inverse` | Inverse text | Text on light backgrounds |
| `cbnv-text-dark` | Dark text | Text on white/light surfaces |
| `cbnv-warning` | Warning | Deadlines, important notices |
| `cbnv-white` | White | Light surface, cards |

### Typography

| Token | Font | Usage |
|---|---|---|
| `font-cbnv-display` | Newsreader, Georgia, serif | Headlines, display text |
| `font-cbnv-sans` | Inter, system-ui, sans-serif | Body text, UI elements |
| `font-cbnv-label` | Space Grotesk, Inter, sans-serif | Labels, navigation, badges |

### Radius

| Token | Value | Usage |
|---|---|---|
| `radius-cbnv-sm` | 0.375rem | Small elements |
| `radius-cbnv-md` | 0.5rem | Buttons, inputs |
| `radius-cbnv-lg` | 0.75rem | Cards |
| `radius-cbnv-xl` | 1rem | Panels |
| `radius-cbnv-full` | 9999px | Pills, badges, avatars |

### Shadows / Glow

| Token | Usage |
|---|---|
| `shadow-cbnv-glow-blue` | Blue glow for CTAs |
| `shadow-cbnv-glow-green` | Green glow for accents |
| `shadow-cbnv-card` | Card elevation shadow |

## Component Partials

All components live in `templates/components/`.

### Layout Components

| Partial | Description |
|---|---|
| `skip_link.html` | Skip-to-content link for keyboard users |
| `header.html` | Fixed header with navigation, identity, CTA |
| `mobile_nav.html` | Mobile navigation overlay |
| `footer.html` | Footer with links, FAPEMIG, social icons |
| `page_shell.html` | Content container (narrow/normal/wide) |

### UI Components

| Partial | Variants | Description |
|---|---|---|
| `button.html` | primary, secondary, outline, ghost | CTA and action buttons |
| `card.html` | light, dark | Information cards |
| `badge.html` | confirmed, pending, rejected, info, draft, review | Status/category badges |
| `section_heading.html` | — | Section header with eyebrow, heading, description, CTA |
| `timeline.html` | — | Vertical timeline for program items |
| `form_field.html` | — | Django form field with label, help, errors |
| `alert.html` | info, success, warning, error (dark/light) | Status alerts |
| `icon_link.html` | instagram, youtube, email, external | Icon-only accessible links |
| `input.html` | text, textarea, select | Standalone input fields |

### State Components

| Partial | Description |
|---|---|
| `states/empty.html` | Empty state with icon, message, action |
| `states/error.html` | Error state with icon, message, action |
| `states/loading.html` | Loading spinner with message |

## Usage Examples

### Button

```django
{% include "components/button.html" with label="Ver programação" variant="primary" href="/programacao/" %}
{% include "components/button.html" with label="Salvar" variant="secondary" tag="button" type="submit" %}
```

### Card

```django
{% include "components/card.html" with title="Notícia" body="Descrição..." dark=True %}
```

### Badge

```django
{% include "components/badge.html" with label="Confirmado" variant="confirmed" %}
```

### Section heading

```django
{% include "components/section_heading.html" with eyebrow="Programação" heading="Confira a grade" description="Descrição do evento" cta_label="Ver mais" cta_href="/programacao/" %}
```

### Alert

```django
{% include "components/alert.html" with variant="warning" title="Prazo próximo" message="Submissões encerram em 3 dias." dark=True %}
```

### Icon link

```django
{% include "components/icon_link.html" with href=url icon="instagram" label="Siga-nos no Instagram" external=True %}
```

### Page shell

```django
{% include "components/page_shell.html" with width="normal" %}
  {# content here #}
{% endinclude %}
```

## Accessibility Contracts

### Required for all components

- **Focus visible**: All interactive elements show a visible blue focus ring (`:focus-visible` in `src/input.css`)
- **Keyboard navigation**: All interactive elements are reachable via Tab and operable via Enter/Space
- **Reduced motion**: Animations and transitions disabled when `prefers-reduced-motion: reduce` is active
- **Semantic HTML**: Use `<nav>`, `<main>`, `<header>`, `<footer>`, `<article>` appropriately

### Specific requirements

- **Skip link**: Present in `public.html` layout, links to `#main-content`
- **Icon-only links**: Must have `aria-label` (handled by `icon_link.html`)
- **Mobile menu**: Uses `aria-controls`, `aria-expanded`, Escape to close
- **Badges**: Always include text labels — never rely on color alone
- **Alerts**: Use `role="alert"` for errors, `role="status"` for others
- **Form fields**: Use `id`/`for` linking, `aria-describedby` for help/error text, `aria-invalid` on errors
- **External links**: Marked with `sr-only` text indicating external link

## Out of Scope

This design system does NOT include:

- Full Wagtail page models or CMS content
- Real program/speaker/submission content
- Authentication flows or dashboard pages
- HTMX dynamic behavior (only minimal Alpine.js for mobile nav)
- Image galleries or carousels
- Complex JavaScript interactions
- Production deployment configuration
- Certificate generation or payment integration

## Layout Templates

| Template | Usage |
|---|---|
| `base.html` | Root template — dark-mode body, fonts, scripts |
| `layouts/public.html` | Public pages — header + footer + skip link |
| `layouts/dashboard.html` | Authenticated pages — sidebar + top bar |
