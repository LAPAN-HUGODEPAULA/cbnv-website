# Legacy Ghost Facts Inventory - Round 1

## Metadata

- Change: `verify-cross-page-content-consistency`
- Reviewed commit: `d3044e5`
- Data profiles: empty/default fallback profile and populated/custom canonical-seed profile.

## Canonical Current-Event Facts

- Event: `XII Congresso Brasileiro de Neurociências da Visão`
- Short name: `CBNV 2026`
- Theme: `Neurovisão na Era da Inteligência Artificial`
- Dates: `11 a 13 de novembro de 2026`
- Venue: `Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha`
- Short venue: `CAD-1/UFMG`
- Address: `R. Prof. Baeta Viana, s/n - Pampulha, Belo Horizonte - MG, 31270-901`
- Map URL: `https://maps.app.goo.gl/xzqJ2LCAHVP4hsFp6`

## Inventory

| Legacy fact | Pattern | Allowed context | Forbidden context | Found? | Action |
|---|---|---|---|---|---|
| XI/11th CBNV 2024 | `11ª`, `11o`, `XI`, `2024`, `20 a 22 de novembro de 2024` | Previous editions page, `Edition` fixtures, archive docs, tests for archive data | Current About/Home/Contact/Program/current dashboards/current notifications | Yes: previous-edition fallback is allowed; committee fallback says `11o CBNV` in current About fallback | CCR1-002 |
| Engineering Auditorium venue | `Auditório da Escola de Engenharia`, `Av. Pres. Antônio Carlos, 6627` | Historical notes if explicitly archived | Current About/Contact/Home venue content | Yes: `pages/content.py` fallback location and map fields | CCR1-001 |
| Old UFMG generic location | `UFMG — Belo Horizonte, MG` | Previous editions | Current canonical venue fields | Yes, only previous-edition fallback and fixture contexts observed | No action |
| Previous themes | `Neurociência da Visão: Da Biologia à Clínica`, `Uma década...`, `Neurovisão e interfaces internacionais` | Previous editions and historic docs | Current event theme contexts | Yes, in previous-edition fallback/fixtures and docs | No action |
| Old proceedings ResearchGate links | `researchgate.net/publication/...Congresso_Brasileiro_de_Neurovisao` | Previous editions only | Current proceedings/anais page for 2026 | Yes, previous-edition fallback only | No action |
| Old YouTube archive channel | `youtube.com/@congressoneurovis...` | Previous editions/video archive/channel links | Current-event video gallery if presented as confirmed 2026 content | Yes, fixture video is titled "Canal da 11ª Edição — CBNV" with public status | Verify gallery framing; potential follow-up if shown as current video |
| 2025 prototype sample dates | `12/08/2025`, `05/08/2025`, `15/08/2025` | Stitch prototypes under `docs/stitch_cbnv_2026_digital_platform/` | Runtime templates, live seeded content | Yes, prototype docs only | No action |
| Old registration/submission links | Previous external platforms or stale URLs | Archive/planning docs | Current registration/submission CTAs | No active stale current link found in source review | No action |
| Workshop/program references | `workshop`, previous program names | Historical/program archive | Current Program page unless confirmed | No active current contamination found in source review | No action |
| Old sponsor/support labels | Historical partner lists | Archive contexts | Current sponsor taxonomy | No old sponsor fact outside active supporting-entity taxonomy found | No action |

## Search Scope

- Included: `pages`, `templates`, `core`, `submissions`, `reviews`, `proceedings`, `reports`, `videos`, `sponsors`, active `docs/content`.
- Excluded as archival/reference by policy: `_legacy`, archived OpenSpec changes, generated dependency folders.
