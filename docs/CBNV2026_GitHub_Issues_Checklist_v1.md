# XII CBNV 2026 — Issues e Checklist Executável OpenSpec v1.0

**Projeto:** Website e plataforma digital do XII Congresso Brasileiro de Neurociências da Visão  
**Origem:** `docs/CBNV2026_OpenSpec_Plano_Implementacao_v2.md`  
**Uso previsto:** backlog operacional para GitHub Issues, OpenSpec changes e execução por agentes de codificação  
**Data:** 2026-05-08  

---

## 1. Como usar este arquivo

Este arquivo transforma o plano OpenSpec v2 em uma lista operacional de issues. Cada issue abaixo pode ser copiada para o GitHub como uma issue individual ou usada como checklist interno durante execução por change proposals.

A unidade principal de trabalho continua sendo a **change proposal OpenSpec**. A issue é o artefato de acompanhamento; a proposal é o artefato de especificação.

Regra operacional:

1. abrir uma branch por change proposal;
2. criar/validar a change em `openspec/changes/<change-id>/`;
3. implementar somente o escopo aprovado;
4. rodar checks;
5. abrir PR;
6. revisar;
7. arquivar a change somente depois de aceite.

Comandos padrão por proposal:

```bash
openspec validate <change-id> --strict
uv run python manage.py check
uv run python manage.py makemigrations --check --dry-run
uv run pytest
```

Para proposals com Docker:

```bash
docker compose build --no-cache
docker compose up
```

---

## 2. Labels sugeridas para GitHub

Criar estes labels no repositório:

```text
type:foundation
type:frontend
type:cms
type:content
type:domain
type:auth
type:submissions
type:reviews
type:reports
type:ops
type:qa

priority:p0
priority:p1
priority:p2
priority:p3

status:needs-spec
status:spec-ready
status:implementation
status:review
status:blocked

area:openspec
area:django
area:wagtail
area:tailwind
area:ui-ux
area:editorial
area:security
area:accessibility
area:deployment
```

---

## 3. Milestones sugeridos

### Milestone 1 — Foundation stabilized

Inclui:

- `stabilize-platform-foundation`

Resultado: projeto executável, versões alinhadas, User padrão + UserProfile, Docker coerente, checks e testes passando.

### Milestone 2 — Public site foundation

Inclui:

- `add-design-system-and-layout-shells`
- `add-core-cms-content-models`
- `seed-canonical-event-content`
- `add-program-speakers-and-venue-models`
- `add-public-site-pages-mvp`

Resultado: site público navegável e editável via CMS.

### Milestone 3 — Public site refinement

Inclui:

- `review-public-site-ui-ux-round-1`
- `produce-public-site-content-round-1`
- `verify-cross-page-content-consistency`
- `implement-public-site-polish-round-1`

Resultado: site público editorialmente consistente, visualmente refinado e pronto para servir de base estável.

### Milestone 4 — Scientific workflow MVP

Inclui:

- `add-accounts-profiles-and-dashboards`
- `add-author-submission-initial-flow`
- `add-review-decision-workflow`

Resultado: submissão e revisão científica funcionais.

### Milestone 5 — Outputs, operations and release readiness

Inclui:

- `add-final-materials-proceedings-videos`
- `add-reports-exports-and-indicators`
- `harden-deployment-security-and-backups`
- `complete-accessibility-performance-and-qa`

Resultado: plataforma pronta para staging/produção e pós-evento.

---

# 4. Issues operacionais

---

## Issue 01 — Stabilize platform foundation

**Change ID:** `stabilize-platform-foundation`  
**Labels:** `type:foundation`, `priority:p0`, `area:openspec`, `area:django`, `area:wagtail`, `area:deployment`  
**Milestone:** Foundation stabilized  

### Objetivo

Estabilizar a fundação técnica do projeto, eliminando drift entre documentação, dependências, Docker, settings, migrations e autenticação.

### Contexto

Durante a implementação inicial houve drift entre versões e decisões arquiteturais. A fundação deve ser realinhada antes de evoluir CMS, páginas públicas, submissões ou revisão científica.

### Escopo

