# Public Site Delta (seed-canonical-event-content)

## ADDED Requirements

### Requirement: Public pages use seeded canonical values
Future public pages SHALL use seeded canonical values for repeated event facts.

#### Scenario: Page needs event dates
- **GIVEN** a public page needs the event dates
- **WHEN** it renders after the canonical seed exists
- **THEN** it SHALL use the CMS-backed canonical dates rather than hardcoded template text.

#### Scenario: Page needs venue address
- **GIVEN** a public page needs the event address
- **WHEN** it renders after the canonical seed exists
- **THEN** it SHALL use the CMS-backed CAD-1/UFMG address rather than hardcoded or inherited previous-edition location.

### Requirement: Coming-soon link states
Future public pages SHALL render unknown external links as clear coming-soon states.

#### Scenario: Registration URL is pending
- **GIVEN** registration status is coming soon
- **WHEN** a public CTA requests registration
- **THEN** the UI SHALL render an accessible “em breve” state instead of a broken link.

### Requirement: Institutional support data is reusable
Future public pages and footer SHALL reuse seeded institutional support data.

#### Scenario: Footer needs FAPEMIG acknowledgement
- **GIVEN** the canonical seed includes FAPEMIG support data
- **WHEN** the footer later renders institutional acknowledgement
- **THEN** it SHALL use CMS-backed support data rather than duplicating hardcoded text.
