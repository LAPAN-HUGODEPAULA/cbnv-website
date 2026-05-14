# accessibility

## Purpose

Define verification requirements for consistency of non-visual content such as alt text, ARIA labels, icon labels, form labels and accessible status names.

## ADDED Requirements

### Requirement: Non-visual content consistency review

The audit MUST check non-visual content for consistency.

#### Scenario: Non-visual content reviewed

Given public pages and dashboards render icons, logos, forms and status badges
When the audit is performed
Then accessible labels and alt text MUST be reviewed.

### Requirement: Logo alt-text consistency

Institutional logo alt text MUST be consistent across contexts.

#### Scenario: FAPEMIG logo reviewed

Given the FAPEMIG logo appears in multiple locations
When alt text is compared
Then labels MUST be consistent or context-specific differences MUST be documented.

### Requirement: Status badge accessible-name consistency

Status badges MUST convey the same state textually and visually.

#### Scenario: Submission status badge reviewed

Given a submission status badge is rendered
When the accessible name is inspected
Then it MUST match the intended persona-facing status label.
