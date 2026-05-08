## 1. Modelagem e Snippets do App Program

- [x] 1.1 Criar modelos `Speaker`, `ProgramDay`, `ProgramSession` e `ProgramTalk` em `program/models.py`
- [x] 1.2 Implementar escolhas para `ActivityType`, `Format` e `SpeakerStatus`
- [x] 1.3 Registrar todos como Snippets do Wagtail com panels apropriados
- [x] 1.4 Gerar e aplicar migrations: `uv run python manage.py makemigrations program && uv run python manage.py migrate`

## 2. Página Wagtail ProgramPage

- [x] 2.1 Criar `ProgramPage` em `pages/models.py` (herda de Page, sem subpáginas)
- [x] 2.2 Adicionar `ProgramPage` como child permitida de `HomePage`
- [x] 2.3 Implementar `get_context` para retornar dias, sessões e talks confirmados
- [x] 2.4 Gerar e aplicar migrations para o app `pages`

## 3. Templates

- [x] 3.1 Criar `templates/pages/program_page.html` usando o componente `timeline.html` existente
- [x] 3.2 Garantir responsividade e acessibilidade (headings, labels, foco)
- [x] 3.3 Validar renderização com dados de fixture no dev server

## 4. Fixtures e Seed

- [x] 4.1 Criar management command `seed_program` que carrega a programação preliminar canônica (3 dias, ~30 sessões)
- [x] 4.2 Incluir palestrantes confirmados: Hugo Bastos de Paula, Jerome Baron, Carla Stangherlim Neves
- [x] 4.3 Executar o seed: `uv run python manage.py seed_program`
- [x] 4.4 Validar que apenas items `confirmed` aparecem no frontend

## 5. Validação e Finalização

- [x] 5.1 Adicionar testes para visibilidade: itens `pending`/`hidden` não aparecem no context da ProgramPage
- [x] 5.2 Verificar renderização correta dos tipos de atividade (badges)
- [x] 5.3 Executar `uv run python manage.py check`, `uv run pytest` e `openspec validate add-program-speakers-and-fixtures --strict`
