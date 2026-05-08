## ADDED Requirements

### Requirement: Review progress summary
The system SHALL provide a summary view for the commission showing the number of reviews completed vs pending for each submission.

#### Scenario: Viewing progress summary
- **WHEN** a commission member accesses the reports dashboard
- **THEN** they SHALL see a list of works with their current review status and reviewer assignments

### Requirement: Submission status export
The system SHALL allow the commission to export a list of all submissions with their final decisions and assigned modalities in CSV format.

#### Scenario: Exporting decisions
- **WHEN** the commission clicks the "Export Decisions" button
- **THEN** a CSV file with ID, Title, Author, Status, and Modality SHALL be downloaded
