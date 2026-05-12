# QA

## Purpose

This delta specification defines the testing and validation requirements for the account management and dashboard implementation.

## ADDED Requirements

### Requirement: Account and dashboard tests

The account/profile/dashboard foundation SHALL include tests for core authentication and authorization behavior.

#### Scenario: Registration test exists

Given the test suite runs
Then it SHALL verify that registration creates a user and profile.

#### Scenario: Dashboard auth test exists

Given the test suite runs
Then it SHALL verify that unauthenticated dashboard access redirects to login.

#### Scenario: Role access tests exist

Given the test suite runs
Then it SHALL verify role-specific dashboard access for author, reviewer and chair roles.

### Requirement: Validation commands

The change SHALL pass project validation commands.

#### Scenario: Validation is complete

Given the implementation is complete
When validation is run
Then `openspec validate add-accounts-profiles-and-dashboards --strict`, `uv run python manage.py check`, `uv run python manage.py makemigrations --check --dry-run`, and `uv run pytest` SHALL pass.
