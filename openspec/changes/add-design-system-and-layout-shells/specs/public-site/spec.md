# Public Site Layout Shell Delta

## ADDED Requirements

### Requirement: Shared public base template

The public site SHALL use a shared base template for common document structure, assets, landmarks and layout slots.

#### Scenario: Page extends base template

Given a public page template is implemented  
When the page renders  
Then it SHALL use or extend the shared public base template.

#### Scenario: Main landmark exists

Given a public page renders  
When assistive technology inspects the document  
Then the page SHALL contain a `main` landmark with a stable target for skip navigation.

### Requirement: Skip link

The public layout SHALL include a skip link to the main content.

#### Scenario: Keyboard user reaches skip link

Given a keyboard user loads a public page  
When they press Tab from the top of the page  
Then a skip link SHALL be available to move focus to the main content.

### Requirement: Responsive public header

The public site SHALL provide a responsive header with site identity, primary navigation and a CTA slot.

#### Scenario: Desktop navigation

Given a visitor uses a desktop viewport  
When the header renders  
Then the primary navigation SHALL be visible and usable.

#### Scenario: Mobile navigation

Given a visitor uses a mobile viewport  
When the header renders  
Then a mobile navigation pattern SHALL be available and keyboard accessible.

### Requirement: Public footer shell

The public site SHALL provide a reusable footer shell.

#### Scenario: Footer renders essential links

Given a public page renders  
When the visitor reaches the footer  
Then essential navigation and institutional/support slots SHALL be available.

#### Scenario: Footer supports institutional acknowledgement

Given institutional support must be shown  
When the footer renders  
Then it SHALL provide a slot for FAPEMIG or equivalent support acknowledgement.

### Requirement: No final content hardcoding in layout shell

The layout shell SHALL avoid hardcoding final editorial claims that belong to CMS/content proposals.

#### Scenario: Layout uses placeholders only

Given the layout shell is implemented before final content proposals  
When placeholder content is necessary  
Then it SHALL use neutral placeholders and SHALL NOT include exaggerated claims or unverified statements.
