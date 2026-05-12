# Submissions

## Purpose

This delta specification ensures that the initial account foundation does not prematurely implement submission workflows while providing necessary placeholders.

## ADDED Requirements

### Requirement: No submission workflow in account foundation

The accounts/dashboard foundation SHALL not implement the author submission workflow.

#### Scenario: Author dashboard exists before submission flow

Given the author dashboard is implemented
When the user opens it
Then it MAY show a future submission placeholder
And SHALL NOT create, edit, submit or upload scientific submissions.

### Requirement: Future submission integration point

The author dashboard SHALL provide a clear integration point for the later submission-flow proposal.

#### Scenario: Later submission proposal starts

Given the author dashboard shell exists
When the submission-flow proposal is implemented later
Then it SHALL be able to attach submission listing/creation behavior without replacing authentication foundation.
