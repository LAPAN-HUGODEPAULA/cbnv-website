## Why

O projeto XII CBNV 2026 possui uma fundação técnica (Django/Wagtail/Docker), mas carece de uma identidade visual consistente e componentes reutilizáveis. Sem um Design System e shells de layout (header, footer, dashboards), as próximas fases de implementação (páginas públicas e fluxos de submissão) resultariam em código duplicado, inconsistência visual e retrabalho de interface. Esta change traduz a referência do Stitch para tokens e componentes Tailwind/Django.

## What Changes

- Definir tokens de design (cores, tipografia, espaçamento) no `tailwind.config.js` baseados na estética do Stitch.
- Criar templates base e shells de layout reutilizáveis:
    - `base.html`: Estrutura HTML5 com recursos de acessibilidade.
    - `base_public.html`: Layout para o site público (com header/footer).
    - `base_dashboard.html`: Layout para áreas autenticadas (sidebar/topbar).
- Desenvolver biblioteca de componentes Django (partials/includes) reutilizáveis:
    - Header responsivo com menu mobile.
    - Footer institucional com menção obrigatória à FAPEMIG.
    - Botões, Badges de status e Inputs de formulário acessíveis.
    - Cards científicos e Timeline para programação.
    - Empty, Loading e Error states.
- Implementar utilitários de acessibilidade (skip links, focus visible).

## Capabilities

### New Capabilities
- `design-system`: Tokens de design, biblioteca de componentes reutilizáveis, padrões de acessibilidade e shells de layout (Public/Dashboard).

### Modified Capabilities
- `public-site`: Define os requisitos para os shells de layout e componentes das páginas públicas.
- `accounts-auth`: Define os requisitos para o shell de layout do dashboard e componentes de formulário de perfil.
- `developer-experience`: Define os requisitos para a organização dos templates base e partials para facilitar o desenvolvimento.

## Impact

- **Frontend**: `tailwind.config.js` será atualizado com a paleta oficial; novos arquivos de template em `templates/`.
- **Arquitetura**: Estabelece o padrão de "Includes/Partials" para componentes reutilizáveis.
- **Acessibilidade**: Introduz padrões globais de navegação por teclado e semântica HTML.
- **Desenvolvimento**: Reduz o esforço de criação de novas páginas ao fornecer shells prontos.