- alinhar baseline para Python 3.14.x, Django 6.0.x, Wagtail 7.4.x LTS, PostgreSQL 18.3 e Tailwind 4.x;
- manter dependências diretas usadas pelo projeto: `django-widget-tweaks`, `django-axes`, `django-countries`;
- usar Django default User + `accounts.UserProfile`;
- remover custom user model se ainda não houver dados reais;
- corrigir rotas Wagtail/Django Admin;
- corrigir Docker e `.env.example`;
- garantir que checks e testes passem.

### Checklist

- [ ] Criar `openspec/changes/stabilize-platform-foundation/`.
- [ ] Criar `proposal.md`, `design.md`, `tasks.md`.
- [ ] Criar delta specs:
  - [ ] `specs/platform/spec.md`
  - [ ] `specs/accounts/spec.md`
  - [ ] `specs/deployment/spec.md`
- [ ] Atualizar `README.md` com baseline técnico atual.
- [ ] Atualizar `openspec/project.md` ou `openspec/config.yaml`.
- [ ] Atualizar `docs/CBNV2026_Requisitos_Arquitetura_v1(2).md` quando necessário.
- [ ] Atualizar `pyproject.toml`.
- [ ] Atualizar `uv.lock`.
- [ ] Confirmar que `django-widget-tweaks`, `django-axes` e `django-countries` continuam declarados.
- [ ] Remover `AUTH_USER_MODEL = "accounts.User"` se revertendo ao User padrão.
- [ ] Criar `accounts.UserProfile`.
- [ ] Registrar `UserProfile` no Django Admin.
- [ ] Regenerar migrations iniciais dos apps próprios, se aplicável.
- [ ] Separar `/admin/` para Wagtail Admin e `/django-admin/` para Django Admin.
- [ ] Adicionar Wagtail public routing em `/`.
- [ ] Corrigir `docker-compose.yml` para usar `DB_HOST=db` no serviço web.
- [ ] Usar imagem PostgreSQL 18.3.
- [ ] Adicionar `.dockerignore`.
- [ ] Remover supressão silenciosa de erro em `collectstatic`.
- [ ] Garantir que `.env` não está rastreado.
- [ ] Atualizar `.env.example` com placeholders seguros.
- [ ] Rodar validações.

### Validação

```bash
openspec validate stabilize-platform-foundation --strict
uv run python manage.py check
uv run python manage.py makemigrations --check --dry-run
uv run pytest
docker compose build --no-cache
docker compose up
```

### Critérios de aceite

- [ ] `manage.py check` passa.
- [ ] `makemigrations --check --dry-run` passa.
- [ ] `pytest` passa.
- [ ] Docker sobe sem correção manual de DB host.
- [ ] User padrão + UserProfile estão documentados e implementados.
- [ ] Docs, specs, código e Docker declaram o mesmo baseline.

---

## Issue 02 — Add design system and layout shells

**Change ID:** `add-design-system-and-layout-shells`  
**Labels:** `type:frontend`, `priority:p0`, `area:tailwind`, `area:ui-ux`, `area:accessibility`  
**Milestone:** Public site foundation  

### Objetivo

Transformar a direção visual do Stitch em um design system implementável em Django templates, evitando duplicação e reescrita posterior.

### Escopo

- tokens de cor, tipografia, spacing, radius, sombras e grid;
- layout base público;
- header responsivo;
- menu mobile;
- footer base;
- componentes de CTA, card, badge, timeline, section heading, container, alert e empty state;
- foco visível, contraste e responsividade.

### Checklist

- [ ] Criar change OpenSpec `add-design-system-and-layout-shells`.
- [ ] Criar delta specs em `design-system` e `public-site`.
- [ ] Definir tokens no CSS fonte, não apenas no CSS compilado.
- [ ] Definir tipografia final ou fallback adequado.
- [ ] Implementar `templates/base.html`.
- [ ] Implementar partials:
  - [ ] header
  - [ ] footer
  - [ ] navigation
  - [ ] CTA button
  - [ ] card
  - [ ] badge
  - [ ] section heading
  - [ ] timeline shell
  - [ ] form field wrapper
- [ ] Garantir dark-mode first se essa decisão permanecer.
- [ ] Garantir `prefers-reduced-motion`.
- [ ] Adicionar documentação curta de uso dos componentes.

### Validação

```bash
openspec validate add-design-system-and-layout-shells --strict
npm run build
uv run python manage.py check
uv run pytest
```

