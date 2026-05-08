# Conteúdo CMS (content-cms)

## Purpose
Integrar modelos de programação ao admin Wagtail como Snippets.

## MODIFIED Requirements

### Requirement: Structured Page Models
O sistema SHALL fornecer modelos de página Wagtail para a estrutura principal incluindo `ProgramPage`.

#### Scenario: Program page setup
- **WHEN** um admin cria uma `ProgramPage` no Wagtail
- **THEN** ela SHALL servir como base para renderizar a timeline de programação usando o componente `timeline.html` do design system

### Requirement: Domain app ownership
Modelos de programação (`Speaker`, `ProgramDay`, `ProgramSession`, `ProgramTalk`) SHALL residir em `program/models.py`.

#### Scenario: Developer locates program models
- **WHEN** um desenvolvedor precisa alterar o modelo de palestrante
- **THEN** SHALL encontrar `Speaker` em `program/models.py`
