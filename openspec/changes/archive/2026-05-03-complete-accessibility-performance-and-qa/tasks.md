## 1. Setup and Tooling

- [x] 1.1 Install Playwright and Axe-core for accessibility testing: `npm install -D playwright @playwright/test @axe-core/playwright`
- [x] 1.2 Configure Playwright for Django environment (base URL, browser contexts)
- [x] 1.3 Install Lighthouse CLI for performance auditing: `npm install -D lighthouse`
- [x] 1.4 Add `a11y:test` and `perf:audit` scripts to `package.json`

## 2. Design System and Global Accessibility

- [x] 2.1 Update `src/input.css` to ensure all `@theme` colors meet WCAG 2.2 AA contrast ratios
- [x] 2.2 Standardize the focus ring component in CSS using Tailwind's `focus-visible:ring-2`
- [x] 2.3 Implement the "Skip to Content" link in `templates/layouts/base.html`
- [x] 2.4 Audit and fix heading hierarchy in `public.html` and `dashboard.html` layouts
- [x] 2.5 Add `motion-safe` utilities to ensure Reduced Motion support across transitions

## 3. Public Site and Performance

- [x] 3.1 Implement ARIA landmarks (`<header>`, `<nav>`, `<main>`, `<footer>`) in `public.html` layout
- [x] 3.2 Update image tags to use modern formats (WebP/AVIF) and `loading="lazy"` via Wagtail image tags
- [x] 3.3 Audit mobile views (320px+) and fix horizontal overflow issues
- [x] 3.4 Ensure all interactive elements have 44x44px touch targets on mobile
- [x] 3.5 Implement template fragment caching for the `ProgramTimeline` block

## 4. Submissions and Reviews Functional QA

- [x] 4.1 Update submission forms with `aria-live` and `aria-describedby` for validation errors
- [x] 4.2 Add descriptive `aria-label` attributes to file download links in the Chair Dashboard
- [x] 4.3 Ensure numeric rating scales in reviews are keyboard-accessible (radio groups or styled select)
- [x] 4.4 Add accessible progress indicators to the two-phase submission workflow

## 5. End-to-End (E2E) Test Implementation

- [x] 5.1 Create E2E test for **Visitor** journey: Home -> Program -> Info pages
- [x] 5.2 Create E2E test for **Author** journey: Login -> Submission Creation -> Status Check
- [x] 5.3 Create E2E test for **Reviewer** journey: Login -> Assigned Work -> Evaluation Form Submission
- [x] 5.4 Create E2E test for **Chair** journey: Login -> Dashboard -> Submission Filtering -> File Access

## 6. Final Validation and Auditing

- [x] 6.1 Run full accessibility audit with Axe-core and fix remaining violations
- [x] 6.2 Run Lighthouse performance audit and optimize assets to reach target score (90+)
- [x] 6.3 Verify mobile responsiveness across all browsers in Playwright
- [x] 6.4 Perform manual screen reader pass on critical paths
