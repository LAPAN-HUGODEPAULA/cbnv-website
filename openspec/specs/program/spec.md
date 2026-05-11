# Programação e Palestrantes (program)

## Purpose
Definir a estrutura de dados e regras de negócio para a gestão da programação científica e dos palestrantes do evento, garantindo integridade relacional, visibilidade pública segura e ordenação determinística.

## Requirements

### Requirement: Program data structure
O sistema SHALL implementar modelos para `ProgramDay` (datas do evento), `ProgramSession` (blocos de horários), `ProgramTalk` (atividades dentro de sessões) e `Speaker` (palestrantes e participantes). Todos SHALL ser Snippets do Wagtail.

#### Scenario: Relational integrity for talks
- **WHEN** uma `ProgramTalk` é criada
- **THEN** ela MUST estar vinculada a uma `ProgramSession` e MAY estar vinculada a um `Speaker`

#### Scenario: Admin manages program entities
- **WHEN** o administrador acessa o Wagtail
- **THEN** ele SHALL conseguir gerenciar dias, sessoes, falas e palestrantes sem alterar codigo

### Requirement: Speaker visibility control
O modelo `Speaker` SHALL possuir um campo de status (`confirmed`, `pending`, `hidden`).

#### Scenario: Hide non-confirmed items
- **GIVEN** um palestrante com status `pending` ou `hidden`
- **WHEN** a timeline pública, índice de palestrantes ou consulta pública de programação é renderizada
- **THEN** o sistema SHALL omitir inteiramente quaisquer talks/sessões não confirmadas — sem slots vazios

#### Scenario: Show confirmed speaker
- **GIVEN** um palestrante com status `confirmed`
- **WHEN** a timeline pública ou índice de palestrantes é renderizada
- **THEN** o sistema SHALL poder exibir os dados públicos configurados para esse palestrante

### Requirement: Public program query contract
O sistema SHALL fornecer um contrato de consulta para recuperar programação pública agrupada por dia, ordenada cronologicamente e filtrada por status público.

#### Scenario: Public program is chronologically grouped
- **GIVEN** existem dias, sessões e falas publicados
- **WHEN** a consulta pública de programação é executada
- **THEN** o resultado SHALL retornar os itens agrupados por data e ordenados por dia, horário de início e ordem configurada

#### Scenario: Draft program items are excluded
- **GIVEN** existe uma sessão com status de rascunho, pendente ou cancelado
- **WHEN** a consulta pública de programação é executada
- **THEN** essa sessão SHALL NOT ser retornada para exibição pública

### Requirement: Pending participant privacy
O sistema SHALL proteger nomes e detalhes de participantes não confirmados contra exibição pública involuntária.

#### Scenario: Pending speaker is not exposed publicly
- **GIVEN** uma fala está vinculada a um palestrante com status pendente ou oculto
- **WHEN** a consulta pública de palestrantes ou programação é executada
- **THEN** o nome, foto, instituição e biografia desse palestrante SHALL NOT ser retornados como conteúdo público

#### Scenario: Confirmed speaker can be listed
- **GIVEN** um palestrante possui status confirmado e está vinculado a atividade pública
- **WHEN** a consulta pública de palestrantes é executada
- **THEN** o palestrante SHALL ser retornado com nome público, instituição e dados permitidos para exibicao

### Requirement: Program venue reference
Sessões de programação SHALL suportar informação de sala, ambiente ou referência ao local oficial suficiente para a página pública orientar visitantes sem repetir endereço completo em texto ad hoc.

#### Scenario: Session has room information
- **GIVEN** uma sessão pública ocorre em uma sala específica do local oficial
- **WHEN** o admin cadastra a sessão
- **THEN** o sistema SHALL permitir salvar a sala ou ambiente da sessão junto dos demais dados da programação

#### Scenario: Public session can reference canonical venue
- **GIVEN** uma página pública renderiza uma sessão da programação
- **WHEN** a sessão precisa indicar localização
- **THEN** o sistema SHALL disponibilizar a sala da sessão e a fonte canônica do local do evento sem exigir endereço duplicado no template

