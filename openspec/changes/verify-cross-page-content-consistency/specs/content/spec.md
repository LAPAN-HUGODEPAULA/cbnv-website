# content

## Purpose

Define verification requirements for public copy, repeated facts, terminology, content placement, legacy contamination and editorial consistency across current-event and archive contexts.

## ADDED Requirements

### Requirement: Cross-surface content consistency matrix

The audit MUST create a matrix comparing repeated facts and labels across public pages, dashboards, notifications and exports.

#### Scenario: Matrix is created

Given the consistency audit is performed
When the review documents are produced
Then a cross-surface consistency matrix MUST exist.

### Requirement: Canonical facts verification

The audit MUST verify visible content against canonical event facts.

#### Scenario: Event date checked

Given canonical event dates exist in site settings
When public pages, dashboards, notifications and exports are reviewed
Then visible event dates MUST match the canonical source or be flagged.

### Requirement: Legacy ghost facts inventory

The audit MUST identify legacy facts that must not appear as current CBNV 2026 content.

#### Scenario: Legacy venue appears in current page

Given a previous-edition venue appears outside an archive context
When the audit is performed
Then the issue MUST be recorded as legacy contamination.
