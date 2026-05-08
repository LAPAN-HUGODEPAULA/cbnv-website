# Design System Delta

## ADDED Requirements

### Requirement: Source-level design tokens

The platform SHALL define source-level design tokens for the CBNV visual system.

#### Scenario: Tokens exist in source CSS

Given a developer opens the source CSS  
When they inspect the design-system definitions  
Then they SHALL find named tokens for primary navy, electric blue, neuro green, text colors, surfaces, borders and warning/accent states.

#### Scenario: Generated CSS is not the only source of truth

Given CSS is built through Tailwind  
When a developer needs to change visual identity  
Then they SHALL edit source token definitions rather than editing generated CSS directly.

### Requirement: Typography roles

The platform SHALL define explicit typography roles for display text, body text and technical labels.

#### Scenario: Font fallback is available

Given custom fonts fail to load or are not yet configured  
When the site renders  
Then readable system fallbacks SHALL be used.

### Requirement: Reusable component partials

The platform SHALL provide reusable Django template partials for common UI components.

#### Scenario: Button partial is reused

Given a template needs a primary CTA  
When the template renders a CTA  
Then it SHOULD use the shared button partial or the documented button class pattern.

#### Scenario: Card partial is reused

Given a template needs an information card  
When the template renders the card  
Then it SHOULD use the shared card partial or the documented card class pattern.

#### Scenario: Badge conveys meaning through text

Given a badge represents status or category  
When the badge is rendered  
Then the badge SHALL include text that conveys the meaning without relying only on color.

### Requirement: Accessibility baseline for UI primitives

The design system SHALL provide accessible defaults for interactive and structural components.

#### Scenario: Focus is visible

Given a keyboard user tabs through interactive elements  
When an element receives focus  
Then the focus state SHALL be visible.

#### Scenario: Motion can be reduced

Given a user prefers reduced motion  
When components render animations or transitions  
Then non-essential motion SHALL be reduced or disabled.

#### Scenario: Icon-only link has an accessible name

Given an icon-only link is rendered  
When a screen reader accesses it  
Then the link SHALL expose an accessible label.

### Requirement: Responsive layout primitives

The design system SHALL provide mobile-first layout primitives.

#### Scenario: Layout works on mobile

Given a visitor opens the site on a narrow viewport  
When the layout renders  
Then core navigation, content containers and cards SHALL remain usable without horizontal scrolling.

### Requirement: Component usage documentation

The platform SHALL document the design-system primitives.

#### Scenario: Developer reads design-system docs

Given a developer needs to create a new public template  
When they open the design-system documentation  
Then they SHALL find the available tokens, partials, examples and accessibility expectations.
