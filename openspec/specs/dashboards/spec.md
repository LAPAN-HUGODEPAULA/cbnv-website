# Dashboards

## Purpose

Esta especificação define os requisitos para as áreas internas de dashboard sensíveis ao papel (role-aware) para autores, revisores e membros do comitê científico.
## Requirements
### Requirement: Índice de dashboard autenticado
A plataforma SHALL fornecer um índice de dashboard autenticado.

#### Scenario: Visitante não autenticado abre o dashboard
- **GIVEN** que um visitante não autenticado solicita o dashboard
- **WHEN** a requisição é processada
- **THEN** o visitante SHALL ser redirecionado para o login.

#### Scenario: Usuário autenticado abre o dashboard
- **GIVEN** que um usuário autenticado solicita o dashboard
- **WHEN** a requisição é processada
- **THEN** ele SHALL ver as áreas de dashboard disponíveis baseadas nos papéis do seu perfil.

### Requirement: Shell de dashboard do autor
A plataforma SHALL fornecer um shell de dashboard do autor.

#### Scenario: Autor abre o dashboard do autor
- **GIVEN** que um usuário autenticado possui o papel de autor
- **WHEN** ele abre o dashboard do autor
- **THEN** ele SHALL ver uma área de autor com placeholders para submissões futuras.

#### Scenario: Não-autor abre o dashboard do autor
- **GIVEN** que um usuário autenticado não possui o papel de autor
- **WHEN** ele abre o dashboard do autor
- **THEN** o acesso SHALL ser negado ou redirecionado.

### Requirement: Shell de dashboard do revisor
A plataforma SHALL fornecer um shell de dashboard do revisor.

#### Scenario: Revisor abre o dashboard do revisor
- **GIVEN** que um usuário autenticado possui o papel de revisor
- **WHEN** ele abre o dashboard do revisor
- **THEN** ele SHALL ver uma área de revisor com placeholders para revisões futuras.

### Requirement: Shell de dashboard do chair
A plataforma SHALL fornecer um shell de dashboard do chair/comitê científico.

#### Scenario: Chair abre o dashboard do chair
- **GIVEN** que um usuário autenticado possui o papel de chair
- **WHEN** ele abre o dashboard do chair
- **THEN** ele SHALL ver uma área de comitê com placeholders para fluxos de trabalho futuros.

### Requirement: Shells de dashboard não implementam fluxos de trabalho
Os shells de dashboard SHALL NOT implementar fluxos de trabalho de submissão ou revisão nesta mudança.

#### Scenario: Dashboard do autor renderiza
- **GIVEN** que o dashboard do autor renderiza
- **THEN** ele SHALL NOT fornecer a criação real de submissões a menos que a proposta posterior de fluxo de submissão tenha sido implementada.


