## Context

The public website already uses Django, Wagtail page models, shared public layouts, and page-specific templates for Home, Sobre, Programação and Edições Anteriores. The requested change is content-heavy and spans page templates, seeded CMS content, static/media assets, global footer content, and tests.

Legacy sources are split across `_legacy/` assets, the mirrored previous CBNV Wix page at `_legacy/mirror/congressoneurovisa.wixsite.com/cbnv/general-4.html`, and bibliographic/proceedings material in `_legacy/cbnv/`. Stitch references are static HTML prototypes under `docs/stitch_cbnv_2026_digital_platform/` and should guide layout density, hierarchy, and section composition without replacing the existing Django/Wagtail template architecture.

## Goals / Non-Goals

**Goals:**

- Inject institutional, organizational, historical and news imagery content from legacy sources into the public site.
- Keep Home, Sobre, Programação and Edições Anteriores visually coherent with the current Home implementation while borrowing layout structure from the relevant Stitch prototypes.
- Preserve Wagtail editability where the existing models already expose CMS fields, but allow fixed institutional lists where the content is canonical for XII CBNV.
- Normalize copied organizer photos into predictable, ASCII-safe filenames based on organizer names.
- Add focused tests for rendered content, links, image references and removed duplicated sections.

**Non-Goals:**

- Building a new CMS content model unless the existing page/snippet models cannot represent the required content cleanly.
- Rewriting the whole design system or changing unrelated public pages.
- Scraping private or authenticated content from external sites.
- Treating the external Lapan events page as the source of truth when local legacy anais provide the same information.

## Decisions

- **Use existing Wagtail pages and snippets first.** Home, AboutPage, ProgramPage, PreviousEditionsPage, NewsArticlePage, Sponsor and Edition already exist. The implementation should prefer template/context updates, fixtures and seed command adjustments over new models. Alternative considered: create dedicated Organization and Organizer snippets. That is only warranted if editors need ongoing CMS management beyond this one curated injection.

- **Centralize organization data.** The organization list should be defined in one reusable place, such as a helper/context provider or fixture-backed snippet query, then rendered by both Home and Sobre. This prevents the Home and Sobre organization sections from drifting. Alternative considered: duplicate static HTML in both templates, which is simpler but creates avoidable maintenance risk.

- **Keep FAPEMIG in the global footer.** The FAPEMIG logo and institutional name belong in `templates/components/footer.html` or context/settings consumed by that partial so all public pages inherit the acknowledgement. Alternative considered: adding FAPEMIG only to Home, which would miss the requested footer behavior.

- **Use Stitch as layout reference, not a direct paste.** The Stitch prototypes use standalone Tailwind setup and some speculative copy. The implementation should translate the section rhythm, grids, archive cards and program treatment into existing project classes/templates while avoiding sensationalist language and decorative excess. Alternative considered: copy prototype HTML directly, which would conflict with current layout composition and CMS data.

- **Treat legacy copied assets as first-class static/media files.** Logos and the Save the Date image should be copied into project-controlled static or Wagtail media import locations with descriptive names. Organizer photos copied from the legacy mirror should be renamed to normalized filenames based on each person's name; Hugo de Paula's photo comes from `_legacy/hugo-bastos-de-paula.jpg`.

- **Use local legacy proceedings first, external Lapan content as supplemental validation.** The page "Edições Anteriores" should be enriched from `_legacy/cbnv/Exported Items.json` and `_legacy/cbnv/Exported Items/Exported Items.bib`; the Lapan events URL can fill gaps where local data is missing and should not be required during tests.

## Risks / Trade-offs

- **[Risk] Legacy Wix markup may contain noisy or duplicated text** -> **Mitigation:** extract only named sections, organizer names/roles/photos and factual event details; rewrite public copy in a neutral institutional tone.
- **[Risk] Organization logo filenames differ in case or spelling** -> **Mitigation:** verify asset paths during implementation and normalize destination filenames while keeping alt text and names exactly aligned with the requested entities.
- **[Risk] External Google Maps embeds can affect performance and privacy** -> **Mitigation:** use a lazy-loaded iframe with a clear title, fixed aspect ratio and no blocking JavaScript.
- **[Risk] Previous-edition metadata may be incomplete across sources** -> **Mitigation:** render missing fields gracefully and add tests around the known local anais-derived records.
- **[Risk] Static content can diverge from CMS content** -> **Mitigation:** keep canonical lists in fixtures/helpers and document where future editors should update organization and organizer data.

## Migration Plan

- Copy and normalize required assets into the project's static/media convention.
- Update fixtures or seed commands so local development and tests can recreate the injected content.
- Update templates and context providers for footer, Home, Sobre, Programação, Edições Anteriores and the Save the Date news article.
- Add or adjust tests, then run `uv run pytest`; for UI verification, run the Django server on `localhost:8001` and inspect the changed pages.
