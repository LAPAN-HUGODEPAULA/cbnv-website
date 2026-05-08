# Tasks: Add Design System and Layout Shells

## OpenSpec

- [x] Create `openspec/changes/add-design-system-and-layout-shells/`.
- [x] Add `proposal.md`.
- [x] Add `design.md`.
- [x] Add `tasks.md`.
- [x] Add delta spec `specs/design-system/spec.md`.
- [x] Add delta spec `specs/public-site/spec.md`.
- [x] Run `openspec validate add-design-system-and-layout-shells --strict`.

## CSS and tokens

- [x] Review existing `src/input.css`.
- [x] Define source-level Tailwind/design tokens for:
  - [x] navy scale;
  - [x] electric blue;
  - [x] neuro green;
  - [x] text colors;
  - [x] surface colors;
  - [x] border colors;
  - [x] warning/accent color;
  - [x] display font;
  - [x] body font;
  - [x] label font;
  - [x] radius;
  - [x] shadows or glow styles if used.
- [x] Add reduced-motion handling.
- [x] Add focus-visible defaults.
- [x] Add base body background/text treatment.
- [x] Ensure `npm run build` works.

## Template structure

- [x] Review current `templates/base.html`.
- [x] Implement or update `templates/base.html`.
- [x] Add semantic landmarks:
  - [x] skip link;
  - [x] header;
  - [x] nav;
  - [x] main with `id="main-content"`;
  - [x] footer.
- [x] Create `templates/partials/layout/`.
- [x] Create `templates/partials/components/`.

## Layout partials

- [x] Create `partials/layout/skip_link.html`.
- [x] Create `partials/layout/header.html`.
- [x] Create `partials/layout/mobile_nav.html`.
- [x] Create `partials/layout/footer.html`.
- [x] Create `partials/layout/page_shell.html` or equivalent.

## Component partials

- [x] Create `partials/components/button.html`.
- [x] Create `partials/components/card.html`.
- [x] Create `partials/components/badge.html`.
- [x] Create `partials/components/section_heading.html`.
- [x] Create `partials/components/timeline_shell.html`.
- [x] Create `partials/components/form_field.html`.
- [x] Create `partials/components/alert.html`.
- [x] Create `partials/components/empty_state.html`.
- [x] Create `partials/components/icon_link.html`.

## Header and navigation

- [x] Add site identity slot.
- [x] Add primary navigation items.
- [x] Add primary CTA slot.
- [x] Add mobile menu trigger.
- [x] Ensure menu can be used with keyboard.
- [x] Ensure active/current nav state can be represented.
- [x] Ensure external links can be marked accessibly.

## Footer

- [x] Add concise event identity slot.
- [x] Add essential navigation links.
- [x] Add institutional/support area.
- [x] Add FAPEMIG slot, but do not require final logo asset in this change.
- [x] Add Instagram/icon-link slot with accessible label.
- [x] Avoid duplicative long footer copy.

## Accessibility

- [x] Ensure all icon-only controls have accessible names.
- [x] Ensure focus-visible style is obvious.
- [x] Ensure components do not depend on color alone.
- [x] Ensure badges use text labels.
- [x] Ensure mobile menu has appropriate ARIA attributes if JS state is used.
- [x] Ensure reduced-motion behavior is present.
- [x] Ensure templates use semantic heading order where applicable.

## Documentation

- [x] Create or update `docs/design-system.md`.
- [x] Document tokens.
- [x] Document component partials.
- [x] Document basic usage examples.
- [x] Document accessibility contracts.
- [x] Document out-of-scope items.

## Validation

- [x] Run `openspec validate add-design-system-and-layout-shells --strict`.
- [x] Run `npm run build`.
- [x] Run `uv run python manage.py check`.
- [x] Run `uv run python manage.py makemigrations --check --dry-run`.
- [x] Run `uv run pytest`.

## PR checklist

- [x] Branch is `change/add-design-system-and-layout-shells`.
- [ ] PR title starts with `[add-design-system-and-layout-shells]`.
- [ ] PR body includes `Closes #2`.
- [ ] PR body includes validation checklist.
- [ ] No final page content or domain feature was implemented.