### Critérios de aceite

- [ ] As páginas futuras podem reutilizar componentes sem duplicar markup complexo.
- [ ] Header e footer são responsivos.
- [ ] O CSS fonte contém tokens claros.
- [ ] O design system respeita contraste básico e foco visível.

---

## Issue 03 — Add core CMS content models

**Change ID:** `add-core-cms-content-models`  
**Labels:** `type:cms`, `priority:p0`, `area:wagtail`, `area:editorial`  
**Milestone:** Public site foundation  

### Objetivo

Criar a base editorial do CMS para evitar hardcode de conteúdo institucional, links e blocos recorrentes.

### Escopo

- `SiteSettings`;
- notícias/avisos;
- patrocinadores/entidades apoiadoras;
- links globais;
- blocos editoriais reutilizáveis;
- campos de SEO básicos;
- controle de exibição pública.

### Checklist

- [ ] Criar change OpenSpec.
- [ ] Criar delta specs em `content` e `public-site`.
- [ ] Implementar `SiteSettings`.
- [ ] Implementar modelo de notícias/avisos.
- [ ] Implementar patrocinadores/entidades apoiadoras.
- [ ] Implementar links globais editáveis:
  - [ ] inscrição
  - [ ] transmissão
  - [ ] YouTube
  - [ ] Instagram
  - [ ] mapa
  - [ ] contato
- [ ] Implementar blocos reutilizáveis para páginas.
- [ ] Configurar painel Wagtail.
- [ ] Criar testes básicos de modelos.

### Validação

```bash
openspec validate add-core-cms-content-models --strict
uv run python manage.py makemigrations --check --dry-run
uv run python manage.py check
uv run pytest
```

### Critérios de aceite

- [ ] Admin consegue editar dados globais do evento.
- [ ] Links externos ficam centralizados.
- [ ] Notícias podem ser marcadas como destaque na Home.
- [ ] Patrocinadores/entidades podem ser exibidos por categoria.

---

## Issue 04 — Seed canonical event content

**Change ID:** `seed-canonical-event-content`  
**Labels:** `type:content`, `priority:p0`, `area:editorial`, `area:wagtail`  
**Milestone:** Public site foundation  

### Objetivo

Popular o CMS com dados canônicos mínimos do CBNV 2026 para suportar páginas públicas sem duplicação manual.

### Conteúdo canônico obrigatório

- nome formal;
- nome curto;
- tema;
- datas;
- formato;
- cidade;
- local;
- endereço completo;
- Google Maps URL;
- parceiros institucionais;
- FAPEMIG;
- link do canal/playlist YouTube, quando disponível;
- links de inscrição/transmissão em estado “em breve”, se ainda indisponíveis.

### Endereço oficial

```text
Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha.
R. Prof. Baeta Viana, s/n - Pampulha, Belo Horizonte - MG, 31270-901
```

Google Maps:

```text
https://maps.app.goo.gl/xzqJ2LCAHVP4hsFp6
```

### Checklist

- [ ] Criar fixtures ou management command de seed.
- [ ] Popular `SiteSettings`.
- [ ] Popular parceiros/entidades.
- [ ] Popular links globais.
- [ ] Popular texto inicial curto e neutro do evento.
- [ ] Incluir menção institucional à FAPEMIG.
- [ ] Garantir idempotência do seed.

### Validação

```bash
openspec validate seed-canonical-event-content --strict
uv run python manage.py check
uv run pytest
```

### Critérios de aceite

- [ ] Dados globais do evento aparecem em uma fonte única.
- [ ] Endereço oficial não fica hardcoded em múltiplas páginas.
- [ ] Seed pode ser rodado mais de uma vez sem duplicar dados.

---

## Issue 05 — Add program, speakers and venue models

**Change ID:** `add-program-speakers-and-venue-models`  
**Labels:** `type:domain`, `priority:p0`, `area:wagtail`, `area:editorial`  
**Milestone:** Public site foundation  

### Objetivo

Implementar programação, palestrantes e local do evento como modelos estruturados, editáveis e reutilizáveis.

### Escopo

- `ProgramDay`;
- `ProgramSession`;
- `ProgramTalk`;
- `Speaker`;
- status de palestrante/participante;
- venue/local e dados de mapa;
- fixtures da programação preliminar.

