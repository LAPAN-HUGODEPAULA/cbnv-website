# notifications

## Purpose

Define verification requirements for notification copy, triggers, recipients, state transitions, duplicate-send risk and dashboard consistency after notifications.

## ADDED Requirements

### Requirement: Notification trigger matrix

The audit MUST create a notification trigger consistency matrix.

#### Scenario: Matrix is produced

Given notification flows exist
When the audit is completed
Then `docs/reviews/notification-trigger-consistency-round-1.md` MUST exist.

### Requirement: Notification copy consistency

The audit MUST verify notification subject and body terminology.

#### Scenario: Submission confirmation email reviewed

Given a submission confirmation notification exists
When it is reviewed
Then its terminology MUST match public submission rules and author dashboard status.

### Requirement: Notification timing consistency

The audit MUST verify that notifications are sent at the correct workflow transition.

#### Scenario: Final materials requested notification reviewed

Given final materials are requested
When the notification trigger is reviewed
Then the notification MUST align with the submission entering the final-materials phase.
