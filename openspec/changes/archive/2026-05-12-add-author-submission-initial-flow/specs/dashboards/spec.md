# dashboards

## Purpose

Define how author-facing dashboard surfaces expose initial submission status and links while keeping workflow implementation scoped to the submissions app.

## ADDED Requirements

### Requirement: Author dashboard submission list

The author dashboard SHALL show the authenticated author's own submissions.

#### Scenario: Author has submissions

Given an authenticated author has one or more submissions  
When they open the author dashboard  
Then their submissions SHALL be listed with title, code, status and relevant date.

#### Scenario: Author has no submissions

Given an authenticated author has no submissions  
When they open the author dashboard  
Then an empty state SHALL explain how to start a submission if submissions are open.

### Requirement: Dashboard shows submission status safely

The author dashboard SHALL show submission status without exposing review workflow not yet implemented.

#### Scenario: Submitted item shown

Given a submission has submitted status  
When the dashboard renders  
Then the status SHALL be shown as submitted/received, not accepted or rejected.

### Requirement: Dashboard links only to owned submissions

The author dashboard SHALL link only to submissions owned by the authenticated user.

#### Scenario: Other user's submission exists

Given another user's submission exists  
When the author dashboard renders  
Then the other user's submission SHALL NOT be listed.
