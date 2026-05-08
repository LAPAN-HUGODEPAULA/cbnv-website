# XII CBNV 2026 — Plano de Implementação OpenSpec v2.0

**Projeto:** Website e plataforma digital do XII Congresso Brasileiro de Neurociências da Visão  
**Metodologia:** SDD — Spec Driven Design com OpenSpec  
**Stack aprovada:** Django + Wagtail + PostgreSQL + Tailwind CSS + HTMX/Alpine.js  
**Documento fonte:** `docs/CBNV2026_Requisitos_Arquitetura_v1(2).md`  
**Referência visual:** `stitch_cbnv_2026_digital_platform.zip`  
**Data:** 2026-05-08  
**Status:** Working plan / backlog consolidado para a nova fase do sistema  

---

## 1. Finalidade deste documento

Este arquivo substitui operacionalmente o plano v1 e consolida as decisões mais recentes sobre:

1. estabilização da fundação técnica do projeto;
2. alinhamento da stack com versões atuais;
3. simplificação do modelo de autenticação;
4. organização da sequência de change proposals para minimizar retrabalho;
5. inclusão explícita de ciclos de revisão de UI/UX;
6. inclusão explícita de produção e revisão editorial de conteúdo;
7. inclusão de uma proposal específica para verificação de consistência entre conteúdos e páginas.

Ele **não substitui** o Documento de Requisitos e Arquitetura. Ele traduz esse documento em um plano operacional de execução por proposals OpenSpec.

---

## 2. O que mudou em relação ao plano v1

### 2.1 Mudanças de fundação

1. A proposal inicial deixa de ser `bootstrap-django-wagtail-platform` e passa a ser **`stabilize-platform-foundation`**.
2. A fundação deve ser realinhada para as **versões atuais estáveis compatíveis** do ecossistema.
3. O projeto deve preferir **defaults idiomáticos do Django/Wagtail** sempre que isso reduzir engenharia desnecessária.
4. A estratégia de autenticação passa a favorecer o **User padrão do Django + UserProfile** para metadados do congresso.

### 2.2 Mudanças de produto/processo

1. O plano agora prevê **revisões explícitas de UI e UX** antes e depois da implementação das páginas públicas.
2. O plano agora prevê uma trilha própria de **produção de conteúdo** para Home, Sobre, Programação, Submissões, Inscrição, Patrocínio, Edições Anteriores e rodapé.
3. O plano agora prevê uma proposal própria de **verificação de consistência entre conteúdos**, para evitar drift editorial entre Home, Sobre, Programação, cards, CTAs, rodapé e dados estruturados.
4. As observações levantadas durante a revisão do frontend atual entram neste backlog como itens concretos de revisão e implementação.

---

## 3. Premissas obrigatórias

1. O Documento de Requisitos e Arquitetura continua sendo o **single source of truth**.
2. O ZIP do Stitch é **referência visual**, não fonte funcional de verdade.
3. O site legado Wix e o Notion **não orientam mais escopo ou arquitetura**; podem ser usados apenas como apoio controlado para acervo histórico ou checagem pontual de conteúdo.
4. A stack principal permanece: **Django + Wagtail + PostgreSQL + Tailwind + HTMX/Alpine**.
5. Não implementar Next.js + Strapi.
6. Não implementar pagamento próprio.
7. Não implementar certificados próprios.
8. Não implementar QR code de credenciamento próprio.
9. Não hospedar vídeos completos; usar apenas links/playlist do YouTube.
10. Não implementar RBAC editorial complexo no MVP.
11. O admin editorial principal é **um único usuário central**.
12. Os papéis científicos continuam existindo no domínio transacional: autor, revisor, chair/comissão.
13. A submissão inicial não deve exigir vídeo.
14. Os arquivos de submissão devem permanecer protegidos, nunca públicos por URL direta.
15. O site deve ser centrado no usuário, responsivo, acessível, visualmente forte e editorialmente coerente.
16. O desenvolvimento deve privilegiar **Django idiomático**, templates legíveis, testes, migrations incrementais e decisões que agentes de codificação consigam executar com baixa ambiguidade.

---

## 4. Baseline técnico desta fase

### 4.1 Regra geral

