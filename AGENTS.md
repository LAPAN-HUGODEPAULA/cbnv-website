# Repository Guidelines

## Project Structure & Module Organization
- `docs/` is the primary working area for 2026 planning, specs, and design artifacts.
- `docs/stitch_cbnv_2026_digital_platform/` contains page-level prototypes, usually as `code.html` + `screen.png` pairs.
- `_legacy/` stores historical material (Notion exports, mirrored Wix assets, past-event records). Treat this as archival reference, not active product code.
- `README.md` is a short project identifier and should remain brief.

## Build, Test, and Development Commands
Use **uv** for ALL Python dependency and environment operations. **NEVER** use `pip`, `python -m pip`, or `pip install` in this repository.
- `uv sync`: Sync Python environment with `pyproject.toml` / `uv.lock`.
- `uv add <package>`: Add a runtime dependency.
- `uv add --dev <package>`: Add a development/test dependency.
- `uv run python manage.py migrate`: Apply Django migrations.
- `uv run python manage.py runserver`: Start the Django dev server.
- `uv run pytest`: Run the test suite.
- `npm run build`: Build Tailwind CSS.
- `npm run watch`: Watch Tailwind CSS for changes.

## Coding Style & Naming Conventions
- Prefer Markdown for specs and decision records; keep sections scannable with short headings.
- Preserve existing naming patterns in `docs/stitch_*` folders (slug-like names with paired assets).
- Use UTF-8 text, but prefer ASCII filenames for new files when possible.
- Keep edits focused: do not reorganize `_legacy/` unless migration work explicitly requires it.

## Testing Guidelines
- **Framework:** `pytest` (with `pytest-django`).
- Run all tests before any change proposal validation.
- Every new feature or bug fix MUST include a new test case.
- For UI changes, validate manually in the browser via `localhost:8001`.
- For public-site shell or header changes, keep menu links as normal anchor navigation unless a specific view explicitly needs HTMX behavior; do not add `hx-boost` to the outer public layout by default.
- After any change to shared layouts, confirm the top menu still navigates correctly on Home, Sobre, Programação and Edições Anteriores before merging.

## Commit & Pull Request Guidelines
- Use Conventional Commits.
- Recommended format: `type(scope): 🏷️ summary` (e.g., `feat(ui): 🎨 add scientific card component`).
- PRs should include:
  - concise purpose and changed paths,
  - screenshots when UI/prototype files change,
  - linked issue or planning note when applicable.

## OpenSpec Format & Standards
Maintain a strict format for all specification files (`openspec/specs/**/*.md` and `openspec/changes/**/specs/**/*.md`).

- **Mandatory Sections:**
  - `# Title (capability-name)`
  - `## Purpose`: A brief explanation of the capability's goal.
  - `## Requirements`: (or `## ADDED Requirements`, `## MODIFIED Requirements`). This section **MUST** exist and contain at least one requirement.
- **Requirement Structure:**
  - `### Requirement: <Short Descriptive Title>`
  - Use RFC 2119 keywords (**SHALL**, **MUST**, **SHOULD**) within the requirement description.
- **Scenario Structure:**
  - `#### Scenario: <Description of specific behavior>`
  - Use Gherkin-style steps: `- **GIVEN**`, `- **WHEN**`, `- **THEN**`, `- **AND**`.
- **Validation:** Never create or update a spec file without including both a Purpose and a Requirements section.

## Security & Configuration Tips
- Do not commit secrets, personal attendee data, or private credentials.
- Large binary additions should be intentional and justified.
