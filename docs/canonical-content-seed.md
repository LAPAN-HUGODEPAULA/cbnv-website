# Canonical Content Seed

## Purpose

This document describes the canonical CBNV 2026 content seed. The seed initializes editable CMS data that future public pages can reuse instead of hardcoding repeated event facts in templates.

## Command

Run the seed after migrations:

```bash
uv run python manage.py seed_canonical_event_content
```

Preview the same operation without committing database writes:

```bash
uv run python manage.py seed_canonical_event_content --dry-run
```

Overwrite protected manually editable fields:

```bash
uv run python manage.py seed_canonical_event_content --force
```

## Idempotence

The command is safe to run repeatedly in local development and staging.

Authoritative canonical fields are updated every run:

- formal event name;
- short event name;
- edition;
- theme;
- display date range;
- start and end dates;
- format;
- city, state and country;
- venue name and short name;
- location summary;
- Google Maps URL.

Protected editorial fields are only filled when blank, unless `--force` is used:

- FAPEMIG acknowledgement text;
- default SEO title;
- default SEO description.

Supporting entities are upserted by stable organization name because `sponsors.Sponsor` does not currently expose a slug field. The shared tier is upserted by the stable slug `apoio-institucional-e-cientifico`.

## Seeded Event Data

- Formal name: `XII Congresso Brasileiro de Neurociências da Visão`
- Short name: `CBNV 2026`
- Edition: `XII`
- Theme: `Neurovisão na Era da Inteligência Artificial`
- Format: `Presencial com transmissão híbrida`
- Dates: `11 a 13 de novembro de 2026`
- Start date: `2026-11-11`
- End date: `2026-11-13`
- City: `Belo Horizonte`
- State: `Minas Gerais`
- Country: `Brasil`

## Seeded Venue

- Venue name: `Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha`
- Venue short name: `CAD-1/UFMG`
- Google Maps URL: `https://maps.app.goo.gl/xzqJ2LCAHVP4hsFp6`

Address:

```text
Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha.
R. Prof. Baeta Viana, s/n - Pampulha, Belo Horizonte - MG, 31270-901
```

## Seeded Supporting Entities

The seed creates the tier `Apoio institucional e científico` and these active supporting entities:

- UFMG;
- FUNDEP;
- FAPEMIG;
- Sociedade Brasileira de Neurovisão;
- Hospital de Olhos de Minas Gerais / HOLHOS;
- UFRJ;
- USP;
- UFRN;
- UEMG.

Categories are conservative. FAPEMIG is seeded as a funding agency, universities and scientific organizations are not treated as commercial sponsors.

## Pending Links

Unknown registration and livestream URLs are represented by `coming_soon` status with blank URL fields. The seed does not write `#` placeholder links.

YouTube channel, YouTube playlist and Instagram URLs are left blank unless already configured by an editor or another seed.

## Intentionally Not Seeded

The command does not create public pages, final Home/About copy, program sessions, speakers, submissions, reviews, proceedings, production secrets or external API integrations.

Initial announcements are intentionally skipped. Future editorial work can add draft or published announcements once copy is approved.
