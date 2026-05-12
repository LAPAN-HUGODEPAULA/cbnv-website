# Reviews

## Purpose

This delta specification ensures that the initial account foundation does not prematurely implement review workflows while providing necessary placeholders.

## ADDED Requirements

### Requirement: No review workflow in account foundation

The accounts/dashboard foundation SHALL not implement review assignment, review forms or decision workflow.

#### Scenario: Reviewer dashboard exists before review workflow

Given the reviewer dashboard is implemented
When a reviewer opens it
Then it MAY show a future assigned-reviews placeholder
And SHALL NOT create review assignments or review forms.

### Requirement: Future review integration point

Reviewer and chair dashboards SHALL provide clear integration points for later review workflow implementation.

#### Scenario: Later review proposal starts

Given reviewer and chair dashboard shells exist
When the review workflow is implemented later
Then it SHALL be able to attach review assignment and decision behavior without replacing authentication foundation.
