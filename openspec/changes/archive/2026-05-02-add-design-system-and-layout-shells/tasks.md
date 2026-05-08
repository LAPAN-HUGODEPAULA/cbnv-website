## 1. Tokens e Configuração

- [x] 1.1 Atualizar `src/input.css` para Tailwind CSS `4.2.4` CSS-first com `@import "tailwindcss";`, `@source` para templates Django e tokens `@theme` (sem criar `tailwind.config.js` por padrão).
- [x] 1.2 Definir tokens de fontes em `src/input.css` (Newsreader/Inter/Space Grotesk ou equivalentes) e carregar fontes oficiais no template base.
- [x] 1.3 Validar build do Tailwind e verificar se as novas classes utilitárias estão disponíveis.

## 2. Estrutura de Templates Base

- [x] 2.1 Criar `templates/base.html` com suporte a skip links, blocos meta e carregamento de assets.
- [x] 2.2 Criar `templates/layouts/public.html` que herda de `base.html`.
- [x] 2.3 Criar `templates/layouts/dashboard.html` que herda de `base.html`.

## 3. Biblioteca de Componentes (Partials)

- [x] 3.1 Criar `templates/components/header.html` responsivo (com menu mobile em Alpine.js).
- [x] 3.2 Criar `templates/components/footer.html` com menção obrigatória à FAPEMIG.
- [x] 3.3 Criar `templates/components/button.html` com suporte a variantes (primary, secondary, outline).
- [x] 3.4 Criar `templates/components/card.html` para contexto científico.
- [x] 3.5 Criar `templates/components/badge.html` para status.
- [x] 3.6 Criar `templates/components/input.html` acessível (com label associado e focus visible).
- [x] 3.7 Criar `templates/components/timeline.html` para exibição de programação.

## 4. Estados de Interface

- [x] 4.1 Criar `templates/components/states/loading.html`.
- [x] 4.2 Criar `templates/components/states/empty.html`.
- [x] 4.3 Criar `templates/components/states/error.html`.

## 5. Validação e Documentação

- [x] 5.1 Criar uma view temporária `DesignSystemView` em `core/views.py` para visualizar todos os componentes.
- [x] 5.2 Mapear a URL da DesignSystemView no `cbnv/urls.py`.
- [x] 5.3 Testar navegação por teclado e contraste (WCAG 2.2 AA).
- [x] 5.4 Criar `docs/design/DESIGN_SYSTEM_GUIDE.md` (conforme especificado na spec de developer-experience).
- [x] 5.5 Validar a change com `openspec validate add-design-system-and-layout-shells --strict`.