Usar as **versões estáveis mais atuais compatíveis** no momento da stabilização da fundação, com pinagem explícita e lockfile atualizado.

### 4.2 Baseline aprovado para a proposal de fundação

- Python 3.14.x estável (ou a versão estável mais recente da linha aprovada no ambiente)
- Django 6.0.x
- Wagtail 7.4.x LTS
- PostgreSQL 18.3
- Tailwind CSS 4.x
- Node.js 24 LTS (se necessário para o pipeline frontend)

### 4.3 Regra de dependências

1. `pyproject.toml` deve listar principalmente **dependências diretas**.
2. Dependências transitivas devem ser deixadas a cargo do resolvedor, salvo necessidade explícita.
3. Dependências diretas efetivamente usadas pelo projeto devem permanecer declaradas, inclusive quando exigidas por settings, templates ou segurança.
4. Já identificadas como diretas nesta fase:
   - `django-widget-tweaks`
   - `django-axes`
   - `django-countries`

---

## 5. Estratégia OpenSpec para esta fase

### 5.1 Estrutura esperada

```text
openspec/
├── AGENTS.md
├── project.md ou config.yaml
├── specs/
│   ├── platform/
│   ├── accounts/
│   ├── design-system/
│   ├── content/
│   ├── program/
│   ├── public-site/
│   ├── submissions/
│   ├── reviews/
│   ├── proceedings/
│   ├── reports/
│   ├── deployment/
│   ├── accessibility/
│   └── qa/
└── changes/
    ├── archive/
    └── <change-id>/
        ├── proposal.md
        ├── design.md
        ├── tasks.md
        └── specs/
            └── <domain>/spec.md
```

### 5.2 Regra de operação

1. Cada mudança relevante entra por uma **change proposal**.
2. Os deltas ficam em `openspec/changes/<change-id>/specs/...`, não diretamente em `openspec/specs/`.
3. Validar cada proposal com `openspec validate <change-id> --strict`.
4. Evitar múltiplas proposals ativas com forte interdependência.
5. Só arquivar/incorporar uma change quando:
   - a proposal estiver aprovada;
   - a implementação estiver concluída;
   - testes e checks estiverem passando;
   - a consistência com o Documento de Requisitos estiver revisada.

---

## 6. Estratégia de execução por fases

Para reduzir reescrita, a sequência desta fase é:

1. **fundação técnica**;
2. **sistema visual e shells de layout**;
3. **modelos editoriais e estrutura de conteúdo**;
4. **conteúdo canônico e programação**;
5. **páginas públicas MVP**;
6. **revisões de UI/UX**;
7. **produção e revisão editorial de conteúdo**;
8. **checagem de consistência entre conteúdos**;
9. **áreas autenticadas e fluxos científicos**;
10. **anais, vídeos, relatórios, segurança e QA**.

---

## 7. Backlog / working plan da nova fase

A tabela abaixo é a trilha operacional recomendada.

