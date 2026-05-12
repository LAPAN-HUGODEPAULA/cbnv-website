# vídeos (videos)

## Purpose
Gerenciar a integração, análise e exibição de conteúdos de vídeo (YouTube) associados a submissões e edições do congresso.

## Requirements

### Requirement: YouTube URL Parsing
O sistema SHALL ser capaz de analisar URLs do YouTube para extrair o ID do vídeo e identificar o tipo (vídeo individual, playlist ou shorts).

#### Scenario: Valid YouTube URL parsed
- **WHEN** uma URL válida do YouTube é fornecida
- **THEN** o sistema SHALL retornar o ID correto e o tipo do conteúdo.

#### Scenario: Invalid URL rejected
- **WHEN** uma URL que não é do YouTube ou está malformada é fornecida
- **THEN** o sistema SHALL retornar um erro de validação.

### Requirement: YouTube Embed Rendering
O sistema SHALL fornecer helpers para renderizar o iframe de embed do YouTube de forma responsiva e acessível.

#### Scenario: Embed rendered for video
- **WHEN** um ID de vídeo é fornecido ao helper de template
- **THEN** ele SHALL gerar o código HTML correto para o iframe com parâmetros de segurança (`autoplay=0`, etc.).
