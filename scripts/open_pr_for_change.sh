#!/usr/bin/env bash
set -euo pipefail

REPO="${REPO:-LAPAN-HUGODEPAULA/cbnv-website}"

ISSUE="${1:?Usage: scripts/open_pr_for_change.sh <issue-number> <change-id>}"
CHANGE_ID="${2:?Usage: scripts/open_pr_for_change.sh <issue-number> <change-id>}"

BRANCH="change/$CHANGE_ID"

openspec validate "$CHANGE_ID" --strict
uv run python manage.py check
uv run python manage.py makemigrations --check --dry-run
uv run pytest

cat > /tmp/pr_body.md <<EOF
Closes #$ISSUE

## Change ID

\`$CHANGE_ID\`

## OpenSpec

- [x] \`openspec validate $CHANGE_ID --strict\` passes.
- [ ] Delta specs are present under \`openspec/changes/$CHANGE_ID/specs/\`.
- [ ] Implementation matches the approved proposal.
- [ ] No out-of-scope feature was added.

## Validation

- [x] \`uv run python manage.py check\`
- [x] \`uv run python manage.py makemigrations --check --dry-run\`
- [x] \`uv run pytest\`

## Notes

TBD.
EOF

git push -u origin "$BRANCH"

gh pr create \
  --repo "$REPO" \
  --base main \
  --head "$BRANCH" \
  --title "[$CHANGE_ID] Implement approved OpenSpec change" \
  --body-file /tmp/pr_body.md