### Requirement: Canonical activity types
O sistema SHALL suportar tipos de atividade predefinidos: recepção, mesa solene, conferência plenária, palestra, sessão temática, pôsteres, oral, mesa-redonda e intervalos.

#### Scenario: Visual styling by activity type
- **WHEN** uma sessão do tipo "Conferência Plenária" é renderizada na timeline
- **THEN** ela SHALL receber destaque visual diferenciado via badge do design system

### Requirement: Preliminary program fixtures
O sistema SHALL fornecer um management command idempotente que carregue a programação preliminar canônica para os dias do evento quando os dados oficiais estiverem disponíveis.

#### Scenario: Initial setup seeding
- **WHEN** o comando `uv run python manage.py seed_program` é executado
- **THEN** a estrutura completa de dias, sessões, talks e palestrantes confirmados SHALL ser carregada no banco

#### Scenario: Re-running program seed
- **GIVEN** a programação preliminar já foi carregada
- **WHEN** o comando `uv run python manage.py seed_program` é executado novamente
- **THEN** o sistema SHALL evitar duplicar dias, sessões, falas ou palestrantes existentes

### Requirement: Speaker Display and Indexing
Palestrantes SHALL ser exibidos inline na timeline (nome, instituição, bio) e também listados na `SpeakerIndexPage`.

#### Scenario: Speaker info in timeline
- **WHEN** um talk confirmado com palestrante é renderizado na timeline
- **THEN** SHALL exibir nome do palestrante e instituição como parte do item da timeline

#### Scenario: Speaker index display
- **WHEN** um visitante acessa a `SpeakerIndexPage`
- **THEN** SHALL ver a lista de todos os palestrantes confirmados com suas fotos e afiliações

### Requirement: Speaker Management Details
O sistema SHALL fornecer uma interface de gerenciamento para palestrantes do congresso, incluindo nome, biografia, foto e afiliação.

#### Scenario: Admin adds a speaker
- **WHEN** o administrador insere os detalhes do palestrante no CMS
- **THEN** o palestrante SHALL ser salvo e ficar disponível para ser vinculado a sessões da programação

### Requirement: Program Session Management
O sistema SHALL permitir a criação de sessões de programação com título, descrição, horário de início, horário de término e palestrantes vinculados.

#### Scenario: Admin creates a session
- **WHEN** o administrador define uma sessão com horário e palestrantes
- **THEN** a sessão SHALL ser armazenada e ficar pronta para exibição pública

### Requirement: Public Program Schedule
O sistema SHALL exibir a programação do congresso em uma lista estruturada e ordenada cronologicamente, acessível a todos os visitantes.

#### Scenario: Visitor views the program
- **WHEN** o visitante navega para a página de Programação
- **THEN** SHALL ver a lista de sessões agrupadas por data e hora

### Requirement: Program page Stitch-aligned presentation
A pagina Programacao SHALL aplicar layout inspirado em `docs/stitch_cbnv_2026_digital_platform/programa_o_xii_cbnv_2026_design_atualizado/`, mantendo coerencia com o estilo e os componentes publicos atuais.

#### Scenario: Visitor views program page
- **WHEN** o visitante acessa a pagina Programacao
- **THEN** SHALL ver a programacao agrupada por dia e horario em uma apresentacao visual alinhada ao design atualizado
- **AND** SHALL manter navegacao legivel em desktop e mobile

### Requirement: Program data behavior preserved
A reestruturacao visual da Programacao SHALL preservar as regras existentes de exibicao de sessoes publicadas e atividades confirmadas.

#### Scenario: Unconfirmed activities remain hidden
- **GIVEN** uma sessao ou atividade nao confirmada
- **WHEN** a pagina Programacao e renderizada
- **THEN** essa atividade SHALL permanecer omitida da programacao publica

#### Scenario: Empty program state remains available
- **GIVEN** nao existem sessoes publicadas para exibicao
- **WHEN** a pagina Programacao e renderizada
- **THEN** SHALL exibir o estado vazio informando que a programacao sera disponibilizada em breve
