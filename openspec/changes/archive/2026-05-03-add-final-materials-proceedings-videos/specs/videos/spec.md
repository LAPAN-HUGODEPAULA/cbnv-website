## MODIFIED Requirements

### Requirement: Video link per accepted submission (ADDED)
Trabalhos aprovados com modalidade oral ou vídeo SHALL poder ter um link YouTube associado como parte dos materiais finais.

#### Scenario: Author provides video URL with final materials
- **WHEN** o autor de um trabalho aprovado (oral ou vídeo) preenche o campo `video_url` nos materiais finais
- **THEN** o sistema SHALL validar que a URL é um link YouTube válido (vídeo ou playlist)
- **AND** o vídeo SHALL ser exibido como player incorporado na página pública de anais

#### Scenario: Poster submission cannot have video
- **GIVEN** uma submissão aprovada com modalidade pôster
- **WHEN** o autor tenta preencher o campo `video_url`
- **THEN** o sistema SHALL ignorar ou não exibir o campo de vídeo

### Requirement: Video validation reuse (ADDED)
A validação de URLs YouTube nos materiais finais SHALL reutilizar a função `parse_youtube_url` existente no app `videos`.

#### Scenario: Invalid YouTube URL in materials
- **WHEN** o autor informa uma URL que não é do YouTube no campo `video_url`
- **THEN** o sistema SHALL rejeitar com erro de validação
