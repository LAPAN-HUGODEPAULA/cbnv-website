## Context

O XII CBNV 2026 exige uma interface moderna, científica e acessível (WCAG 2.2 AA). O design de referência foi criado no Stitch, utilizando uma estética dark-mode first com tons de azul profundo e detalhes em verde neon. Esta fase do projeto traduz essa referência visual em uma estrutura técnica reutilizável dentro do Django, garantindo que as próximas entregas (Páginas Públicas e Submissões) herdem automaticamente a identidade visual e os padrões de acessibilidade.

## Goals / Non-Goals

**Goals:**

- Traduzir os tokens de cor e tipografia do Stitch para `src/input.css` usando `@theme` do Tailwind CSS `4.2.4`.
- Criar uma estrutura de templates baseada em herança (`base.html` -> layouts -> páginas).
- Desenvolver uma biblioteca de componentes "dry" (includes) para elementos recorrentes.
- Garantir que todos os componentes base sejam navegáveis por teclado e possuam contraste adequado.
- Implementar o shell do site público e o shell do dashboard científico.

**Non-Goals:**

- Implementar dados reais vindos do banco (as telas iniciais usarão placeholders).
- Criar a lógica de submissão de trabalhos (foco apenas no formulário visual).
- Finalizar o conteúdo editorial do CMS (Wagtail).
- Implementar micro-interações complexas (foco no layout e estrutura).

## Decisions

### D1: Estrutura de Templates e Herança

**Decisão:** Utilizar herança tripla:
1. `templates/base.html`: Estrutura HTML5 global, carregamento de CSS/JS, tags meta, skip links.
2. `templates/layouts/public.html`: Estende base, inclui Header e Footer.
3. `templates/layouts/dashboard.html`: Estende base, inclui Sidebar e Topbar.

**Alternativa considerada:** Arquivo único por página — rejeitado por causar duplicação massiva de código.

**Racional:** Permite que mudanças globais (como adicionar um script de analytics) sejam feitas em um só lugar, enquanto a estrutura visual de "site" vs "sistema" permanece isolada.

### D2: Componentização via Django Includes

**Decisão:** Criar diretório `templates/components/` contendo arquivos `.html` individuais para componentes (ex: `scientific_card.html`). Passagem de dados via argumentos do `{% include %}`.

**Alternativa considerada:** Django Components (biblioteca externa) — rejeitado para manter o projeto o mais "vanilla" e idiomatizado possível no início.

**Racional:** Mantém a simplicidade técnica, facilita a manutenção por agentes de IA e desenvolvedores, e não adiciona dependências extras de terceiros.

### D3: Tailwind CSS 4.2.4 CSS-first para Tokens

**Decisão:** Definir a paleta oficial em `src/input.css` usando a configuração CSS-first do Tailwind CSS `4.2.4`, com `@import "tailwindcss";`, `@source` explícito para templates Django e `@theme` para tokens semânticos (`cbnv-navy-950`, `cbnv-blue-600`, `cbnv-green-400`, `font-display`, etc.). Não criar `tailwind.config.js` por padrão.

**Alternativa considerada:** `tailwind.config.js` com `content` paths — rejeitado por ser o padrão antigo do Tailwind v3 e desnecessário no Tailwind `4.2.4`, que favorece configuração CSS-first.

**Racional:** Mantém o projeto alinhado com a direção atual do Tailwind 4, reduz arquivos de configuração e concentra tokens, fontes, fontes de scan e utilitários de projeto no ponto de entrada CSS usado pelo build.

### D4: Alpine.js para Interações Leves

**Decisão:** Usar Alpine.js apenas para o menu mobile (dropdown/hambúrguer) e alertas dispensáveis.

**Alternativa considerada:** HTMX para menu mobile — rejeitado pois HTMX é focado em requisições servidor; interações puramente de UI (abrir/fechar) são mais rápidas e simples com Alpine.

## Risks / Trade-offs

- **[Contraste em Dark Mode]** → Mitigação: Validar as cores do Stitch contra WCAG 2.2 AA e ajustar tons de texto secundário se necessário.
- **[Performance de CSS]** → Mitigação: O build do Tailwind 4 realiza detecção de classes; declarar `@source "../templates";` e `@source "../**/templates";` em `src/input.css` para garantir que templates Django sejam escaneados de forma explícita.
- **[Complexidade de Sidebar Mobile]** → Mitigação: Usar padrões simples de drawer e garantir que o foco seja "trap" quando o menu estiver aberto.

## Migration Plan

1. Atualizar `src/input.css` com `@import "tailwindcss";`, `@source` para templates Django e tokens `@theme`.
2. Criar `templates/base.html`.
3. Criar `templates/layouts/public.html` e `templates/layouts/dashboard.html`.
4. Criar partials em `templates/components/`.
5. Criar uma `DesignSystemView` (demo page) para validar visualmente todos os componentes em uma única página.
6. Validar acessibilidade com ferramentas de auditoria (Lighthouse/Axe).

## Open Questions

1. O layout de Dashboard deve ser "full width" ou possuir um container centralizado? (Decisão: Container centralizado `max-w-7xl` para melhor legibilidade em monitores ultra-wide).
2. Como lidar com imagens de placeholder? (Decisão: Usar gradientes e formas geométricas baseadas nos tokens do Design System para manter a estética do projeto sem depender de assets externos).
