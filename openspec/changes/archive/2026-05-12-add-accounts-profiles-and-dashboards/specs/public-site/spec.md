# Public-Site

## Purpose

This delta specification defines how the public site links to account management and ensures consistency in design.

## ADDED Requirements

### Requirement: Public pages can link to account entry points

The public site SHALL be able to link to account registration, login or dashboard entry points without implying unfinished workflows are available.

#### Scenario: Submission CTA before workflow exists

Given the submission workflow is not yet implemented
When a user follows an account-related submission CTA
Then the resulting account/dashboard page SHALL clearly state the workflow is not yet available.

### Requirement: Account forms use public design system

Public account forms SHALL use the established design system and layout conventions.

#### Scenario: Registration form renders

Given the registration page renders
When a user views the form
Then the form SHALL have labels, visible errors and responsive layout consistent with the public site.
