# XII CBNV 2026 — Plano de Implementação OpenSpec v1.0

**Projeto:** Website e plataforma digital do XII Congresso Brasileiro de Neurociências da Visão  
**Metodologia:** SDD — Spec Driven Design com OpenSpec  
**Stack aprovada:** Django 6.0.4 + Wagtail 7.3.1 + PostgreSQL 18 + Tailwind CSS 4.2.4 + HTMX/Alpine.js + uv  
**Documento fonte:** `docs/CBNV2026_Requisitos_Arquitetura_v1.md`  
**Referência visual:** `docs/stitch_cbnv_2026_digital_platform/`  
**Data:** 2026-05-01  
**Status:** Plano operacional para criação de change proposals OpenSpec

---

## 1. Objetivo deste plano

Este arquivo define a estratégia de implementação do CBNV 2026 usando OpenSpec. Ele não substitui o Documento de Requisitos e Arquitetura; ele traduz esse documento em uma sequência de change proposals implementáveis por agentes de codificação.

A prioridade é reduzir reescrita. Para isso, a ordem das proposals segue esta lógica:

1. primeiro, fixar contexto, convenções e arquitetura;
2. depois, criar a base Django/Wagtail com modelo de usuário correto desde o início;
3. em seguida, implementar o design system extraído do Stitch antes das páginas;
4. só então implementar modelos editoriais, programação, páginas públicas e fluxos autenticados;
5. por fim, implementar revisão científica, anais, relatórios, hardening e QA.

O resultado esperado é uma plataforma monolítica modular, simples de operar, segura, responsiva, acessível e compatível com desenvolvimento assistido por IA.

---

## 2. Premissas obrigatórias

1. O Documento de Requisitos e Arquitetura v1.0 é o single source of truth.
2. O ZIP do Stitch é referência visual, não fonte funcional de verdade.
3. O site legado Wix e o Notion não devem orientar novas decisões de escopo.
4. Não implementar Next.js + Strapi.
5. Não implementar pagamento próprio.
6. Não implementar certificados próprios.
7. Não implementar QR code de credenciamento próprio.
8. Não hospedar vídeos completos.
9. Usar apenas links de YouTube/playlist para vídeos.
10. Não implementar RBAC editorial complexo.
11. Manter admin editorial único no CMS.
12. Manter papéis científicos (is_author, is_reviewer, is_chair) como flags booleanas no modelo de usuário.
13. A submissão inicial não deve exigir vídeo.
14. O vídeo/link de vídeo só deve entrar na fase de material final para trabalhos aprovados, quando aplicável.
15. Os arquivos de submissão não podem ficar públicos por URL direta.
16. O desenvolvimento deve privilegiar Django idiomático, templates legíveis, testes e migrations incrementais.
17. Usar `uv` para todo gerenciamento Python (`uv sync`, `uv add`, `uv add --dev`, `uv run`); não usar `pip` diretamente.
18. Usar Tailwind CSS 4.2.4 com configuração CSS-first em `src/input.css` (`@import`, `@source`, `@theme`); não criar `tailwind.config.js` por padrão.

---

## 3. Estrutura esperada do OpenSpec

Após o `openspec init`, a estrutura deve ficar próxima de:

```text
openspec/
├── AGENTS.md
├── project.md              # se a versão local gerar este arquivo
├── config.yaml             # preferível nas versões atuais, se disponível
├── specs/
│   ├── architecture/
│   ├── developer-experience/
│   ├── design-system/
│   ├── content-cms/
│   ├── program/
│   ├── public-site/
│   ├── accounts-auth/
│   ├── submissions/
│   ├── reviews/
│   ├── proceedings/
│   ├── reports/
│   ├── notifications/
│   └── deployment-security/
└── changes/
    ├── archive/
    └── <change-id>/
        ├── proposal.md
        ├── design.md
        ├── tasks.md
        └── specs/
            └── <domain>/
                └── spec.md
```

Observação: algumas versões do OpenSpec priorizam `openspec/config.yaml` em vez de `openspec/project.md`. Se ambos existirem, mantenha os dois coerentes; se apenas um existir, preencha o arquivo gerado pela versão instalada.

---

## 4. Fluxo operacional recomendado

Para cada proposal:

```bash
openspec list
openspec spec list --long
# criar ou gerar a proposal via slash command no agente
openspec validate <change-id> --strict
# revisar proposal.md, design.md, tasks.md e specs/
# aprovar manualmente
# aplicar com agente de codificação
# rodar testes e validações
openspec validate <change-id> --strict
openspec archive <change-id> --yes
```

Regra: manter apenas uma change proposal ativa por vez, salvo pequenas correções sem dependência. Isso reduz conflitos de schema, migrations e templates.

---

## 5. Prompt de inicialização do OpenSpec

### 5.1 Comandos preliminares

Executar no diretório raiz do repositório:

```bash
npm install -g @fission-ai/openspec@latest
openspec --version
openspec init --tools all
```

Se estiver usando perfil expandido e a versão instalada suportar:

```bash
openspec config profile expanded
openspec update
```

Copiar para o repositório:

```text
docs/CBNV2026_Requisitos_Arquitetura_v1.md
docs/design/stitch_cbnv_2026_digital_platform/
docs/design/stitch_cbnv_2026_digital_platform/neurovision_ai/DESIGN.md
```

### 5.2 Prompt para o agente após `openspec init`