### Checklist

- [ ] Criar delta specs em `program`.
- [ ] Implementar modelos.
- [ ] Implementar Wagtail snippets/admin panels.
- [ ] Implementar status:
  - [ ] confirmado
  - [ ] convidado
  - [ ] pendente
  - [ ] oculto
  - [ ] substituído
- [ ] Implementar ocultação pública de participantes pendentes.
- [ ] Criar seed/fixture da programação.
- [ ] Adicionar testes de modelos e queries públicas.

### Critérios de aceite

- [ ] A programação é editável sem código.
- [ ] Nomes pendentes podem ser ocultados.
- [ ] O texto público não promete workshops se não houver workshops.
- [ ] O local exibido é CAD-1/UFMG, não local herdado de edição anterior.

---

## Issue 06 — Add public site pages MVP

**Change ID:** `add-public-site-pages-mvp`  
**Labels:** `type:frontend`, `type:cms`, `priority:p1`, `area:wagtail`, `area:ui-ux`  
**Milestone:** Public site foundation  

### Objetivo

Implementar as páginas públicas principais do CBNV 2026.

### Páginas

- Início
- Sobre
- Programação
- Palestrantes
- Submissões
- Inscrição
- Patrocínio
- Edições anteriores
- Contato

### Checklist

- [ ] Criar delta specs em `public-site`.
- [ ] Implementar tipos de página Wagtail.
- [ ] Implementar templates.
- [ ] Consumir `SiteSettings`.
- [ ] Consumir notícias.
- [ ] Consumir programação e palestrantes.
- [ ] Consumir patrocinadores/entidades.
- [ ] Implementar estados “em breve” para inscrição/transmissão.
- [ ] Implementar SEO básico.
- [ ] Implementar navegação e breadcrumbs quando aplicável.

### Critérios de aceite

- [ ] Site público é navegável.
- [ ] Páginas usam CMS/modelos, não conteúdo disperso.
- [ ] Home comunica tema, datas, local, CTAs e programação.
- [ ] Programação tem visualização por dia.
- [ ] Sobre tem conteúdo institucional mínimo.

---

## Issue 07 — Review public site UI/UX round 1

**Change ID:** `review-public-site-ui-ux-round-1`  
**Labels:** `type:frontend`, `priority:p1`, `area:ui-ux`, `area:accessibility`  
**Milestone:** Public site refinement  

### Objetivo

Realizar revisão crítica de UI/UX do site público implementado e produzir backlog priorizado de correções.

### Checklist de revisão

#### Home

- [ ] Avaliar inserção de notícias recentes na Home.
- [ ] Avaliar remoção/substituição do card “Híbrido”.
- [ ] Verificar se o card de local exibe endereço completo.
- [ ] Verificar mapa e link de localização.
- [ ] Remover ou reescrever copy exagerado.
- [ ] Corrigir ícones/labels inconsistentes com a data real.
- [ ] Revisar “O que esperar?” com base na programação real.
- [ ] Remover menção a workshops se não existirem.
- [ ] Revisar grid de entidades parceiras.
- [ ] Revisar footer, FAPEMIG, Instagram e redundâncias.

#### Sobre

- [ ] Avaliar qualidade e profundidade do texto.
- [ ] Remover ou consolidar bloco “O que esperar?” se redundante.
- [ ] Revisar hierarquia de títulos.
- [ ] Revisar “Local e acesso”.
- [ ] Corrigir mapa/local herdado.
- [ ] Revisar cards/fotos da equipe.
- [ ] Revisar redundância de instituições parceiras.

#### Global

- [ ] Revisar responsividade.
- [ ] Revisar contraste.
- [ ] Revisar navegação mobile.
- [ ] Revisar clareza dos CTAs.
- [ ] Revisar consistência entre seções.

### Entregável

- [ ] Relatório Markdown de UI/UX.
- [ ] Backlog priorizado.
- [ ] Lista de decisões: manter, remover, consolidar ou reescrever.

### Critérios de aceite

- [ ] A review gera tarefas acionáveis.
- [ ] Problemas são classificados por severidade.
- [ ] Não há implementação misturada à review.

---

## Issue 08 — Produce public site content round 1

