# Public Site Content Integration

# Purpose
Define how content is structured, integrated, and framed across public-facing pages, focusing on coverage and appropriate context.

## ADDED Requirements

### Requirement: Page-specific content coverage

Round-1 content SHALL cover every MVP public page.

#### Scenario: Home content is produced

Given the content document exists  
When the Home section is inspected  
Then it SHALL include hero copy, short event description, CTA/microcopy and section guidance.

#### Scenario: About content is produced

Given the content document exists  
When the About section is inspected  
Then it SHALL include expanded institutional/scientific copy and 2026 theme context.

#### Scenario: Program content is produced

Given the content document exists  
When the Program section is inspected  
Then it SHALL include introductory and status/pending-participant language consistent with the current program.

#### Scenario: Registration content is produced

Given the content document exists  
When the Registration section is inspected  
Then it SHALL explain that registration is external and may be unavailable or coming soon.

### Requirement: Previous editions framed as archive

Previous-edition content SHALL be framed as archive/history.

#### Scenario: Previous editions copy is inspected

Given the Previous Editions copy is read  
Then it SHALL NOT present legacy facts as current 2026 event facts.

### Requirement: Footer content is concise

Footer copy SHALL be concise and avoid redundant long slogans.

#### Scenario: Footer copy is inspected

Given footer content exists  
Then it SHALL include institutional acknowledgement needs without repeating the full event pitch unnecessarily.
