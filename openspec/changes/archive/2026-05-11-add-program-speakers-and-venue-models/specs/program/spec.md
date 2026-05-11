# Programacao e Palestrantes Delta

## Purpose

Refinar a capacidade de programacao e palestrantes para suportar dados canonicos, visibilidade publica segura, ordenacao deterministica e integracao futura com informacoes do local do evento.

## ADDED Requirements

### Requirement: Public program query contract
O sistema SHALL fornecer um contrato de consulta para recuperar programacao publica agrupada por dia, ordenada cronologicamente e filtrada por status publico.

#### Scenario: Public program is chronologically grouped
- **GIVEN** existem dias, sessoes e falas publicados
- **WHEN** a consulta publica de programacao e executada
- **THEN** o resultado SHALL retornar os itens agrupados por data e ordenados por dia, horario de inicio e ordem configurada

#### Scenario: Draft program items are excluded
- **GIVEN** existe uma sessao com status de rascunho, pendente ou cancelado
- **WHEN** a consulta publica de programacao e executada
- **THEN** essa sessao SHALL NOT ser retornada para exibicao publica

### Requirement: Pending participant privacy
O sistema SHALL proteger nomes e detalhes de participantes nao confirmados contra exibicao publica involuntaria.

#### Scenario: Pending speaker is not exposed publicly
- **GIVEN** uma fala esta vinculada a um palestrante com status pendente ou oculto
- **WHEN** a consulta publica de palestrantes ou programacao e executada
- **THEN** o nome, foto, instituicao e biografia desse palestrante SHALL NOT ser retornados como conteudo publico

#### Scenario: Confirmed speaker can be listed
- **GIVEN** um palestrante possui status confirmado e esta vinculado a atividade publica
- **WHEN** a consulta publica de palestrantes e executada
- **THEN** o palestrante SHALL ser retornado com nome publico, instituicao e dados permitidos para exibicao

### Requirement: Program venue reference
Sessoes de programacao SHALL suportar informacao de sala, ambiente ou referencia ao local oficial suficiente para a pagina publica orientar visitantes sem repetir endereco completo em texto ad hoc.

#### Scenario: Session has room information
- **GIVEN** uma sessao publica ocorre em uma sala especifica do local oficial
- **WHEN** o admin cadastra a sessao
- **THEN** o sistema SHALL permitir salvar a sala ou ambiente da sessao junto dos demais dados da programacao

#### Scenario: Public session can reference canonical venue
- **GIVEN** uma pagina publica renderiza uma sessao da programacao
- **WHEN** a sessao precisa indicar localizacao
- **THEN** o sistema SHALL disponibilizar a sala da sessao e a fonte canonica do local do evento sem exigir endereco duplicado no template

## MODIFIED Requirements

### Requirement: Program data structure
O sistema SHALL implementar modelos para `ProgramDay` (datas do evento), `ProgramSession` (blocos de horarios), `ProgramTalk` (atividades dentro de sessoes) e `Speaker` (palestrantes e participantes). Todos SHALL ser gerenciaveis no Wagtail e SHALL preservar integridade relacional entre dias, sessoes, falas e participantes.

#### Scenario: Relational integrity for talks
- **WHEN** uma `ProgramTalk` e criada
- **THEN** ela MUST estar vinculada a uma `ProgramSession` e MAY estar vinculada a um `Speaker`

#### Scenario: Admin manages program entities
- **WHEN** o administrador acessa o Wagtail
- **THEN** ele SHALL conseguir gerenciar dias, sessoes, falas e palestrantes sem alterar codigo

### Requirement: Speaker visibility control
O modelo `Speaker` SHALL possuir um campo de status com valores publicamente seguros, incluindo `confirmed`, `pending` e `hidden`.

#### Scenario: Hide non-confirmed items
- **GIVEN** um palestrante com status `pending` ou `hidden`
- **WHEN** a timeline publica, indice de palestrantes ou consulta publica de programacao e renderizada
- **THEN** o sistema SHALL omitir dados identificaveis desse palestrante sem criar slots vazios

#### Scenario: Show confirmed speaker
- **GIVEN** um palestrante com status `confirmed`
- **WHEN** a timeline publica ou indice de palestrantes e renderizada
- **THEN** o sistema SHALL poder exibir os dados publicos configurados para esse palestrante

### Requirement: Preliminary program fixtures
O sistema SHALL fornecer um management command idempotente que carregue a programacao preliminar canonica para os dias do evento quando os dados oficiais estiverem disponiveis.

#### Scenario: Initial setup seeding
- **WHEN** o comando `uv run python manage.py seed_program` e executado
- **THEN** a estrutura de dias, sessoes, talks e palestrantes confirmados disponivel na fonte canonica SHALL ser carregada no banco

#### Scenario: Re-running program seed
- **GIVEN** a programacao preliminar ja foi carregada
- **WHEN** o comando `uv run python manage.py seed_program` e executado novamente
- **THEN** o sistema SHALL evitar duplicar dias, sessoes, falas ou palestrantes existentes
