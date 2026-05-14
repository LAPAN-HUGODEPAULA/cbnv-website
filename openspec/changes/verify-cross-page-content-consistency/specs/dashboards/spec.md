# dashboards

## Purpose

Define verification requirements for public, author, reviewer and chair dashboard labels, navigation, role-specific states and workflow status presentation.

## ADDED Requirements

### Requirement: Dashboard persona consistency

The audit MUST verify each dashboard according to the persona it serves.

#### Scenario: Author dashboard reviewed

Given an author dashboard displays submissions and final materials
When the audit is performed
Then labels MUST align with author-facing terms in the persona status map.

### Requirement: Dashboard and notification state consistency

The audit MUST verify that dashboard states match notification-trigger outcomes.

#### Scenario: Notification sent after decision

Given a decision notification is sent
When the recipient dashboard is reviewed
Then the dashboard status MUST not contradict the notification.
