## Context

The XII CBNV 2026 platform has reached functional maturity. The current state requires a focused pass on accessibility (WCAG 2.2 AA), mobile responsiveness, and performance optimization to ensure a high-quality user experience. Additionally, a robust QA suite is needed to prevent regressions during the final countdown to the congress.

## Goals / Non-Goals

**Goals:**
- Achieve 100% WCAG 2.2 AA compliance for critical paths.
- Lighthouse Performance score > 90 for the public site.
- 100% responsive usability (no horizontal scrolling on mobile, 44px touch targets).
- Implement E2E testing for all core user journeys.
- Integrate automated accessibility and performance checks into the developer workflow.

**Non-Goals:**
- Adding new features or pages.
- Significant database schema changes.
- Replacing the existing tech stack (Wagtail/Tailwind/Alpine.js).

## Decisions

### 1. Accessibility (A11y) Strategy
- **Framework**: Use `axe-core` via Playwright for automated auditing.
- **Manual Check**: Periodic testing with screen readers (NVDA/VoiceOver) and keyboard-only navigation.
- **Components**: Standardize `Focus Ring` and `Skip Link` in the base design system.
- **Rationale**: Axe-core catches ~50% of issues automatically; manual testing is required for the rest (logical order, meaningful labels).

### 2. Performance Optimization
- **Images**: Use Django-Wagtail's built-in image processing to generate WebP/AVIF versions. Implement `loading="lazy"` on all non-above-the-fold images.
- **Assets**: Ensure Tailwind build is minified and uses the `@theme` first approach to minimize CSS size.
- **Caching**: Leverage Django's template fragment caching for high-traffic components like the Program Timeline.
- **Rationale**: Images are the largest contributors to LCP. Caching is essential for the complex timeline component.

### 3. Responsive Design
- **Tooling**: Use Tailwind CSS container queries and responsive utilities (`sm:`, `md:`, `lg:`).
- **Mobile First**: Refine layouts starting from 320px width. Ensure touch targets are distinct and easy to tap.
- **Rationale**: Many congress participants will access the site via mobile devices during the event.

### 4. Quality Assurance (QA) and E2E Testing
- **Framework**: Playwright for E2E tests, Pytest-Django for integration tests.
- **Coverage**:
    - **Visitor**: Home -> Program -> Info pages.
    - **Author**: Login -> Submit Work -> Dashboard.
    - **Reviewer**: Login -> Assigned Reviews -> Evaluation Form.
    - **Committee (Chair)**: Dashboard -> Submission List -> File Access.
- **Rationale**: Playwright provides the most reliable browser automation and built-in accessibility testing integration.

## Risks / Trade-offs

- **[Risk]** Accessibility fixes may require breaking some aesthetic choices (e.g., low-contrast colors) → **[Mitigation]** Use the Green/Blue/Deep Navy palette from the Stitch design system, adjusting shades for contrast compliance while maintaining brand identity.
- **[Risk]** Performance tools may add complexity to the build pipeline → **[Mitigation]** Keep tools lightweight; use `lighthouse-cli` as a standalone audit tool.
- **[Risk]** E2E tests can be brittle → **[Mitigation]** Use robust selectors (data-testid, ARIA labels) instead of fragile CSS paths.

## Acceptance Criteria

- [ ] All pages pass `axe-core` automated audits with zero critical violations.
- [ ] Lighthouse Performance, Accessibility, and Best Practices scores are all 90+.
- [ ] Site is fully usable via keyboard alone (visible focus, logical tab order).
- [ ] All Playwright E2E suites pass in headless mode.
- [ ] No horizontal overflow on screens down to 320px width.
