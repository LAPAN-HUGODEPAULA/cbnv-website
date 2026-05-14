# reviews

## Purpose

Define verification requirements for reviewer-facing, chair-facing and author-facing review and decision labels, including intentional persona asymmetry.

## ADDED Requirements

### Requirement: Review workflow status mapping

The audit MUST map review assignment, review and decision states by persona.

#### Scenario: Review status checked

Given a submission is under review
When author, reviewer and chair surfaces are compared
Then status labels MUST be documented as consistent or intentionally asymmetric.

### Requirement: Decision label consistency

Decision labels MUST be checked across chair dashboards, author dashboards, notifications and reports.

#### Scenario: Accepted oral decision appears

Given a submission has an accepted oral decision
When surfaces are compared
Then the modality label MUST be consistent or documented.

### Requirement: Reviewer privacy consistency

The audit MUST verify that reviewer identities and review content are not exposed in unauthorized contexts.

#### Scenario: Author sees decision result

Given an author views a decision status
When the page is reviewed
Then reviewer identity MUST not be exposed unless policy explicitly allows it.
