# Patrocinadores (sponsors)

## Purpose
Definir o cadastro editorial e a exibição pública de patrocinadores, apoiadores e instituições parceiras.

## ADDED Requirements

### Requirement: Sponsor Management
O sistema SHALL permitir o gerenciamento de patrocinadores e apoiadores via Snippets do Wagtail. Os campos MUST incluir: Nome, Categoria (Diamante, Ouro, Prata, Apoio), Logotipo, URL e Ordem de exibição.

#### Scenario: Displaying sponsor logos
- **WHEN** a Home ou página de Patrocínio é carregada
- **THEN** SHALL exibir os logotipos dos patrocinadores ativos, agrupados por categoria e respeitando a ordem definida
