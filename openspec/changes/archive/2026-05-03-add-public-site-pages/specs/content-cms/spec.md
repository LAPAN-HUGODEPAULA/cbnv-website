## ADDED Requirements

### Requirement: Program Page Models
The system SHALL provide `ProgramPage` and `SpeakerIndexPage` models to manage and display the congress schedule and speaker list.

#### Scenario: Admin sets up program page
- **WHEN** the administrator creates a `ProgramPage` in the CMS
- **THEN** they can select program sessions to be displayed on that page

### Requirement: Sponsors Page Models
The system SHALL provide a `SponsorsPage` model to display the list of sponsors grouped by their respective tiers.

#### Scenario: Admin configures sponsors page
- **WHEN** the administrator creates a `SponsorsPage`
- **THEN** the system automatically pulls all active sponsors from the snippets and displays them by tier

### Requirement: Video Gallery Page Models
The system SHALL provide a `VideoGalleryPage` model to aggregate and display video resources linked to external platforms.

#### Scenario: Admin creates video gallery
- **WHEN** the administrator creates a `VideoGalleryPage`
- **THEN** they can select video categories or individual videos to show in the gallery
