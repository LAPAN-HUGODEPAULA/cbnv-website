# security Delta

## ADDED Requirements

### Requirement: Review access control

Access to reviewer-only and chair-only views SHALL be strictly enforced based on user roles.

#### Scenario: Unauthorized access to assignment
- **WHEN** a non-chair user attempts to access the reviewer assignment view
- **THEN** access SHALL be denied (403 Forbidden).

#### Scenario: Unauthorized access to review form
- **WHEN** a user who is not the assigned reviewer attempts to access a specific evaluation form
- **THEN** access SHALL be denied (403 Forbidden).

### Requirement: Single-blind anonymity

Reviewer identities SHALL NOT be exposed to authors.

#### Scenario: Author views submission details
- **WHEN** an author views the decision or feedback on their submission
- **THEN** the names of the reviewers SHALL NOT be displayed.
