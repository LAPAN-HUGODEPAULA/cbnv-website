# CMS Admin Delta

## ADDED Requirements

### Requirement: Single-admin editorial workflow

The CMS SHALL support a simple single-admin editorial workflow for MVP.

#### Scenario: Admin manages global settings

Given the central admin accesses the Wagtail admin
When they open global site settings
Then they SHALL be able to update key event/site metadata without code changes.

#### Scenario: Admin manages news

Given the central admin accesses the Wagtail admin
When they create or update a news/announcement entry
Then the entry SHALL be manageable without developer intervention.

#### Scenario: Admin manages supporting entities

Given the central admin accesses the Wagtail admin
When they create or update partners, supporters or sponsors
Then those entities SHALL be manageable without developer intervention.

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
