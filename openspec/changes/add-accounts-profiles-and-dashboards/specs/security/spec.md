# Account Security Delta

## ADDED Requirements

### Requirement: Safe authentication

Account authentication SHALL use Django authentication primitives.

#### Scenario: Password is set

Given a user registers
When their password is stored
Then it SHALL be stored using Django's password hashing, not plain text.

#### Scenario: CSRF protection is active

Given a user submits login, registration or profile forms
When the form is processed
Then Django CSRF protection SHALL apply.

### Requirement: Privilege escalation prevention

Public account forms SHALL not expose privileged role or staff fields.

#### Scenario: Public registration form is inspected

Given the registration form is rendered
When its fields are inspected
Then `is_staff`, `is_superuser` and chair role fields SHALL NOT be user-editable.

### Requirement: Role-protected internal areas

Role-specific dashboards SHALL enforce role checks.

#### Scenario: User lacks reviewer role

Given a user lacks reviewer role
When they request the reviewer dashboard
Then access SHALL be denied or redirected.

### Requirement: Safe redirects

Authentication views SHALL avoid unsafe redirects.

#### Scenario: Login next parameter is external

Given a login request includes an unsafe external `next` URL
When login succeeds
Then the user SHALL NOT be redirected to the unsafe external URL.