| Ordem | Change ID | Tipo | Objetivo principal | Dependências | Observações |
|---:|---|---|---|---|---|
| 01 | `stabilize-platform-foundation` | foundation | Alinhar versões, Docker, settings, rotas e autenticação | nenhuma | substitui a antiga bootstrap proposal |
| 02 | `add-design-system-and-layout-shells` | frontend foundation | Consolidar tokens, componentes base, grid, tipografia, navegação e footer | 01 | deve refletir o Stitch, mas ser implementável em Django templates |
| 03 | `add-core-cms-content-models` | cms | Criar modelos editoriais centrais, settings do site, notícias, patrocinadores, blocos reutilizáveis | 01, 02 | evita hardcode espalhado |
| 04 | `seed-canonical-event-content` | editorial/data | Cadastrar conteúdo canônico inicial do evento, venue, links, entidades e metadados globais | 03 | prepara Home/Sobre/rodapé |
| 05 | `add-program-speakers-and-venue-models` | domain | Implementar programação, dias, sessões, palestras, participantes pendentes, local e mapa | 03, 04 | deve seguir a programação oficial |
| 06 | `add-public-site-pages-mvp` | public site | Implementar Início, Sobre, Programação, Palestrantes, Submissões, Inscrição, Patrocínio, Edições Anteriores, Contato | 02, 03, 04, 05 | entrega o MVP público navegável |
| 07 | `review-public-site-ui-ux-round-1` | review | Revisar UI/UX do site público implementado e produzir backlog de ajustes | 06 | revisão crítica antes de refinamentos |
| 08 | `produce-public-site-content-round-1` | editorial | Reescrever e expandir o conteúdo das páginas principais com copy coerente e humilde | 06, 07 | foca em conteúdo, não em lógica |
| 09 | `verify-cross-page-content-consistency` | validation/editorial | Verificar consistência entre Home, Sobre, Programação, cards, footer, CTAs, venue, datas, labels e entidades | 06, 07, 08 | nova proposal obrigatória desta fase |
| 10 | `implement-public-site-polish-round-1` | refinement | Aplicar correções de layout, copy, imagens, cards, footer, mapas e elementos apontados nas revisões | 07, 08, 09 | fecha o primeiro ciclo de refinamento público |
| 11 | `add-accounts-profiles-and-dashboards` | auth | Implementar login, perfil, dashboards e áreas-base de autor/revisor/chair | 01, 02 | usar User padrão + UserProfile |
| 12 | `add-author-submission-initial-flow` | submissions | Implementar fase 1 da submissão bifásica | 11 | primeira trilha científica |
| 13 | `add-review-decision-workflow` | reviews | Implementar revisão, distribuição, pareceres e decisão | 12 | depende de submissões estáveis |
| 14 | `add-final-materials-proceedings-videos` | proceedings | Implementar materiais finais, anais e links para vídeos | 13 | integra YouTube e anais |
| 15 | `add-reports-exports-and-indicators` | reporting | Indicadores, exportações e dados para relatório técnico | 12, 13, 14 | importante para prestação de contas |
| 16 | `harden-deployment-security-and-backups` | ops/security | Produção, segurança, backup, observabilidade, secrets, deploy | 01-15 | quando os fluxos centrais estiverem estáveis |
| 17 | `complete-accessibility-performance-and-qa` | qa | A11y, performance, regressão, revisão final e readiness de staging | 06-16 | fecha a fase |

---

## 8. Proposal 01 — `stabilize-platform-foundation`

### Objetivo

Estabilizar a fundação técnica do projeto e eliminar o drift de baseline introduzido durante a implementação inicial.

### Escopo

1. alinhar `README`, OpenSpec, docs, Docker, settings e dependências com o baseline atual;
2. usar versões atuais compatíveis de Django/Wagtail/PostgreSQL;
3. corrigir `docker-compose` para funcionamento previsível;
4. separar rotas de Wagtail Admin e Django Admin;
5. expor corretamente as rotas públicas do Wagtail;
6. remover engenharia desnecessária de autenticação;
7. usar **Django default User + UserProfile**;
8. regenerar migrations iniciais de apps próprios, se ainda não houver dados reais dependentes;
9. garantir que `manage.py check`, `makemigrations --check --dry-run` e `pytest` passem.

### Saídas esperadas

- baseline técnico estabilizado;
- `pyproject.toml` e `uv.lock` coerentes;
- `.env.example` seguro;
- Docker funcional;
- testes passando;
- delta specs de platform/accounts/deployment atualizados.

### Critérios de aceite

1. a aplicação sobe localmente com a stack aprovada;
2. `check`, `makemigrations --check --dry-run` e `pytest` passam;
3. a autenticação usa User padrão + UserProfile;
4. o projeto não depende mais de suposições antigas conflitantes.

---

## 9. Proposal 02 — `add-design-system-and-layout-shells`

### Objetivo

Transformar a direção visual do Stitch em um design system implementável e reutilizável em Django templates.

### Escopo

1. tokens de cor, tipografia, spacing, radius, shadows e grids;
2. classes base e componentes reutilizáveis;
3. shell de layout público;
4. header, navegação, menu mobile, footer, CTA bar e patterns base;
5. padrões de cards, seções, hero, timelines e listas;
6. guidelines de acessibilidade visual e contraste.

### Critérios de aceite

1. páginas públicas conseguem reutilizar componentes sem duplicação excessiva;
2. existe consistência entre Home e páginas internas;
3. o sistema visual é legível, responsivo e acessível.

### Observações

