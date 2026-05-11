# Public Site CMS Integration Delta

## ADDED Requirements

### Requirement: Public layout consumes CMS-backed globals

The public layout SHALL be able to consume CMS-backed global values instead of hardcoded repeated values.

#### Scenario: Footer consumes global settings

Given the footer needs event identity, social links or institutional acknowledgement
When the footer renders
Then it SHALL use CMS-backed global settings where available.

#### Scenario: Header consumes global link state

Given the header needs a registration CTA
When registration is not yet available
Then the header SHALL be able to render a clear “em breve” state instead of a broken link.

### Requirement: Public pages can query featured content

Public pages SHALL be able to query featured news/announcements and supporting entities.

#### Scenario: Home requests featured news

Given the Home page later needs a latest-news block
When it queries CMS content
Then it SHALL be able to retrieve published featured or recent news entries.

#### Scenario: Footer requests supporting entities

Given the footer later needs supporting entities
When it queries CMS content
Then it SHALL be able to retrieve active entities marked for footer display.

### Requirement: No final page implementation in CMS foundation

This CMS foundation change SHALL NOT implement the final public pages.

#### Scenario: CMS models are implemented before pages

Given this change is complete
When the public-site MVP proposal starts
Then it SHALL be able to consume CMS models created here without this change having implemented full public-page templates.
