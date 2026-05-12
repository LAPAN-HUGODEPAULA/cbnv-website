# Accounts-Auth

## Purpose

This delta specification defines the requirements for user accounts, profiles, and role management, ensuring a solid foundation for scientific workflows.

## ADDED Requirements

### Requirement: Default Django User authentication

The platform SHALL use Django's default User model for account authentication.

#### Scenario: Default User remains active

Given Django settings are loaded
When the authentication user model is inspected
Then the platform SHALL use Django's default User model and SHALL NOT introduce a custom user model for this change.

### Requirement: UserProfile metadata

The platform SHALL store congress-specific user metadata in a profile model linked one-to-one with Django User.

#### Scenario: Profile exists for registered user

Given a user registers through the public account flow
When registration completes
Then a `UserProfile` or equivalent profile SHALL exist for that user.

#### Scenario: Profile stores institution metadata

Given a user edits their profile
When institution, country and position are saved
Then those values SHALL be stored in the profile, not in custom User fields.

### Requirement: Independent scientific role flags

The profile SHALL support independent role flags for author, reviewer and chair/scientific committee.

#### Scenario: User has multiple roles

Given a user is both author and reviewer
When their profile is inspected
Then both author and reviewer role flags MAY be true.

#### Scenario: Chair role is privileged

Given a public user registers
When the registration form is submitted
Then the user SHALL NOT be able to grant themselves chair/scientific committee access.
