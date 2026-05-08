## ADDED Requirements

### Requirement: Submission confirmation email
The system SHALL send an automated email confirmation to the corresponding author immediately after a successful submission (transition to Submitted status).

#### Scenario: Sending confirmation
- **WHEN** a submission is finalized and its status becomes "Submitted"
- **THEN** the system SHALL queue and send an email to the corresponding author's address

### Requirement: Email templates
Confirmation emails SHALL include the submission title, the assigned submission ID, and a summary of the next steps in the evaluation process.

#### Scenario: Email content verification
- **WHEN** the confirmation email is generated
- **THEN** it SHALL contain the title of the work and its unique identifier

### Requirement: Email language
Confirmation emails SHALL be written in Portuguese Brazilian, matching the institutional/scientific tone of the congress.
