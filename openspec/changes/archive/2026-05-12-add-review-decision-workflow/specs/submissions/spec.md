# submissions Delta

## ADDED Requirements

### Requirement: Submission status transitions for decision

The submission status machine SHALL support transitions from review states to final decision states.

#### Scenario: Decision to accept as oral
- **WHEN** a decision is made to accept a submission as oral presentation
- **THEN** the status SHALL transition to `accepted_oral` and `final_modality` SHALL be set to `oral`.

#### Scenario: Decision to reject
- **WHEN** a decision is made to reject a submission
- **THEN** the status SHALL transition to `rejected`.

### Requirement: Decision metadata

Submissions SHALL store the final modality and decision notes provided by the chair.

#### Scenario: Chair provides decision notes
- **WHEN** a chair issues a decision with notes
- **THEN** these notes SHALL be stored with the submission and included in the author notification.
