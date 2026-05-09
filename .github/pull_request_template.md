## Change ID

<!-- Example: add-design-system-and-layout-shells -->

## Linked issue

Closes #

## OpenSpec checklist

- [ ] Branch name is `change/<change-id>`.
- [ ] OpenSpec change exists in `openspec/changes/<change-id>/`.
- [ ] `proposal.md` is complete.
- [ ] `design.md` is complete or explicitly not needed.
- [ ] `tasks.md` is updated.
- [ ] Delta specs exist under `openspec/changes/<change-id>/specs/`.
- [ ] `openspec validate <change-id> --strict` passes.

## Implementation checklist

- [ ] Implementation matches the approved proposal.
- [ ] No out-of-scope feature was added.
- [ ] Migrations are intentional.
- [ ] No secrets were committed.
- [ ] Documentation was updated if behavior changed.

## Validation

- [ ] `uv run python manage.py check`
- [ ] `uv run python manage.py makemigrations --check --dry-run`
- [ ] `uv run pytest`
- [ ] `npm run build` if frontend/CSS/templates changed