# reports

## Purpose

Define verification requirements for report labels, export headers, indicators, workflow status values, privacy boundaries and protected-file exclusion.

## ADDED Requirements

### Requirement: Report terminology consistency

The audit MUST verify report and indicator terminology against approved workflow terms.

#### Scenario: Report status label reviewed

Given a report displays submission status counts
When labels are reviewed
Then status terminology MUST match the persona status map or be documented.

### Requirement: Export header consistency

The audit MUST verify export column headers.

#### Scenario: CSV export reviewed

Given a CSV export is generated
When headers are reviewed
Then labels MUST use approved terminology and stable meaning.

### Requirement: Export privacy consistency

The audit MUST verify that exports do not expose protected files or unauthorized sensitive fields.

#### Scenario: Proceedings export reviewed

Given proceedings export includes final material metadata
When the export is reviewed
Then protected direct file URLs MUST not be present.
