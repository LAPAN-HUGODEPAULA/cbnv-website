## Context

O projeto XII CBNV 2026 utiliza o Wagtail CMS para gerenciar conteúdo dinâmico. Após o bootstrap da plataforma, é necessário definir a estrutura de dados que permitirá ao administrador gerenciar o site institucional. O foco desta fase é a modelagem editorial e a configuração inicial do fluxo de trabalho administrativo.

## Goals / Non-Goals

**Goals:**

- Implementar `SiteSettings` para centralizar metadados globais e links externos (inscrição, transmissão).
- Definir modelos de página para Home, Sobre, Notícias e Edições Anteriores.
- Criar Snippets nos apps de domínio para Sponsors, Vídeos e Edições Anteriores.
- Garantir que vídeos sejam integrados apenas via links do YouTube.
- Configurar o admin do Wagtail para um único usuário administrador (sem RBAC complexo).

**Non-Goals:**

- Implementar os modelos de Programação (Sessions/Talks) - será feito na Proposal 04.
- Implementar os modelos de Submissão e Revisão.
- Criar o design final das páginas (foco em modelos e placeholders).

## Decisions

### D1: SiteSettings para Metadados Globais

**Decisão:** Utilizar o módulo `wagtail.contrib.settings` para criar a entidade `CoreSettings`.

**Racional:** Permite que campos como "Link de Inscrição" ou "E-mail de Contato" sejam editados em um único lugar e acessados globalmente em qualquer template via `{{ settings.core.CoreSettings.registration_link }}`.

### D2: Snippets vs Pages para Entidades Reutilizáveis

**Decisão:**
- **CoreSettings**: `core.models` (configurações globais do site).
- **Sponsors**: `sponsors.models.Sponsor` como Snippet (permite reutilização em várias páginas).
- **VideoResource**: `videos.models.VideoResource` como Snippet (permite associar a sessões futuras ou páginas de acervo).
- **Edition**: `proceedings.models.Edition` como Snippet (metadados de edições passadas e links de anais/acervo).
- **Notícias**: `pages.models` como Pages (`NewsIndexPage` e `NewsArticlePage`) para aproveitar o sistema de busca, slugs e hierarquia nativa do Wagtail.

**Racional:** Snippets são ideais para dados "globais" ou "atômicos" que não possuem uma URL própria complexa ou hierárquica, enquanto Pages são ideais para conteúdo que compõe a árvore do site. Manter snippets nos apps de domínio evita que `core` vire um catch-all e preserva os limites modulares já definidos na arquitetura.

### D3: Integração de Vídeo via YouTube

**Decisão:** O modelo `VideoResource` conterá um campo `youtube_url` e suportará URLs de vídeo, playlist e canal do YouTube. No método `clean()` ou `save()`, o sistema validará a URL e extrairá `youtube_video_id` e/ou `youtube_playlist_id` quando aplicável. O canal oficial/acervo da 11ª edição deve ser registrado como referência inicial: `https://www.youtube.com/@congressoneurovis%C3%A3o`.

**Alternativa considerada:** Upload de arquivos de vídeo — rejeitado por custos de armazenamento, largura de banda e complexidade de transcodificação.

### D4: Interface Administrativa Simplificada

**Decisão:** Ocultar recursos de "Workflows" e "Moderation" do Wagtail, já que o projeto terá apenas um administrador editorial no MVP.

### D5: URL Base do Admin Wagtail

**Decisão:** Configurar `WAGTAILADMIN_BASE_URL` por variável de ambiente, com default local, para eliminar o aviso do `manage.py check` e preparar links absolutos em notificações/admin.

## Risks / Trade-offs

- **[Migração de Dados]** → Mitigação: Criar fixtures iniciais para o `HomePage` e `SiteSettings` para que o projeto inicie com dados básicos configurados.
- **[Broken Links]** → Mitigação: Implementar validação simples nos campos de URL (especialmente YouTube).

## Migration Plan

1. Criar `CoreSettings` em `core`, snippets nos apps `sponsors`, `videos` e `proceedings`, e modelos de página em `pages`.
2. Executar `uv run python manage.py makemigrations` e `uv run python manage.py migrate`.
3. Criar scripts de `seed` ou fixtures para a estrutura de páginas inicial.
4. Atualizar os templates base para ler dados do `SiteSettings`.
5. Registrar os Snippets no Wagtail Admin.

## Open Questions

1. Onde deve ficar o link de "Inscrição" se ele não estiver no SiteSettings? (Decisão: Manter no SiteSettings como fonte primária para o site todo).
2. Como lidar com "Edições Anteriores" que possuem anais em PDF? (Decisão: Inicialmente, apenas links externos para os PDFs dos anais hospedados em outros lugares ou edições anteriores).
