## ADDED Requirements

### Requirement: Final decision and modality
The scientific commission SHALL issue a final decision (Accepted, Rejected, Accepted with Corrections) and assign a presentation modality (Oral, Poster, Video).

#### Scenario: Issuing an acceptance decision
- **WHEN** the commission selects "Accepted" and modality "Oral"
- **THEN** the submission status SHALL transition to "Accepted" and the modality SHALL be recorded

### Requirement: Revision submission for corrections
If a work is "Accepted with Corrections", the author SHALL be allowed to upload a revised PDF file.

#### Scenario: Author uploads revised PDF
- **WHEN** a submission is in "Accepted with Corrections" status and the author uploads a new file
- **THEN** the system SHALL store the revised file and notify the commission

### Requirement: Simplified author status language
The author dashboard SHALL display submission status using user-friendly terms: "In Evaluation" (for Under Review), "Pending Corrections" (for Accepted with Corrections), and "Finalized" (for Accepted/Rejected).

#### Scenario: Author checks dashboard status
- **WHEN** a submission is internally "Under Review"
- **THEN** the author dashboard SHALL display "In Evaluation"
