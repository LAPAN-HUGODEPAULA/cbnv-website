## ADDED Requirements

### Requirement: Account Creation Notification
The system SHALL send a confirmation email to the user upon successful registration.

#### Scenario: User receives welcome email
- **WHEN** a new account is created
- **THEN** an email is sent to the registered address with a welcome message and login instructions.

### Requirement: Role Assignment Notification
The system SHALL notify users when a new scientific role (Reviewer, Chair) is assigned to them by an administrator.

#### Scenario: Reviewer is notified of role change
- **WHEN** an administrator sets `is_reviewer=True` for an existing user
- **THEN** the user receives a notification informing them of their new responsibilities.