```text
Inicialize o contexto OpenSpec deste repositório para o projeto “XII CBNV 2026 — Website e plataforma digital do Congresso Brasileiro de Neurociências da Visão”.

Antes de qualquer implementação, leia integralmente:
- docs/CBNV2026_Requisitos_Arquitetura_v1.md
- docs/design/stitch_cbnv_2026_digital_platform/neurovision_ai/DESIGN.md

Trate `docs/CBNV2026_Requisitos_Arquitetura_v1.md` como single source of truth. Trate o ZIP/export do Stitch apenas como referência visual. Não use o site legado Wix nem o Notion como fonte de escopo.

Atualize `openspec/config.yaml` ou `openspec/project.md` com o seguinte contexto permanente:

Projeto: plataforma pública e administrativa do XII CBNV 2026.
Stack obrigatória: Django 6.0.4, Wagtail 7.3.1, PostgreSQL 18, Tailwind CSS 4.2.4, HTMX, Alpine.js opcional, Docker Compose, Caddy ou Nginx, SMTP transacional/institucional, uv para dependências Python.
Arquitetura: monólito modular Django com apps por domínio: core, pages, program, submissions, reviews, proceedings, videos, sponsors, accounts, reports, notifications.
Princípios: simplicidade, segurança, acessibilidade, responsividade, Django idiomático, templates server-side, sem SPA complexa.
Fora de escopo: Next.js, Strapi, pagamento próprio, certificados próprios, QR code próprio, hospedagem de vídeos completos, RBAC editorial complexo, integração automática com Sympla/UFMG/FUNDEP além de link externo.
Conteúdo: português brasileiro, tom institucional, científico e claro.
Design: dark-mode first, azul-marinho profundo, azul elétrico, verde neuro/neon, estética científica institucional, glassmorphism moderado, alta legibilidade e WCAG 2.2 AA como alvo.
Regra de submissão: fluxo bifásico; vídeo não é exigido na submissão inicial; link de vídeo somente na fase final para trabalhos aprovados, quando aplicável.
Regra de dados: arquivos de submissão protegidos, nunca públicos por URL direta.
Regra de dependências Python: usar `uv` exclusivamente; não usar `pip` diretamente.
Regra de Tailwind: usar Tailwind CSS 4.2.4 CSS-first em `src/input.css` com `@source` e `@theme`; não criar `tailwind.config.js` por padrão.
Regra de specs: todos os delta specs devem usar ADDED/MODIFIED/REMOVED/RENAMED Requirements e cenários Given/When/Then.
Regra de implementação: não implementar código antes de uma proposal validada e aprovada.

Crie também, se ainda não existir, um README curto em `docs/implementation/README.md` explicando que o OpenSpec é a trilha operacional de implementação e que este repositório deve evoluir por change proposals sequenciais.

Não implemente a aplicação ainda. Apenas prepare o contexto OpenSpec e indique quais arquivos foram criados ou atualizados.
```

---

## 6. Ordem das change proposals

A ordem abaixo deve ser seguida para evitar retrabalho:

| Ordem | Change ID | Objetivo | Por que vem nessa posição |
|---:|---|---|---|
| 01 | `bootstrap-django-wagtail-platform` | Criar base técnica, custom user e ambiente | Evita reescrever auth e migrations depois |
| 02 | `add-design-system-and-layout-shells` | Criar tokens, componentes e shells visuais | Evita reescrever páginas depois |
| 03 | `add-core-cms-content-models` | Criar CMS central e modelos editoriais | Sustenta páginas públicas e conteúdo editável |
| 04 | `add-program-speakers-and-fixtures` | Criar programação, palestrantes e seeds | Sustenta Home, Programação e Palestrantes |
| 05 | `add-public-site-pages` | Implementar site público completo | Reutiliza design system, CMS e programação |
| 06 | `add-accounts-roles-and-dashboards` | Criar autenticação e shells de áreas internas | Prepara submissões e revisão sem refatorar UI |
| 07 | `add-author-submission-initial-flow` | Implementar submissão inicial bifásica fase 1 | Núcleo operacional do MVP |
| 08 | `add-review-decision-workflow` | Implementar revisão, pareceres e decisão | Depende das submissões já estáveis |
| 09 | `add-final-materials-proceedings-videos` | Implementar material final, anais e links YouTube | Depende de decisões e modalidades finais |
| 10 | `add-reports-exports-and-indicators` | Implementar indicadores e exports | Depende dos dados transacionais completos |
| 11 | `harden-deployment-security-and-backups` | Produção, segurança, backups e observabilidade | Melhor quando fluxos centrais já existem |
| 12 | `complete-accessibility-performance-and-qa` | QA final, a11y, performance e regressões | Fecha o ciclo antes de staging/produção |

---

# 7. Change proposals detalhadas

Cada proposal abaixo contém escopo, dependências, domínios OpenSpec, critérios de aceite e prompt pronto para uso no agente.

---

## Proposal 01 — `bootstrap-django-wagtail-platform`

### Objetivo

Criar a fundação técnica do projeto: repositório Django/Wagtail, PostgreSQL, Docker Compose, settings por ambiente, custom user inicial, Tailwind build pipeline, estrutura de apps e testes mínimos.

### Dependências

Nenhuma, além do OpenSpec inicializado.

### Domínios OpenSpec

- `architecture`
- `developer-experience`
- `accounts-auth`
- `deployment-security`

### Escopo

Inclui:

1. projeto Django;
2. Wagtail instalado e funcional;
3. PostgreSQL via Docker Compose;
4. custom user criado desde o início;
5. apps Django vazios por domínio;
6. settings separados para development/test/production;
7. pipeline Tailwind CSS 4.2.4 mínimo com configuração CSS-first em `src/input.css`;
8. templates base mínimos;
9. pytest configurado;
10. healthcheck simples;
11. README de desenvolvimento;
12. `.env.example`;
13. `pyproject.toml` e `uv.lock` como fonte de dependências Python.

Não inclui:

1. páginas públicas finais;
2. design system completo;
3. submissões;
4. revisão;
5. deploy production completo.

### Critérios de aceite

1. `docker compose up` inicia aplicação, PostgreSQL e dependências.
2. `uv run python manage.py migrate` executa sem erro.
3. Wagtail admin abre localmente.
4. Superusuário pode ser criado.
5. Custom user está definido antes das migrations de domínio.
6. Testes mínimos passam.
7. `openspec validate bootstrap-django-wagtail-platform --strict` passa.

### Prompt da proposal

