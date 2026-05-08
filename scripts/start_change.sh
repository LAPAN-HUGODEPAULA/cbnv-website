#!/usr/bin/env bash
set -euo pipefail

REPO="${REPO:-LAPAN-HUGODEPAULA/cbnv-website}"

ISSUE="${1:?Usage: scripts/start_change.sh <issue-number> <change-id>}"
CHANGE_ID="${2:?Usage: scripts/start_change.sh <issue-number> <change-id>}"

BRANCH="change/$CHANGE_ID"

gh issue develop "$ISSUE" \
  --repo "$REPO" \
  --base main \
  --name "$BRANCH" \
  --checkout

mkdir -p "openspec/changes/$CHANGE_ID/specs"

touch "openspec/changes/$CHANGE_ID/proposal.md"
touch "openspec/changes/$CHANGE_ID/design.md"
touch "openspec/changes/$CHANGE_ID/tasks.md"

cat > "openspec/changes/$CHANGE_ID/proposal.md" <<EOF
# Proposal: $CHANGE_ID

## Problem

TBD.

## Proposed Change

TBD.

## Scope

TBD.

## Out of Scope

TBD.
EOF

cat > "openspec/changes/$CHANGE_ID/tasks.md" <<EOF
# Tasks: $CHANGE_ID

- [ ] Write proposal.
- [ ] Write design notes if needed.
- [ ] Write delta specs.
- [ ] Validate OpenSpec change.
- [ ] Implement.
- [ ] Run tests.
- [ ] Open PR.
EOF

echo "Created branch $BRANCH and OpenSpec change folder openspec/changes/$CHANGE_ID"