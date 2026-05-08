## Why

A plataforma digital do XII CBNV 2026 precisa de uma infraestrutura editorial para que o administrador possa gerenciar o conteúdo institucional, notícias, patrocinadores e materiais de edições anteriores sem a necessidade de intervenção técnica no código. Esta change implementa a base do CMS Wagtail, incluindo configurações globais do site e os modelos de conteúdo primários.

## What Changes

- Implementar `SiteSettings` no Wagtail para gerenciar metadados globais (nome do evento, tema, redes sociais, links externos de inscrição e transmissão).
- Criar modelos de página estruturados no Wagtail (`HomePage`, `AboutPage`, `NewsIndexPage`, `NewsArticlePage`, `PreviousEditionsPage`).
- Implementar Snippets para entidades reutilizáveis:
    - `Sponsor`: Gerenciamento de logotipos e links de patrocinadores.
    - `Edition`: Registro de edições passadas do congresso.
    - `VideoResource`: Gerenciamento de links para vídeos e playlists do YouTube (sem hospedagem local).
- Configurar o painel administrativo do Wagtail para um fluxo de trabalho de administrador único, simplificando a interface.
- Criar fixtures básicas e páginas placeholder para validar a renderização do conteúdo vindo do CMS.

## Capabilities

### New Capabilities
- `content-cms`: Modelos editoriais centrais, configurações de site e lógica de publicação do Wagtail.
- `videos`: Requisitos para integração e exibição de conteúdos audiovisuais via YouTube.
- `sponsors`: Requisitos para gestão e exibição de patrocinadores e apoiadores.
- `proceedings`: Gestão de acervo histórico e edições anteriores (inicialmente apenas metadados e links).

### Modified Capabilities
- `public-site`: Adiciona requisitos para que as páginas públicas consumam conteúdo dinâmico do CMS em vez de placeholders estáticos.

## Impact

- **CMS**: O `/admin/` do Wagtail passará a exibir novas seções para Notícias, Patrocinadores, Vídeos e Configurações.
- **Banco de Dados**: Novas tabelas para as entidades editoriais mencionadas.
- **Desenvolvimento**: As próximas fases (`add-program-speakers`) dependerão desta estrutura para associar palestrantes a sessões e vídeos.
- **SEO**: Metadados globais passam a ser controlados via interface.
