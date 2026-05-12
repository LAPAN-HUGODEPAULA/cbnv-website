# videos Delta

## ADDED Requirements

### Requirement: YouTube URL Validation in Forms

Forms collecting YouTube links SHALL validate the URL format and reachability where practical.

#### Scenario: Author provides short URL
- **WHEN** an author provides a `youtu.be/ID` URL
- **THEN** the system SHALL correctly parse it as a valid YouTube video.