**Change ID:** `produce-public-site-content-round-1`  
**Labels:** `type:content`, `priority:p1`, `area:editorial`  
**Milestone:** Public site refinement  

### Objetivo

Revisar e produzir conteúdo editorial do site público, com tom científico, institucional e sóbrio.

### Checklist

- [ ] Reescrever hero copy.
- [ ] Reescrever descrição curta do evento.
- [ ] Expandir página Sobre.
- [ ] Produzir texto de “Por que participar?” ou equivalente.
- [ ] Produzir texto coerente de “O que esperar?” se o bloco for mantido.
- [ ] Revisar Programação.
- [ ] Revisar Submissões.
- [ ] Revisar Inscrição.
- [ ] Revisar Patrocínio.
- [ ] Revisar Footer.
- [ ] Revisar microcopy de estados “em breve”.
- [ ] Criar guidelines editoriais curtas.

### Regras editoriais

- [ ] Evitar exagero promocional.
- [ ] Não afirmar que é o maior evento da América Latina.
- [ ] Não usar “fronteira do conhecimento” se soar genérico ou hiperbólico.
- [ ] Não prometer workshops inexistentes.
- [ ] Separar conteúdo confirmado de conteúdo pendente.
- [ ] Usar português brasileiro claro.

### Critérios de aceite

- [ ] Textos são coerentes com o Documento de Requisitos e programação.
- [ ] Textos não contradizem dados estruturados.
- [ ] Home e Sobre deixam de ser genéricos.

---

## Issue 09 — Verify cross-page content consistency

**Change ID:** `verify-cross-page-content-consistency`  
**Labels:** `type:content`, `type:qa`, `priority:p1`, `area:editorial`, `area:qa`  
**Milestone:** Public site refinement  

### Objetivo

Verificar consistência editorial e factual entre páginas, cards, CTAs, footer, programação, entidades e dados globais.

### Checklist de consistência

- [ ] Nome do evento é consistente.
- [ ] Edição é consistente.
- [ ] Tema é consistente.
- [ ] Datas são consistentes.
- [ ] Local é consistente.
- [ ] Endereço é consistente.
- [ ] Link do mapa é consistente.
- [ ] Formato presencial/híbrido é consistente.
- [ ] CTAs por fase são consistentes.
- [ ] Home e Sobre não repetem blocos contraditórios.
- [ ] Programação e texto “O que esperar?” não divergem.
- [ ] Não há menção indevida a workshops.
- [ ] Entidades parceiras têm nomenclatura padronizada.
- [ ] FAPEMIG aparece nos locais necessários.
- [ ] Footer não repete informação sem função.
- [ ] Ícones e labels fazem sentido.
- [ ] Participantes pendentes não aparecem como confirmados.
- [ ] Links externos funcionam ou aparecem como “em breve”.
- [ ] Conteúdo herdado da edição anterior não aparece como se fosse de 2026.

### Entregáveis

- [ ] Checklist preenchido.
- [ ] Relatório de inconsistências.
- [ ] Issues derivadas para correção.
- [ ] Regras editoriais preventivas.

### Critérios de aceite

- [ ] Inconsistências críticas são identificadas antes de staging/produção.
- [ ] Há rastreabilidade entre problema e correção.
- [ ] Conteúdo duplicado é consolidado ou justificado.

---

## Issue 10 — Implement public site polish round 1

**Change ID:** `implement-public-site-polish-round-1`  
**Labels:** `type:frontend`, `type:content`, `priority:p1`, `area:ui-ux`, `area:editorial`  
**Milestone:** Public site refinement  

### Objetivo

Aplicar correções priorizadas nas reviews de UI/UX, conteúdo e consistência.

### Checklist

- [ ] Aplicar ajustes de Home.
- [ ] Aplicar ajustes de Sobre.
- [ ] Aplicar ajustes de footer.
- [ ] Aplicar ajustes de entidades parceiras.
- [ ] Aplicar ajustes de mapa/local.
- [ ] Aplicar ajustes de cards e grids.
- [ ] Aplicar ajustes de tipografia.
- [ ] Aplicar ajustes de microcopy.
- [ ] Remover blocos redundantes.
- [ ] Rodar nova verificação visual.

### Critérios de aceite

