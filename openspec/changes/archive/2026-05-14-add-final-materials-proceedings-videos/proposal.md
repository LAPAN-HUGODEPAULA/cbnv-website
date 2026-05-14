# Proposal: Add Final Materials, Proceedings and Videos

## Why

After a scientific submission is accepted, authors must provide final versions of their work (e.g., corrected PDF, presentation files) and potentially a link to a video presentation. These materials are essential for the publication of the proceedings and the realization of the congress.

## What Changes

- **Final Material Upload**: Interface for authors to upload the final PDF, presentation file (PDF/PPTX), and provide a YouTube URL.
- **Admin Validation**: Interface for scientific committee members to validate the received final materials.
- **Proceedings Management**: Logic to group validated submissions into editions and prepare them for publication.
- **YouTube Integration**: Integration with the `videos` app to parse and display video links.
- **Previous Editions**: Management of data and links for previous editions of the congress.

## Capabilities

### New Capabilities
- `proceedings`: Implement the final materials and edition management requirements.
- `videos`: Implement YouTube link parsing and display logic.

### Modified Capabilities
- `submissions`: Add status transitions for final materials and proceedings.
- `notifications`: Implement e-mail notifications for materials requested, received, and validated.
- `dashboards`: Add final material actions to author and chair dashboards.
- `security`: Enforce object-level permissions for final material uploads and validation.
- `qa`: Define tests for the final materials and proceedings workflow.

## Impact

- **proceedings app**: Major updates to models, views, and templates.
- **videos app**: Implementation of URL parsing utilities.
- **submissions app**: Updates to status machine.
- **notifications app**: New e-mail templates and services.
- **Database**: New `FinalMaterial` and `Edition` records.
