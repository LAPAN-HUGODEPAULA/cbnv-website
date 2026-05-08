## ADDED Requirements

### Requirement: Author account type enforcement
The system SHALL ensure that only users with the `is_author` flag set to `True` (or superusers) can access the submission forms and author dashboard.

#### Scenario: Unauthorized access prevention
- **WHEN** a regular user (is_author=False) attempts to access `/submissions/new/`
- **THEN** the system SHALL redirect to the login page or return a 403 Forbidden error

### Requirement: Author profile completion
To start a submission, authors MUST have their profile fields completed: `first_name`, `last_name`, `institution`, and `country` must all be non-blank. This SHALL be implemented as a `has_complete_author_profile()` method or property on `accounts.User`.

#### Scenario: Redirect to profile
- **WHEN** an author with an incomplete profile (missing any of first_name, last_name, institution, country) tries to start a new submission
- **THEN** the system SHALL redirect them to the profile edit page with a message indicating which fields are missing

#### Scenario: Complete profile allowed
- **WHEN** an author with all required fields filled accesses `/submissions/new/`
- **THEN** the system SHALL display the submission wizard
