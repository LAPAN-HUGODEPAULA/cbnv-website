# security

## Purpose

Define access control, privacy, and protected-data rules for reports, exports and indicators.

## ADDED Requirements

### Requirement: Reports require committee permission

Reports and exports MUST require chair/scientific committee permission by default.

#### Scenario: Chair accesses reports

Given an authenticated chair user  
When they request reports dashboard  
Then access MUST be allowed.

#### Scenario: Author accesses reports

Given an authenticated author without committee permission  
When they request reports dashboard  
Then access MUST be denied.

### Requirement: Exports require permission

Export endpoints MUST enforce permission checks.

#### Scenario: Unauthorized export request

Given a user without committee permission  
When they request any global export  
Then access MUST be denied.

### Requirement: Sensitive fields protected

Sensitive fields MUST only appear in exports for authorized users.

#### Scenario: Export includes e-mail fields

Given an export includes author e-mail fields  
When the export is generated  
Then the requesting user MUST have documented permission to access those fields.

### Requirement: Protected files excluded from exports

Protected file paths and direct file URLs MUST NOT be included in exports.

#### Scenario: Export includes final material data

Given final materials have protected files  
When an export is generated  
Then direct protected file paths and URLs MUST be excluded.

### Requirement: Public data separation

Public proceedings data MUST be distinguished from internal reports.

#### Scenario: Public proceedings export is generated

Given an export is intended for public proceedings support  
When fields are selected  
Then the export MUST include only publication-approved data unless explicitly marked internal.