```text
/opsx:propose bootstrap-django-wagtail-platform

Crie uma change proposal OpenSpec chamada `bootstrap-django-wagtail-platform`.

Contexto obrigatório:
- Leia `docs/CBNV2026_Requisitos_Arquitetura_v1.md`.
- O projeto é uma plataforma monolítica modular para o XII CBNV 2026.
- Stack obrigatória: Django 6.0.4 + Wagtail 7.3.1 + PostgreSQL 18 + Tailwind CSS 4.2.4 + HTMX/Alpine.js opcional + Docker Compose + uv.
- Não usar Next.js nem Strapi.
- Não implementar funcionalidades de negócio ainda.

Objetivo da change:
Criar a fundação técnica do projeto com Django/Wagtail, custom user inicial, estrutura de apps, PostgreSQL, Docker Compose, settings por ambiente, Tailwind mínimo, pytest, uv e documentação de desenvolvimento.

Gere:
1. `proposal.md` com problema, objetivo, escopo, fora de escopo, riscos e rollback.
2. Delta specs em:
   - `specs/architecture/spec.md`
   - `specs/developer-experience/spec.md`
   - `specs/accounts-auth/spec.md`
   - `specs/deployment-security/spec.md`
3. `design.md` detalhando arquitetura monolítica modular, apps Django, settings, custom user, Docker Compose e decisões técnicas.
4. `tasks.md` com checklist granular e verificável.

Regras:
- Não implementar código ainda.
- Usar requisitos em linguagem SHALL/MUST.
- Cada Requirement deve ter pelo menos um Scenario Given/When/Then.
- Incluir tarefa explícita para validar com `openspec validate bootstrap-django-wagtail-platform --strict`.
```

### Prompt de implementação após aprovação

```text
/opsx:apply bootstrap-django-wagtail-platform

Implemente estritamente as tasks aprovadas em `openspec/changes/bootstrap-django-wagtail-platform/tasks.md`.
Não implemente páginas públicas, submissões ou revisão científica nesta change.
Ao final, rode testes, migrations e validação OpenSpec. Marque as tasks concluídas no `tasks.md`.
```

---
## Proposal 02 — `add-design-system-and-layout-shells`

### Objetivo

Transformar a referência visual do Stitch em um design system implementável com Tailwind CSS 4.2.4 CSS-first, templates Django e componentes reutilizáveis.

### Dependências

- `bootstrap-django-wagtail-platform` arquivada.

### Domínios OpenSpec

- `design-system`
- `public-site`
- `accounts-auth`
- `developer-experience`

### Referências visuais do Stitch

Usar como referência, não como código final obrigatório:

1. `home_xii_cbnv_2026_design_atualizado/`
2. `programa_o_xii_cbnv_2026_design_atualizado/`
3. `submiss_es_xii_cbnv_2026_design_atualizado/`
4. `formul_rio_de_submiss_o_xii_cbnv_2026/`
5. `rea_do_autor_xii_cbnv_2026/`
6. `dashboard_da_comiss_o_xii_cbnv_2026/`
7. `palestrantes_xii_cbnv_2026/`
8. `sobre_e_local_xii_cbnv_2026/`
9. `edi_es_anteriores_xii_cbnv_2026/`
10. `neurovision_ai/DESIGN.md`

### Escopo

Inclui:

1. tokens de cor e tipografia em `src/input.css` via `@theme`;
2. base layout público;
3. base layout autenticado/dashboard;
4. header responsivo;
5. footer institucional;
6. botões;
7. cards científicos;
8. badges de status;
9. inputs acessíveis;
10. timeline component;
11. table component;
12. empty/loading/error states;
13. utilitários para skip link, foco visível e reduced motion.

Não inclui:

1. páginas finais com dados reais;
2. implementação completa de formulários;
3. lógica de submissão.

### Critérios de aceite

1. Existe biblioteca de componentes Django/Tailwind reutilizável.
2. Header e footer aparecem em página demo.
3. Layout público e dashboard shell funcionam em mobile e desktop.
4. Tokens do Stitch foram traduzidos para Tailwind CSS 4.2.4 com nomes consistentes e configuração CSS-first.
5. Componentes usam HTML semântico e foco visível.
6. Não há dependência de SPA.

### Prompt da proposal

```text
/opsx:propose add-design-system-and-layout-shells

Crie uma change proposal OpenSpec chamada `add-design-system-and-layout-shells`.

Contexto obrigatório:
- Leia `docs/CBNV2026_Requisitos_Arquitetura_v1.md`.
- Leia `docs/design/stitch_cbnv_2026_digital_platform/neurovision_ai/DESIGN.md`.
- Consulte os `screen.png` e `code.html` exportados pelo Stitch apenas como referência visual.
- O output do Stitch não é especificação funcional. A especificação funcional é o Documento de Requisitos.

Objetivo da change:
Criar design system e shells reutilizáveis em Tailwind/Django templates para reduzir reescrita nas próximas páginas.

Gere:
1. `proposal.md` com intenção, escopo visual, limitações e critérios de aceite.
2. Delta specs em:
   - `specs/design-system/spec.md`
   - `specs/public-site/spec.md`
   - `specs/accounts-auth/spec.md`
3. `design.md` descrevendo tokens, componentes, padrões de acessibilidade, estrutura de templates, partials/includes e como traduzir o Stitch para Django sem copiar cegamente código estático.
4. `tasks.md` com implementação granular.

Regras:
- Não criar páginas públicas finais ainda.
- Não implementar submissões.
- Não criar lógica de negócio.
- Usar Tailwind CSS 4.2.4 CSS-first em `src/input.css` com `@source` para templates Django e `@theme` para tokens.
- Não criar `tailwind.config.js` por padrão.
- Usar shells canônicos em `templates/layouts/public.html` e `templates/layouts/dashboard.html`.
- Incluir componentes para header, footer, cards, timeline, badges, botões, formulários, dashboard shell, tabelas, empty/loading/error states.
- Incluir validação de responsividade e navegação por teclado.
```

### Prompt de implementação após aprovação

```text
/opsx:apply add-design-system-and-layout-shells

Implemente apenas o design system e os layout shells aprovados.
Reutilize a estética do Stitch: dark-mode first, azul-marinho, azul elétrico, verde neuro, glassmorphism moderado, Newsreader/Inter/Space Grotesk ou equivalentes configuráveis.
Não implemente conteúdo final, submissões ou revisão nesta change.
Ao final, rode testes, lint/build CSS e validação OpenSpec.
```

---

## Proposal 03 — `add-core-cms-content-models`

### Objetivo

Implementar modelos editoriais centrais no Wagtail: SiteSettings, páginas-base, notícias, patrocinadores, edições anteriores e vídeos/links YouTube.

### Dependências

- Proposals 01 e 02 arquivadas.

### Domínios OpenSpec

- `content-cms`
- `public-site`
- `videos`
- `sponsors`
- `proceedings`

### Escopo

Inclui:

1. SiteSettings;
2. tipos de páginas Wagtail;
3. NewsArticle;
4. Sponsor;
5. Edition;
6. VideoResource;
7. admin Wagtail configurado para admin editorial único;
8. seeds/fixtures mínimos;
9. páginas placeholder renderizando dados do CMS.

