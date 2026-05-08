## ADDED Requirements

### Requirement: Reviewer assignment
The scientific commission SHALL be able to assign one or more reviewers to a submission that is in the "Submitted" status.

#### Scenario: Assigning a reviewer
- **WHEN** a commission member selects a reviewer for a specific work
- **THEN** an assignment record SHALL be created and the submission status SHALL transition to "Under Review"

### Requirement: Reviewer feedback form
Reviewers SHALL provide feedback through a standardized form including a recommendation (Accept, Reject, Corrections) and qualitative comments.

#### Scenario: Submitting a review
- **WHEN** a reviewer completes the feedback form and submits
- **THEN** the review SHALL be saved and the commission SHALL be notified

### Requirement: Single-blind review
The system SHALL support single-blind review where reviewers can see author names but authors CANNOT see reviewer names.

#### Scenario: Author viewing review
- **WHEN** an author views their work's feedback
- **THEN** the reviewer's identity SHALL be hidden, showing only the comments and recommendations
