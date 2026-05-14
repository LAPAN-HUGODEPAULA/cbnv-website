# translations

## Purpose

Define verification requirements for Portuguese, English and bilingual terminology across pages, dashboards, notifications, exports, status labels and non-visual content.

## ADDED Requirements

### Requirement: Translation and terminology review

The audit MUST verify consistency of translated or bilingual terminology across user-facing surfaces.

#### Scenario: Portuguese and English labels reviewed

Given both Portuguese and English labels exist in the system
When the audit is performed
Then equivalent concepts MUST be mapped and inconsistencies MUST be recorded.

### Requirement: Preferred terminology inventory

The audit MUST produce or update an inventory of preferred terminology.

#### Scenario: Preferred terms documented

Given the audit identifies repeated terms
When review documents are produced
Then preferred terms for submissions, reviews, proceedings, registration, final materials and videos MUST be documented.
