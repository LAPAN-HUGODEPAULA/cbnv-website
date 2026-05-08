# Programação e Palestrantes (program)

## Purpose
Definir a estrutura de dados e regras de negócio para a gestão da programação científica e dos palestrantes do evento.

## ADDED Requirements

### Requirement: Program data structure
O sistema SHALL implementar modelos para `ProgramDay` (datas do evento), `ProgramSession` (blocos de horários), `ProgramTalk` (atividades dentro de sessões) e `Speaker` (palestrantes e participantes). Todos SHALL ser Snippets do Wagtail.

#### Scenario: Relational integrity for talks
- **WHEN** uma `ProgramTalk` é criada
- **THEN** ela MUST estar vinculada a uma `ProgramSession` e opcionalmente a um `Speaker`

### Requirement: Speaker visibility control
O modelo `Speaker` SHALL possuir um campo de status (`confirmed`, `pending`, `hidden`).

#### Scenario: Hide non-confirmed items
- **GIVEN** um palestrante com status `pending`
- **WHEN** a timeline pública é renderizada
- **THEN** o sistema SHALL omitir inteiramente quaisquer talks/sessões não confirmadas — sem slots vazios

### Requirement: Canonical activity types
O sistema SHALL suportar tipos de atividade predefinidos: recepção, mesa solene, conferência plenária, palestra, sessão temática, pôsteres, oral, mesa-redonda e intervalos.

#### Scenario: Visual styling by activity type
- **WHEN** uma sessão do tipo "Conferência Plenária" é renderizada na timeline
- **THEN** ela SHALL receber destaque visual diferenciado via badge do design system

### Requirement: Preliminary program fixtures
O sistema SHALL fornecer um management command que carregue a programação preliminar canônica para os 3 dias do evento.

#### Scenario: Initial setup seeding
- **WHEN** o comando `uv run python manage.py seed_program` é executado
- **THEN** a estrutura completa de dias, sessões, talks e palestrantes confirmados SHALL ser carregada no banco

### Requirement: Speakers appear inline only
Palestrantes SHALL ser exibidos inline na timeline (nome, instituição, bio). Não SHALL existir `SpeakerIndexPage` nem páginas de perfil individuais nesta fase.

#### Scenario: Speaker info in timeline
- **WHEN** um talk confirmado com palestrante é renderizado na timeline
- **THEN** SHALL exibir nome do palestrante e instituição como parte do item da timeline
