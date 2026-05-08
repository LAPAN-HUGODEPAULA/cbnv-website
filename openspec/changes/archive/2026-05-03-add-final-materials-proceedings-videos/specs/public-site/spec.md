## ADDED Requirements

### Requirement: Proceedings public page
O sistema SHALL fornecer uma página pública em `/anais/` listando todos os trabalhos publicados nos anais do congresso.

#### Scenario: Visitor accesses proceedings page
- **WHEN** um visitante acessa `/anais/`
- **THEN** SHALL ver a listagem de trabalhos publicados com título, autores, modalidade, eixo temático e resumo

#### Scenario: Filtering proceedings by modality
- **WHEN** o visitante seleciona o filtro "Oral" na página de anais
- **THEN** SHALL ver apenas trabalhos com modalidade oral

#### Scenario: Filtering proceedings by thematic axis
- **WHEN** o visitante seleciona um eixo temático no filtro
- **THEN** SHALL ver apenas trabalhos daquele eixo temático

### Requirement: Proceedings detail with embedded video
Trabalhos publicados com vídeo associado SHALL exibir um player YouTube incorporado na página de detalhes ou na listagem.

#### Scenario: Viewing published work with video
- **GIVEN** um trabalho publicado com `video_url` preenchido
- **WHEN** o visitante visualiza o trabalho nos anais
- **THEN** SHALL ver um player YouTube incorporado junto com os metadados do trabalho

#### Scenario: Viewing published work without video
- **GIVEN** um trabalho publicado sem `video_url`
- **WHEN** o visitante visualiza o trabalho nos anais
- **THEN** SHALL ver os metadados e download do PDF, sem player de vídeo

### Requirement: Proceedings PDF download
Trabalhos publicados SHALL ter seu PDF final disponível para download público.

#### Scenario: Downloading proceedings PDF
- **WHEN** o visitante clica no botão de download do PDF de um trabalho publicado
- **THEN** o PDF final SHALL ser baixado diretamente

#### Scenario: PDF not available for unpublished work
- **GIVEN** um trabalho que não está publicado nos anais
- **WHEN** alguém tenta acessar diretamente o URL do PDF
- **THEN** o sistema SHALL negar o acesso (403)
