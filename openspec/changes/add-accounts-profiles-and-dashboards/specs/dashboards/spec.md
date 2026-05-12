# Dashboards Delta

## ADDED Requirements

### Requirement: Authenticated dashboard index

The platform SHALL provide an authenticated dashboard index.

#### Scenario: Unauthenticated visitor opens dashboard

Given an unauthenticated visitor requests the dashboard
When the request is processed
Then the visitor SHALL be redirected to login.

#### Scenario: Authenticated user opens dashboard

Given an authenticated user requests the dashboard
When the request is processed
Then they SHALL see available dashboard areas based on their profile roles.

### Requirement: Author dashboard shell

The platform SHALL provide an author dashboard shell.

#### Scenario: Author opens author dashboard

Given an authenticated user has author role
When they open the author dashboard
Then they SHALL see an author area with future submission placeholders.

#### Scenario: Non-author opens author dashboard

Given an authenticated user does not have author role
When they open the author dashboard
Then access SHALL be denied or redirected.

### Requirement: Reviewer dashboard shell

The platform SHALL provide a reviewer dashboard shell.

#### Scenario: Reviewer opens reviewer dashboard

Given an authenticated user has reviewer role
When they open the reviewer dashboard
Then they SHALL see a reviewer area with future review placeholders.

### Requirement: Chair dashboard shell

The platform SHALL provide a chair/scientific committee dashboard shell.

#### Scenario: Chair opens chair dashboard

Given an authenticated user has chair role
When they open the chair dashboard
Then they SHALL see a committee area with future workflow placeholders.

### Requirement: Dashboard shells do not implement workflows

Dashboard shells SHALL not implement submission or review workflows in this change.

#### Scenario: Author dashboard renders

Given the author dashboard renders
Then it SHALL NOT provide actual submission creation unless the later submission-flow proposal has been implemented.
