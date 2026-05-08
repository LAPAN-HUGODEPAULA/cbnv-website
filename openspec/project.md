# XII CBNV 2026 — OpenSpec Project Context

This file defines the permanent context, architecture, and constraints for the **XII Congresso Brasileiro de Neurociências da Visão (CBNV 2026)** digital platform.

## 1. Project Overview
- **Name:** XII CBNV 2026 — Website e plataforma digital do Congresso Brasileiro de Neurociências da Visão.
- **Goal:** Public and administrative platform for the congress.
- **Language:** Portuguese (Brazil).
- **Tone:** Institutional, scientific, and clear.

## 2. Mandatory Tech Stack
- **Python:** 3.14.x
- **Backend:** Django 6.0.x (Monolithic modular)
- **CMS:** Wagtail 7.4.x LTS
- **Database:** PostgreSQL 18.3
- **Frontend:** Tailwind CSS 4.x + HTMX + Alpine.js (optional for micro-interactions)
- **Node.js:** 24 LTS when frontend tooling is required
- **Infrastructure:** Docker Compose, Caddy or Nginx (Reverse Proxy)
- **Email:** Transactional/Institutional SMTP

## 3. Architecture & Principles
- **Design Pattern:** Django-idiomatic modular monolith.
- **Apps by Domain:** `core`, `pages`, `program`, `submissions`, `reviews`, `proceedings`, `videos`, `sponsors`, `accounts`, `reports`, `notifications`.
- **Rendering:** Server-Side Rendering (SSR) via Django Templates. No complex SPAs.
- **Accessibility:** Target WCAG 2.2 AA (high contrast, keyboard navigation).
- **Security:** Submission files MUST be protected and never accessible via direct public URL.
- **Authentication:** Django's default `auth.User` model with congress metadata stored in `accounts.UserProfile`.

## 4. Design Guidelines
- **Direction:** Dark-mode first, Glassmorphism (moderated).
- **Palette:**
  - Deep Navy (`#081426` / `#04132b`): Primary canvas.
  - Electric Blue (`#214BFF`): Primary actions and links.
  - Neuro Green (`#2FEA8B`): Active states and success signals.
- **Typography:**
  - Headlines: **Newsreader** (Academic/Literary weight).
  - Body: **Inter** (Legibility).
  - Labels: **Space Grotesk** (Technical/Futuristic).

## 5. Critical Business Rules
- **Two-Phase Submission:**
  1. **Initial:** Metadata + PDF (No video required).
  2. **Final:** Revised materials + Video link (for approved works ONLY).
- **Out of Scope:**
  - NO internal payment processing (external links only).
  - NO certificate/QR code generation (external partners).
  - NO video hosting (YouTube links only).
  - NO complex RBAC for CMS (single administrative user for content).
  - NO Next.js or Strapi.

## 6. OpenSpec Operational Rules
- **Delta Specs:** MUST use `ADDED`, `MODIFIED`, `REMOVED`, or `RENAMED` for requirements.
- **Scenarios:** MUST use `Given`, `When`, `Then` format.
- **Process:** No implementation before a proposal is validated and approved.
- **Sequence:** Implementation follows sequential change proposals as defined in the Implementation Plan.

## GitHub/OpenSpec workflow

Every implementation task MUST follow this mapping:

- GitHub issue title starts with `OpenSpec:`
- Issue body contains `Change ID: <change-id>`
- Branch name is `change/<change-id>`
- OpenSpec change folder is `openspec/changes/<change-id>/`
- PR title starts with `[<change-id>]`
- PR body contains `Closes #<issue-number>`
- PR body contains validation checklist
- No code implementation before `openspec validate <change-id> --strict` passes
- No PR merge before tests pass
- Completed changes MUST be archived using `openspec archive <change-id> --yes`

---
*Last updated: 2026-05-08*
