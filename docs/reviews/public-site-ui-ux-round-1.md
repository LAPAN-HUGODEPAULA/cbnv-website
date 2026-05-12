# Public Site UI/UX Review - Round 1

## Metadata

- Change ID: `review-public-site-ui-ux-round-1`
- Reviewer: Codex
- Date: 2026-05-11 21:56:32 -03
- Branch: `change/review-public-site-ui-ux-round-1`
- Commit: `a76324534bd3366421a9f868d5bc20336078e775`
- Environment: local Django development server at `http://127.0.0.1:8001/`
- Browser: Playwright Chromium headless
- Viewports: 390x844, 768x1024, 1366x768
- Seed data state: canonical event settings/supporting entities seeded; `populate_cbnv` data loaded into disposable SQLite DB at `/tmp/cbnv-review-uiux.sqlite3`
- Screenshots: `/tmp/cbnv-uiux-mobile-390-home.png`, `/tmp/cbnv-uiux-mobile-390-programacao.png`, `/tmp/cbnv-uiux-mobile-390-inscricao.png`, `/tmp/cbnv-uiux-tablet-768-home.png`, `/tmp/cbnv-uiux-desktop-1366-home.png`
- Validation before edits: `openspec validate review-public-site-ui-ux-round-1 --strict` passed
- Environment limitation: default PostgreSQL on `localhost:5432` was unavailable and Docker daemon was unavailable, so the review used a disposable SQLite DB through existing settings variables.

## Executive Summary

The public MVP has a coherent visual foundation: dark scientific palette, clear event identity, visible date/location/theme on Home, a readable Program page at mobile and desktop sizes, accessible skip link/focus patterns in shared navigation, and conservative coming-soon language for submissions/registration templates.

The largest issue is page reachability in the seeded local site. `/inscricao/`, `/palestrantes/` and `/contato/` returned 404, even though corresponding templates and page types exist. This blocks participant, speaker-discovery and contact/location journeys and creates broken footer links.

The next-highest risks are navigation coverage and content taxonomy. Header navigation omits several MVP pages, while supporting entities are repeated under multiple labels across Home, About and Sponsorship. These should be standardized before final copy and polish.

## Top Findings

1. `UXR1-001`: Registration, Speakers and Contact were not reachable in the seeded local site.
2. `UXR1-002`: Header navigation does not expose all MVP pages.
3. `UXR1-003`: Latest announcements sit below the program preview, which weakens returning-visitor flow.
4. `UXR1-006`: Sponsor/support/partner terminology is inconsistent across pages.
5. `UXR1-007`: Contact form should receive a focused accessibility/forms pass before launch.

## User Journey Review

### General visitor

A visitor landing on Home can identify the event name, theme, dates and CAD-1/UFMG location quickly. The next action is less clear: Program is easy to reach, but Registration and Contact are not reliably reachable in the seeded page tree. The hero supports orientation; navigation completeness is the main blocker.

### Potential author

Submissions is reachable and explicitly states that the initial submission does not require video. The page avoids implying that a workflow is already implemented. The remaining gap is next-action clarity: authors need a factual coming-soon path, expected channel or contact/notification option.

### Potential participant

Participants can find dates, location and program from Home and Program. Registration information is blocked by the missing `/inscricao/` route in the seeded local site, even though the template content is appropriate about external registration and no internal payment/certificate/QR processing.

### Potential sponsor/supporter

Sponsorship is reachable at `/patrocinadores/`, and the page includes support entities and contact intent. The header does not include a Patrocinio item in the seeded configured menu, so sponsors need footer discovery or a guessed URL. Terminology also needs cleanup before public copy.

### Returning visitor

Returning visitors can access News from the configured header, and Home includes recent announcements. The announcements are placed after the program preview, so updates are not a strong first-screen signal. Previous Editions is clearly archival, which helps separate current and historical content.

## Page-by-Page Review

### Home

Home communicates identity, theme, date, location and format clearly. The Program preview is useful and responsive. Recent announcements are present but appear too low for returning visitors. The supporting-entity grid is useful but repeats similar institutional content that also appears on About and Sponsorship.

### About

About covers theme, welcome, objectives, local/access, organization and committee. It needs stronger institutional copy and a clearer explanation of why this edition exists. Local/access content uses current CAD-1/UFMG data and a map embed, which is appropriate. The committee section works as a fallback but should be treated as provisional until a structured committee model or final source is confirmed.

### Program

Program renders day-based schedule content and remains readable at 390, 768 and 1366 px with no horizontal overflow. It has clear day headings, time ranges and badges. It may need stronger scan aids once final program density increases, such as anchors, compact day tabs or a more obvious time rail.

### Speakers

The SpeakerIndex template is sound, with photo fallback initials, affiliation display, status badge and program links. However, `/palestrantes/` was not published in the seeded local page tree, making the page unavailable to visitors. This is a launch blocker for the speaker journey.

### Submissions

Submissions is reachable and handles the key rule well: initial submission does not require video. It also avoids overpromising workflow availability. The page should add phase-aware next action copy once submission dates/channel are known.

### Registration

The Registration template correctly explains external registration and states that this site does not process payment, certificate or QR code. The seeded local route `/inscricao/` returned 404, so the participant journey fails until page creation/navigation are fixed.

### Sponsorship

Sponsorship is reachable and includes a contact section. The page is a reasonable placeholder for support information, but it needs clearer distinction between organizers, funding agencies, sponsors, partners and supporters.

### Previous Editions

