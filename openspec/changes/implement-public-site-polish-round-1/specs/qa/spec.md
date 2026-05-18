# qa

## Purpose

Define validation, traceability and test requirements for the implementation polish pass.

## ADDED Requirements

### Requirement: Implementation report

The change MUST include an implementation report.

#### Scenario: Implementation report exists

Given this change is completed  
When repository documents are inspected  
Then `docs/reviews/public-site-polish-round-1-implementation-report.md` MUST exist.

### Requirement: Finding traceability

Every non-trivial fix MUST be traceable to an audit finding or acceptance criterion.

#### Scenario: Template fix is made

Given a non-trivial template or copy fix is committed  
Then the implementation report MUST reference the source finding or rationale.

### Requirement: Validation commands

The change MUST pass required validation commands.

#### Scenario: Validation runs

Given the implementation is complete  
When validation is run  
Then OpenSpec validation, Django checks, migration dry-run and tests MUST pass unless a documented external limitation applies.
