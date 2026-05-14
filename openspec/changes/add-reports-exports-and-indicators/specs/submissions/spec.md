# submissions

## Purpose

Define submission-related reporting and export requirements, including status, thematic axis, modality, author and institution data.

## ADDED Requirements

### Requirement: Submission report data source

Submission reports MUST derive from the canonical submission models.

#### Scenario: Submission report is generated

Given submissions exist  
When a report or export is generated  
Then the data MUST come from the submission records and related author records.

### Requirement: Submission filters

Submission reports and exports MUST support practical filtering by workflow fields where feasible.

#### Scenario: Status filter applied

Given a chair user filters reports by submission status  
When the report is generated  
Then the result MUST include only matching submissions.

#### Scenario: Thematic axis filter applied

Given a chair user filters reports by thematic axis  
When the report is generated  
Then the result MUST include only matching submissions.

### Requirement: Submission export ownership privacy

Submission exports MUST include personal data only for authorized internal users.

#### Scenario: Chair downloads submission export

Given a chair user downloads submission export  
Then the export MAY include submitter/corresponding-author identity fields according to documented privacy rules.

#### Scenario: Non-privileged user requests submission export

Given a non-privileged user requests submission export  
Then access MUST be denied.