Esta proposal deve capturar explicitamente diretrizes úteis do fluxo de design e UI review, mas **sem amarrar a implementação a artifícios frágeis do protótipo**.

---

## 10. Proposal 03 — `add-core-cms-content-models`

### Objetivo

Implementar a base editorial do CMS para evitar conteúdo hardcoded e dar controle ao admin único.

### Escopo

1. `SiteSettings`;
2. modelos de notícias/avisos;
3. patrocinadores/entidades apoiadoras;
4. blocos reutilizáveis para CTA, cards e seções editoriais;
5. configurações de links externos (inscrição, transmissão, YouTube, Instagram etc.);
6. elementos globais do footer e branding institucional.

### Critérios de aceite

1. conteúdos globais não ficam espalhados em templates fixos;
2. o admin consegue atualizar links e blocos recorrentes pelo CMS;
3. Home, Sobre e rodapé podem consumir dados do CMS.

---

## 11. Proposal 04 — `seed-canonical-event-content`

### Objetivo

Popular o CMS com o conteúdo canônico mínimo do evento para suportar as páginas públicas.

### Escopo

1. nome, tema, datas, local e formato do evento;
2. endereço completo do CAD-1/UFMG;
3. links institucionais e redes;
4. links de mapa, inscrição e YouTube;
5. parceiros e entidades apoiadoras;
6. texto institucional curto e neutro sobre o congresso;
7. menção obrigatória à FAPEMIG;
8. estado inicial de notícias/avisos.

### Critérios de aceite

1. os dados básicos aparecem de forma centralizada e reutilizável;
2. Home, Sobre e footer conseguem consumir esses dados;
3. venue e endereço não precisam ser repetidos manualmente em múltiplos templates.

---

## 12. Proposal 05 — `add-program-speakers-and-venue-models`

### Objetivo

Modelar programação, palestrantes e informações do local de forma canônica e exibível no site.

### Escopo

1. dias e sessões da programação oficial;
2. palestras, mesas, sessões paralelas e tipos de atividade;
3. participantes com status (`confirmado`, `pendente`, `oculto`, etc.);
4. dados do local do evento, endereço, mapa e instruções de acesso;
5. suporte a exibição/ocultação de nomes pendentes.

### Critérios de aceite

1. a página de Programação não depende de conteúdo textual ad hoc;
2. os nomes pendentes podem ser ocultados do site;
3. o local oficial do evento pode ser exibido com dados corretos e consistentes.

---

## 13. Proposal 06 — `add-public-site-pages-mvp`

### Objetivo

Entregar o conjunto de páginas públicas principais do CBNV 2026.

### Escopo

1. Início;
2. Sobre;
3. Programação;
4. Palestrantes;
5. Submissões;
6. Inscrição;
7. Patrocínio;
8. Edições anteriores;
9. Contato.

### Critérios de aceite

1. o site público é navegável de ponta a ponta;
2. as páginas consomem dados do CMS e dos modelos de programação;
3. o site já comunica adequadamente o congresso, mesmo antes de refinamentos editoriais.

---

## 14. Proposal 07 — `review-public-site-ui-ux-round-1`

### Objetivo

Realizar uma revisão crítica e estruturada de UI/UX do site público já implementado, produzindo um backlog de correções priorizadas.

### O que esta review deve cobrir

1. hierarquia visual;
2. densidade de informação;
3. clareza dos CTAs;
4. consistência entre Home e páginas internas;
5. responsividade;
6. legibilidade;
7. arquitetura da informação percebida;
8. problemas de redundância, ruído e desalinhamento editorial/visual;
9. aderência às boas práticas de design web.

### Itens explicitamente já identificados e que devem ser verificados

#### Home

1. exibir **Latest news** na Home;
2. reavaliar se o card “Híbrido” deve ser removido ou substituído;
3. exibir o **endereço completo** do local;
4. incluir mapa/integração coerente do local do evento;
5. reescrever o copy exagerado (“fronteira do conhecimento”, “maior evento da América Latina” etc.) em tom mais humilde e fiel ao projeto;
6. corrigir ícones ou labels inconsistentes de data;
7. revisar o texto “O que esperar?” para ficar coerente com a programação real;
8. garantir que não haja menção indevida a workshops;
9. revisar o grid de “Entidades parceiras” para melhor distribuição visual (ex.: 3 por linha/coluna conforme layout final);
10. revisar rodapé: logo FAPEMIG, menção textual, uso de ícone do Instagram, simplificação de texto redundante.

