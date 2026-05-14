# submissions

## Purpose

Define verification requirements for submission instructions, author-facing labels, dashboard states, upload messages and initial-video rules.

## ADDED Requirements

### Requirement: Submission status persona mapping

The audit MUST map internal submission statuses to labels shown to each persona.

#### Scenario: Author status label differs from chair status label

Given an internal submission status has different author and chair labels
When the audit is performed
Then the difference MUST be documented as intentional or flagged.

### Requirement: Initial video rule consistency

The audit MUST verify that initial submission surfaces consistently state that video is not required initially.

#### Scenario: Initial submission form reviewed

Given the initial submission form and public submission page exist
When they are reviewed
Then they MUST not require or imply video during initial submission.

### Requirement: Submission CTA status consistency

The audit MUST verify consistency between public submission CTAs and author dashboard submission availability.

#### Scenario: Public page says submissions are closed

Given the public page indicates submissions are closed
When the author dashboard is reviewed
Then the dashboard MUST not present unrestricted new-submission actions.
