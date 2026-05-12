# Content Placement Review Delta

## ADDED Requirements

### Requirement: Content placement diagnosis

The review SHALL identify content gaps, copy risks and misplaced or redundant content.

#### Scenario: Copy risk is identified

Given the review finds exaggerated, misleading or unsupported copy
When the backlog is inspected
Then the finding SHALL be categorized as `copy-risk` and assigned to a follow-up proposal.

#### Scenario: Content gap is identified

Given a page lacks sufficient explanation for its user journey
When the backlog is inspected
Then the finding SHALL be categorized as `copy-gap` and assigned to `produce-public-site-content-round-1` unless another proposal is more appropriate.

### Requirement: Content production handoff

The review SHALL produce a handoff for the content-production proposal.

#### Scenario: Content handoff exists

Given the review report exists
When the handoff section is inspected
Then it SHALL list pages and sections requiring new, shorter, longer, clearer or corrected copy.
