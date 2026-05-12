# notifications Delta

## ADDED Requirements

### Requirement: Reviewer assigned notification

The system SHALL notify reviewers via e-mail when they are assigned to a submission.

#### Scenario: Reviewer notified of assignment
- **WHEN** a chair assigns a reviewer to a submission
- **THEN** an e-mail SHALL be sent to the reviewer with the submission title and a link to the evaluation form.

### Requirement: Decision notification for authors

The system SHALL notify authors via e-mail when a final decision has been issued for their submission.

#### Scenario: Author notified of decision
- **WHEN** a chair issues a final decision for a submission
- **THEN** an e-mail SHALL be sent to the corresponding author containing the decision outcome and any public notes from the commission.
