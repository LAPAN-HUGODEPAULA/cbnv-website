## ADDED Requirements

### Requirement: Speaker Management
The system SHALL provide a management interface for congress speakers, including name, bio, photo, and affiliation.

#### Scenario: Admin adds a speaker
- **WHEN** the administrator enters speaker details in the CMS
- **THEN** the speaker is saved and available to be linked to program sessions

### Requirement: Program Session Management
The system SHALL allow the creation of program sessions with title, description, start time, end time, and linked speakers.

#### Scenario: Admin creates a session
- **WHEN** the administrator defines a session with a schedule and speakers
- **THEN** the session is stored and ready for public display

### Requirement: Public Program Schedule
The system SHALL display the congress program in a structured, chronologically ordered list accessible to all visitors.

#### Scenario: Visitor views the program
- **WHEN** the visitor navigates to the Program page
- **THEN** they see the list of sessions grouped by date and time