- [ ] Backlog crítico da review round 1 está resolvido.
- [ ] Site público está mais coerente e menos redundante.
- [ ] Ajustes não introduzem regressão de responsividade.

---

## Issue 11 — Add accounts, profiles and dashboards

**Change ID:** `add-accounts-profiles-and-dashboards`  
**Labels:** `type:auth`, `priority:p1`, `area:django`  
**Milestone:** Scientific workflow MVP  

### Objetivo

Implementar autenticação e áreas internas base para autores, revisores e chair/comissão.

### Checklist

- [ ] Criar delta specs em `accounts`.
- [ ] Implementar formulários de login/cadastro.
- [ ] Implementar perfil do usuário.
- [ ] Implementar dashboard do autor.
- [ ] Implementar dashboard do revisor.
- [ ] Implementar dashboard da comissão.
- [ ] Implementar controle simples por flags de profile.
- [ ] Implementar testes de autorização.

### Critérios de aceite

- [ ] Usuário consegue autenticar.
- [ ] Perfil armazena metadados do congresso.
- [ ] Dashboards existem e respeitam papel científico.

---

## Issue 12 — Add author submission initial flow

**Change ID:** `add-author-submission-initial-flow`  
**Labels:** `type:submissions`, `priority:p1`, `area:django`  
**Milestone:** Scientific workflow MVP  

### Objetivo

Implementar a fase inicial da submissão científica bifásica.

### Checklist

- [ ] Criar modelos `Submission`, `SubmissionAuthor`, `SubmissionFile`.
- [ ] Implementar estados iniciais.
- [ ] Implementar formulário de submissão.
- [ ] Implementar autores/afiliação.
- [ ] Implementar upload de PDF.
- [ ] Validar tipo e tamanho de arquivo.
- [ ] Proteger arquivos de URL pública direta.
- [ ] Enviar e-mail de confirmação.
- [ ] Implementar dashboard de status.

### Critério essencial

- [ ] Vídeo não é exigido na submissão inicial.

---

## Issue 13 — Add review and decision workflow

**Change ID:** `add-review-decision-workflow`  
**Labels:** `type:reviews`, `priority:p2`, `area:django`  
**Milestone:** Scientific workflow MVP  

### Objetivo

Implementar workflow de revisão, pareceres e decisão.

### Checklist

- [ ] Criar `ReviewAssignment`.
- [ ] Criar `Review`.
- [ ] Criar `Decision`.
- [ ] Implementar atribuição de revisores.
- [ ] Implementar declaração de conflito.
- [ ] Implementar formulário de parecer.
- [ ] Implementar decisão final.
- [ ] Implementar “aceito com ressalvas”.
- [ ] Implementar modalidade final.
- [ ] Enviar notificações.

### Critérios de aceite

- [ ] Chair consegue atribuir revisor.
- [ ] Revisor consegue avaliar.
- [ ] Comissão consegue decidir.
- [ ] Autor vê status simplificado.

---

## Issue 14 — Add final materials, proceedings and videos

**Change ID:** `add-final-materials-proceedings-videos`  
**Labels:** `type:submissions`, `type:reports`, `priority:p2`, `area:django`, `area:editorial`  
**Milestone:** Outputs, operations and release readiness  

### Objetivo

Implementar a fase final para trabalhos aprovados, anais e links de vídeo.

### Checklist

- [ ] Criar `FinalMaterial`.
- [ ] Implementar upload de PDF final.
- [ ] Implementar link de vídeo.
- [ ] Implementar link/arquivo de pôster se aplicável.
- [ ] Implementar autorização de publicação.
- [ ] Implementar validação pela comissão.
- [ ] Implementar dados para anais.
- [ ] Implementar `VideoResource`.
- [ ] Publicar links do YouTube sem hospedar vídeos.

### Critérios de aceite

- [ ] Trabalhos aprovados enviam material final.
- [ ] Vídeos são links, não arquivos hospedados.
- [ ] Dados para anais são exportáveis.

---

## Issue 15 — Add reports, exports and indicators

**Change ID:** `add-reports-exports-and-indicators`  
**Labels:** `type:reports`, `priority:p2`, `area:django`  
**Milestone:** Outputs, operations and release readiness  

### Objetivo

Implementar indicadores e exportações para anais, acompanhamento e relatório técnico-científico.

