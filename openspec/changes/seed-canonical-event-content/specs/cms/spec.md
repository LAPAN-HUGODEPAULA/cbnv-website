# CMS Seed Delta

## ADDED Requirements

### Requirement: Idempotent CMS seed

The platform SHALL provide an idempotent seed mechanism for canonical CMS content.

#### Scenario: Seed can run twice

Given the seed command or fixture has been executed once  
When it is executed again  
Then it SHALL complete successfully without creating duplicate global settings or supporting entities.

#### Scenario: Seed reports results

Given the seed command is executed  
When it completes  
Then it SHOULD report created, updated or skipped records in a readable summary.

### Requirement: Manual edits are protected where appropriate

The seed mechanism SHALL document whether it overwrites existing values or only creates missing content.

#### Scenario: Idempotence behavior is documented

Given a developer reads the seed documentation  
When they inspect how existing records are handled  
Then they SHALL know which fields are authoritative and which fields are preserved after manual edits.

### Requirement: Pending external links are represented safely

The seed SHALL represent unknown external links with an explicit pending state rather than broken placeholder URLs.

#### Scenario: Unknown registration URL

Given the registration URL is not known  
When canonical content is seeded  
Then registration status SHALL be stored as coming soon or equivalent  
And the seed SHALL NOT store `#` as the registration URL.
