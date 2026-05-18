# reports

## Purpose

Define committee-facing report pages and report documentation for operational monitoring, technical-scientific reporting, and export discovery.

## ADDED Requirements

### Requirement: Reports dashboard

The platform MUST provide an internal reports dashboard for chair/scientific committee users.

#### Scenario: Chair opens reports dashboard

Given an authenticated chair or scientific committee user  
When they open the reports dashboard  
Then they MUST see available indicators and export actions.

#### Scenario: Author opens reports dashboard

Given an authenticated author without committee permission  
When they attempt to open the reports dashboard  
Then access MUST be denied.

### Requirement: Report sections

The reports dashboard MUST group information into operational sections.

#### Scenario: Dashboard sections render

Given the reports dashboard renders  
Then it MUST include sections for submissions, reviews or decisions, final materials or proceedings, authors or institutions, and exports.

### Requirement: Reports documentation

The platform MUST document available reports and exports.

#### Scenario: Developer reads reports documentation

Given `docs/reports-exports-and-indicators.md` exists  
When it is inspected  
Then it MUST describe available indicators, exports, filters, permissions, and privacy boundaries.
