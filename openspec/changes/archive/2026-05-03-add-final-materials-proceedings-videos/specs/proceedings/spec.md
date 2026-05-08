## ADDED Requirements

### Requirement: FinalMaterial model
O sistema SHALL possuir um modelo `FinalMaterial` vinculado a `Submission` (um-para-um) para armazenar os materiais finais do trabalho aprovado.

#### Scenario: Creating final materials record
- **GIVEN** uma submissão aprovada (status `accepted_oral`, `accepted_poster` ou `accepted_video`)
- **WHEN** o autor faz upload dos materiais finais
- **THEN** o sistema SHALL criar/atualizar um registro `FinalMaterial` com `final_pdf`, `presentation_file`, `video_url` (opcional) e `received_at`

### Requirement: Final materials file validation
Os arquivos de materiais finais SHALL obedecer às seguintes restrições:
- `final_pdf`: PDF, máximo 10 MB
- `presentation_file`: PDF ou PPTX, máximo 50 MB
- `video_url`: URL válida do YouTube (opcional, apenas para modalidades oral e vídeo)

#### Scenario: Author uploads invalid file type
- **WHEN** o autor faz upload de um arquivo que não é PDF para `final_pdf`
- **THEN** o sistema SHALL rejeitar o upload com mensagem de erro

#### Scenario: Author uploads oversized file
- **WHEN** o autor faz upload de um `presentation_file` maior que 50 MB
- **THEN** o sistema SHALL rejeitar o upload com mensagem de erro

### Requirement: Material validation by commission
A comissão científica SHALL poder validar os materiais finais recebidos, marcando-os como aceitos e registrando quem validou e quando.

#### Scenario: Chair validates materials
- **WHEN** um membro da comissão valida os materiais de uma submissão
- **THEN** o sistema SHALL registrar `validated_at` e `validated_by`, e a submissão SHALL transitar para `ready_for_proceedings`

### Requirement: Proceedings publication
A comissão científica SHALL poder publicar trabalhos nos anais digitais, transitando o status para `published_in_proceedings`.

#### Scenario: Publishing to proceedings
- **WHEN** a comissão publica um trabalho validado
- **THEN** a submissão SHALL transitar para `published_in_proceedings` e o trabalho SHALL aparecer na página pública de anais

### Requirement: Public proceedings page
O sistema SHALL fornecer uma página pública listando todos os trabalhos publicados nos anais, com título, autores, resumo, modalidade, eixo temático e link para download do PDF.

#### Scenario: Visitor browses proceedings
- **WHEN** um visitante acessa a página de anais
- **THEN** SHALL ver a lista de trabalhos publicados com filtros por modalidade e eixo temático

#### Scenario: Visitor downloads proceedings PDF
- **WHEN** um visitante clica no link de download de um trabalho publicado
- **THEN** o PDF SHALL ser disponibilizado para download

#### Scenario: Unpublished work not visible
- **GIVEN** um trabalho com status diferente de `published_in_proceedings`
- **WHEN** um visitante acessa a página de anais
- **THEN** esse trabalho SHALL NÃO aparecer na listagem
