## ADDED Requirements

### Requirement: Protected submission storage
Files uploaded as part of a scientific submission SHALL be stored in a directory that is NOT served by the public web server (e.g., outside the `media/` public root or via a private S3 bucket).

#### Scenario: Direct URL access denial
- **WHEN** an unauthenticated user attempts to access a submission PDF via its direct file path URL
- **THEN** the web server or application SHALL return a 403 Forbidden or 404 Not Found error

### Requirement: Controlled file download
The system SHALL provide a dedicated view that checks for appropriate permissions before serving a submission file. In Phase 1, only the submitting author may download their own submission PDF.

#### Scenario: Author downloading their own work
- **WHEN** an authenticated author requests their own submitted PDF through the secure download endpoint
- **THEN** the system SHALL stream the file to the user

#### Scenario: Author cannot download others' work
- **WHEN** an authenticated author attempts to download a submission PDF that belongs to another user
- **THEN** the system SHALL return a 403 Forbidden error
