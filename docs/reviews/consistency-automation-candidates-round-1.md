# Consistency Automation Candidates - Round 1

## Metadata

- Change: `verify-cross-page-content-consistency`
- Reviewed commit: `d3044e5`
- Scope: candidate checks only. No automation was implemented in this change.

## Candidates

| Check | Risk | Suggested mechanism | Current feasibility | Priority | Target proposal |
|---|---|---|---|---|---|
| Canonical event facts render in public pages | Repeated event dates/venue/name drift across Home/About/Contact/Footer/SEO | Django smoke tests that seed `CoreSettings` and assert rendered page text | High; existing public-site tests already cover parts of this | P1 | automated smoke tests |
| Notification templates use canonical event context | Hardcoded dates/venue in e-mails become stale after settings change | Unit tests render all notification templates with custom event settings | Medium; services need shared context injection | P1 | notification correction |
| Legacy facts outside archive contexts | Old dates, venue, 11th-edition copy leak into current pages | Static grep allowlist for previous-editions, docs archive and prototypes | High | P1 | management-command/static check |
| Status labels in reports/exports | Raw machine statuses appear in user-facing reports | Export tests asserting label or code+label columns for each export | High | P1 | export/report correction |
| Proceedings publication boundary | Ready-for-proceedings items appear as published public works | View tests for `ready_for_proceedings` vs `published_in_proceedings` visibility | High | P1 | proceedings correction |
| Protected file URL exposure | Direct protected-media paths leak in public pages or exports | Tests for public pages and export bodies not containing protected storage paths | High | P0 | security/privacy check |
| Final-material requirement alignment | Form labels/e-mails say required fields that validation does not require | Template/content tests for required markers and form validation rules | Medium | P2 | final-material workflow correction |
| Notification duplicate-send behavior | Repeated transitions or uploads send duplicate transactional e-mails | Workflow tests using mail outbox and sent marker/idempotence behavior | Medium | P2 | notification correction |
| Accessibility labels for icon-only controls | Screen-reader action names drift from visible actions | Template lint or axe/Playwright checks for icon-only buttons/links | Medium | P2 | accessibility correction |
| Persona status map regression | Author/chair/reviewer status labels drift after future workflow changes | Unit tests for status-label helper per persona | Medium; requires helper extraction | P2 | domain/model correction |
| Video gallery promotion rule | Final-material YouTube URL appears publicly without explicit `VideoResource` promotion | Proceedings/video tests asserting no embed without public video resource | High; similar tests exist | P2 | video/proceedings check |
| CTA link state | Registration/submission/livestream CTAs become active without configured links | Public page smoke tests for `available`, `coming_soon`, `unavailable` states | High | P2 | public-site smoke tests |

## Prioritization

The first automation pass should cover canonical facts, legacy fact allowlisting, status/export labels, proceedings publication boundary and protected-file URL exposure. These checks have the best risk-to-effort ratio and directly cover P0/P1 classes from the backlog.
