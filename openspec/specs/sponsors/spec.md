# Patrocinadores (sponsors)

## Purpose
Definir o cadastro editorial e a exibição pública de patrocinadores, apoiadores e instituições parceiras.

## Requirements

### Requirement: Sponsor Management
O sistema SHALL permitir o gerenciamento de patrocinadores e apoiadores via Snippets do Wagtail. Os campos MUST incluir: Nome, Categoria (Diamante, Ouro, Prata, Apoio), Logotipo, URL e Ordem de exibição.

#### Scenario: Displaying sponsor logos
- **WHEN** a Home ou página de Patrocínio é carregada
- **THEN** SHALL exibir os logotipos dos patrocinadores ativos, agrupados por categoria e respeitando a ordem definida

### Requirement: Tier-based Visual Hierarchy
O sistema SHALL exibir os patrocinadores com uma hierarquia visual que reflita seu nível (por exemplo, logotipos Diamante maiores que Ouro, que por sua vez são maiores que Prata).

#### Scenario: Multi-tier sponsor display
- **WHEN** a página de Patrocinadores é renderizada
- **THEN** os patrocinadores do nível Diamante SHALL ser exibidos no topo com um tamanho maior que os níveis subsequentes

### Requirement: Sponsor External Linking
O sistema SHALL permitir que cada logotipo de patrocinador aponte para seu respectivo site externo quando clicado.

#### Scenario: Visitor clicks a sponsor logo
- **WHEN** o visitante clica no logotipo de um patrocinador
- **THEN** SHALL ser redirecionado para a URL especificada no cadastro do patrocinador em uma nova aba

### Requirement: Institutional organization display
O sistema SHALL suportar a exibicao publica das entidades organizadoras do XII CBNV em uma secao propria, distinta da hierarquia comercial de patrocinadores.

#### Scenario: Organization entities render consistently
- **WHEN** uma pagina publica renderiza a secao "Organizacao"
- **THEN** SHALL exibir as entidades organizadoras com logotipo, nome acessivel e URL externa quando houver
- **AND** SHALL preservar uma ordem editorial consistente entre Home e Sobre

### Requirement: Requested organization entities
A secao "Organizacao" SHALL incluir Universidade Federal de Minas Gerais, Laboratorio de Pesquisa Aplicada a Neurociencias da Visao, LAboratorio de Neurodinamica da Visao, Programa de Pos-Graduacao em Neurociencias, Laboratorio de Fisiologia Sensorial e Comportamental, Hospital de Olhos de Minas Gerais e Fundacao Hospital de Olhos.

#### Scenario: All requested organizations are present
- **WHEN** a secao "Organizacao" e renderizada
- **THEN** SHALL incluir todas as sete entidades solicitadas
- **AND** SHALL usar os logotipos legados correspondentes quando disponiveis

### Requirement: FAPEMIG support display
O apoio da FAPEMIG SHALL ser exibido no rodape publico com logotipo e nome, independentemente de haver uma pagina de patrocinadores dedicada.

#### Scenario: FAPEMIG support is not tied to sponsor page
- **WHEN** o visitante acessa uma pagina publica que nao seja a pagina de Patrocinadores
- **THEN** SHALL continuar vendo o apoio da FAPEMIG no rodape
