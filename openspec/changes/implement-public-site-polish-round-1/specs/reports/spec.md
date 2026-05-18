# reports

## Purpose

Define implementation requirements for aligning report labels, export headers, indicator labels and privacy-sensitive report behavior with the consistency audit.

## MODIFIED Requirements

### Requirement: Export headers use approved terminology

Export headers MUST use approved terminology from the consistency audit.

#### Scenario: Export header mismatch exists

Given the audit identifies an export header mismatch  
When this polish change is implemented  
Then the header MUST be corrected or explicitly deferred.

### Requirement: Exports avoid protected file URLs

Exports MUST not include protected direct file URLs.

#### Scenario: Protected URL exposure finding exists

Given the audit identifies protected file URL exposure in an export  
When this polish change is implemented  
Then the protected URL MUST be removed or the export MUST be disabled until corrected.
