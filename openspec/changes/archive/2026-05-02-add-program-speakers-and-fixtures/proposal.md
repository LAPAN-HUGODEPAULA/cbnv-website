## Why

The XII CBNV 2026 needs a robust way to manage its scientific program and speakers. This change implements the core data structures and administrative interfaces to manage event days, sessions, talks, and participating experts, ensuring that preliminary program data can be seeded and unconfirmed participants can be managed without being visible to the public.

## What Changes

- **New `program` app**: Implements models for `Speaker`, `ProgramDay`, `ProgramSession`, and `ProgramTalk` as Wagtail Snippets.
- **Wagtail CMS Integration**: All program models exposed as Snippets for centralized admin management.
- **`ProgramPage`**: A single Wagtail page that renders the program timeline by day, reusing the existing `timeline.html` design system component. No `SpeakerIndexPage` — speakers appear inline.
- **Preliminary Fixtures**: Seeds the database with the canonical preliminary program data for Days 1, 2, and 3, including confirmed speakers (Hugo, Jerome, Carla).
- **Visibility Control**: Items with status other than `confirmed` are entirely omitted from rendering — no empty time slots in the timeline.

## Capabilities

### New Capabilities
- `program`: Management of the scientific program structure, including days, sessions, talks, and speakers, with support for visibility statuses and activity types.

### Modified Capabilities
- `content-cms`: Integration of program-related snippets into the administrative interface.
- `public-site`: Addition of the ProgramPage to the public-facing website.

## Impact

- **Database**: New tables for program and speakers.
- **Admin**: New Snippet sections in Wagtail admin for managing program data.
- **Templates**: One new page template (`ProgramPage`) reusing existing timeline component.
- **Fixtures**: Management command for seeding the preliminary program.
- **Design System**: Reuses `timeline.html`, `badge.html` components. No new frontend components needed.
