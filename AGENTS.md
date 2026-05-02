# Repository Guidelines

## Project Structure & Module Organization
- `docs/` is the primary working area for 2026 planning, specs, and design artifacts.
- `docs/stitch_cbnv_2026_digital_platform/` contains page-level prototypes, usually as `code.html` + `screen.png` pairs.
- `_legacy/` stores historical material (Notion exports, mirrored Wix assets, past-event records). Treat this as archival reference, not active product code.
- `README.md` is a short project identifier and should remain brief.

## Build, Test, and Development Commands
This repository currently has no formal build pipeline (`package.json`, `Makefile`, and Python project files are absent).
Use these commands for local validation:
- `rg --files docs` lists tracked documentation/prototype files.
- `find docs -type f | sort` audits generated assets and file naming.
- `python -m http.server 8000` serves HTML prototypes locally for manual review.

## Coding Style & Naming Conventions
- Prefer Markdown for specs and decision records; keep sections scannable with short headings.
- Preserve existing naming patterns in `docs/stitch_*` folders (slug-like names with paired assets).
- Use UTF-8 text, but prefer ASCII filenames for new files when possible.
- Keep edits focused: do not reorganize `_legacy/` unless migration work explicitly requires it.

## Testing Guidelines
- No automated test framework is configured yet.
- For HTML prototype updates, validate by opening files in a browser and checking layout/content regressions.
- For Markdown changes, verify links and headings manually before opening a PR.

## Commit & Pull Request Guidelines
- Current history only has `Initial commit`; adopt Conventional Commits going forward.
- Recommended format: `type(scope): summary` (example: `docs(program): update 12o CBNV agenda draft`).
- PRs should include:
  - concise purpose and changed paths,
  - screenshots when UI/prototype files change,
  - linked issue or planning note when applicable,
  - explicit note if `_legacy/` data was modified.

## Security & Configuration Tips
- Do not commit secrets, personal attendee data, or private credentials in docs/assets.
- Large binary additions (videos, high-res images, PDFs) should be intentional and justified in the PR description.
