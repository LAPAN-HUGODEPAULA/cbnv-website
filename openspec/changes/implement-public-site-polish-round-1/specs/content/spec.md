# content

## Purpose

Define implementation requirements for applying consistency-audit content fixes, including copy, terminology, duplicated sections and canonical source alignment.

## MODIFIED Requirements

### Requirement: Content findings are traceably implemented

Content corrections MUST map to documented consistency findings.

#### Scenario: Content finding is fixed

Given a content finding exists in the consistency backlog  
When the corresponding copy is changed  
Then the implementation report MUST reference the finding ID.

### Requirement: Repeated terms use approved terminology

Repeated public and internal terms MUST use approved terminology from the consistency audit.

#### Scenario: Deprecated term appears

Given the consistency audit marks a term as deprecated  
When this polish change updates the affected surface  
Then the deprecated term MUST be replaced or deferred with rationale.
