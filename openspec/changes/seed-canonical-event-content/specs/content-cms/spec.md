# Content CMS Delta (seed-canonical-event-content)

## ADDED Requirements

### Requirement: Idempotent CMS seed
The platform SHALL provide an idempotent seed mechanism for canonical CMS content.

#### Scenario: Seed can run twice
- **GIVEN** the seed command or fixture has been executed once
- **WHEN** it is executed again
- **THEN** it SHALL complete successfully without creating duplicate global settings or supporting entities.

#### Scenario: Seed reports results
- **GIVEN** the seed command is executed
- **WHEN** it completes
- **THEN** it SHOULD report created, updated or skipped records in a readable summary.

### Requirement: Manual edits are protected where appropriate
The seed mechanism SHALL document whether it overwrites existing values or only creates missing content.

#### Scenario: Idempotence behavior is documented
- **GIVEN** a developer reads the seed documentation
- **WHEN** they inspect how existing records are handled
- **THEN** they SHALL know which fields are authoritative and which fields are preserved after manual edits.

### Requirement: Pending external links are represented safely
The seed SHALL represent unknown external links with an explicit pending state rather than broken placeholder URLs.

#### Scenario: Unknown registration URL
- **GIVEN** the registration URL is not known
- **WHEN** canonical content is seeded
- **THEN** registration status SHALL be stored as coming soon or equivalent
- **AND** the seed SHALL NOT store `#` as the registration URL.

### Requirement: Canonical event identity seed
The platform SHALL provide a seed mechanism for canonical CBNV 2026 event identity.

#### Scenario: Seed event identity
- **GIVEN** the CMS global settings model exists
- **WHEN** the canonical content seed is executed
- **THEN** the formal event name, short name, edition, theme, dates, format, city, state and country SHALL be created or updated in the central settings model.

### Requirement: Canonical venue seed
The platform SHALL seed the official CBNV 2026 venue and address.

#### Scenario: Seed official venue
- **GIVEN** the canonical content seed is executed
- **WHEN** venue fields exist in the global settings model
- **THEN** the venue SHALL be set to CAD-1/UFMG with the official full address and Google Maps URL.

#### Scenario: Previous edition venue is not used
- **GIVEN** the seed is executed
- **WHEN** venue data is created or updated
- **THEN** it SHALL NOT use venue data inherited from previous CBNV editions.

### Requirement: Canonical supporting entities seed
The platform SHALL seed known institutional/support entities.

#### Scenario: Seed supporting entities
- **GIVEN** supporting-entity models exist
- **WHEN** the seed is executed
- **THEN** known entities such as UFMG, FUNDEP, FAPEMIG, Sociedade Brasileira de Neurovisão, HOLHOS, UFRJ, USP, UFRN and UEMG SHALL be created or updated.

#### Scenario: Supporting entities are not duplicated
- **GIVEN** the seed has already been executed once
- **WHEN** the seed is executed again
- **THEN** duplicate supporting entities SHALL NOT be created.

### Requirement: Conservative seeded content
Seeded content SHALL avoid unverified claims and final promotional copy.

#### Scenario: Seed avoids inflated claims
- **GIVEN** the seed creates default text or announcements
- **WHEN** the content is inspected
- **THEN** it SHALL NOT claim that the event is the largest in Latin America or use similarly unverified promotional claims.
