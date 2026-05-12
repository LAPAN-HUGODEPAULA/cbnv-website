# qa

## Purpose

Define validation and test expectations for the initial author submission flow.

## ADDED Requirements

### Requirement: Submission workflow tests

The initial submission flow SHALL include tests for core workflow behavior.

#### Scenario: Valid submission test

Given the test suite runs  
Then it SHALL verify an authenticated author can create a valid initial submission with PDF.

#### Scenario: Video not required test

Given the test suite runs  
Then it SHALL verify initial submission succeeds without video.

#### Scenario: File validation tests

Given the test suite runs  
Then it SHALL verify non-PDF and oversized files are rejected.

#### Scenario: Permission tests

Given the test suite runs  
Then it SHALL verify users cannot view or download another user's submissions/files.

### Requirement: Validation commands

The change SHALL pass project validation commands.

#### Scenario: Validation is complete

Given the implementation is complete  
When validation is run  
Then `openspec validate add-author-submission-initial-flow --strict`, `uv run python manage.py check`, `uv run python manage.py makemigrations --check --dry-run`, and `uv run pytest` SHALL pass.