Não inclui:

1. Programação científica detalhada;
2. submissões;
3. revisão;
4. relatórios.

### Critérios de aceite

1. Admin consegue editar SiteSettings.
2. Admin consegue criar/editar notícias.
3. Admin consegue criar patrocinadores.
4. Admin consegue cadastrar links YouTube sem hospedar vídeos.
5. Admin consegue cadastrar edições anteriores.
6. O site renderiza placeholders públicos sem erro.

### Prompt da proposal

```text
/opsx:propose add-core-cms-content-models

Crie uma change proposal OpenSpec chamada `add-core-cms-content-models`.

Contexto obrigatório:
- Documento de Requisitos é a fonte de verdade.
- O CMS deve permitir um admin editorial único, sem RBAC editorial complexo.
- Vídeos devem ser cadastrados apenas como links YouTube/playlist; não hospedar vídeos completos.
- Inscrição externa deve ser representada por link configurável em SiteSettings ou página de inscrição.

Objetivo da change:
Implementar a fundação editorial Wagtail: SiteSettings, páginas públicas estruturadas, notícias, patrocinadores, edições anteriores e VideoResource.

Gere:
1. `proposal.md`.
2. Delta specs em:
   - `specs/content-cms/spec.md`
   - `specs/public-site/spec.md`
   - `specs/videos/spec.md`
   - `specs/sponsors/spec.md`
   - `specs/proceedings/spec.md`
3. `design.md` detalhando modelos, relações, admin panels, snippets, settings, fixtures e decisões de publicação/ocultação.
4. `tasks.md` com checklist granular.

Regras:
- Não implementar ProgramDay/ProgramSession/ProgramTalk ainda.
- Não implementar submissões/revisão.
- Incluir cenários para publicar/despublicar conteúdo, destacar notícia na Home, cadastrar patrocinador, cadastrar vídeo por link e configurar inscrição externa.
```

### Prompt de implementação após aprovação

```text
/opsx:apply add-core-cms-content-models

Implemente os modelos editoriais e páginas placeholder conforme a change aprovada.
Use Wagtail idiomático, snippets/settings quando apropriado, migrations incrementais e fixtures mínimas.
Não implemente programação científica detalhada nem submissões nesta change.
```

---

## Proposal 04 — `add-program-speakers-and-fixtures`

### Objetivo

Implementar programação, palestrantes, sessões e fixtures baseadas na programação preliminar do XII CBNV 2026.

### Dependências

- Proposals 01, 02 e 03 arquivadas.

### Domínios OpenSpec

- `program`
- `content-cms`
- `public-site`

### Escopo

Inclui:

1. Speaker;
2. ProgramDay;
3. ProgramSession;
4. ProgramTalk;
5. tipos de atividade;
6. status de palestrante e visibilidade pública;
7. import/fixtures da programação canônica;
8. páginas preliminares de programação e palestrantes usando componentes existentes.

Não inclui:

1. submissões;
2. revisão;
3. agenda personalizada;
4. integração com calendário.

### Critérios de aceite

1. Admin consegue editar dias, sessões, falas e palestrantes.
2. Palestrantes pendentes podem ficar ocultos.
3. A programação é filtrável por dia/tipo no front-end.
4. Mobile exibe timeline vertical.
5. Desktop exibe timeline ou grade estruturada.
6. Fixtures representam Dia 1, Dia 2 e Dia 3 conforme documento fonte.

### Prompt da proposal

```text
/opsx:propose add-program-speakers-and-fixtures

Crie uma change proposal OpenSpec chamada `add-program-speakers-and-fixtures`.

Contexto obrigatório:
- Leia a seção de Programação Canônica do Documento de Requisitos.
- A programação preliminar é fonte de verdade para dias, temas, estrutura e horários.
- Palestrantes/participantes com confirmação pendente devem poder ficar cadastrados, mas ocultos no site.
- Componentes visuais devem reutilizar o design system já implementado.

Objetivo da change:
Implementar modelos e telas de Programação e Palestrantes, com fixtures da programação preliminar.

Gere:
1. `proposal.md`.
2. Delta specs em:
   - `specs/program/spec.md`
   - `specs/public-site/spec.md`
   - `specs/content-cms/spec.md`
3. `design.md` detalhando modelagem, status, filtros, fixtures, admin, templates e acessibilidade da timeline.
4. `tasks.md` com checklist granular.

Regras:
- Não implementar submissões.
- Não implementar painel de autor/revisor.
- Usar os componentes de card, badge e timeline da proposal de design system.
- Incluir cenários para ocultar participantes pendentes e publicar programação atualizada sem código.
```

### Prompt de implementação após aprovação

```text
/opsx:apply add-program-speakers-and-fixtures

Implemente ProgramDay, ProgramSession, ProgramTalk, Speaker, admin Wagtail/Django e fixtures.
Reutilize componentes visuais existentes.
Garanta filtros por dia e tipo, status de palestrante e visibilidade pública.
Não implemente submissões ou revisão nesta change.
```

---

## Proposal 05 — `add-public-site-pages`

### Objetivo

Implementar o site público completo do MVP: Home, Sobre, Programação, Palestrantes, Submissões informativa, Inscrição externa, Patrocínio, Edições anteriores e Contato.

### Dependências

- Proposals 01–04 arquivadas.

### Domínios OpenSpec

- `public-site`
- `content-cms`
- `program`
- `sponsors`
- `videos`

### Escopo

Inclui:

1. Home final;
2. Sobre/Local;
3. Programação pública final;
4. Palestrantes pública final;
5. página informativa de Submissões;
6. página de Inscrição externa;
7. Patrocínio;
8. Edições anteriores;
9. Contato;
10. SEO básico;
11. breadcrumbs;
12. estados “em breve”;
13. menção FAPEMIG em rodapé/materiais pertinentes.

Não inclui:

1. área autenticada;
2. formulário real de submissão;
3. revisão;
4. anais finais.

### Critérios de aceite

1. Páginas do MVP estão publicáveis.
2. Site é navegável no mobile.
3. CTAs mudam conforme estado configurável.
4. Página de inscrição aceita link externo ou estado “em breve”.
5. Página de submissões informa explicitamente que vídeo não é exigido inicialmente.
6. Site não depende de conteúdo hardcoded que deveria estar no CMS.

