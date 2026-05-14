# qa

## Purpose

Define validation, documentation and optional automation expectations for the consistency verification change.

## ADDED Requirements

### Requirement: Required review documents

The change MUST produce the required review documents.

#### Scenario: Documents exist

Given the change is completed
When repository documents are inspected
Then required consistency, backlog, persona-status, legacy-fact, automation-candidate and notification-trigger documents MUST exist.

### Requirement: Two-profile review evidence

The audit MUST record evidence from empty/default and populated/custom data profiles.

#### Scenario: Finding recorded

Given a finding is documented
When the finding is inspected
Then it MUST include the data profile that exposed it.

### Requirement: Automation candidates

The audit MUST identify automation candidates for recurring consistency checks.

#### Scenario: Automation candidate documented

Given a high-risk repeated fact or label exists
When the audit is completed
Then an automation candidate MUST be documented or explicitly rejected with rationale.

### Requirement: OpenSpec validation

The change MUST pass OpenSpec validation.

#### Scenario: OpenSpec validation runs

Given the change files are present
When `openspec validate verify-cross-page-content-consistency --strict` is run
Then validation MUST pass.
