# Vídeos (videos)

## Purpose
Definir o cadastro de recursos audiovisuais exclusivamente por links YouTube, incluindo vídeos, playlists e canais de acervo.

## Requirements

### Requirement: YouTube-only Video Management
O sistema SHALL gerenciar recursos de vídeo exclusivamente através de links para o YouTube, canais ou playlists. A hospedagem local de arquivos de vídeo de longa duração é proibida.

#### Scenario: Adding a YouTube video
- **WHEN** um admin cadastra um `VideoResource` com uma URL válida do YouTube
- **THEN** o sistema SHALL extrair o ID do vídeo e armazenar metadados como título, descrição e thumbnail

#### Scenario: Adding a YouTube playlist
- **WHEN** um admin cadastra um `VideoResource` com uma URL válida de playlist do YouTube
- **THEN** o sistema SHALL extrair o ID da playlist e armazenar a URL como recurso de playlist

#### Scenario: Adding the previous edition channel
- **WHEN** um admin cadastra `https://www.youtube.com/@congressoneurovis%C3%A3o`
- **THEN** o sistema SHALL aceitar o canal como recurso de acervo sem tentar hospedar vídeos localmente

### Requirement: Video Metadata and Categorization
Cada `VideoResource` MUST conter: Título, Descrição, URL do YouTube, ID do vídeo (opcional), ID da Playlist (opcional), tipo do recurso (vídeo, playlist ou canal) e Status (Rascunho, Público, Oculto).

#### Scenario: Hidden video behavior
- **GIVEN** um vídeo marcado como "Oculto" no CMS
- **WHEN** um visitante acessa a página de edições anteriores
- **THEN** o vídeo SHALL não ser listado publicamente

### Requirement: Video Gallery Display
O sistema SHALL fornecer uma galeria de vídeos pública onde os usuários podem navegar e assistir a vídeos incorporados do YouTube de edições anteriores e conteúdo promocional.

#### Scenario: Visitor watches a video
- **WHEN** o visitante seleciona um vídeo na galeria
- **THEN** o vídeo do YouTube SHALL ser reproduzido em um player incorporado na página sem redirecionar o usuário

### Requirement: Video link per accepted submission
Trabalhos aprovados com modalidade oral ou vídeo SHALL poder ter um link YouTube associado como parte dos materiais finais.

#### Scenario: Author provides video URL with final materials
- **WHEN** o autor de um trabalho aprovado (oral ou vídeo) preenche o campo `video_url` nos materiais finais
- **THEN** o sistema SHALL validar que a URL é um link YouTube válido (vídeo ou playlist)
- **AND** o vídeo SHALL ser exibido como player incorporado na página pública de anais

#### Scenario: Poster submission cannot have video
- **GIVEN** uma submissão aprovada com modalidade pôster
- **WHEN** o autor tenta preencher o campo `video_url`
- **THEN** o sistema SHALL ignorar ou não exibir o campo de vídeo

### Requirement: Video validation reuse
A validação de URLs YouTube nos materiais finais SHALL reutilizar a função `parse_youtube_url` existente no app `videos`.

#### Scenario: Invalid YouTube URL in materials
- **WHEN** o autor informa uma URL que não é do YouTube no campo `video_url`
- **THEN** o sistema SHALL rejeitar com erro de validação
