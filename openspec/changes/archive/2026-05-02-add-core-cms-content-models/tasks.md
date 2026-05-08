## 1. Configurações e Snippets por Domínio

- [x] 1.1 Implementar `CoreSettings` em `core/models.py` usando `BaseSiteSetting`.
- [x] 1.2 Implementar snippet `Sponsor` em `sponsors/models.py`.
- [x] 1.3 Implementar snippet `VideoResource` em `videos/models.py` com validação de URL do YouTube e extração de `youtube_video_id` e/ou `youtube_playlist_id`.
- [x] 1.4 Implementar snippet `Edition` em `proceedings/models.py` para acervo histórico.
- [x] 1.5 Registrar snippets no Wagtail Admin nos seus apps de domínio.
- [x] 1.6 Configurar `WAGTAILADMIN_BASE_URL` via ambiente com default local.

## 2. Modelos de Página (App `pages`)

- [x] 2.1 Implementar `HomePage` em `pages/models.py`.
- [x] 2.2 Implementar `AboutPage` em `pages/models.py`.
- [x] 2.3 Implementar `NewsIndexPage` e `NewsArticlePage` em `pages/models.py`.
- [x] 2.4 Implementar `PreviousEditionsPage` em `pages/models.py`.
- [x] 2.5 Gerar e aplicar as migrações: `uv run python manage.py makemigrations && uv run python manage.py migrate`.

## 3. Integração e Templates

- [x] 3.1 Atualizar `templates/layouts/public.html` para ler metadados do `CoreSettings`.
- [x] 3.2 Criar diretórios de templates em `pages/templates/pages/` para cada modelo de página.
- [x] 3.3 Adicionar lógica básica de renderização (placeholders) que consomem os novos modelos.
- [x] 3.4 Validar que o admin único consegue criar e publicar páginas sem erros de permissão.

## 4. Dados Iniciais e Validação

- [x] 4.1 Criar script de `seed` ou fixture `initial_cms_data.json` com estrutura básica (Settings, Home).
- [x] 4.2 Incluir no seed referência inicial ao canal/acervo YouTube da 11ª edição: `https://www.youtube.com/@congressoneurovis%C3%A3o`.
- [x] 4.3 Executar o seed: `uv run python manage.py loaddata initial_cms_data.json`.
- [x] 4.4 Validar que o endpoint `/admin/` reflete os novos modelos e snippets.
- [x] 4.5 Adicionar testes para validação/extração de URLs do YouTube (vídeo, playlist e canal).
- [x] 4.6 Executar `uv run python manage.py check`, `uv run pytest` e `openspec validate add-core-cms-content-models --strict`.
