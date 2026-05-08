# Delta: Anais e Acervo (proceedings)

## MODIFIED Requirements

### Requirement: Previous Editions Management
O sistema SHALL permitir o cadastro de edições anteriores do congresso para preservação do acervo histórico. Os campos MUST incluir: Número da Edição, Ano, Tema, Datas, Local, Link dos Anais (externo) e Link da Playlist (YouTube). O Manager de proceedings SHALL fornecer método `materials_status()` para consultar status de materiais finais (entregues vs. pendentes).

#### Scenario: Listing past editions
- **WHEN** um usuário acessa a página de "Edições Anteriores"
- **THEN** SHALL visualizar a lista cronológica das edições cadastradas com links para seus respectivos materiais

#### Scenario: Reports consulta status de materiais
- **WHEN** o app reports chama método de status de materiais
- **THEN** SHALL retornar contagem de trabalhos aceitos com materiais entregues, pendentes e proceedings publicados

## ADDED Requirements

### Requirement: Proceedings Export QuerySet
O Manager de proceedings SHALL fornecer método `export_queryset()` que retorna queryset otimizado com dados de proceedings, materiais finais e links de vídeo para exportação detalhada.

#### Scenario: Export de proceedings
- **WHEN** chamado o método de export do manager
- **THEN** SHALL retornar queryset com título, autores, modalidade, status de materiais, link de vídeo e data de publicação
