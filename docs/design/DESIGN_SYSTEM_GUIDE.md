# Design System Guide — CBNV 2026

## Visão Geral

O design system do CBNV 2026 é baseado em tokens Tailwind CSS 4 (CSS-first) definidos em `src/input.css`. Todos os componentes são partials Django em `templates/components/`.

## Tokens

### Cores

| Token | Hex | Uso |
|---|---|---|
| `cbnv-navy-950` | `#081426` | Background principal (dark mode) |
| `cbnv-navy-900` | `#0E1E3A` | Superfícies escuras |
| `cbnv-blue-600` | `#214BFF` | CTAs, links, foco |
| `cbnv-green-400` | `#2FEA8B` | Acentos, status de sucesso |
| `cbnv-text-light` | `#E7ECF7` | Texto sobre fundo escuro |
| `cbnv-text-muted` | `#9AA8C7` | Texto secundário |
| `cbnv-text-dark` | `#111827` | Texto sobre fundo claro |

### Tipografia

| Token | Fonte | Uso |
|---|---|---|
| `font-display` | Newsreader (serif) | Títulos, hero |
| `font-body` | Inter (sans) | Corpo, interface |
| `font-mono` | Space Grotesk (monospace) | Horários, código |

## Estrutura de Templates

```
templates/
├── base.html              # HTML5 global, skip link, fonts, Alpine.js
├── layouts/
│   ├── public.html        # Site público (header + footer)
│   └── dashboard.html     # Área autenticada (sidebar + topbar)
├── components/
│   ├── header.html        # Navegação responsiva com Alpine.js
│   ├── footer.html        # Rodapé com menção FAPEMIG
│   ├── button.html        # Variantes: primary, secondary, outline, ghost
│   ├── card.html          # Card científico (suporta `dark` variant)
│   ├── badge.html         # Variantes: confirmed, pending, rejected, info, draft, review
│   ├── input.html         # Input, textarea, select (acessível)
│   ├── timeline.html      # Programação por timeline vertical
│   └── states/
│       ├── loading.html   # Spinner com mensagem
│       ├── empty.html     # Vazio com CTA opcional
│       └── error.html     # Erro com detalhe e CTA opcional
```

## Uso dos Componentes

### Button

```django
{# Link #}
{% include "components/button.html" with label="Saiba mais" variant="outline" href="/sobre" %}

{# Botão #}
{% include "components/button.html" with label="Enviar" variant="primary" size="lg" tag="button" %}
```

Variantes: `primary`, `secondary`, `outline`, `ghost`. Tamanhos: `sm`, padrão, `lg`.

### Card

```django
{% include "components/card.html" with title="Título" body="Descrição" meta="Categoria" cta_label="Ver mais" cta_href="/link" %}
```

### Badge

```django
{% include "components/badge.html" with label="Confirmado" variant="confirmed" %}
```

### Input

```django
{% include "components/input.html" with id="email" label="E-mail" type="email" required="true" help_text="Texto auxiliar." %}
```

Suporta `tag="textarea"` e `tag="select"` (com `choices`).

### Timeline

```django
{% include "components/timeline.html" with title="Programação" items=timeline_items %}
```

Cada item: `time`, `title`, `description`, `speaker`, `badge` (dict com `label` e `variant`).

## Acessibilidade

- Skip link em `base.html` (pula para `#main-content`)
- Focus visible ring em `:focus-visible` (2px azul)
- `prefers-reduced-motion` respeitado (desativa animações)
- Labels associados em todos os inputs
- Contraste WCAG 2.2 AA nos tokens de cor

## Preview

Acesse `/design-system/` para visualizar todos os componentes.
