#!/usr/bin/env bash
set -euo pipefail

# CBNV 2026 — Create GitHub labels, milestones and issues
# Usage:
#   chmod +x scripts/create_github_backlog.sh
#   ./scripts/create_github_backlog.sh
#
# Optional:
#   REPO="LAPAN-HUGODEPAULA/cbnv-website" DRY_RUN=1 ./scripts/create_github_backlog.sh
#
# Requirements:
#   gh auth login
#   gh auth status
#
# This script is intentionally idempotent for labels, milestones and issues:
# - labels are created or updated with --force
# - milestones are created only if missing
# - issues are created only if no issue with exactly the same title exists

REPO="LAPAN-HUGODEPAULA/cbnv-website"
DRY_RUN="${DRY_RUN:-0}"

run() {
  if [[ "$DRY_RUN" == "1" ]]; then
    printf '[dry-run] '
    printf '%q ' "$@"
    printf '\n'
  else
    "$@"
  fi
}

require_gh() {
  command -v gh >/dev/null 2>&1 || {
    echo "ERROR: GitHub CLI 'gh' is not installed or not in PATH." >&2
    exit 1
  }
  gh auth status >/dev/null 2>&1 || {
    echo "ERROR: gh is not authenticated. Run: gh auth login" >&2
    exit 1
  }
}

ensure_label() {
  local name="$1"
  local color="$2"
  local description="$3"
  echo "Ensuring label: $name"
  run gh label create "$name" \
    --repo "$REPO" \
    --color "$color" \
    --description "$description" \
    --force >/dev/null
}

ensure_milestone() {
  local title="$1"
  local description="$2"

  echo "Ensuring milestone: $title"
  if [[ "$DRY_RUN" == "1" ]]; then
    echo "[dry-run] would check/create milestone: $title"
    return 0
  fi

  local number
  number="$(gh api "repos/$REPO/milestones?state=all&per_page=100" \
    --jq ".[] | select(.title == \"$title\") | .number" | head -n 1 || true)"

  if [[ -z "$number" ]]; then
    gh api "repos/$REPO/milestones" \
      -f title="$title" \
      -f description="$description" >/dev/null
    echo "Created milestone: $title"
  else
    echo "Milestone exists: $title (#$number)"
  fi
}

issue_exists() {
  local title="$1"
  gh issue list \
    --repo "$REPO" \
    --state all \
    --search "\"$title\" in:title" \
    --json number,title \
    --jq ".[] | select(.title == \"$title\") | .number" | head -n 1
}

create_issue_if_missing() {
  local title="$1"
  local labels_csv="$2"
  local milestone="$3"
  local body="$4"

  echo "Ensuring issue: $title"

  if [[ "$DRY_RUN" != "1" ]]; then
    local existing
    existing="$(issue_exists "$title" || true)"
    if [[ -n "$existing" ]]; then
      echo "Issue exists: #$existing $title"
      return 0
    fi
  fi

  local body_file
  body_file="$(mktemp)"
  printf '%s\n' "$body" > "$body_file"

  local label_args=()
  IFS=',' read -ra labels <<< "$labels_csv"
  for label in "${labels[@]}"; do
    label="$(echo "$label" | xargs)"
    [[ -n "$label" ]] && label_args+=(--label "$label")
  done

  run gh issue create \
    --repo "$REPO" \
    --title "$title" \
    --body-file "$body_file" \
    --milestone "$milestone" \
    "${label_args[@]}"

  rm -f "$body_file"
}

