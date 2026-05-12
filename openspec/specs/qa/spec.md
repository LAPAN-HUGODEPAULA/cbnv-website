# Review QA (qa)

## Purpose
Define quality gates for diagnostic review changes, including scope control, finding routing and severity classification.

## Requirements

### Requirement: Review-only change boundary
The review change SHALL not implement UI/layout/content fixes.

#### Scenario: Review PR contains diagnostics only
- **GIVEN** the PR for this change is inspected
- **WHEN** changed files are reviewed
- **THEN** changes SHALL be limited to OpenSpec files and review documentation unless a minor documentation-only supporting file is justified.

### Requirement: Follow-up routing
Every actionable finding SHALL be routed to an appropriate follow-up proposal.

#### Scenario: Finding has target proposal
- **GIVEN** a backlog finding exists
- **WHEN** its metadata is inspected
- **THEN** it SHALL include a target proposal such as `produce-public-site-content-round-1`, `verify-cross-page-content-consistency`, `implement-public-site-polish-round-1` or a named future proposal.

### Requirement: Severity classification
Every actionable finding SHALL have a severity classification.

#### Scenario: Finding has severity
- **GIVEN** a backlog finding exists
- **WHEN** it is inspected
- **THEN** it SHALL have severity P0, P1, P2 or P3.
