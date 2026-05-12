# Design: Produce Public Site Content Round 1

## Overview

This change produces the first coherent editorial layer for the public CBNV 2026 website. It follows the UI/UX review and prepares the site for cross-page consistency verification.

The output is not only prose. It is a content system: page copy, microcopy, copy map, editorial guidelines and open questions.

## Content Design Principles

### 1. Accuracy before persuasion

The site should be credible. Avoid scale claims, inflated language or generic promotional phrases.

### 2. Specificity before abstraction

Prefer concrete facts: dates, location, theme, format, submission phase, external registration.

### 3. Progressive disclosure

Home should be concise. About, Submissions and Registration can provide more explanation.

### 4. Confirmed vs pending

The copy must make clear when something is confirmed, preliminary, pending or coming soon.

### 5. Reuse language consistently

Use the same terms across pages:

- CBNV 2026
- XII Congresso Brasileiro de Neurociências da Visão
- Neurovisão na Era da Inteligência Artificial
- CAD-1/UFMG
- inscrições
- submissões
- programação
- anais
- trabalhos aprovados
- participantes a confirmar

### 6. Content must fit the UI

Do not write paragraphs that cannot fit the implemented layout. If a section needs more text than the layout supports, document the mismatch for `implement-public-site-polish-round-1`.

## Voice and Tone

The voice should be institutional but not bureaucratic, scientific but accessible, direct but not abrupt, welcoming but not promotional, modest and precise.

Avoid “maior evento”, “imperdível”, “revolucionário”, unsupported “fronteira do conhecimento” phrasing and “garanta sua vaga” if registration is not open or capacity details are not actively being used.

## Page Content Design

### Home

Purpose: orient quickly. Home should answer: what event, when, where, what theme and what action is available now.

### About

Purpose: explain institutional/scientific meaning. About should be the main place for what the congress is, why the 2026 theme matters, and how the event connects visual neuroscience, clinical translation and AI.

### Program

Purpose: help users understand structure. Program copy should not compete with schedule data. Use short intros and notes.

### Speakers

Purpose: introduce people who are public/confirmed. Avoid implying all speakers are confirmed if not.

### Submissions

Purpose: reduce author uncertainty. This page needs precise operational copy.

### Registration

Purpose: clarify external process and status.

### Sponsorship

Purpose: explain support/contact path without implying undefined sponsor packages.

### Previous Editions

Purpose: archive context.

### Contact

Purpose: route inquiries and venue information.

## Required Documents

### `public-site-content-round-1.md`

Recommended structure:

```markdown
# Public Site Content — Round 1

## Metadata
## Editorial summary
## Home
## About
## Program
## Speakers
## Submissions
## Registration
## Sponsorship
## Previous Editions
## Contact
## Footer
## Microcopy
## Open factual questions
```

### `public-site-copy-map-round-1.md`

Recommended table:

```markdown
| Page | Section | Content key | Proposed copy | Target location | Source/rationale | Status |
|---|---|---|---|---|---|---|
```

### `public-site-editorial-guidelines.md`

Recommended structure:

```markdown
# Editorial Guidelines

## Voice
## Terms to use
## Terms to avoid
## Confirmed vs pending language
## CTAs
## Accessibility and readability
## Institutional acknowledgements
## Previous editions
```

## Content Quality Checklist

Every produced content block should pass:

1. Is it true?
2. Is it necessary?
3. Is it specific?
4. Is it placed on the right page?
5. Does it duplicate another page?
6. Does it avoid overclaiming?
7. Does it distinguish pending from confirmed?
8. Does it support a user action or understanding?
9. Can it fit the current layout?
10. Does it create a consistency issue for the next proposal?

## Implementation Guidance

When content is inserted into the codebase:

- prefer CMS fields and seed data over templates;
- avoid embedding long copy inside layout partials;
- do not add new fields unless unavoidable;
- if a field is missing, document the need rather than expanding schema casually;
- keep layout changes out of this proposal.

## Handoff to Consistency Verification

This proposal must explicitly hand off repeated facts, standardized terms, known unresolved questions, pages with provisional text, CTAs/link states and sections requiring implementation polish.
