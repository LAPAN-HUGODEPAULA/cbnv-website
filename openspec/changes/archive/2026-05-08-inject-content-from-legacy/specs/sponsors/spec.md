# Patrocinadores (sponsors)

## Purpose

Definir como patrocinadores, apoiadores e instituições organizadoras são exibidos publicamente quando o conteúdo institucional legado é injetado no site.

## ADDED Requirements

### Requirement: Institutional organization display
O sistema SHALL suportar a exibição pública das entidades organizadoras do XII CBNV em uma seção própria, distinta da hierarquia comercial de patrocinadores.

#### Scenario: Organization entities render consistently
- **WHEN** uma página pública renderiza a seção "Organização"
- **THEN** SHALL exibir as entidades organizadoras com logotipo, nome acessível e URL externa quando houver
- **AND** SHALL preservar uma ordem editorial consistente entre Home e Sobre

### Requirement: Requested organization entities
A seção "Organização" SHALL incluir Universidade Federal de Minas Gerais, Laboratório de Pesquisa Aplicada à Neurociências da Visão, LAboratório de Neurodinâmica da Visão, Programa de Pós-Graduação em Neurociências, Laboratório de Fisiologia Sensorial e Comportamental, Hospital de Olhos de Minas Gerais e Fundação Hospital de Olhos.

#### Scenario: All requested organizations are present
- **WHEN** a seção "Organização" é renderizada
- **THEN** SHALL incluir todas as sete entidades solicitadas
- **AND** SHALL usar os logotipos legados correspondentes quando disponíveis

### Requirement: FAPEMIG support display
O apoio da FAPEMIG SHALL ser exibido no rodapé público com logotipo e nome, independentemente de haver uma página de patrocinadores dedicada.

#### Scenario: FAPEMIG support is not tied to sponsor page
- **WHEN** o visitante acessa uma página pública que não seja a página de Patrocinadores
- **THEN** SHALL continuar vendo o apoio da FAPEMIG no rodapé