### Prompt da proposal

```text
/opsx:propose add-public-site-pages

Crie uma change proposal OpenSpec chamada `add-public-site-pages`.

Contexto obrigatório:
- Reutilizar design system, CMS e modelos de programação já implementados.
- Implementar as páginas públicas do MVP conforme Documento de Requisitos.
- A página de inscrição deve apontar para plataforma externa ou exibir “em breve”.
- A página de submissões é informativa nesta change; o formulário real será implementado depois.
- A Home deve ser clara, responsiva, centrada no usuário e alinhada ao Stitch.

Objetivo da change:
Implementar o site público completo do MVP sem ainda criar fluxos autenticados de submissão.

Gere:
1. `proposal.md`.
2. Delta specs em:
   - `specs/public-site/spec.md`
   - `specs/content-cms/spec.md`
   - `specs/program/spec.md`
   - `specs/sponsors/spec.md`
   - `specs/videos/spec.md`
3. `design.md` detalhando composição de páginas, SEO, estados vazios, CTAs por fase, responsividade e acessibilidade.
4. `tasks.md` granular.

Regras:
- Não criar formulário real de submissão nesta change.
- Não criar dashboards autenticados.
- Não implementar pagamento, certificado, QR code ou hospedagem de vídeo.
- Incluir testes de renderização das páginas principais.
```

### Prompt de implementação após aprovação

```text
/opsx:apply add-public-site-pages

Implemente as páginas públicas do MVP usando os modelos e componentes existentes.
Priorize Home, Programação, Submissões informativa, Inscrição e Contato.
Garanta responsividade, SEO básico, CTAs configuráveis e estados “em breve”.
Não implemente submissão autenticada nesta change.
```

---

## Proposal 06 — `add-accounts-roles-and-dashboards`

### Objetivo

Implementar autenticação, papéis transacionais e shells de dashboards para autor, revisor, comissão/chair e admin técnico.

### Dependências

- Proposals 01–05 arquivadas.

### Domínios OpenSpec

- `accounts-auth`
- `submissions`
- `reviews`
- `reports`
- `notifications`

### Escopo

Inclui:

1. login/logout;
2. cadastro de autor;
3. recuperação de senha;
4. papéis transacionais;
5. guards/decorators/mixins;
6. dashboard shell do autor;
7. dashboard shell do revisor;
8. dashboard shell da comissão;
9. perfil de usuário;
10. audit log foundation para ações futuras.

Não inclui:

1. submissão real;
2. parecer real;
3. exportações reais.

### Critérios de aceite

1. Autor consegue criar conta e entrar.
2. Usuários veem dashboards conforme papel.
3. Usuário sem papel adequado não acessa painel restrito.
4. Admin técnico consegue atribuir papéis.
5. AuditLog básico registra login e ações relevantes, se configurado.

### Prompt da proposal

```text
/opsx:propose add-accounts-roles-and-dashboards

Crie uma change proposal OpenSpec chamada `add-accounts-roles-and-dashboards`.

Contexto obrigatório:
- O CMS editorial continua com admin único; não criar RBAC editorial complexo.
- Papéis transacionais são necessários para fluxos científicos: Autor, Revisor, Chair/Comissão Científica e Admin técnico/organizador.
- Reutilizar dashboard shell criado no design system.

Objetivo da change:
Implementar autenticação, cadastro de autor, papéis transacionais, controle de acesso e dashboards vazios para preparar submissões/revisão.

Gere:
1. `proposal.md`.
2. Delta specs em:
   - `specs/accounts-auth/spec.md`
   - `specs/submissions/spec.md`
   - `specs/reviews/spec.md`
   - `specs/notifications/spec.md`
3. `design.md` detalhando auth, role model, access control, dashboard routing, audit logging foundation e segurança.
4. `tasks.md` granular.

Regras:
- Não implementar o formulário de submissão real ainda.
- Não implementar avaliação científica ainda.
- Não complicar o CMS editorial.
- Incluir cenários de autorização para cada papel.
```

### Prompt de implementação após aprovação

```text
/opsx:apply add-accounts-roles-and-dashboards

Implemente autenticação, cadastro, roles transacionais e dashboards vazios conforme a change aprovada.
Garanta que o código não crie RBAC editorial complexo.
Não implemente submissões ou revisões reais nesta change.
```

---

## Proposal 07 — `add-author-submission-initial-flow`

### Objetivo

Implementar a Fase 1 da submissão científica: cadastro/login de autor, formulário de submissão, autores, afiliações, resumo, eixo temático, palavras-chave, upload de PDF protegido, status e confirmação por e-mail.

### Dependências

- Proposals 01–06 arquivadas.

### Domínios OpenSpec

- `submissions`
- `accounts-auth`
- `notifications`
- `deployment-security`

### Escopo

Inclui:

1. Submission;
2. SubmissionAuthor;
3. SubmissionFile;
4. form wizard ou fluxo multi-step;
5. salvar rascunho;
6. submeter;
7. upload PDF inicial;
8. validação de arquivo;
9. status `draft`, `submitted`, `admin_screening`;
10. confirmação por e-mail;
11. painel do autor com lista e detalhe;
12. export CSV básico para comissão.

Não inclui:

1. revisão por pares;
2. decisão final;
3. material final;
4. vídeo.

### Critérios de aceite

1. Autor cria rascunho.
2. Autor submete trabalho sem vídeo.
3. PDF é validado e armazenado fora de URL pública direta.
4. Autor recebe confirmação por e-mail.
5. Autor vê status do trabalho.
6. Comissão/admin consegue listar e exportar submissões básicas.

### Prompt da proposal

```text
/opsx:propose add-author-submission-initial-flow

Crie uma change proposal OpenSpec chamada `add-author-submission-initial-flow`.

Contexto obrigatório:
- A submissão é bifásica.
- Na fase inicial, NÃO exigir vídeo.
- Exigir metadados, autores/afiliações, resumo, eixo temático, palavras-chave e PDF para avaliação.
- Arquivos de submissão devem ser protegidos e não acessíveis por URL pública direta.
- Enviar confirmação por e-mail ao autor.

Objetivo da change:
Implementar a Fase 1 da submissão científica e o painel do autor para rascunho, envio e acompanhamento.

Gere:
1. `proposal.md`.
2. Delta specs em:
   - `specs/submissions/spec.md`
   - `specs/accounts-auth/spec.md`
   - `specs/notifications/spec.md`
   - `specs/deployment-security/spec.md`
3. `design.md` detalhando modelagem, estados, upload seguro, formulários, permissões, e-mails, export básico e decisões de UX.
4. `tasks.md` granular.

Regras:
- Não implementar revisão por pares nesta change.
- Não implementar decisão final.
- Não implementar material final.
- Não pedir link de vídeo na submissão inicial.
- Incluir testes para criar rascunho, submeter, validar upload, enviar confirmação e impedir acesso público ao arquivo.
```