#### Sobre

1. ampliar e qualificar o texto da página;
2. remover ou repensar redundância entre “O que esperar” na Home e no Sobre;
3. melhorar escala tipográfica de títulos de seção;
4. renomear “Local e acessibilidade” para “Local e acesso” se isso fizer mais sentido editorial e visualmente;
5. exibir mapa lado a lado com endereço;
6. corrigir localização herdada da edição anterior;
7. reduzir impacto visual das fotos da equipe;
8. aplicar tratamento/máscara mais adequada nas imagens da comissão organizadora;
9. revisar redundância entre “Instituições parceiras” e “Entidades parceiras”.

### Saída esperada

- relatório estruturado de UI/UX;
- backlog priorizado de ajustes;
- decisões de manter/remover/consolidar seções.

---

## 15. Proposal 08 — `produce-public-site-content-round-1`

### Objetivo

Produzir, revisar e expandir o conteúdo editorial do site público com base no tom, posicionamento e fatos canônicos do CBNV 2026.

### Escopo

1. reescrever hero copy e microcopy da Home;
2. produzir texto robusto para a página Sobre;
3. revisar cards e destaques da Home;
4. revisar textos de Programação, Submissões, Inscrição e Patrocínio;
5. revisar textos do rodapé, redes e menções institucionais;
6. produzir copy consistente para seções de local, acesso, entidades apoiadoras e notícias.

### Regras editoriais

1. evitar exagero promocional;
2. adotar tom institucional, claro, científico e sóbrio;
3. alinhar texto com o termo do projeto e a programação oficial;
4. separar claramente conteúdo confirmado de conteúdo pendente;
5. evitar redundância entre páginas.

### Entregáveis

- copy revisada para as páginas públicas principais;
- guidelines editoriais curtas para manutenção do tom do site;
- lista de conteúdos pendentes que dependem de confirmação externa.

---

## 16. Proposal 09 — `verify-cross-page-content-consistency`

### Objetivo

Criar um mecanismo estruturado de verificação de consistência entre conteúdos, labels, dados do evento e elementos repetidos em múltiplas páginas.

### Por que esta proposal é necessária

Ao longo da implementação do site, surgiram sinais de inconsistência como:

1. repetição de blocos semelhantes com conteúdo divergente;
2. slogans exagerados ou conflitantes;
3. local e mapas herdados da edição anterior;
4. cards e seções redundantes;
5. textos de expectativa desalinhados com a programação real;
6. inconsistências de footer e entidades parceiras.

### Escopo

A proposal deve verificar, pelo menos:

1. nome do evento e edição;
2. tema;
3. datas e período;
4. local e endereço;
5. links de mapa;
6. CTAs principais;
7. textos da Home e do Sobre;
8. nomes de seções repetidas;
9. entidades parceiras/apoiadoras;
10. menção à FAPEMIG;
11. dados de programação vs texto descritivo;
12. status de palestrantes/participantes pendentes;
13. footer, redes e branding institucional;
14. consistência entre labels visuais e conteúdo real (ex.: ícones de calendário, formatos, modalidade híbrida etc.).

### Entregáveis

1. checklist de consistência reutilizável;
2. relatório de inconsistências encontradas;
3. backlog de correções por severidade;
4. possíveis regras ou testes editoriais básicos para prevenir regressão.

### Critérios de aceite

1. existe um processo claro de verificação editorial;
2. as inconsistências críticas são encontradas antes de staging/produção;
3. Home, Sobre, Programação e Footer deixam de divergir entre si.

---

## 17. Proposal 10 — `implement-public-site-polish-round-1`

### Objetivo

Aplicar o backlog de ajustes gerado pelas reviews de UI/UX, conteúdo e consistência.

### Escopo

1. ajustes de layout e espaçamento;
2. atualização de cards e grids;
3. ajustes tipográficos;
4. refino da Home;
5. refino da página Sobre;
6. footer final round 1;
7. mapa e local do evento;
8. entidades parceiras/apoiadoras;
9. ícones e elementos visuais (Instagram, FAPEMIG etc.);
10. eliminação de blocos redundantes.

