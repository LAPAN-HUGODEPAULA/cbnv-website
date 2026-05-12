# Content Placement Review (content)

## Purpose
Define review expectations for public-site content placement, copy risk, content gaps and handoff into content production.

## Requirements

### Requirement: Content placement diagnosis
The review SHALL identify content gaps, copy risks and misplaced or redundant content.

#### Scenario: Copy risk is identified
- **GIVEN** the review finds exaggerated, misleading or unsupported copy
- **WHEN** the backlog is inspected
- **THEN** the finding SHALL be categorized as `copy-risk` and assigned to a follow-up proposal.

#### Scenario: Content gap is identified
- **GIVEN** a page lacks sufficient explanation for its user journey
- **WHEN** the backlog is inspected
- **THEN** the finding SHALL be categorized as `copy-gap` and assigned to `produce-public-site-content-round-1` unless another proposal is more appropriate.

### Requirement: Content production handoff
The review SHALL produce a handoff for the content-production proposal.

#### Scenario: Content handoff exists
- **GIVEN** the review report exists
- **WHEN** the handoff section is inspected
- **THEN** it SHALL list pages and sections requiring new, shorter, longer, clearer or corrected copy.
