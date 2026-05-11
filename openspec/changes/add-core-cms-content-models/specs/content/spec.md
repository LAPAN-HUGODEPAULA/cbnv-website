# Content CMS Delta

## ADDED Requirements

### Requirement: Global site settings

The platform SHALL provide editable global site settings for reusable event and site metadata.

#### Scenario: Admin edits event identity

Given the admin opens global site settings
When they update the event name, short name, theme, dates, city or format
Then the updated values SHALL be saved in a central CMS-backed location.

#### Scenario: Public templates can access global settings

Given a public template needs global event metadata
When the template renders
Then it SHALL be able to retrieve the values from the central settings model or documented template context mechanism.

### Requirement: External public links

The platform SHALL centralize external public links used across the site.

#### Scenario: Registration link is configured

Given the registration platform is external
When the admin sets a registration URL and status
Then public templates SHALL be able to render either the configured link or a clear “em breve” state.

#### Scenario: Social and media links are configured

Given YouTube or Instagram links are available
When the admin edits global settings
Then those links SHALL be stored centrally and reusable by public templates.

### Requirement: Institutional acknowledgement

The platform SHALL provide a central CMS-backed field or slot for FAPEMIG acknowledgement.

#### Scenario: Footer needs FAPEMIG acknowledgement

Given the footer or public page needs to show institutional support
When the page renders
Then it SHALL be able to obtain the FAPEMIG acknowledgement from the central CMS-backed source.

### Requirement: News and announcements

The platform SHALL provide CMS-backed news or announcement entries.

#### Scenario: Admin creates announcement

Given the admin creates a news or announcement entry
When the entry is published
Then it SHALL become available for later public-page rendering.

#### Scenario: Home can select featured news

Given multiple news or announcement entries exist
When one or more are marked as featured
Then later Home rendering SHALL be able to retrieve featured entries.

#### Scenario: Draft news is hidden

Given a news or announcement entry has draft status
When public content queries are used
Then the draft entry SHALL NOT be returned as publicly visible.

### Requirement: Supporting entities

The platform SHALL provide CMS-backed entities for partners, supporters, sponsors and institutional acknowledgements.

#### Scenario: Admin creates supporting entity

Given the admin creates a supporting entity with name, category and status
When the entity is active
Then it SHALL be available for later public display according to its display flags.

#### Scenario: Hidden entity is not public

Given a supporting entity is hidden or inactive
When public display queries are used
Then the entity SHALL NOT be returned for public display.

#### Scenario: Entity display order is deterministic

Given multiple supporting entities exist
When they are queried for public display
Then they SHALL be ordered by configured sort order and a deterministic fallback.
