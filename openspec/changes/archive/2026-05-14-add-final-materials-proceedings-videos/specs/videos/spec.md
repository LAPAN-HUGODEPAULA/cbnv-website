# videos

# Purpose

The purpose of this capability is to handle the integration and validation of video content, specifically YouTube links, for submissions and other congress materials.

## ADDED Requirements

### Requirement: YouTube URL Validation in Forms

Forms collecting YouTube links SHALL validate the URL format and reachability where practical.

#### Scenario: Author provides short URL
- **WHEN** an author provides a `youtu.be/ID` URL
- **THEN** the system SHALL correctly parse it as a valid YouTube video.
