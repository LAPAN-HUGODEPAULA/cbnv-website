# security

## Purpose

Define verification requirements for privacy-sensitive consistency checks, protected-file exposure, role-specific information boundaries and export/notification leakage risks.

## ADDED Requirements

### Requirement: Protected file exposure check

The audit MUST verify that protected files are not exposed through public pages, dashboards or exports.

#### Scenario: Final PDF reference reviewed

Given final material files are protected
When public pages and exports are reviewed
Then direct protected file URLs MUST not be visible to unauthorized users.

### Requirement: Role-specific privacy check

The audit MUST verify role-specific information boundaries.

#### Scenario: Reviewer identity reviewed

Given reviewer identity is sensitive
When author-facing pages, notifications and exports are reviewed
Then reviewer identity MUST not be exposed outside authorized contexts.

### Requirement: Notification privacy check

The audit MUST verify notification recipient and content privacy.

#### Scenario: Decision notification reviewed

Given a decision notification is sent
When recipient and body are reviewed
Then private review notes MUST not be sent to unauthorized recipients.
