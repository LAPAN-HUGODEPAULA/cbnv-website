# Anais e Acervo (proceedings)

## Purpose

Definir os requisitos para enriquecer e reestruturar a página "Edições Anteriores" com conteúdo histórico e anais legados.

## ADDED Requirements

### Requirement: Previous editions Stitch-aligned layout
A página "Edições Anteriores" SHALL usar layout inspirado em `docs/stitch_cbnv_2026_digital_platform/edi_es_anteriores_xii_cbnv_2026/`, mantendo a identidade visual do site atual.

#### Scenario: Visitor views previous editions archive
- **WHEN** o visitante acessa "Edições Anteriores"
- **THEN** SHALL ver edições anteriores em cards ou blocos estruturados com número da edição, ano, tema, datas, local e links de materiais quando disponíveis

### Requirement: Previous editions de-duplication
A página "Edições Anteriores" SHALL eliminar conteúdo duplicado sobre as mesmas edições e materiais.

#### Scenario: Duplicate edition data is collapsed
- **GIVEN** múltiplas fontes legadas descrevem a mesma edição
- **WHEN** a página "Edições Anteriores" é renderizada
- **THEN** SHALL exibir uma única entrada consolidada para aquela edição

### Requirement: Proceedings-derived edition metadata
As informações das edições anteriores SHALL ser enriquecidas a partir dos anais e referências bibliográficas em `_legacy/cbnv/`.

#### Scenario: Local proceedings data is used
- **WHEN** houver metadados de edição nos arquivos `_legacy/cbnv/Exported Items.json` ou `_legacy/cbnv/Exported Items/Exported Items.bib`
- **THEN** a página SHALL usar esses dados para preencher ou complementar a entrada da edição correspondente

### Requirement: External event archive as supplemental source
O conteúdo público de `https://lapan.com.br/eventos/` MAY ser usado como fonte suplementar para preencher lacunas de edições anteriores, mas a renderização pública SHALL funcionar sem acesso de rede.

#### Scenario: External source unavailable
- **GIVEN** a fonte externa não está acessível durante testes ou desenvolvimento local
- **WHEN** a página "Edições Anteriores" é renderizada
- **THEN** SHALL continuar exibindo os dados locais disponíveis sem erro
