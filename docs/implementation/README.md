# Implementation Strategy

This directory contains the operational roadmap for the **XII CBNV 2026** platform.

## OpenSpec Workflow

The project follows **Spec-Driven Design (SDD)** using the OpenSpec methodology. This ensures that every feature is grounded in the architectural mandates and business requirements before a single line of code is written.

### 1. Sequential Change Proposals
The implementation must follow the sequence defined in `docs/CBNV2026_OpenSpec_Plano_Implementacao_v1.md`. Each step in the plan requires a corresponding **Change Proposal** in `openspec/changes/`.

### 2. Operational Rules
- **No Early Implementation:** Do not start coding until the proposal is validated and approved.
- **Delta Requirements:** Clearly mark changes using `ADDED`, `MODIFIED`, `REMOVED`, or `RENAMED`.
- **Validation Scenarios:** Define clear `Given/When/Then` scenarios for every feature.
- **Single Source of Truth:** Always consult `docs/CBNV2026_Requisitos_Arquitetura_v1.md` as the primary reference.

### 3. Repository Evolution
This repository will evolve through atomic, sequential updates. Each successful proposal and its subsequent implementation represent a stable milestone in the platform's development.

---
*For more details on the architecture and tech stack, refer to `openspec/project.md`.*
