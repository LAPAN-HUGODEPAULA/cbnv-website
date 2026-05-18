# exports

## Purpose

Define CSV/XLSX export behavior, deterministic export structure, field coverage, and privacy-safe export constraints.

## ADDED Requirements

### Requirement: Submissions export

The platform MUST provide a submissions export for authorized committee users.

#### Scenario: Chair downloads submissions export

Given an authenticated chair user requests the submissions export  
When the export is generated  
Then it MUST include deterministic columns for submission code, title, thematic axis, status, modality and relevant timestamps.

### Requirement: Authors export

The platform MUST provide an authors export for authorized committee users.

#### Scenario: Chair downloads authors export

Given an authenticated chair user requests the authors export  
When the export is generated  
Then it MUST include ordered author rows linked to submission codes.

### Requirement: Institutions export

The platform MUST provide an institutions export for authorized committee users.

#### Scenario: Chair downloads institutions export

Given submissions contain author institution data  
When the institutions export is generated  
Then it MUST include institution names and aggregate counts.

### Requirement: Proceedings export

The platform MUST provide a proceedings-support export for authorized committee users.

#### Scenario: Chair downloads proceedings export

Given validated proceedings-eligible submissions exist  
When the proceedings export is generated  
Then it MUST include submission code, title, authors, affiliations, abstract, thematic axis, final modality and proceedings status.

### Requirement: Review and decision export

The platform MUST provide review and decision exports with permission controls.

#### Scenario: Chair downloads review export

Given an authenticated chair user requests the review export  
When the export is generated  
Then it MUST include review or decision metadata according to the chair permission level.

#### Scenario: Unauthorized user requests review export

Given a user without committee permission requests the review export  
Then access MUST be denied.

### Requirement: CSV encoding

CSV exports MUST use UTF-8 encoding and deterministic column order.

#### Scenario: CSV export is generated

Given a committee user downloads a CSV export  
When the file is opened  
Then the header order MUST be stable and the encoding MUST support Brazilian Portuguese text.

### Requirement: XLSX support

XLSX exports MUST be implemented if project dependency support exists, otherwise the CSV-only limitation MUST be documented.

#### Scenario: XLSX dependency is available

Given the project has an approved XLSX generation dependency  
When a committee user downloads an XLSX export  
Then the workbook MUST use deterministic sheet names and column order.

#### Scenario: XLSX is not implemented

Given XLSX export is not implemented in this change  
When documentation is inspected  
Then the limitation MUST be documented and CSV exports MUST remain available.

### Requirement: Protected files excluded

Exports MUST NOT expose protected file URLs.

#### Scenario: Export includes final material metadata

Given a final material has a protected file  
When an export is generated  
Then the export MUST NOT include a direct protected file URL.