### Critérios de aceite

1. backlog crítico da revisão round 1 foi endereçado;
2. a percepção de consistência entre as páginas melhorou;
3. a Home e o Sobre estão editorialmente mais maduros.

---

## 18. Proposal 11 — `add-accounts-profiles-and-dashboards`

### Objetivo

Implementar autenticação e áreas-base internas sem reabrir a fundação técnica.

### Escopo

1. UserProfile;
2. login/logout/recuperação básica;
3. dashboard do autor;
4. dashboard do revisor;
5. dashboard da comissão/chair;
6. layout interno base.

### Observação

Usar User padrão do Django + UserProfile. Não reintroduzir um custom user model sem necessidade forte.

---

## 19. Proposal 12 — `add-author-submission-initial-flow`

### Objetivo

Implementar a fase 1 do fluxo bifásico de submissão.

### Escopo

1. cadastro/autenticação do autor;
2. criação de submissão;
3. metadados;
4. autores e afiliações;
5. resumo;
6. palavras-chave;
7. eixo temático;
8. upload de PDF inicial;
9. aceite das regras;
10. dashboard de acompanhamento.

### Critério essencial

**Não exigir vídeo na submissão inicial.**

---

## 20. Proposal 13 — `add-review-decision-workflow`

### Objetivo

Implementar distribuição, revisão, parecer e decisão dos trabalhos.

### Escopo

1. triagem administrativa;
2. distribuição de revisores;
3. declarações de conflito;
4. formulários de parecer;
5. consolidação de revisões;
6. decisão: aceito, aceito com ressalvas, rejeitado;
7. modalidade final: oral, pôster, vídeo.

---

## 21. Proposal 14 — `add-final-materials-proceedings-videos`

### Objetivo

Implementar fase final para trabalhos aprovados, anais e links de vídeo.

### Escopo

1. PDF final;
2. pôster final, se aplicável;
3. link de vídeo, se aplicável;
4. autorização de publicação;
5. exportação/organização para anais;
6. publicação de links de vídeo/playlist do YouTube.

---

## 22. Proposal 15 — `add-reports-exports-and-indicators`

### Objetivo

Disponibilizar exportações e indicadores necessários ao relatório técnico-científico e à gestão do congresso.

### Escopo

1. exportação de submissões;
2. exportação de autores e instituições;
3. indicadores por eixo, modalidade e status;
4. dados para anais e relatório técnico;
5. contagens e métricas administrativas relevantes.

---

## 23. Proposal 16 — `harden-deployment-security-and-backups`

### Objetivo

Levar a solução a um patamar seguro de produção e operação.

### Escopo

1. secrets e settings de produção;
2. HTTPS/proxy reverso;
3. storage e arquivos protegidos;
4. backups;
5. e-mail transacional;
6. observabilidade/logging;
7. hardening de autenticação;
8. proteção operacional mínima.

---

## 24. Proposal 17 — `complete-accessibility-performance-and-qa`

### Objetivo

Fechar a fase com revisão abrangente de qualidade.

### Escopo

1. auditoria de acessibilidade;
2. performance front-end e assets;
3. testes de regressão;
4. revisão final de responsividade;
5. revisão final editorial básica;
6. readiness para staging/produção.

---

## 25. Backlog editorial/UI já identificado

Esta seção serve como backlog imediato derivado da revisão humana do site atual.

### 25.1 Home — itens de trabalho

1. inserir notícias/avisos recentes em local mais útil da Home;
2. avaliar remoção ou substituição do card “Híbrido”;
3. exibir endereço completo do local do evento;
4. integrar mapa correto do CAD-1/UFMG;
5. revisar e tornar mais humilde o texto de abertura;
6. revisar claims promocionais excessivos;
7. corrigir ícones e sinais visuais inconsistentes com a data real do evento;
8. revisar o bloco “O que esperar?” para refletir a programação real;
9. remover referência a workshops se não existirem;
10. ajustar layout das entidades parceiras;
11. inserir referência visual adequada à FAPEMIG no footer;
12. substituir texto “Instagram” por ícone, conforme decisão visual final;
13. simplificar o footer para reduzir redundância.

### 25.2 Sobre — itens de trabalho

