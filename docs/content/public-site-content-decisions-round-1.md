# Public Site Content Decisions - Round 1

## Metadata

- Change ID: `produce-public-site-content-round-1`
- Status: decisions for content production handoff

## Decisions

| Decision | Outcome | Rationale | Handoff |
|---|---|---|---|
| Home "O que esperar?" | Do not reintroduce as a separate section in round 1. | The UI review found no rendered section and warned against duplicating Home/About content. | Revisit only in public-site polish if layout gives it a distinct user role. |
| Event scale language | Use modest national/technical-scientific positioning. | Requirements define national scope and medium size; no source supports largest-event claims. | Consistency verification should scan all pages for inflated claims. |
| Format wording | Treat as provisional. | Sources differ between "presencial com transmissão híbrida" and "presencial com transmissão on-line"; operational details are pending. | Confirm final public wording before lock. |
| Workshops | Do not mention workshops. | Current program seed includes talks, sessions, posters, oral presentations and roundtables, but no workshop activity. | Add only if official program data changes. |
| Submissions | State clearly that initial submission does not require video. | Required by source-of-truth and OpenSpec deltas. | Keep sentence visible on Submissions and author-facing teaser copy. |
| Registration | Describe as external. | Payment, certificates and QR/check-in are outside the platform scope. | Keep CTA disabled while external link is unavailable. |
| Previous editions | Frame as archive/history. | Prevent historical facts from being mistaken for current 2026 information. | Add stronger labels during polish if needed. |
| CMS implementation | Do not add fields or migrations in this round. | Current fields cover many page intros, but several section-level copy blocks lack stable CMS targets. | Copy map marks missing targets as `needs-field` or `defer`. |
| Legacy seed | Do not update `populate_cbnv` as authoritative content. | `docs/program-venue-data.md` treats it as legacy/dev-only. | Future seed work should use canonical seed paths. |

## Safe Implementation Notes

Round-1 copy can be applied later to existing Wagtail page fields where safe:

- `HomePage.intro`
- `ProgramPage.intro`
- `SpeakerIndexPage.intro`
- `SubmissionsPage.intro`
- `RegistrationPage.intro`
- `SponsorsPage.intro`
- `PreviousEditionsPage.intro`
- `ContactPage.intro`
- selected `CoreSettings` fields

Blocks marked `needs-field` should not force schema expansion in this change.