### Checklist

- [ ] Exportar submissões CSV/XLSX.
- [ ] Exportar autores.
- [ ] Exportar instituições.
- [ ] Exportar pareceres/decisões conforme permissão.
- [ ] Indicadores por eixo.
- [ ] Indicadores por modalidade final.
- [ ] Indicadores por status.
- [ ] Indicadores por instituição/UF/país.
- [ ] Dados para relatório técnico.
- [ ] Testes de exportação.

### Critérios de aceite

- [ ] Comissão consegue exportar dados centrais.
- [ ] Indicadores essenciais estão disponíveis.
- [ ] Exports respeitam privacidade e permissões.

---

## Issue 16 — Harden deployment, security and backups

**Change ID:** `harden-deployment-security-and-backups`  
**Labels:** `type:ops`, `priority:p2`, `area:security`, `area:deployment`  
**Milestone:** Outputs, operations and release readiness  

### Objetivo

Preparar o sistema para staging/produção com segurança operacional mínima.

### Checklist

- [ ] Configurar settings de produção.
- [ ] Exigir `DJANGO_SECRET_KEY`.
- [ ] Configurar `ALLOWED_HOSTS`.
- [ ] Configurar `CSRF_TRUSTED_ORIGINS`.
- [ ] Configurar HTTPS/proxy.
- [ ] Configurar cookies seguros.
- [ ] Configurar SMTP real.
- [ ] Configurar armazenamento protegido.
- [ ] Configurar backups de banco.
- [ ] Configurar backups de media.
- [ ] Configurar logs.
- [ ] Revisar `django-axes`.
- [ ] Rodar `manage.py check --deploy`.

### Critérios de aceite

- [ ] Produção não usa `runserver`.
- [ ] Secrets não ficam no repositório.
- [ ] Arquivos privados continuam protegidos.
- [ ] Backup/restore está documentado.

---

## Issue 17 — Complete accessibility, performance and QA

**Change ID:** `complete-accessibility-performance-and-qa`  
**Labels:** `type:qa`, `priority:p2`, `area:accessibility`, `area:ui-ux`  
**Milestone:** Outputs, operations and release readiness  

### Objetivo

Fechar a fase com revisão abrangente de acessibilidade, performance e regressão.

### Checklist

- [ ] Revisar navegação por teclado.
- [ ] Revisar foco visível.
- [ ] Revisar contraste.
- [ ] Revisar headings.
- [ ] Revisar labels de formulários.
- [ ] Revisar textos alternativos.
- [ ] Revisar responsividade.
- [ ] Revisar performance da Home.
- [ ] Revisar peso de imagens.
- [ ] Revisar lazy loading.
- [ ] Rodar suíte de testes.
- [ ] Revisar fluxo de submissão ponta a ponta.
- [ ] Revisar fluxo de revisão ponta a ponta.
- [ ] Corrigir regressões.

### Critérios de aceite

- [ ] Site atende baseline de acessibilidade definido no projeto.
- [ ] Fluxos críticos estão testados.
- [ ] Não há regressões públicas óbvias.
- [ ] Projeto está pronto para staging/produção.

---

# 5. Issues derivadas específicas de UI/conteúdo já mapeadas

Estas issues podem ser abertas separadamente se você preferir granularidade fina em vez de agrupar tudo nas proposals 07–10.

---

## UI-01 — Add latest news block to Home

**Labels:** `type:frontend`, `type:content`, `area:ui-ux`, `priority:p1`  
**Parent:** `review-public-site-ui-ux-round-1` / `implement-public-site-polish-round-1`

### Checklist

- [ ] Avaliar posição ideal do bloco de notícias.
- [ ] Decidir se substitui o card “Híbrido”.
- [ ] Exibir 2–3 notícias ou avisos recentes.
- [ ] Incluir fallback quando não houver notícias.
- [ ] Garantir responsividade.

---

## UI-02 — Fix venue address and map

**Labels:** `type:frontend`, `type:content`, `area:editorial`, `priority:p0`  
**Parent:** `seed-canonical-event-content` / `add-program-speakers-and-venue-models`

### Endereço

```text
Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha.
R. Prof. Baeta Viana, s/n - Pampulha, Belo Horizonte - MG, 31270-901
```

### Checklist

