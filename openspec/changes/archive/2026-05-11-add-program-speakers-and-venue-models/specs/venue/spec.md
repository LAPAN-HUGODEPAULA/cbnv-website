# Local do Evento (venue)

## Purpose

Definir a fonte canonica para nome, endereco, mapa e instrucoes de acesso ao local oficial do XII CBNV 2026.

## ADDED Requirements

### Requirement: Canonical venue data
O sistema SHALL fornecer uma fonte canonica editavel em `CoreSettings` para os dados do local oficial do evento.

#### Scenario: Admin edits official venue
- **GIVEN** o administrador acessa o Wagtail
- **WHEN** ele atualiza nome, endereco ou URL de mapa do local oficial
- **THEN** os dados SHALL ser salvos em uma fonte canonica reutilizavel por paginas publicas

#### Scenario: Public page reads official venue
- **GIVEN** uma pagina publica precisa exibir local e acesso
- **WHEN** a pagina renderiza
- **THEN** ela SHALL conseguir obter nome, endereco e link de mapa da fonte canonica do local

### Requirement: Venue access instructions
O sistema SHALL permitir cadastrar instrucoes curtas de acesso ao local do evento sem transformar essas instrucoes em copy fixa dentro de templates.

#### Scenario: Admin adds access guidance
- **GIVEN** existem orientacoes de acesso ao CAD-1/UFMG
- **WHEN** o administrador cadastra as instrucoes no CMS
- **THEN** essas instrucoes SHALL ficar disponiveis para paginas publicas que exibem local e acesso

#### Scenario: Missing access guidance is handled
- **GIVEN** instrucoes de acesso ainda nao foram cadastradas
- **WHEN** uma pagina publica solicita dados do local
- **THEN** o sistema SHALL retornar os dados basicos do local sem exigir texto placeholder enganoso

### Requirement: Canonical CBNV 2026 venue baseline
O local canonico inicial do CBNV 2026 SHALL preservar o CAD-1/UFMG Campus Pampulha e o endereco oficial definido no conteudo canonico.

#### Scenario: Canonical seed stores venue
- **WHEN** os dados canonicos do evento sao carregados
- **THEN** o sistema SHALL armazenar `Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha` como local oficial quando o campo existir
- **AND** SHALL armazenar `R. Prof. Baeta Viana, s/n - Pampulha, Belo Horizonte - MG, 31270-901` como endereco oficial quando o campo existir
- **AND** SHALL armazenar `https://maps.app.goo.gl/xzqJ2LCAHVP4hsFp6` como URL de mapa quando o campo existir

### Requirement: Venue visibility and consistency
O sistema SHALL evitar divergencia entre local exibido em Home, Sobre, Programacao, rodape e outros pontos publicos.

#### Scenario: Reused venue source
- **GIVEN** Home, Sobre e Programacao precisam exibir o local do evento
- **WHEN** essas paginas consultam dados de local
- **THEN** elas SHALL usar a mesma fonte canonica em vez de endereco duplicado em cada pagina

#### Scenario: Hidden or unavailable venue details
- **GIVEN** algum detalhe opcional do local esta vazio ou marcado como indisponivel
- **WHEN** a pagina publica renderiza dados de local
- **THEN** o sistema SHALL omitir apenas o detalhe ausente e preservar os demais dados canonicos disponiveis

#### Scenario: Venue remains settings-backed
- **GIVEN** o CBNV 2026 possui um unico local oficial
- **WHEN** o admin edita os dados de local
- **THEN** o sistema SHALL armazenar nome, endereco, cidade, estado, pais, URL de mapa e instrucoes de acesso em `CoreSettings`
- **AND** o sistema SHALL NOT exigir a criacao de um snippet `Venue` para o MVP
