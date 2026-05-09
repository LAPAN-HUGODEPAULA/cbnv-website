# Canonical Content Delta

## ADDED Requirements

### Requirement: Canonical event identity seed

The platform SHALL provide a seed mechanism for canonical CBNV 2026 event identity.

#### Scenario: Seed event identity

Given the CMS global settings model exists  
When the canonical content seed is executed  
Then the formal event name, short name, edition, theme, dates, format, city, state and country SHALL be created or updated in the central settings model.

### Requirement: Canonical venue seed

The platform SHALL seed the official CBNV 2026 venue and address.

#### Scenario: Seed official venue

Given the canonical content seed is executed  
When venue fields exist in the global settings model  
Then the venue SHALL be set to CAD-1/UFMG with the official full address and Google Maps URL.

#### Scenario: Previous edition venue is not used

Given the seed is executed  
When venue data is created or updated  
Then it SHALL NOT use venue data inherited from previous CBNV editions.

### Requirement: Canonical supporting entities seed

The platform SHALL seed known institutional/support entities.

#### Scenario: Seed supporting entities

Given supporting-entity models exist  
When the seed is executed  
Then known entities such as UFMG, FUNDEP, FAPEMIG, Sociedade Brasileira de Neurovisão, HOLHOS, UFRJ, USP, UFRN and UEMG SHALL be created or updated.

#### Scenario: Supporting entities are not duplicated

Given the seed has already been executed once  
When the seed is executed again  
Then duplicate supporting entities SHALL NOT be created.

### Requirement: Conservative seeded content

Seeded content SHALL avoid unverified claims and final promotional copy.

#### Scenario: Seed avoids inflated claims

Given the seed creates default text or announcements  
When the content is inspected  
Then it SHALL NOT claim that the event is the largest in Latin America or use similarly unverified promotional claims.
