## Context

The submission workflow exists through the decision phase (change `add-review-decision-workflow`): submissions can be accepted (oral/poster/video) or rejected. The 13-state machine already includes `final_materials_pending`, `ready_for_proceedings`, and `published_in_proceedings`, but no views, models, or logic implement them.

The `proceedings` app currently only manages historical editions. The `videos` app manages YouTube-only `VideoResource` snippets. Both need extension for the current edition's proceedings workflow.

## Goals / Non-Goals

**Goals:**
- Implement the final materials collection flow for accepted submissions.
- Allow the commission to validate materials and mark works as proceedings-ready.
- Enable publication of proceedings to the public site.
- Associate YouTube video links with accepted oral/video presentations.
- Provide a public proceedings page listing published works.
- Notify authors throughout the materials lifecycle.

**Non-Goals:**
- Video hosting or streaming (YouTube links only — existing `VideoResource`).
- Certificate generation or QR code check-in.
- Complex proceedings formatting (PDF generation, DOI assignment).
- Payment processing or registration integration.

## Decisions

### 1. FinalMaterial Model

A new `FinalMaterial` model linked to `Submission`:

| Field | Type | Purpose |
|---|---|---|
| `submission` | FK → Submission | One-to-one with accepted submissions |
| `final_pdf` | FileField (protected storage) | Author-uploaded revised PDF |
| `presentation_file` | FileField (protected storage) | Presentation slides (PPTX/PDF) |
| `video_url` | URLField | YouTube link for oral/video presentations |
| `received_at` | DateTimeField | When author submitted materials |
| `validated_at` | DateTimeField | When commission validated |
| `validated_by` | FK → User | Commission member who validated |
| `notes` | TextField | Internal notes from commission |

**Rationale**: Separating `FinalMaterial` from `Submission` keeps the submission model focused on metadata. One-to-one ensures at most one set of final materials per submission. Protected storage prevents direct URL access.

### 2. Video Association

Accepted oral/video submissions optionally link to a `VideoResource` via a nullable FK on `FinalMaterial` (`video_resource` field). This reuses the existing `VideoResource` snippet and its YouTube URL parsing/validation.

Alternatively, a simple `video_url` URLField on `FinalMaterial` stores the YouTube link directly without requiring a `VideoResource` to be pre-created in the CMS. This is simpler for the author flow.

**Decision**: Use `video_url` URLField on `FinalMaterial` for simplicity. The commission can optionally link to a `VideoResource` via a separate `video_resource` FK for enriched metadata (thumbnail, description, public gallery). Both fields are optional.

### 3. State Machine Activation

The transitions are already defined in `VALID_TRANSITIONS`:

```
accepted_oral/poster/video → final_materials_pending → ready_for_proceedings → published_in_proceedings
```

Implementation:
- When commission triggers "Request final materials": submission transitions to `final_materials_pending`. Notification sent to author.
- When author uploads materials: `FinalMaterial` is created/updated with `received_at`. No state change yet.
- When commission validates materials: `validated_at` set. Submission transitions to `ready_for_proceedings`. Notification sent to author.
- When commission publishes: Submission transitions to `published_in_proceedings`. Work appears on public proceedings page.

**Rationale**: Commission controls the state transitions. Author only uploads; commission validates and publishes.

### 4. Public Proceedings Page

A public Wagtail page (`ProceedingsPage`) or a regular Django view listing published submissions:

- Filters: `status == "published_in_proceedings"`
- Displays: title, authors, abstract, modality, thematic axis, PDF download link
- For oral/video with video_url: embedded YouTube player

**Decision**: Use a Django view (not Wagtail page) for the proceedings listing. This keeps it simple and avoids Wagtail page creation overhead for what is essentially a filtered query.

### 5. File Validation Rules

- `final_pdf`: PDF only, max 10 MB
- `presentation_file`: PDF or PPTX, max 50 MB
- `video_url`: Valid YouTube URL (reuse `parse_youtube_url` from `videos/models.py`)

### 6. Authorization

| Action | Role |
|---|---|
| Upload final materials | Author (submission owner) |
| View materials upload page | Author (own submission only) |
| Validate materials | Chair |
| Request materials | Chair |
| Publish to proceedings | Chair |
| View public proceedings | Anonymous (public) |
| Download proceedings PDF | Anonymous (public) |

### 7. Notification Flow

1. **Material requested**: Chair triggers → email to author with deadline and upload instructions
2. **Material received**: Auto on upload → confirmation email to author
3. **Material validated**: Chair validates → email to author confirming acceptance
4. **Published in proceedings**: Chair publishes → email to author with link to proceedings page
