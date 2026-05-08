## ADDED Requirements

### Requirement: Tier-based Visual Hierarchy
The system SHALL display sponsors with a visual hierarchy that reflects their tier (e.g., Diamond logos larger than Gold, which are larger than Silver).

#### Scenario: Multi-tier sponsor display
- **WHEN** the Sponsors page is rendered
- **THEN** the Diamond tier sponsors are displayed at the top with a larger size than subsequent tiers

### Requirement: Sponsor External Linking
The system SHALL allow each sponsor logo to link to their respective external website when clicked.

#### Scenario: Visitor clicks a sponsor logo
- **WHEN** the visitor clicks on a sponsor's logo
- **THEN** they are redirected to the URL specified in the sponsor's CMS entry in a new tab