- [ ] Atualizar endereço no CMS.
- [ ] Atualizar Home.
- [ ] Atualizar Sobre.
- [ ] Atualizar Contato.
- [ ] Atualizar mapa.
- [ ] Remover local herdado da edição anterior.

---

## UI-03 — Rewrite exaggerated Home copy

**Labels:** `type:content`, `area:editorial`, `priority:p0`  
**Parent:** `produce-public-site-content-round-1`

### Problema

Textos como “maior evento de Neurovisão da América Latina” e formulações genéricas como “fronteira do conhecimento” não refletem o tom desejado.

### Checklist

- [ ] Reescrever hero.
- [ ] Reescrever subtítulo.
- [ ] Reescrever CTAs auxiliares.
- [ ] Validar com tom institucional, científico e humilde.

---

## UI-04 — Remove workshop references

**Labels:** `type:content`, `priority:p0`, `area:editorial`  
**Parent:** `verify-cross-page-content-consistency`

### Checklist

- [ ] Buscar “workshop” no projeto.
- [ ] Remover ou substituir por atividades reais da programação.
- [ ] Verificar Home, Sobre, Programação e cards.

---

## UI-05 — Footer institutional polish

**Labels:** `type:frontend`, `type:content`, `area:ui-ux`, `priority:p1`

### Checklist

- [ ] Adicionar logo FAPEMIG se houver asset aprovado.
- [ ] Adicionar menção textual adequada à FAPEMIG.
- [ ] Substituir texto “Instagram” por ícone acessível.
- [ ] Remover texto redundante se já houver copyright e branding.
- [ ] Garantir alt text/aria-label.

---

## UI-06 — Improve About page content and layout

**Labels:** `type:content`, `type:frontend`, `area:editorial`, `area:ui-ux`, `priority:p1`

### Checklist

- [ ] Expandir texto da página Sobre.
- [ ] Remover redundância de “O que esperar?” se mantida na Home.
- [ ] Melhorar hierarquia de títulos.
- [ ] Reorganizar “Local e acesso”.
- [ ] Melhorar cards da equipe.
- [ ] Ajustar entidades parceiras.

---

# 6. Checklist de PR para qualquer change

Usar este checklist em todo Pull Request:

```markdown
## OpenSpec

- [ ] A change proposal existe em `openspec/changes/<change-id>/`.
- [ ] `proposal.md` está atualizado.
- [ ] `design.md` está atualizado quando necessário.
- [ ] `tasks.md` reflete o estado real.
- [ ] Delta specs estão em `openspec/changes/<change-id>/specs/...`.
- [ ] `openspec validate <change-id> --strict` passa.

## Implementação

- [ ] O escopo implementado corresponde à proposal.
- [ ] Não há feature fora do escopo.
- [ ] Migrations são intencionais.
- [ ] Não há secrets no commit.
- [ ] Não há arquivos gerados desnecessários.

## Qualidade

- [ ] `uv run python manage.py check` passa.
- [ ] `uv run python manage.py makemigrations --check --dry-run` passa.
- [ ] `uv run pytest` passa.
- [ ] `npm run build` passa quando CSS/templates forem alterados.
- [ ] Responsividade básica foi verificada quando UI foi alterada.
- [ ] Acessibilidade básica foi verificada quando UI foi alterada.

## Conteúdo

- [ ] Textos não contradizem o Documento de Requisitos.
- [ ] Conteúdo pendente está marcado como pendente.
- [ ] Não há claims promocionais exagerados.
- [ ] Datas, local e formato estão consistentes.
```

---

# 7. Ordem recomendada imediata

Considerando o estado atual do projeto, a ordem prática é:

1. finalizar PR/branch da `stabilize-platform-foundation`;
2. atualizar `docs/CBNV2026_OpenSpec_Plano_Implementacao_v2.md`;
3. criar issues principais 01–17 no GitHub;
4. iniciar `add-design-system-and-layout-shells`;
5. iniciar `add-core-cms-content-models`;
6. iniciar `seed-canonical-event-content`;
7. implementar páginas públicas;
8. só então fazer a revisão UI/UX formal.

Não inverta a ordem entre conteúdo/cms/design. Corrigir copy hardcoded antes de estabilizar CMS e layout tende a gerar reescrita.
