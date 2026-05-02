# XII CBNV 2026 — Project Context (GEMINI.md)

This file serves as the foundational mandate for all AI agents working on the **XII CBNV 2026** digital platform.

## 1. Project Overview
The **XII Congresso Brasileiro de Neurociências da Visão (CBNV 2026)** digital platform is a monolithic modular application designed to handle both the public-facing congress website and the administrative scientific workflow (submissions, reviews, and proceedings).

*   **Status:** Planning and Architecture phase.
*   **Single Source of Truth:** `docs/CBNV2026_Requisitos_Arquitetura_v1.md`
*   **Implementation Path:** `docs/CBNV2026_OpenSpec_Plano_Implementacao_v1.md`
*   **Visual Reference:** `docs/stitch_cbnv_2026_digital_platform/` (Stitch export)

## 2. Core Mandates & Constraints

### 2.1 Technology Stack
*   **Framework:** Django (Monolithic modular)
*   **CMS:** Wagtail
*   **Database:** PostgreSQL
*   **Frontend:** Tailwind CSS + HTMX + Alpine.js (minimal micro-interactions)
*   **Rendering:** Server-Side Rendering (SSR) via Django Templates.
*   **Environment:** Docker Compose (Caddy/Nginx as reverse proxy)
*   **Prohibited:** Next.js, Strapi, complex SPAs. (Note: Ignore legacy `.gitignore` entries for Next.js; the project has transitioned to Django/Wagtail).

### 2.2 Functional Boundary (Out of Scope)
*   **NO** internal payment processing (use external links).
*   **NO** certificate generation (handled by external partners).
*   **NO** QR code/check-in system (handled by external partners).
*   **NO** video hosting (use YouTube links/playlists ONLY).
*   **NO** complex RBAC for CMS (single administrative user for content).

### 2.3 Critical Business Rules
*   **Two-Phase Submission:** 
    1.  Initial: Metadata + PDF (NO video required).
    2.  Final: Revised materials + Video link (for approved works).
*   **Security:** Submission files MUST be protected and never accessible via direct public URL.
*   **Acessibility:** Target WCAG 2.2 AA (high contrast, keyboard navigation, screen reader support).

## 3. Development Workflow (Spec Driven Design)
The project follows **Spec Driven Design (SDD)** using **OpenSpec**.

1.  **Requirement First:** Consult `docs/CBNV2026_Requisitos_Arquitetura_v1.md` before any task.
2.  **Proposal Phase:** Create/Validate a Change Proposal in `openspec/changes/`.
3.  **Implementation:** Apply code ONLY after proposal validation.
4.  **Verification:** Run tests and validate against OpenSpec requirements.

### Implementation Order (Sequential)
1.  `bootstrap-django-wagtail-platform`
2.  `add-design-system-and-layout-shells`
3.  `add-core-cms-content-models`
4.  `add-program-speakers-and-fixtures`
5.  `add-public-site-pages`
6.  ... (see Implementation Plan for the full list)

## 4. Key Files & Directories
*   `docs/`: Core documentation and PDF program.
*   `docs/CBNV2026_Requisitos_Arquitetura_v1.md`: Primary requirements.
*   `docs/CBNV2026_OpenSpec_Plano_Implementacao_v1.md`: Implementation steps.
*   `docs/stitch_cbnv_2026_digital_platform/`: Design system and screen references.
*   `_legacy/`: Historical materials (migration use only, not for design reference).

## 5. Coding Standards
*   **Django Idiomatic:** Use standard Django patterns, apps, and ORM.
*   **Wagtail Usage:** Prefer built-in Wagtail features for CMS (SiteSettings, Snippets).
*   **Tailwind:** Use utility classes; maintain a consistent design system based on the Stitch tokens.
*   **A11y:** Semantic HTML is mandatory.

## 6. Commands (Inferred/Planned)
*   **Setup:** `docker compose up --build`
*   **Migrations:** `python manage.py migrate`
*   **Test:** `pytest`
*   **OpenSpec:** `openspec validate <change-id> --strict`

---
*Last updated: 2026-05-02*
