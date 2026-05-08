## ADDED Requirements

### Requirement: Reviewer assignment notification
The system SHALL notify reviewers via email when a new work is assigned to them for review.

#### Scenario: Notifying reviewer
- **WHEN** a reviewer is assigned to a work
- **THEN** an email containing the work title and link to the reviewer portal SHALL be sent

### Requirement: Decision notification for authors
Authors SHALL be notified via email when a final decision (Accept/Reject) or a request for corrections is issued.

#### Scenario: Notifying author of corrections
- **WHEN** the commission issues an "Accepted with Corrections" decision
- **THEN** an email with the reviewer comments and instructions for revision SHALL be sent to the corresponding author
