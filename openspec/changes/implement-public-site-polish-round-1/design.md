# Design: Implement Public Site Polish Round 1

## Overview

This change implements corrections identified by `verify-cross-page-content-consistency`. It is a traceable corrective pass, not a redesign.

## Implementation Principles

### 1. Fix by evidence

Implementation changes MUST be tied to a finding, acceptance criterion or low-risk correction.

### 2. Preserve persona-specific labels

Author, reviewer and chair views may use different labels when the persona status map marks the asymmetry as intentional.

### 3. Prefer canonical sources

Event name, dates, venue, links, contacts and status availability should come from `CoreSettings` or the relevant domain model rather than hardcoded strings.

### 4. Avoid broad redesign

This change can adjust templates, labels, messages and helper mappings. It must not create a new design direction.

### 5. Add automation where cheap and high-value

If a consistency issue can be prevented by a simple test, helper assertion or management command, implement it. If automation is too complex, document deferral.

## Fix Categories

### Canonical fact fixes

Correct event date, venue, theme, contact, registration/submission link and hardcoded current-event facts.

### Persona status fixes

Align author, reviewer, chair and admin labels with the persona status map.

### Legacy contamination fixes

Remove previous-edition dates, venues, themes, sponsors, workshop claims and links from current-event contexts.

### Notification fixes

Correct subjects, bodies and low-risk trigger drift when findings identify mismatch.

### Non-visual content fixes

Correct alt text, ARIA labels, status badge accessible names, icon-only labels and form labels.

### Report/export fixes

Correct export headers, indicator labels, status values, protected-file exposure and privacy-sensitive fields.

## Implementation Strategy

1. Read the consistency backlog.
2. Read the persona status map.
3. Read the legacy ghost facts inventory.
4. Read the notification trigger review.
5. Read the automation candidate matrix.
6. Build a local implementation checklist.
7. Apply P0 fixes.
8. Apply P1 fixes.
9. Apply low-risk P2 fixes.
10. Add selected automation checks.
11. Update implementation report.
12. Run validation.

## Status Label Design

Prefer central helpers where possible:

```text
internal status -> persona -> approved display label
```

Avoid scattering status labels across templates.

## Notification Design

Notification copy should use domain context variables, not hardcoded event facts.

## Report and Export Design

Export headers should be deterministic and use approved terminology. Exports must not include direct protected file URLs.

## Automation Design

Possible automation:

- public page tests using canonical settings;
- status label mapping tests;
- export header tests;
- protected file URL exposure tests;
- registration/submission CTA status tests;
- legacy ghost fact checks outside archive contexts.

## Deferral Rules

A finding may be deferred when it requires new domain model design, factual input, broad i18n architecture, full accessibility audit, workflow redesign, external service integration or large report/export redesign.
