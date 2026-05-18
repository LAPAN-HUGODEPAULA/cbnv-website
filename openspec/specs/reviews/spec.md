# reviews

## Purpose

Define report and export requirements for review assignments, review status, decisions and reviewer-sensitive data.

## ADDED Requirements

### Requirement: Review indicators for committee

Review indicators MUST be available to chair/scientific committee users.

#### Scenario: Chair views review indicators

Given review assignments exist  
When a chair user views reports  
Then they MUST see pending and completed review counts.

### Requirement: Decision indicators for committee

Decision indicators MUST be available to chair/scientific committee users.

#### Scenario: Chair views decision indicators

Given decisions exist  
When a chair user views reports  
Then they MUST see counts by decision outcome and final modality.

### Requirement: Reviewer identity protection

Reviewer identity and review text MUST only appear in exports for users with explicit committee permission.

#### Scenario: Chair exports review data

Given a chair user requests review export  
Then reviewer identity MAY be included according to documented permission rules.

#### Scenario: Unauthorized user exports review data

Given a user without committee permission requests review export  
Then access MUST be denied.

### Requirement: Review text protection

Review text and internal notes MUST be excluded from broad exports unless explicitly permitted.

#### Scenario: Standard review summary export generated

Given a standard review summary export is generated  
Then it MUST include review status metadata and MUST exclude full review text unless the export type explicitly allows it.
