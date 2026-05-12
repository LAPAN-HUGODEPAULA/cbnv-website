# reviews Delta

## ADDED Requirements

### Requirement: Evaluation form with scores and comments

The review form SHALL include numeric scores, qualitative comments for the author, and confidential notes for the commission.

#### Scenario: Reviewer fills evaluation form
- **WHEN** a reviewer fills out the scores (1-5), comments for authors, and confidential notes
- **THEN** all fields SHALL be saved correctly upon submission.

### Requirement: Decision issuance by chair

Chairs SHALL be able to issue a final decision and assign a final modality to submissions with completed reviews.

#### Scenario: Chair issues decision
- **WHEN** a chair selects a final decision (e.g., Accepted Oral) and provides decision notes
- **THEN** the submission status SHALL transition accordingly and the final modality SHALL be recorded.

## MODIFIED Requirements

### Requirement: Reviewer assignment
The scientific commission SHALL be able to assign one or more reviewers to a submission that is in the "submitted" or "admin_screening" status.

#### Scenario: Assigning a reviewer
- **WHEN** a commission member selects a reviewer for a specific work
- **THEN** an assignment record SHALL be created and the submission status SHALL transition to "assigned_to_reviewers" if it was in screening.