### Prompt de implementação após aprovação

```text
/opsx:apply add-author-submission-initial-flow

Implemente a Fase 1 de submissão conforme proposal aprovada.
Garanta upload protegido, status correto, e-mail de confirmação e dashboard do autor.
Não implemente revisão, decisão ou material final nesta change.
```

---

## Proposal 08 — `add-review-decision-workflow`

### Objetivo

Implementar triagem, atribuição de revisores, pareceres, conflito de interesse, decisão da comissão, ressalvas/reenvio e classificação final da modalidade.

### Dependências

- Proposals 01–07 arquivadas.

### Domínios OpenSpec

- `reviews`
- `submissions`
- `notifications`
- `reports`

### Escopo

Inclui:

1. ReviewAssignment;
2. Review;
3. Decision;
4. conflitos de interesse;
5. painel do revisor;
6. painel da comissão;
7. transições de estado;
8. decisão: aceito, aceito com ressalvas, rejeitado;
9. modalidade final: oral, pôster, vídeo;
10. reenvio de PDF revisado;
11. notificações por e-mail;
12. histórico de status.

Não inclui:

1. material final pós-aceite;
2. anais públicos;
3. relatório completo.

### Critérios de aceite

1. Comissão atribui revisores.
2. Revisor registra parecer.
3. Revisor pode declarar conflito.
4. Comissão decide com base nos pareceres.
5. Autor recebe decisão.
6. “Aceito com ressalvas” permite reenvio.
7. Modalidade final é registrada.
8. Histórico de status é visível ao autor.

### Prompt da proposal

```text
/opsx:propose add-review-decision-workflow

Crie uma change proposal OpenSpec chamada `add-review-decision-workflow`.

Contexto obrigatório:
- A submissão inicial já existe.
- A comissão decide aceite, rejeição ou aceite com ressalvas.
- A modalidade final é definida pela comissão/revisão: oral, pôster ou vídeo.
- Autores podem reenviar PDF revisado quando houver ressalvas.
- A interface do autor deve usar linguagem simples para estados internos.

Objetivo da change:
Implementar revisão científica, atribuição de revisores, pareceres, decisão, ressalvas e transições da máquina de estados.

Gere:
1. `proposal.md`.
2. Delta specs em:
   - `specs/reviews/spec.md`
   - `specs/submissions/spec.md`
   - `specs/notifications/spec.md`
   - `specs/reports/spec.md`
3. `design.md` detalhando estado, autorização, workflow, telas do revisor, telas da comissão, notificações e edge cases.
4. `tasks.md` granular.

Regras:
- Não implementar anais digitais nesta change.
- Não implementar material final ainda, exceto reenvio de PDF revisado para ressalvas.
- Incluir testes para atribuição, parecer, decisão, ressalvas, reenvio e autorização.
```

### Prompt de implementação após aprovação

```text
/opsx:apply add-review-decision-workflow

Implemente revisão, pareceres, decisões, ressalvas e transições de estado conforme a change aprovada.
Não implemente anais ou material final pós-aceite nesta change.
```

---

## Proposal 09 — `add-final-materials-proceedings-videos`

### Objetivo

Implementar envio de material final para trabalhos aprovados, publicação de anais digitais, páginas de trabalhos aprovados e links para vídeos/YouTube.

### Dependências

- Proposals 01–08 arquivadas.

### Domínios OpenSpec

- `proceedings`
- `submissions`
- `videos`
- `public-site`
- `notifications`

### Escopo

Inclui:

1. FinalMaterial;
2. PDF final;
3. link de vídeo;
4. autorização de publicação;
5. página pública de anais ou link de anais;
6. página de trabalhos aprovados;
7. associação com VideoResource;
8. e-mails de solicitação e confirmação de material final.

Não inclui:

1. hospedagem de vídeos completos;
2. geração avançada de PDF de anais se não estiver prevista;
3. métricas avançadas.

### Critérios de aceite

1. Trabalho aprovado gera pendência de material final.
2. Autor envia PDF final e link de vídeo.
3. Comissão valida material final.
4. Trabalho validado fica pronto para anais.
5. Site publica anais ou link de anais.
6. Site publica links de vídeos/playlist sem hospedar vídeo.

### Prompt da proposal

```text
/opsx:propose add-final-materials-proceedings-videos

Crie uma change proposal OpenSpec chamada `add-final-materials-proceedings-videos`.

Contexto obrigatório:
- Vídeos completos não devem ser hospedados pelo sistema.
- O sistema deve armazenar links YouTube/playlist.
- Material final só é solicitado para trabalhos aprovados.
- Modalidades finais possíveis: oral, pôster.
- Anais digitais e trabalhos aprovados devem poder ser publicados no site.

Objetivo da change:
Implementar fluxo de material final, anais digitais, trabalhos aprovados e links para vídeos.

Gere:
1. `proposal.md`.
2. Delta specs em:
   - `specs/proceedings/spec.md`
   - `specs/submissions/spec.md`
   - `specs/videos/spec.md`
   - `specs/public-site/spec.md`
   - `specs/notifications/spec.md`
3. `design.md` detalhando FinalMaterial, validação, publicação em anais, associação com vídeos, páginas públicas e permissões.
4. `tasks.md` granular.

Regras:
- Não implementar streaming próprio.
- Não hospedar vídeo completo.
- Não implementar certificado ou QR code.
- Incluir cenários para material pendente, material recebido, validação e publicação.
```

### Prompt de implementação após aprovação

```text
/opsx:apply add-final-materials-proceedings-videos

Implemente material final, anais, trabalhos aprovados e links YouTube conforme a proposal aprovada.
Garanta que nenhum vídeo completo seja hospedado pela plataforma.
```

---

## Proposal 10 — `add-reports-exports-and-indicators`