main() {
  require_gh

  echo "Repository: $REPO"
  echo "DRY_RUN: $DRY_RUN"

  # Labels
  ensure_label "type:foundation" "5319E7" "Technical foundation, baseline, project structure"
  ensure_label "type:frontend" "1D76DB" "Frontend, templates, CSS, layout, UI implementation"
  ensure_label "type:cms" "0E8A16" "Wagtail CMS models, settings and editorial admin"
  ensure_label "type:content" "C2E0C6" "Editorial content, copywriting and content production"
  ensure_label "type:domain" "FBCA04" "Domain models such as program, speakers, venue"
  ensure_label "type:auth" "D93F0B" "Authentication, profiles, dashboards and permissions"
  ensure_label "type:submissions" "B60205" "Scientific submission workflow"
  ensure_label "type:reviews" "D876E3" "Review, decision and scientific committee workflow"
  ensure_label "type:reports" "006B75" "Reports, exports, proceedings indicators"
  ensure_label "type:ops" "5319E7" "Operations, deployment, backups and infrastructure"
  ensure_label "type:qa" "BFDADC" "Quality assurance, regression and validation"

  ensure_label "priority:p0" "B60205" "Critical; blocks subsequent work"
  ensure_label "priority:p1" "D93F0B" "High priority"
  ensure_label "priority:p2" "FBCA04" "Medium priority"
  ensure_label "priority:p3" "C5DEF5" "Low priority or later-phase work"

  ensure_label "status:needs-spec" "EDEDED" "Needs OpenSpec proposal or delta spec"
  ensure_label "status:spec-ready" "C2E0C6" "OpenSpec proposal is ready for implementation"
  ensure_label "status:implementation" "1D76DB" "Implementation in progress"
  ensure_label "status:review" "BFDADC" "Needs review"
  ensure_label "status:blocked" "B60205" "Blocked"

  ensure_label "area:openspec" "5319E7" "OpenSpec proposals, specs and tasks"
  ensure_label "area:django" "0E8A16" "Django backend"
  ensure_label "area:wagtail" "0E8A16" "Wagtail CMS"
  ensure_label "area:tailwind" "1D76DB" "Tailwind CSS and design tokens"
  ensure_label "area:ui-ux" "A2EEEF" "User interface and user experience"
  ensure_label "area:editorial" "C2E0C6" "Editorial content and copy"
  ensure_label "area:security" "B60205" "Security"
  ensure_label "area:accessibility" "7057FF" "Accessibility"
  ensure_label "area:deployment" "5319E7" "Deployment and infrastructure"
  ensure_label "area:qa" "BFDADC" "Quality assurance"

  # Milestones
  ensure_milestone "Foundation stabilized" "Project foundation stabilized: runtime baseline, Docker, settings, auth model, routing, checks and tests."
  ensure_milestone "Public site foundation" "Design system, CMS models, canonical content, program models and public site MVP."
  ensure_milestone "Public site refinement" "UI/UX review, editorial content round, consistency verification and public-site polish."
  ensure_milestone "Scientific workflow MVP" "Accounts, profiles, submissions and review/decision workflow."
  ensure_milestone "Outputs, operations and release readiness" "Proceedings, videos, reports, deployment, security, backups, accessibility and QA."

  # Main issues
  create_issue_if_missing \
    "OpenSpec: stabilize platform foundation" \
    "type:foundation,priority:p0,area:openspec,area:django,area:wagtail,area:deployment,status:needs-spec" \
    "Foundation stabilized" \
'\n### Change ID\n\n`stabilize-platform-foundation`\n\n### Objective\n\nStabilize the technical foundation of the project, eliminating drift between documentation, dependencies, Docker, settings, migrations and authentication.\n\n### Scope\n\n- Align baseline to Python 3.14.x, Django 6.0.x, Wagtail 7.4.x LTS, PostgreSQL 18.3 and Tailwind 4.x.\n- Keep direct dependencies used by the project: `django-widget-tweaks`, `django-axes`, `django-countries`.\n- Use Django default User + `accounts.UserProfile`.\n- Remove custom user model if no real data depends on it.\n- Fix Wagtail/Django Admin routes.\n- Fix Docker and `.env.example`.\n- Ensure checks and tests pass.\n\n### Checklist\n\n- [ ] Create `openspec/changes/stabilize-platform-foundation/`.\n- [ ] Create `proposal.md`, `design.md`, `tasks.md`.\n- [ ] Create delta specs in `platform`, `accounts`, and `deployment`.\n- [ ] Update `README.md` with current technical baseline.\n- [ ] Update `openspec/project.md` or `openspec/config.yaml`.\n- [ ] Update architecture docs where needed.\n- [ ] Update `pyproject.toml` and `uv.lock`.\n- [ ] Confirm `django-widget-tweaks`, `django-axes`, and `django-countries` remain declared.\n- [ ] Remove `AUTH_USER_MODEL = "accounts.User"` if reverting to default User.\n- [ ] Create `accounts.UserProfile`.\n- [ ] Register `UserProfile` in Django Admin.\n- [ ] Regenerate initial migrations for project-owned apps if applicable.\n- [ ] Use `/admin/` for Wagtail Admin and `/django-admin/` for Django Admin.\n- [ ] Add Wagtail public routing at `/`.\n- [ ] Set `DB_HOST=db` for web service in Docker Compose.\n- [ ] Use PostgreSQL 18.3 image.\n- [ ] Add `.dockerignore`.\n- [ ] Remove silent `collectstatic` failure.\n- [ ] Ensure `.env` is not tracked.\n- [ ] Update `.env.example` with safe placeholders.\n\n### Validation\n\n```bash\nopenspec validate stabilize-platform-foundation --strict\nuv run python manage.py check\nuv run python manage.py makemigrations --check --dry-run\nuv run pytest\ndocker compose build --no-cache\ndocker compose up\n```\n\n### Acceptance criteria\n\n- [ ] `manage.py check` passes.\n- [ ] `makemigrations --check --dry-run` passes.\n- [ ] `pytest` passes.\n- [ ] Docker starts without manual DB host correction.\n- [ ] Default User + UserProfile are documented and implemented.\n- [ ] Docs, specs, code and Docker declare the same baseline.\n'

  create_issue_if_missing \
    "OpenSpec: add design system and layout shells" \
    "type:frontend,priority:p0,area:tailwind,area:ui-ux,area:accessibility,status:needs-spec" \
    "Public site foundation" \
'\n### Change ID\n\n`add-design-system-and-layout-shells`\n\n### Objective\n\nConvert the Stitch visual direction into an implementable Django-template design system.\n\n### Scope\n\n- Color, typography, spacing, radius, shadow and grid tokens.\n- Public layout shell.\n- Responsive header and mobile menu.\n- Base footer.\n- CTA, card, badge, timeline, section heading, container, alert and empty-state components.\n- Visible focus, contrast and responsiveness.\n\n### Checklist\n\n- [ ] Create OpenSpec change.\n- [ ] Create delta specs in `design-system` and `public-site`.\n- [ ] Define tokens in source CSS, not only generated CSS.\n- [ ] Define final typography or robust fallbacks.\n- [ ] Implement `templates/base.html`.\n- [ ] Implement partials: header, footer, navigation, CTA button, card, badge, section heading, timeline shell, form field wrapper.\n- [ ] Respect `prefers-reduced-motion`.\n- [ ] Add short component usage docs.\n\n### Validation\n\n```bash\nopenspec validate add-design-system-and-layout-shells --strict\nnpm run build\nuv run python manage.py check\nuv run pytest\n```\n\n### Acceptance criteria\n\n- [ ] Future pages can reuse components without excessive duplicate markup.\n- [ ] Header and footer are responsive.\n- [ ] Source CSS contains clear design tokens.\n- [ ] The design system respects basic contrast and visible focus.\n'

  create_issue_if_missing \
    "OpenSpec: add core CMS content models" \
    "type:cms,priority:p0,area:wagtail,area:editorial,status:needs-spec" \
    "Public site foundation" \
'\n### Change ID\n\n`add-core-cms-content-models`\n\n### Objective\n\nCreate the editorial CMS foundation to avoid hardcoded institutional content, links and recurring blocks.\n\n### Scope\n\n- `SiteSettings`\n- news/announcements\n- sponsors/supporting entities\n- global links\n- reusable editorial blocks\n- basic SEO fields\n- public visibility controls\n\n### Checklist\n\n- [ ] Create OpenSpec change.\n- [ ] Create delta specs in `content` and `public-site`.\n- [ ] Implement `SiteSettings`.\n- [ ] Implement news/announcement model.\n- [ ] Implement sponsors/supporting entities.\n- [ ] Implement editable global links: registration, livestream, YouTube, Instagram, map, contact.\n- [ ] Implement reusable blocks.\n- [ ] Configure Wagtail panels.\n- [ ] Add basic model tests.\n\n### Acceptance criteria\n\n- [ ] Admin can edit global event data.\n- [ ] External links are centralized.\n- [ ] News can be featured on Home.\n- [ ] Sponsors/supporting entities can be shown by category.\n'

  create_issue_if_missing \
    "OpenSpec: seed canonical event content" \
    "type:content,priority:p0,area:editorial,area:wagtail,status:needs-spec" \
    "Public site foundation" \
'\n### Change ID\n\n`seed-canonical-event-content`\n\n### Objective\n\nPopulate the CMS with the minimum canonical CBNV 2026 data needed by public pages.\n\n### Mandatory canonical content\n\n- formal name\n- short name\n- theme\n- dates\n- format\n- city\n- venue\n- full address\n- Google Maps URL\n- institutional partners\n- FAPEMIG\n- YouTube channel/playlist if available\n- registration/livestream links as “coming soon” if unavailable\n\n### Official address\n\n```text\nCentro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha.\nR. Prof. Baeta Viana, s/n - Pampulha, Belo Horizonte - MG, 31270-901\n```\n\nGoogle Maps:\n\n```text\nhttps://maps.app.goo.gl/xzqJ2LCAHVP4hsFp6\n```\n\n### Checklist\n\n- [ ] Create fixtures or an idempotent management command.\n- [ ] Populate `SiteSettings`.\n- [ ] Populate partners/supporting entities.\n- [ ] Populate global links.\n- [ ] Populate short neutral event description.\n- [ ] Include institutional FAPEMIG mention.\n- [ ] Ensure the seed is idempotent.\n\n### Acceptance criteria\n\n- [ ] Global event data has a single source.\n- [ ] Official address is not hardcoded in multiple pages.\n- [ ] Seed can run more than once without duplicating data.\n'

  create_issue_if_missing \
    "OpenSpec: add program, speakers and venue models" \
    "type:domain,priority:p0,area:wagtail,area:editorial,status:needs-spec" \
    "Public site foundation" \
'\n### Change ID\n\n`add-program-speakers-and-venue-models`\n\n### Objective\n\nImplement program, speaker and venue data as structured, editable and reusable models.\n\n### Scope\n\n- `ProgramDay`\n- `ProgramSession`\n- `ProgramTalk`\n- `Speaker`\n- participant/speaker status\n- venue/map data\n- preliminary program fixtures\n\n### Checklist\n\n- [ ] Create delta specs in `program`.\n- [ ] Implement models.\n- [ ] Implement Wagtail snippets/admin panels.\n- [ ] Implement statuses: confirmed, invited, pending, hidden, replaced.\n- [ ] Implement public hiding of pending participants.\n- [ ] Create program seed/fixture.\n- [ ] Add model and public-query tests.\n\n### Acceptance criteria\n\n- [ ] Program is editable without code.\n- [ ] Pending names can be hidden.\n- [ ] Public text does not promise workshops if there are no workshops.\n- [ ] Venue shown is CAD-1/UFMG, not an inherited previous-edition location.\n'

  create_issue_if_missing \
    "OpenSpec: add public site pages MVP" \
    "type:frontend,type:cms,priority:p1,area:wagtail,area:ui-ux,status:needs-spec" \
    "Public site foundation" \
'\n### Change ID\n\n`add-public-site-pages-mvp`\n\n### Objective\n\nImplement the main public pages for CBNV 2026.\n\n### Pages\n\n- Home\n- About\n- Program\n- Speakers\n- Submissions\n- Registration\n- Sponsorship\n- Previous editions\n- Contact\n\n### Checklist\n\n- [ ] Create delta specs in `public-site`.\n- [ ] Implement Wagtail page types.\n- [ ] Implement templates.\n- [ ] Consume `SiteSettings`.\n- [ ] Consume news.\n- [ ] Consume program and speakers.\n- [ ] Consume sponsors/supporting entities.\n- [ ] Implement “coming soon” states for registration/livestream.\n- [ ] Implement basic SEO.\n- [ ] Implement navigation and breadcrumbs where applicable.\n\n### Acceptance criteria\n\n- [ ] Public site is navigable.\n- [ ] Pages use CMS/models, not scattered hardcoded content.\n- [ ] Home communicates theme, dates, venue, CTAs and program.\n- [ ] Program has day-based visualization.\n- [ ] About has minimum institutional content.\n'

  create_issue_if_missing \
    "OpenSpec: review public site UI/UX round 1" \
    "type:frontend,priority:p1,area:ui-ux,area:accessibility,status:needs-spec" \
    "Public site refinement" \
'\n### Change ID\n\n`review-public-site-ui-ux-round-1`\n\n### Objective\n\nPerform a critical UI/UX review of the implemented public site and produce a prioritized correction backlog.\n\n### Review checklist\n\n#### Home\n\n- [ ] Evaluate latest-news placement.\n- [ ] Evaluate removing/replacing the “Híbrido” card.\n- [ ] Check whether venue card shows full address.\n- [ ] Check map and location link.\n- [ ] Remove or rewrite exaggerated copy.\n- [ ] Fix icons/labels inconsistent with event date.\n- [ ] Review “O que esperar?” against the actual program.\n- [ ] Remove workshop references if workshops do not exist.\n- [ ] Review supporting-entities grid.\n- [ ] Review footer, FAPEMIG, Instagram and redundancies.\n\n#### About\n\n- [ ] Evaluate depth and quality of copy.\n- [ ] Remove or consolidate “O que esperar?” if redundant.\n- [ ] Review heading hierarchy.\n- [ ] Review “Local e acesso”.\n- [ ] Fix inherited wrong map/location.\n- [ ] Review team cards/photos.\n- [ ] Review supporting-institutions redundancy.\n\n#### Global\n\n- [ ] Review responsiveness.\n- [ ] Review contrast.\n- [ ] Review mobile navigation.\n- [ ] Review CTA clarity.\n- [ ] Review cross-section consistency.\n\n### Deliverable\n\n- [ ] Markdown UI/UX report.\n- [ ] Prioritized backlog.\n- [ ] Decision list: keep, remove, consolidate or rewrite.\n\n### Acceptance criteria\n\n- [ ] Review produces actionable tasks.\n- [ ] Problems are classified by severity.\n- [ ] No implementation is mixed into the review.\n'

  create_issue_if_missing \
    "OpenSpec: produce public site content round 1" \
    "type:content,priority:p1,area:editorial,status:needs-spec" \
    "Public site refinement" \
'\n### Change ID\n\n`produce-public-site-content-round-1`\n\n### Objective\n\nReview and produce public-site editorial content with scientific, institutional and sober tone.\n\n### Checklist\n\n- [ ] Rewrite hero copy.\n- [ ] Rewrite short event description.\n- [ ] Expand About page.\n- [ ] Produce “Why participate?” or equivalent.\n- [ ] Produce coherent “What to expect?” text if retained.\n- [ ] Review Program copy.\n- [ ] Review Submissions copy.\n- [ ] Review Registration copy.\n- [ ] Review Sponsorship copy.\n- [ ] Review Footer copy.\n- [ ] Review “coming soon” microcopy.\n- [ ] Create short editorial guidelines.\n\n### Editorial rules\n\n- [ ] Avoid promotional exaggeration.\n- [ ] Do not claim it is the largest event in Latin America.\n- [ ] Avoid generic/overblown “frontier of knowledge” phrasing.\n- [ ] Do not promise non-existent workshops.\n- [ ] Separate confirmed from pending content.\n- [ ] Use clear Brazilian Portuguese.\n\n### Acceptance criteria\n\n- [ ] Texts align with requirements and program.\n- [ ] Texts do not contradict structured data.\n- [ ] Home and About are no longer generic.\n'

  create_issue_if_missing \
    "OpenSpec: verify cross-page content consistency" \
    "type:content,type:qa,priority:p1,area:editorial,area:qa,status:needs-spec" \
    "Public site refinement" \
'\n### Change ID\n\n`verify-cross-page-content-consistency`\n\n### Objective\n\nVerify editorial and factual consistency across pages, cards, CTAs, footer, program, entities and global data.\n\n### Consistency checklist\n\n- [ ] Event name is consistent.\n- [ ] Edition is consistent.\n- [ ] Theme is consistent.\n- [ ] Dates are consistent.\n- [ ] Venue is consistent.\n- [ ] Address is consistent.\n- [ ] Map link is consistent.\n- [ ] In-person/hybrid format is consistent.\n- [ ] CTAs by phase are consistent.\n- [ ] Home and About do not repeat contradictory blocks.\n- [ ] Program and “What to expect?” do not diverge.\n- [ ] There is no improper workshop mention.\n- [ ] Partner/supporting-entity terminology is standardized.\n- [ ] FAPEMIG appears where needed.\n- [ ] Footer does not repeat information without purpose.\n- [ ] Icons and labels make sense.\n- [ ] Pending participants are not displayed as confirmed.\n- [ ] External links work or appear as “coming soon”.\n- [ ] Content inherited from the previous edition does not appear as 2026 content.\n\n### Deliverables\n\n- [ ] Completed checklist.\n- [ ] Inconsistency report.\n- [ ] Derived correction issues.\n- [ ] Preventive editorial rules.\n\n### Acceptance criteria\n\n- [ ] Critical inconsistencies are identified before staging/production.\n- [ ] Problem-to-fix traceability exists.\n- [ ] Duplicate content is consolidated or justified.\n'

  create_issue_if_missing \
    "OpenSpec: implement public site polish round 1" \
    "type:frontend,type:content,priority:p1,area:ui-ux,area:editorial,status:needs-spec" \
    "Public site refinement" \
'\n### Change ID\n\n`implement-public-site-polish-round-1`\n\n### Objective\n\nApply prioritized corrections generated by UI/UX, content and consistency reviews.\n\n### Checklist\n\n- [ ] Apply Home adjustments.\n- [ ] Apply About adjustments.\n- [ ] Apply footer adjustments.\n- [ ] Apply supporting-entity adjustments.\n- [ ] Apply map/venue adjustments.\n- [ ] Apply card and grid adjustments.\n- [ ] Apply typography adjustments.\n- [ ] Apply microcopy adjustments.\n- [ ] Remove redundant blocks.\n- [ ] Run another visual check.\n\n### Acceptance criteria\n\n- [ ] Critical round-1 review backlog is resolved.\n- [ ] Public site is more coherent and less redundant.\n- [ ] Adjustments do not introduce responsiveness regressions.\n'

  create_issue_if_missing \
    "OpenSpec: add accounts, profiles and dashboards" \
    "type:auth,priority:p1,area:django,status:needs-spec" \
    "Scientific workflow MVP" \
'\n### Change ID\n\n`add-accounts-profiles-and-dashboards`\n\n### Objective\n\nImplement authentication and base internal areas for authors, reviewers and chair/scientific committee.\n\n### Checklist\n\n- [ ] Create delta specs in `accounts`.\n- [ ] Implement login/registration forms.\n- [ ] Implement user profile.\n- [ ] Implement author dashboard.\n- [ ] Implement reviewer dashboard.\n- [ ] Implement committee/chair dashboard.\n- [ ] Implement simple profile-flag access control.\n- [ ] Add authorization tests.\n\n### Acceptance criteria\n\n- [ ] User can authenticate.\n- [ ] Profile stores congress metadata.\n- [ ] Dashboards exist and respect scientific role.\n'

  create_issue_if_missing \
    "OpenSpec: add author submission initial flow" \
    "type:submissions,priority:p1,area:django,status:needs-spec" \
    "Scientific workflow MVP" \
'\n### Change ID\n\n`add-author-submission-initial-flow`\n\n### Objective\n\nImplement phase 1 of the two-phase scientific submission workflow.\n\n### Checklist\n\n- [ ] Create `Submission`, `SubmissionAuthor`, `SubmissionFile`.\n- [ ] Implement initial states.\n- [ ] Implement submission form.\n- [ ] Implement authors/affiliations.\n- [ ] Implement PDF upload.\n- [ ] Validate file type and size.\n- [ ] Protect files from direct public URL access.\n- [ ] Send confirmation email.\n- [ ] Implement status dashboard.\n\n### Essential criterion\n\n- [ ] Video is not required in the initial submission.\n'

  create_issue_if_missing \
    "OpenSpec: add review and decision workflow" \
    "type:reviews,priority:p2,area:django,status:needs-spec" \
    "Scientific workflow MVP" \
'\n### Change ID\n\n`add-review-decision-workflow`\n\n### Objective\n\nImplement review assignment, reviews, decisions and scientific committee workflow.\n\n### Checklist\n\n- [ ] Create `ReviewAssignment`.\n- [ ] Create `Review`.\n- [ ] Create `Decision`.\n- [ ] Implement reviewer assignment.\n- [ ] Implement conflict declaration.\n- [ ] Implement review form.\n- [ ] Implement final decision.\n- [ ] Implement “accepted with revisions”.\n- [ ] Implement final modality.\n- [ ] Send notifications.\n\n### Acceptance criteria\n\n- [ ] Chair can assign reviewer.\n- [ ] Reviewer can evaluate.\n- [ ] Committee can decide.\n- [ ] Author sees simplified status.\n'

  create_issue_if_missing \
    "OpenSpec: add final materials, proceedings and videos" \
    "type:submissions,type:reports,priority:p2,area:django,area:editorial,status:needs-spec" \
    "Outputs, operations and release readiness" \
'\n### Change ID\n\n`add-final-materials-proceedings-videos`\n\n### Objective\n\nImplement final-material phase for accepted works, proceedings and video links.\n\n### Checklist\n\n- [ ] Create `FinalMaterial`.\n- [ ] Implement final PDF upload.\n- [ ] Implement video link.\n- [ ] Implement poster link/file if applicable.\n- [ ] Implement publication authorization.\n- [ ] Implement committee validation.\n- [ ] Implement proceedings data.\n- [ ] Implement `VideoResource`.\n- [ ] Publish YouTube links without hosting videos.\n\n### Acceptance criteria\n\n- [ ] Accepted works can submit final materials.\n- [ ] Videos are links, not hosted files.\n- [ ] Proceedings data is exportable.\n'

  create_issue_if_missing \
    "OpenSpec: add reports, exports and indicators" \
    "type:reports,priority:p2,area:django,status:needs-spec" \
    "Outputs, operations and release readiness" \
'\n### Change ID\n\n`add-reports-exports-and-indicators`\n\n### Objective\n\nImplement indicators and exports for proceedings, monitoring and technical-scientific reporting.\n\n### Checklist\n\n- [ ] Export submissions CSV/XLSX.\n- [ ] Export authors.\n- [ ] Export institutions.\n- [ ] Export reviews/decisions according to permissions.\n- [ ] Indicators by thematic axis.\n- [ ] Indicators by final modality.\n- [ ] Indicators by status.\n- [ ] Indicators by institution/state/country.\n- [ ] Data for technical report.\n- [ ] Export tests.\n\n### Acceptance criteria\n\n- [ ] Committee can export core data.\n- [ ] Essential indicators are available.\n- [ ] Exports respect privacy and permissions.\n'

  create_issue_if_missing \
    "OpenSpec: harden deployment, security and backups" \
    "type:ops,priority:p2,area:security,area:deployment,status:needs-spec" \
    "Outputs, operations and release readiness" \
'\n### Change ID\n\n`harden-deployment-security-and-backups`\n\n### Objective\n\nPrepare the system for staging/production with minimum operational security.\n\n### Checklist\n\n- [ ] Configure production settings.\n- [ ] Require `DJANGO_SECRET_KEY`.\n- [ ] Configure `ALLOWED_HOSTS`.\n- [ ] Configure `CSRF_TRUSTED_ORIGINS`.\n- [ ] Configure HTTPS/proxy.\n- [ ] Configure secure cookies.\n- [ ] Configure real SMTP.\n- [ ] Configure protected storage.\n- [ ] Configure database backups.\n- [ ] Configure media backups.\n- [ ] Configure logs.\n- [ ] Review `django-axes`.\n- [ ] Run `manage.py check --deploy`.\n\n### Acceptance criteria\n\n- [ ] Production does not use `runserver`.\n- [ ] Secrets are not in the repository.\n- [ ] Private files remain protected.\n- [ ] Backup/restore is documented.\n'

  create_issue_if_missing \
    "OpenSpec: complete accessibility, performance and QA" \
    "type:qa,priority:p2,area:accessibility,area:ui-ux,status:needs-spec" \
    "Outputs, operations and release readiness" \
'\n### Change ID\n\n`complete-accessibility-performance-and-qa`\n\n### Objective\n\nClose the phase with comprehensive accessibility, performance and regression review.\n\n### Checklist\n\n- [ ] Review keyboard navigation.\n- [ ] Review visible focus.\n- [ ] Review contrast.\n- [ ] Review headings.\n- [ ] Review form labels.\n- [ ] Review alternative texts.\n- [ ] Review responsiveness.\n- [ ] Review Home performance.\n- [ ] Review image weight.\n- [ ] Review lazy loading.\n- [ ] Run test suite.\n- [ ] Review submission flow end to end.\n- [ ] Review review flow end to end.\n- [ ] Fix regressions.\n\n### Acceptance criteria\n\n- [ ] Site meets the project accessibility baseline.\n- [ ] Critical flows are tested.\n- [ ] No obvious public regressions remain.\n- [ ] Project is ready for staging/production.\n'

  # Derived UI/content issues
  create_issue_if_missing \
    "UI/content: add latest news block to Home" \
    "type:frontend,type:content,area:ui-ux,priority:p1,status:needs-spec" \
    "Public site refinement" \
'\n### Parent\n\n`review-public-site-ui-ux-round-1` / `implement-public-site-polish-round-1`\n\n### Checklist\n\n- [ ] Evaluate ideal placement for news block.\n- [ ] Decide whether it replaces the “Híbrido” card.\n- [ ] Show 2–3 recent news/announcements.\n- [ ] Include fallback when no news exists.\n- [ ] Ensure responsiveness.\n'

  create_issue_if_missing \
    "UI/content: fix venue address and map" \
    "type:frontend,type:content,area:editorial,priority:p0,status:needs-spec" \
    "Public site refinement" \
'\n### Official address\n\n```text\nCentro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha.\nR. Prof. Baeta Viana, s/n - Pampulha, Belo Horizonte - MG, 31270-901\n```\n\n### Google Maps\n\n```text\nhttps://maps.app.goo.gl/xzqJ2LCAHVP4hsFp6\n```\n\n### Checklist\n\n- [ ] Update address in CMS.\n- [ ] Update Home.\n- [ ] Update About.\n- [ ] Update Contact.\n- [ ] Update map.\n- [ ] Remove inherited previous-edition venue.\n'

  create_issue_if_missing \
    "UI/content: rewrite exaggerated Home copy" \
    "type:content,area:editorial,priority:p0,status:needs-spec" \
    "Public site refinement" \
'\n### Problem\n\nPhrases such as “maior evento de Neurovisão da América Latina” and generic/overblown wording such as “fronteira do conhecimento” do not fit the desired tone.\n\n### Checklist\n\n- [ ] Rewrite hero.\n- [ ] Rewrite subtitle.\n- [ ] Rewrite auxiliary CTAs.\n- [ ] Validate institutional, scientific and humble tone.\n'

  create_issue_if_missing \
    "UI/content: remove workshop references" \
    "type:content,priority:p0,area:editorial,status:needs-spec" \
    "Public site refinement" \
'\n### Checklist\n\n- [ ] Search for “workshop” across the project.\n- [ ] Remove or replace with real activities from the program.\n- [ ] Check Home, About, Program and cards.\n'

  create_issue_if_missing \
    "UI/content: footer institutional polish" \
    "type:frontend,type:content,area:ui-ux,priority:p1,status:needs-spec" \
    "Public site refinement" \
'\n### Checklist\n\n- [ ] Add FAPEMIG logo if an approved asset exists.\n- [ ] Add appropriate FAPEMIG text mention.\n- [ ] Replace “Instagram” text with an accessible icon.\n- [ ] Remove redundant text if copyright and branding already cover it.\n- [ ] Ensure alt text and aria-label.\n'

  create_issue_if_missing \
    "UI/content: improve About page content and layout" \
    "type:content,type:frontend,area:editorial,area:ui-ux,priority:p1,status:needs-spec" \
    "Public site refinement" \
'\n### Checklist\n\n- [ ] Expand About page text.\n- [ ] Remove redundant “O que esperar?” if retained on Home.\n- [ ] Improve heading hierarchy.\n- [ ] Reorganize “Local e acesso”.\n- [ ] Improve team cards.\n- [ ] Adjust supporting entities.\n'

  echo "Done."
}

main "$@"