1. expandir e qualificar o conteúdo textual;
2. resolver a redundância do bloco “O que esperar”;
3. melhorar hierarquia tipográfica dos títulos de seção;
4. renomear e redesenhar o bloco de local/acesso conforme decisão editorial;
5. corrigir local e mapa herdados incorretamente;
6. melhorar exibição da comissão organizadora;
7. reduzir visualmente ruído de fotos com fundos ruins;
8. eliminar redundância entre blocos de entidades parceiras.

### 25.3 Backlog editorial transversal

1. alinhar o tom do site ao projeto e à escala real do evento;
2. revisar slogans, chamadas e microcopy;
3. padronizar nomes de seções;
4. padronizar linguagem de inscrições, submissões, participação e programação;
5. garantir consistência entre Home, Sobre e Programação;
6. separar o que é confirmado do que é pendente.

---

## 26. Prompt atualizado de init/contexto para OpenSpec

```text
Inicialize ou atualize o contexto OpenSpec deste repositório para o projeto “XII CBNV 2026 — Website e plataforma digital do Congresso Brasileiro de Neurociências da Visão”.

Antes de qualquer implementação, leia integralmente:
- docs/CBNV2026_Requisitos_Arquitetura_v1(2).md
- docs/CBNV2026_OpenSpec_Plano_Implementacao_v2.md
- docs/design/stitch_cbnv_2026_digital_platform/neurovision_ai/DESIGN.md

Trate `docs/CBNV2026_Requisitos_Arquitetura_v1(2).md` como single source of truth funcional.
Trate `docs/CBNV2026_OpenSpec_Plano_Implementacao_v2.md` como working plan / backlog oficial da fase atual.
Trate o material do Stitch apenas como referência visual.

Atualize `openspec/project.md` ou `openspec/config.yaml` com o seguinte contexto:
- stack: Django + Wagtail + PostgreSQL + Tailwind CSS + HTMX/Alpine.js;
- baseline técnico atual: Python 3.14.x, Django 6.0.x, Wagtail 7.4.x LTS, PostgreSQL 18.3, Tailwind 4.x;
- arquitetura: monólito modular Django;
- autenticação: Django default User + UserProfile;
- conteúdos: em português brasileiro, tom institucional/científico/sóbrio;
- princípios: simplicidade, segurança, acessibilidade, responsividade, consistência editorial e mínima reescrita;
- fora de escopo: pagamento próprio, certificados próprios, QR code próprio, hospedagem de vídeos completos, Next.js, Strapi e RBAC editorial complexo.

Não implemente nada ainda.
Apenas alinhe o contexto OpenSpec e indique quais arquivos precisam ser atualizados para refletir o plano v2.
```

---

## 27. Regra prática para priorização

Se houver dúvida entre duas proposals concorrentes, seguir estas regras:

1. primeiro resolver **drift estrutural**;
2. depois resolver **reutilização de componentes**;
3. depois resolver **modelagem de conteúdo**;
4. depois resolver **conteúdo e consistência**;
5. só então ampliar fluxos científicos mais complexos.

Em outras palavras: **não corrigir copy dispersa em templates antes que a base de CMS, layout e conteúdo canônico exista**.

---

## 28. Definition of Done desta fase pública inicial

A fase pública inicial pode ser considerada madura quando:

1. a fundação técnica estiver estabilizada;
2. as páginas públicas principais estiverem implementadas;
3. houver uma rodada formal de UI/UX review;
4. houver uma rodada formal de produção/revisão de conteúdo;
5. a proposal de consistência entre conteúdos estiver concluída;
6. o backlog crítico dessa revisão tiver sido aplicado;
7. o site estiver pronto para servir como base estável antes da expansão dos fluxos científicos autenticados.

---

## 29. Próximo passo imediato

O próximo passo recomendado é:

1. concluir e registrar formalmente a proposal **`stabilize-platform-foundation`**;
2. atualizar o arquivo `docs/CBNV2026_OpenSpec_Plano_Implementacao_v2.md` no repositório;
3. validar o backlog v2 com o repositório real;
4. iniciar a proposal **`add-design-system-and-layout-shells`**;
5. em seguida avançar para **`add-core-cms-content-models`** e **`seed-canonical-event-content`**.

