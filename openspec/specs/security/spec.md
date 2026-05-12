# security Specification

## Purpose
Define authentication, authorization, CSRF, object-level permission, and private-file security requirements for the core platform and scientific flows.
## Requirements
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

### Requirement: Object-level submission permissions

Submission detail, edit and file views SHALL enforce object-level ownership checks.

#### Scenario: User requests another user's submission

Given a submission belongs to another user  
When the current user requests its detail page  
Then access SHALL be denied.

### Requirement: CSRF protection

Submission forms SHALL use Django CSRF protection.

#### Scenario: Submission form posted

Given an author posts the submission form  
When CSRF validation fails  
Then the submission SHALL NOT be accepted.

### Requirement: No public exposure of private files

Submission files SHALL remain private by default.

#### Scenario: File URL is rendered

Given a submission file exists  
When public pages render  
Then they SHALL NOT expose direct public file URLs.

### Requirement: Submitted records protected from accidental modification

Submitted records SHALL be read-only to authors by default unless reopened by an explicit later workflow.

#### Scenario: Author edits submitted submission

Given a submission is submitted  
When the author attempts to edit it  
Then the system SHALL deny editing or show read-only state unless the submission has been reopened.

### Requirement: Review access control

Access to reviewer-only and chair-only views SHALL be strictly enforced based on user roles.

#### Scenario: Unauthorized access to assignment
- **WHEN** a non-chair user attempts to access the reviewer assignment view
- **THEN** access SHALL be denied (403 Forbidden).

#### Scenario: Unauthorized access to review form
- **WHEN** a user who is not the assigned reviewer attempts to access a specific evaluation form
- **THEN** access SHALL be denied (403 Forbidden).

### Requirement: Single-blind anonymity

Reviewer identities SHALL NOT be exposed to authors.

#### Scenario: Author views submission details
- **WHEN** an author views the decision or feedback on their submission
- **THEN** the names of the reviewers SHALL NOT be displayed.

