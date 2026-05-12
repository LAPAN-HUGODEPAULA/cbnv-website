# accounts

## Purpose

Define how the initial submission flow integrates with authenticated users, author profiles, and profile metadata without introducing a custom user model.

## ADDED Requirements

### Requirement: Submission requires authenticated author identity

Initial submissions SHALL be associated with an authenticated user.

#### Scenario: Submission owner is recorded

Given an authenticated author creates a submission  
When the submission is saved  
Then the submitting user SHALL be stored as the owner or submitter.

### Requirement: Author role integration

The submission flow SHALL integrate with profile author role.

#### Scenario: User starts first submission

Given an authenticated user without author role attempts to start a submission  
When the system handles the request  
Then the system SHALL either assign author role according to documented policy or redirect the user to complete author profile/role setup.

### Requirement: Author profile metadata reuse

The submission flow SHALL support reuse of profile metadata where appropriate.

#### Scenario: Corresponding author defaults

Given an authenticated author has profile name, e-mail and institution  
When they open the initial submission form  
Then the form SHALL be able to prefill corresponding author metadata from the profile when the implementation provides this convenience behavior.
