## ADDED Requirements

### Requirement: Accessibility Landmarks
The public site layouts SHALL include ARIA landmarks (`<header>`, `<nav>`, `<main>`, `<footer>`) to facilitate navigation for screen reader users.

#### Scenario: Landmarks present on homepage
- **WHEN** the homepage is loaded
- **THEN** a screen reader SHALL identify the banner, navigation, main content, and footer regions

### Requirement: Skip to Content Link
The `public.html` layout SHALL include a "Skip to Content" link as the first focusable element on every page.

#### Scenario: Skipping navigation
- **WHEN** a keyboard user presses TAB on page load
- **THEN** a "Skip to Content" link SHALL become visible
- **AND** clicking it SHALL move focus to the `<main>` element

### Requirement: Image Optimization for Performance
The public site SHALL serve images in modern formats (WebP/AVIF) with appropriate `srcset` attributes for responsive delivery.

#### Scenario: Responsive images served
- **WHEN** a user accesses the site from a mobile device
- **THEN** the system SHALL serve a lower-resolution version of the hero image to save bandwidth

### Requirement: Mobile Touch Targets
All interactive elements on mobile views SHALL have a minimum touch target size of 44x44 pixels.

#### Scenario: Buttons are easy to tap
- **WHEN** viewed on a mobile screen
- **THEN** all links and buttons SHALL meet the 44px minimum touch target size requirement
