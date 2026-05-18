# qa

## Purpose

Define test and validation expectations for reports, exports, indicators, permissions and privacy boundaries.

## ADDED Requirements

### Requirement: Report access tests

The test suite MUST cover report access permissions.

#### Scenario: Chair access test

Given tests run  
Then there MUST be coverage proving chair users can access reports.

#### Scenario: Unauthorized access test

Given tests run  
Then there MUST be coverage proving unauthorized users cannot access reports.

### Requirement: Indicator tests

The test suite MUST cover indicator calculations.

#### Scenario: Submission indicator test

Given test submissions exist  
When indicators are calculated  
Then tests MUST verify counts by status, thematic axis or modality.

#### Scenario: Proceedings indicator test

Given final-material/proceedings records exist  
When indicators are calculated  
Then tests MUST verify proceedings readiness counts.

### Requirement: Export structure tests

The test suite MUST cover export headers and deterministic structure.

#### Scenario: CSV header test

Given a CSV export is generated  
Then tests MUST verify the expected header order.

#### Scenario: XLSX structure test

Given XLSX export is implemented  
Then tests MUST verify expected sheet names and columns.

### Requirement: Export privacy tests

The test suite MUST verify privacy-sensitive export behavior.

#### Scenario: Protected file URL test

Given exports include final material metadata  
Then tests MUST verify protected direct file URLs are not exported.

#### Scenario: Unauthorized review export test

Given an unauthorized user requests review export  
Then tests MUST verify access is denied.

### Requirement: Validation commands

The change MUST pass project validation commands.

#### Scenario: Validation commands pass

Given implementation is complete  
When validation is run  
Then `openspec validate add-reports-exports-and-indicators --strict`, `uv run python manage.py check`, `uv run python manage.py makemigrations --check --dry-run`, and `uv run pytest` MUST pass.
