# dashboards

## Purpose

Define dashboard integration for reports, exports and indicators in committee-facing navigation.

## ADDED Requirements

### Requirement: Chair dashboard reports link

The chair dashboard MUST link to reports and exports.

#### Scenario: Chair opens dashboard

Given an authenticated chair user opens the chair dashboard  
Then a reports or exports link/card MUST be visible.

### Requirement: Reports dashboard export actions

The reports dashboard MUST expose export actions.

#### Scenario: Chair opens reports dashboard

Given an authenticated chair user opens reports dashboard  
Then export actions for submissions, authors, institutions and proceedings MUST be available.

### Requirement: Empty state

The reports dashboard MUST handle missing data gracefully.

#### Scenario: No submissions exist

Given no submissions exist  
When a chair user opens reports dashboard  
Then the dashboard MUST show zero counts or empty states rather than failing.
