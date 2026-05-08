## ADDED Requirements

### Requirement: Accessible Review Forms
Review forms SHALL use standard `<label>` elements for all inputs and ensure that instructions (e.g., scoring rubrics) are associated with fields via `aria-describedby`.

#### Scenario: Review input has label
- **WHEN** a reviewer accesses the evaluation form
- **THEN** every numeric input and text area SHALL have a programmatically associated label

### Requirement: Keyboard-Friendly Rating Scales
Numeric rating scales (e.g., 1-5) SHALL be implemented using accessible radio groups or dropdowns that support standard keyboard interactions (arrow keys, space).

#### Scenario: Rating via keyboard
- **WHEN** a reviewer uses arrow keys to navigate a rating scale
- **THEN** the selection SHALL update and be announced by the screen reader
