# proceedings

# Purpose

The purpose of this capability is to manage the final materials for accepted submissions, including the upload, validation, and integration of these materials into the congress proceedings, as well as managing information about previous editions.

## ADDED Requirements

### Requirement: Final material submission

The platform SHALL allow authors of accepted submissions to upload final materials.

#### Scenario: Author uploads final materials
- **WHEN** an author of an accepted submission uploads a final PDF, presentation, and video link
- **THEN** a `FinalMaterial` record SHALL be created or updated.

### Requirement: Admin validation of materials

The scientific committee SHALL be able to validate received final materials.

#### Scenario: Admin validates materials
- **WHEN** an admin reviews and validates a `FinalMaterial` record
- **THEN** the validation timestamp and user SHALL be recorded, and the author SHALL be notified.

### Requirement: Previous editions management

The system SHALL support the management of previous congress editions and their external links.

#### Scenario: Admin registers previous edition
- **WHEN** an admin creates an `Edition` snippet in Wagtail
- **THEN** it SHALL be available to be listed in the public site.
