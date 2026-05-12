# Public Site Content Round 1

# Purpose
Define the scope, artifacts, and tone of the first round of public-site content production, including the delivery of core content documents and guidelines.

## ADDED Requirements

### Requirement: Round-1 public content document

The platform SHALL include a versioned round-1 public-site content document.

#### Scenario: Content document exists

Given the content-production change is completed  
When the repository is inspected  
Then `docs/content/public-site-content-round-1.md` SHALL exist.

#### Scenario: Content document covers required pages

Given the content document exists  
When it is read  
Then it SHALL include content for Home, About, Program, Speakers, Submissions, Registration, Sponsorship, Previous Editions, Contact and Footer.

### Requirement: Copy map

The platform SHALL include a copy map linking content to implementation targets.

#### Scenario: Copy map exists

Given the content-production change is completed  
When the repository is inspected  
Then `docs/content/public-site-copy-map-round-1.md` SHALL exist.

#### Scenario: Copy map identifies target location

Given a content block is listed in the copy map  
When the row is inspected  
Then it SHALL identify page, section, target implementation location and status.

### Requirement: Editorial guidelines

The platform SHALL include public-site editorial guidelines.

#### Scenario: Guidelines exist

Given the content-production change is completed  
When the repository is inspected  
Then `docs/content/public-site-editorial-guidelines.md` SHALL exist.

### Requirement: Conservative scientific tone

Public-site content SHALL use a sober, scientific and institutional tone.

#### Scenario: Content avoids inflated claims

Given public-site content is inspected  
Then it SHALL NOT claim the event is the largest Neurovision event in Latin America or use unsupported promotional claims.

### Requirement: Initial submission video rule

Submissions content SHALL state that video is not required during the initial submission phase.

#### Scenario: Author reads submissions copy

Given a potential author reads the Submissions page copy  
Then they SHALL understand that video is only relevant later for approved/final materials when applicable.