### Objetivo

Implementar indicadores, relatórios e exports para comissão, anais e prestação de contas técnico-científica.

### Dependências

- Proposals 01–09 arquivadas.

### Domínios OpenSpec

- `reports`
- `submissions`
- `reviews`
- `proceedings`

### Escopo

Inclui:

1. dashboard de indicadores;
2. export CSV/JSON;
3. export para anais;
4. métricas de submissões;
5. métricas de aceitação/rejeição;
6. trabalhos por eixo;
7. modalidade final;
8. autores/instituições/estados/países;
9. revisores e prazos;
10. materiais publicados;
11. vídeos/links publicados;
12. auditabilidade básica.

Não inclui:

1. business intelligence complexo;
2. dashboards em tempo real;
3. integração automática com plataforma externa de inscrição, salvo import manual se definido.

### Critérios de aceite

1. Comissão visualiza métricas principais.
2. Comissão exporta CSV de submissões.
3. Comissão exporta dados para anais.
4. Indicadores mínimos do documento fonte estão cobertos.
5. Exports respeitam permissões.

### Prompt da proposal

```text
/opsx:propose add-reports-exports-and-indicators

Crie uma change proposal OpenSpec chamada `add-reports-exports-and-indicators`.

Contexto obrigatório:
- O sistema deve apoiar anais, indicadores e relatório técnico-científico.
- Indicadores mínimos incluem submissões, aceites, rejeições, eixos, modalidades, autores, instituições, revisores, prazos, materiais e vídeos/links publicados.
- O painel é para comissão/admin técnico, não para público geral.

Objetivo da change:
Implementar dashboards de indicadores e exports CSV/JSON para prestação de contas, anais e acompanhamento científico.

Gere:
1. `proposal.md`.
2. Delta specs em:
   - `specs/reports/spec.md`
   - `specs/submissions/spec.md`
   - `specs/reviews/spec.md`
   - `specs/proceedings/spec.md`
3. `design.md` detalhando queries, agregações, permissões, exports, formato dos arquivos e testes.
4. `tasks.md` granular.

Regras:
- Não implementar BI complexo.
- Não integrar automaticamente com UFMG/FUNDEP/Sympla nesta change.
- Incluir testes para permissões e consistência dos exports.
```

### Prompt de implementação após aprovação

```text
/opsx:apply add-reports-exports-and-indicators

Implemente indicadores e exports conforme a change aprovada.
Garanta que os dados exportados sejam consistentes, testados e acessíveis apenas à comissão/admin técnico.
```

---

## Proposal 11 — `harden-deployment-security-and-backups`

### Objetivo

Preparar a aplicação para staging/produção com segurança, backups, HTTPS, media protegida, rate limiting, headers, logs e restore testado.

### Dependências

- Proposals 01–10 arquivadas.

### Domínios OpenSpec

- `deployment-security`
- `developer-experience`
- `notifications`
- `submissions`

### Escopo

Inclui:

1. Docker Compose de produção ou staging;
2. Caddy/Nginx;
3. static/media strategy;
4. proteção de media privada;
5. backups PostgreSQL;
6. backups de media;
7. script de restore;
8. cabeçalhos de segurança;
9. HTTPS;
10. rate limiting;
11. logging;
12. Sentry/observabilidade opcional;
13. checklist de deploy.

Não inclui:

1. migração para cloud complexa;
2. Kubernetes;
3. alta disponibilidade.

### Critérios de aceite

1. Ambiente staging sobe por Docker Compose.
2. Arquivos privados continuam protegidos.
3. Backup e restore são testáveis.
4. Headers e CSRF/HTTPS estão configurados.
5. Rate limit existe para login/formulários críticos.
6. Documentação de deploy está clara.

### Prompt da proposal

```text
/opsx:propose harden-deployment-security-and-backups

Crie uma change proposal OpenSpec chamada `harden-deployment-security-and-backups`.

Contexto obrigatório:
- A aplicação já possui fluxos centrais.
- Arquivos de submissão devem permanecer privados.
- Produção deve usar HTTPS, headers de segurança, backups e variáveis fora do repositório.
- Não usar Kubernetes ou arquitetura complexa.

Objetivo da change:
Endurecer a aplicação para staging/produção, incluindo reverse proxy, HTTPS, backups, restore, media protegida, rate limiting, logs e documentação.

Gere:
1. `proposal.md`.
2. Delta specs em:
   - `specs/deployment-security/spec.md`
   - `specs/developer-experience/spec.md`
   - `specs/submissions/spec.md`
   - `specs/notifications/spec.md`
3. `design.md` detalhando deploy, rede, volumes, backups, restore, headers, media privada, SMTP e riscos.
4. `tasks.md` granular.

Regras:
- Não reescrever a aplicação.
- Não trocar stack.
- Não implementar features de produto novas.
- Incluir teste ou checklist de restore.
```

### Prompt de implementação após aprovação

```text
/opsx:apply harden-deployment-security-and-backups

Implemente hardening de deploy, segurança, backups e documentação conforme a change aprovada.
Não adicione novas features de produto nesta change.
```

---

## Proposal 12 — `complete-accessibility-performance-and-qa`

### Objetivo

Fechar QA transversal: acessibilidade, performance, responsividade, testes end-to-end, regressões visuais, conteúdo de seed e checklist final do MVP.

### Dependências

- Proposals 01–11 arquivadas.

### Domínios OpenSpec

- `design-system`
- `public-site`
- `submissions`
- `reviews`
- `deployment-security`
- `developer-experience`

### Escopo

Inclui:

1. auditoria WCAG 2.2 AA alvo;
2. navegação por teclado;
3. foco visível;
4. contraste;
5. reduced motion;
6. testes Playwright ou equivalente;
7. testes de formulário de submissão;
8. testes de revisão;
9. testes de export;
10. performance básica;
11. responsividade;
12. revisão de microcopy;
13. seed final para staging.

Não inclui:

1. redesenho completo;
2. mudança de arquitetura;
3. features novas.

### Critérios de aceite

1. Fluxos críticos passam em E2E.
2. Páginas principais passam checagem básica de acessibilidade.
3. Site funciona em mobile.
4. Home carrega sem dependências front-end pesadas.
5. Checklist MVP está cumprido.
6. Defeitos bloqueantes são corrigidos ou documentados.

### Prompt da proposal

