## 1. Legacy Inventory and Asset Preparation

- [x] 1.1 Verify the exact filenames and formats for FAPEMIG, organization logos, Hugo de Paula photo, Save the Date image and organizer photos in `_legacy/`.
- [x] 1.2 Extract the 11o CBNV organizing committee names, roles, affiliations and image references from `_legacy/mirror/congressoneurovisa.wixsite.com/cbnv/general-4.html`.
- [x] 1.3 Normalize organizer photo filenames to ASCII slug names based on each organizer name and copy required images into the project static/media location.
- [x] 1.4 Copy or import organization logos, FAPEMIG logo and `_legacy/save-the-date.jpg` into the project static/media convention with descriptive names.
- [x] 1.5 Inspect `_legacy/cbnv/Exported Items.json` and `_legacy/cbnv/Exported Items/Exported Items.bib` to identify edition metadata and proceedings links available locally.

## 2. Shared Public Content Data

- [x] 2.1 Define a reusable organization data source for the seven requested entities with logo path, name, URL and display order.
- [x] 2.2 Add or update the FAPEMIG footer data source so every public page can render the logo and name.
- [x] 2.3 Set the congress Instagram URL to `https://www.instagram.com/cbnvufmg/` through settings, fixtures or the existing seed command.
- [x] 2.4 Add or update seed/fixture content for the Save the Date news article so it references the imported Save the Date image.

## 3. About Page Restructure

- [x] 3.1 Rewrite the About page template/content to include "Bem vindos", "O evento", "Objetivos", "O que esperar", "Local e acessibilidade", "Comissão organizadora" and "Organização".
- [x] 3.2 Translate the Stitch About layout into current project styles without copying standalone prototype scaffolding.
- [x] 3.3 Remove the "eventos recentes" section from the About page.
- [x] 3.4 Add an inline lazy-loaded Google Maps iframe for the event venue with accessible title and stable responsive dimensions.
- [x] 3.5 Render organizer cards with photo, name, role and affiliation/description, including Hugo de Paula as Subcoordenador do Congresso.
- [x] 3.6 Render the About "Organização" section with names and external links for entities that have URLs.

## 4. Home, Footer and Social Updates

- [x] 4.1 Add the Home "Organização" section at the end of the main page content using the shared organization data source.
- [x] 4.2 Update the global footer to render the FAPEMIG logo and institutional name.
- [x] 4.3 Update persistent public social navigation or footer links to include the congress Instagram URL with safe external-link attributes.
- [x] 4.4 Confirm all organization and footer logos have useful alt text and do not cause mobile layout overflow.

## 5. Previous Editions Page

- [x] 5.1 Translate the Stitch Previous Editions layout into `PreviousEditionsPage` using existing project components and visual language.
- [x] 5.2 Consolidate duplicate edition data before rendering the page.
- [x] 5.3 Enrich `Edition` fixture/seed data from local proceedings files in `_legacy/cbnv/`.
- [x] 5.4 Add supplemental edition details from `https://lapan.com.br/eventos/` only where local data is missing, keeping tests independent from network access.
- [x] 5.5 Render missing proceedings or playlist links gracefully without broken buttons.

## 6. Program Page

- [x] 6.1 Translate the Stitch Program layout into the existing `ProgramPage` template.
- [x] 6.2 Preserve the existing published-session and confirmed-talk filtering behavior.
- [x] 6.3 Preserve the empty state when no public program data exists.
- [x] 6.4 Verify the Program layout remains readable and navigable on mobile and desktop widths.

## 7. Tests and Validation

- [x] 7.1 Add tests for public footer FAPEMIG logo/name and Instagram link.
- [x] 7.2 Add tests for Home and About organization sections, including linked and unlinked organizations.
- [x] 7.3 Add tests for About page sections, absence of "eventos recentes", organizer content and Google Maps iframe.
- [x] 7.4 Add tests for Save the Date article image rendering.
- [x] 7.5 Add tests for Previous Editions de-duplication and local proceedings-derived metadata.
- [x] 7.6 Add tests for Program page layout preserving confirmed/published filtering and empty state behavior.
- [x] 7.7 Run `uv run pytest`.
- [x] 7.8 Run the public site locally on `localhost:8001` and manually verify Home, Sobre, Programação, Edições Anteriores and the Save the Date article.
