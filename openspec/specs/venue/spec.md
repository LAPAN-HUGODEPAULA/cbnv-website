# Local do Evento (venue)

## Purpose

Definir a fonte canônica para nome, endereço, mapa e instruções de acesso ao local oficial do XII CBNV 2026, garantindo consistência entre as diferentes páginas do site.

## Requirements

### Requirement: Canonical venue data
O sistema SHALL fornecer uma fonte canônica editável em `CoreSettings` para os dados do local oficial do evento.

#### Scenario: Admin edits official venue
- **GIVEN** o administrador acessa o Wagtail
- **WHEN** ele atualiza nome, endereço ou URL de mapa do local oficial
- **THEN** os dados SHALL ser salvos em uma fonte canônica reutilizável por páginas públicas

#### Scenario: Public page reads official venue
- **GIVEN** uma página pública precisa exibir local e acesso
- **WHEN** a página renderiza
- **THEN** ela SHALL conseguir obter nome, endereço e link de mapa da fonte canônica do local

### Requirement: Venue access instructions
O sistema SHALL permitir cadastrar instruções curtas de acesso ao local do evento sem transformar essas instruções em copy fixa dentro de templates.

#### Scenario: Admin adds access guidance
- **GIVEN** existem orientações de acesso ao CAD-1/UFMG
- **WHEN** o administrador cadastra as instruções no CMS
- **THEN** essas instruções SHALL ficar disponíveis para páginas públicas que exibem local e acesso

#### Scenario: Missing access guidance is handled
- **GIVEN** instruções de acesso ainda não foram cadastradas
- **WHEN** uma página pública solicita dados do local
- **THEN** o sistema SHALL retornar os dados básicos do local sem exigir texto placeholder enganoso

### Requirement: Canonical CBNV 2026 venue baseline
O local canônico inicial do CBNV 2026 SHALL preservar o CAD-1/UFMG Campus Pampulha e o endereço oficial definido no conteúdo canônico.

#### Scenario: Canonical seed stores venue
- **WHEN** os dados canônicos do evento são carregados
- **THEN** o sistema SHALL armazenar `Centro de Atividades Didáticas 1 (CAD-1), UFMG Campus Pampulha` como local oficial quando o campo existir
- **AND** SHALL armazenar `R. Prof. Baeta Viana, s/n - Pampulha, Belo Horizonte - MG, 31270-901` como endereço oficial quando o campo existir
- **AND** SHALL armazenar `https://maps.app.goo.gl/xzqJ2LCAHVP4hsFp6` como URL de mapa quando o campo existir

### Requirement: Venue visibility and consistency
O sistema SHALL evitar divergência entre local exibido em Home, Sobre, Programação, rodapé e outros pontos públicos.

#### Scenario: Reused venue source
- **GIVEN** Home, Sobre e Programação precisam exibir o local do evento
- **WHEN** essas páginas consultam dados de local
- **THEN** elas SHALL usar a mesma fonte canônica em vez de endereço duplicado em cada página

#### Scenario: Hidden or unavailable venue details
- **GIVEN** algum detalhe opcional do local está vazio ou marcado como indisponível
- **WHEN** a página pública renderiza dados de local
- **THEN** o sistema SHALL omitir apenas o detalhe ausente e preservar os demais dados canônicos disponíveis

#### Scenario: Venue remains settings-backed
- **GIVEN** o CBNV 2026 possui um único local oficial
- **WHEN** o admin edita os dados de local
- **THEN** o sistema SHALL armazenar nome, endereço, cidade, estado, país, URL de mapa e instruções de acesso em `CoreSettings`
- **AND** o sistema SHALL NOT exigir a criação de um snippet `Venue` para o MVP