```text
/opsx:propose complete-accessibility-performance-and-qa

Crie uma change proposal OpenSpec chamada `complete-accessibility-performance-and-qa`.

Contexto obrigatório:
- Não adicionar novas features.
- Esta change fecha qualidade, acessibilidade, performance e testes do MVP.
- O alvo de acessibilidade é WCAG 2.2 AA, com foco em contraste, teclado, labels, headings, foco visível e reduced motion.
- O site precisa funcionar bem em mobile.

Objetivo da change:
Implementar QA transversal e corrigir problemas bloqueantes sem alterar a arquitetura.

Gere:
1. `proposal.md`.
2. Delta specs em:
   - `specs/design-system/spec.md`
   - `specs/public-site/spec.md`
   - `specs/submissions/spec.md`
   - `specs/reviews/spec.md`
   - `specs/developer-experience/spec.md`
3. `design.md` detalhando estratégia de testes, a11y, performance, responsividade, ferramentas e critérios de aceite.
4. `tasks.md` granular.

Regras:
- Não criar novas funcionalidades.
- Não reescrever templates sem necessidade.
- Corrigir problemas pontuais e documentar exceções.
- Incluir cenários E2E para visitante, autor, revisor e comissão.
```

### Prompt de implementação após aprovação

```text
/opsx:apply complete-accessibility-performance-and-qa

Execute a QA transversal conforme a proposal aprovada.
Corrija problemas de acessibilidade, responsividade, performance e testes sem criar novas funcionalidades.
Atualize tasks e registre limitações remanescentes.
```

---

## 8. Critérios globais de Definition of Done

Uma proposal só deve ser considerada pronta quando:

1. `openspec validate <change-id> --strict` passa.
2. `proposal.md`, `design.md`, `tasks.md` e delta specs existem e estão coerentes.
3. A implementação corresponde aos specs aprovados.
4. Testes automatizados relevantes passam.
5. Migrations estão criadas e aplicadas em ambiente local.
6. Não há feature fora do escopo da proposal.
7. Não há regressão nos fluxos previamente implementados.
8. README ou documentação afetada foi atualizada.
9. Tasks foram marcadas como concluídas.
10. A change foi arquivada antes da próxima proposal dependente.

---

## 9. Estratégia de modelagem para evitar reescrita

1. Criar custom user (`accounts.User`) na primeira proposal com flags booleanas (`is_author`, `is_reviewer`, `is_chair`) e campos de perfil. Isso evita migração dolorosa depois.
2. Criar apps Django vazios cedo. Isso estabiliza imports e boundaries.
3. Criar design system antes das páginas. Isso evita retrabalho visual.
4. Criar modelos editoriais antes da Home. A Home deve consumir conteúdo real, não hardcoded.
5. Criar Program/Speaker antes da Home final. Programação e palestrantes são conteúdo central da Home.
6. Criar auth/roles antes de submissões. Submissões devem nascer com permissões corretas.
7. Criar submissões antes de revisão. Revisão depende de estados e arquivos estáveis.
8. Criar revisão antes de anais. Anais dependem de decisões finais.
9. Criar relatórios depois dos fluxos centrais. Indicadores precisam de dados reais.
10. Fazer hardening depois dos fluxos, mas antes do QA final.

---

## 10. Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Escopo crescer durante implementação | Cada proposal tem fora de escopo explícito |
| Agente criar SPA complexa | Config OpenSpec deve proibir SPA e privilegiar Django templates |
| Reescrita de auth | Custom user na primeira proposal |
| Design ficar desconectado do Stitch | Design system implementado antes das páginas |
| CMS virar RBAC complexo | Admin editorial único como regra de contexto |
| Upload público acidental | Testes e specs exigem media privada |
| Vídeos hospedados por engano | Specs exigem links YouTube apenas |
| Submissão pedir vídeo cedo | Specs da proposal 07 proíbem vídeo inicial |
| Relatórios incompletos | Proposal 10 cobre indicadores do documento fonte |
| Deploy frágil | Proposal 11 dedicada a hardening e restore |

---

## 11. Sequência curta de execução

Para cada item abaixo, criar, validar, aprovar, aplicar, testar e arquivar:

```text
01 bootstrap-django-wagtail-platform
02 add-design-system-and-layout-shells
03 add-core-cms-content-models
04 add-program-speakers-and-fixtures
05 add-public-site-pages
06 add-accounts-roles-and-dashboards
07 add-author-submission-initial-flow
08 add-review-decision-workflow
09 add-final-materials-proceedings-videos
10 add-reports-exports-and-indicators
11 harden-deployment-security-and-backups
12 complete-accessibility-performance-and-qa
```

---

## 12. Prompt de revisão entre proposals

Use este prompt antes de arquivar qualquer change:

```text
Revise a change OpenSpec `<change-id>` antes de arquivar.

Verifique:
1. A implementação segue `proposal.md`, `design.md`, `tasks.md` e os delta specs.
2. Não há funcionalidades fora de escopo.
3. Os testes relevantes passam.
4. Os requisitos usam SHALL/MUST e cenários Given/When/Then.
5. As tasks estão marcadas corretamente.
6. A documentação afetada foi atualizada.
7. Não há regressões nos fluxos já implementados.
8. A change pode ser arquivada com segurança.

Se houver problemas, liste-os como bloqueantes ou não-bloqueantes. Não arquive automaticamente sem aprovação humana.
```

---

## 13. Prompt de recuperação quando o agente fugir do escopo

```text
Pare a implementação atual e compare as mudanças feitas com a change OpenSpec ativa.

Identifique:
1. arquivos alterados fora do escopo;
2. funcionalidades adicionadas sem requisito;
3. decisões técnicas que contradizem o Documento de Requisitos;
4. violações das regras: sem SPA complexa, sem Next.js/Strapi, sem pagamento próprio, sem certificado próprio, sem QR code próprio, sem hospedagem de vídeo, sem RBAC editorial complexo.

Proponha um plano de reversão mínimo para retornar ao escopo aprovado.
Não continue implementando até eu aprovar o plano de correção.
```

---

## 14. Observação final

Este plano foi desenhado para que os agentes construam primeiro os trilhos permanentes — arquitetura, design system, CMS e modelos centrais — e só depois preencham as funcionalidades. Essa ordem reduz reescrita, preserva coerência visual e mantém o OpenSpec como registro auditável das decisões.
