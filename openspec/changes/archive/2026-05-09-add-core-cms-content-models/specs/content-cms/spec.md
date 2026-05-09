# Content CMS Delta

## ADDED Requirements

### Requirement: Clear admin labels

CMS fields SHALL use clear Portuguese labels and help text where needed.

#### Scenario: Admin edits a public link

Given the admin edits an external link field
When the field is displayed in the CMS
Then the label and help text SHALL make clear where the link appears or what it controls.

### Requirement: Visibility controls

CMS editorial models SHALL include simple visibility controls.

#### Scenario: Admin hides content

Given a news item or supporting entity should not appear publicly
When the admin marks it as draft, hidden or inactive
Then later public queries SHALL exclude it.

### Requirement: External public links

The platform SHALL centralize external public links used across the site.

#### Scenario: Registration link is configured

Given the registration platform is external
When the admin sets a registration URL and status
Then public templates SHALL be able to render either the configured link or a clear "em breve" state.

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
