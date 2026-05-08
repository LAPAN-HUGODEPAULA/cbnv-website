# Vídeos (videos)

## Purpose
Definir o cadastro de recursos audiovisuais exclusivamente por links YouTube, incluindo vídeos, playlists e canais de acervo.

## ADDED Requirements

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