Previous Editions is clearly framed as historical archive and did not override current 2026 facts. The page should use stronger archive labeling in the final polish pass so historical locations/themes are not mistaken for current event information while scanning.

### Contact

The Contact template provides separate general, submissions and sponsorship contact channels plus current venue information. In the seeded local site, `/contato/` returned 404, which blocks trust and location confirmation. The form markup has labels and focus replacement, but should receive an autocomplete/helper/error-state pass.

## Accessibility Observations

- Shared layout includes a skip link to `#main-content`.
- Header, nav, main and footer landmarks are present.
- Header and mobile nav links use visible `focus-visible` outlines.
- Icon-only Instagram link uses an accessible label; decorative SVG menu icons are inside a labeled button.
- Form fields on Contact have visible labels and focus replacement, but need `autocomplete` values and more detailed form affordance review.
- Heading baseline is acceptable on rendered pages: each checked public page had one `h1`; page sections use `h2`.
- Program readability does not rely only on color because activity badges include text labels.
- Missing public routes render development 404 pages; at 390 px those pages showed horizontal overflow.

## Responsive Observations

Checked viewports: 390x844, 768x1024 and 1366x768.

Rendered pages with 200 status had no horizontal overflow in Playwright checks. Program remained readable on mobile through stacked cards. The 404 pages for missing seeded routes overflowed horizontally on 390 px, which reinforces the need to prevent missing public MVP pages before launch.

## Content Placement and Copy Risks

- Home is structurally ready for final copy but should elevate latest updates.
- About needs deeper institutional narrative before content production.
- Submissions needs clearer coming-soon/next-action copy without inventing workflow details.
- Registration copy is appropriately cautious but unavailable in the seeded site.
- Sponsor/support labels need a shared taxonomy.
- Avoid claims such as largest/best/leading event unless a factual source is added.
- Keep "video not required for initial submission" prominent.

## Section Decisions

| Section | Decision | Rationale | Target proposal |
|---|---|---|---|
| Home latest news/announcements | move | Returning visitors need faster access to updates. | implement-public-site-polish-round-1 |
| Home format/Hibrido card | merge | Keep format visible but merge with date/location metadata unless hybrid details are confirmed. | produce-public-site-content-round-1 |
| Home/About "O que esperar?" | remove | It is not present in rendered pages; do not reintroduce a duplicate block without a precise content role. | produce-public-site-content-round-1 |
| Partner/support grids | rewrite | Keep entities, but standardize taxonomy and labels across pages. | verify-cross-page-content-consistency |
| About committee section | defer | Useful fallback, but should remain provisional until final committee source/model is confirmed. | produce-public-site-content-round-1 |
| Footer long event text | simplify | Footer facts are useful, but should be shorter after links are fixed. | implement-public-site-polish-round-1 |
| Contact page | keep | Required for trust, venue and contact routing; currently blocked by missing seeded route. | implement-public-site-polish-round-1 |
| Registration page | keep | Template accurately frames external registration; route/publishing must be fixed. | implement-public-site-polish-round-1 |
| Speakers page | keep | Template supports the program journey; route/publishing must be fixed. | implement-public-site-polish-round-1 |

## Backlog Summary

The prioritized backlog is maintained in `docs/reviews/public-site-ui-ux-round-1-backlog.md`.

Counts:

- P0: 1
- P1: 6
- P2: 6
- P3: 1

## Handoff: `produce-public-site-content-round-1`

- Expand About with institutional context, edition purpose and audience fit.
- Preserve clear "initial submission does not require video" language.
- Add next-action copy for Submissions without promising an unavailable workflow.
- Confirm whether format should say presencial, hybrid or livestream-supported.
- Rewrite support/sponsor labels only after taxonomy is agreed.
- Keep claims factual and avoid promotional exaggeration.
- Treat committee copy as provisional unless final names/roles are approved.

## Handoff: `verify-cross-page-content-consistency`

- Verify event name, edition, theme, dates and venue across Home, About, Program, Registration, Contact and Footer.
- Standardize page labels: Patrocinio vs Apoiadores vs Entidades de Apoio vs Organizacao.
- Check footer links against published Wagtail pages.
- Confirm current CAD-1/UFMG address appears anywhere venue is shown.
- Check Previous Editions content never overrides current 2026 facts.
- Standardize CTA labels for Program, Registration, Submissions and Contact.

## Handoff: `implement-public-site-polish-round-1`

- Ensure seeded canonical public page tree includes Registration, Speakers and Contact.
- Align primary navigation with the required MVP page set.
- Move or summarize latest announcements closer to Home hero.
- Add a contact form accessibility pass: autocomplete, helper text and error focus.
- Simplify footer and remove broken links.
- Consider a branded public 404 page after MVP route stability is fixed.
- Recheck top menu navigation on Home, Sobre, Programacao and Edicoes Anteriores.

## Risks for Next Proposal

- Writing final copy before fixing page reachability will hide critical journey failures.
- Sponsor/support copy may be rewritten multiple times unless taxonomy is settled first.
- Registration/submission wording can accidentally imply workflow readiness if not kept phase-aware.
- Local QA needs either running PostgreSQL/Docker or a documented disposable DB path.

## Recommended Next Steps

1. Fix page creation/navigation reachability in `implement-public-site-polish-round-1`.
2. Run `verify-cross-page-content-consistency` before final copy lock.
3. Use this backlog to scope `produce-public-site-content-round-1` and avoid rewriting sections marked remove/defer.
