# security

## Purpose

Define authentication, authorization, CSRF, object-level permission, and private-file security requirements for the initial submission flow.

## ADDED Requirements

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
