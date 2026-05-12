# qa Delta

## ADDED Requirements

### Requirement: Review workflow testing

The platform SHALL include automated tests for the full review and decision cycle.

#### Scenario: Review cycle test
- **WHEN** the test suite runs
- **THEN** it SHALL verify that a chair can assign a reviewer, the reviewer can submit an evaluation, and the chair can issue a final decision.

#### Scenario: Review permission test
- **WHEN** the test suite runs
- **THEN** it SHALL verify that unauthorized users cannot perform review or decision actions.
