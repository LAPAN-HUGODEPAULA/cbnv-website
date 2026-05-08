# Anais e Acervo (proceedings)

## Purpose
Definir a gestão inicial de edições anteriores e materiais históricos do congresso, incluindo links externos para anais e playlists.

## Requirements

### Requirement: Previous Editions Management
O sistema SHALL permitir o cadastro de edições anteriores do congresso para preservação do acervo histórico. Os campos MUST incluir: Número da Edição, Ano, Tema, Datas, Local, Link dos Anais (externo) e Link da Playlist (YouTube). O Manager de proceedings SHALL fornecer método `materials_status()` para consultar status de materiais finais (entregues vs. pendentes).

#### Scenario: Listing past editions
- **WHEN** um usuário acessa a página de "Edições Anteriores"
- **THEN** SHALL visualizar a lista cronológica das edições cadastradas com links para seus respectivos materiais

#### Scenario: Reports consulta status de materiais
- **WHEN** o app reports chama método de status de materiais
- **THEN** SHALL retornar contagem de trabalhos aceitos com materiais entregues, pendentes e proceedings publicados

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

### Requirement: Proceedings Export QuerySet
O Manager de proceedings SHALL fornecer método `export_queryset()` que retorna queryset otimizado com dados de proceedings, materiais finais e links de vídeo para exportação detalhada.

#### Scenario: Export de proceedings
- **WHEN** chamado o método de export do manager
- **THEN** SHALL retornar queryset com título, autores, modalidade, status de materiais, link de vídeo e data de publicação

### Requirement: Previous editions Stitch-aligned layout
A pagina "Edicoes Anteriores" SHALL usar layout inspirado em `docs/stitch_cbnv_2026_digital_platform/edi_es_anteriores_xii_cbnv_2026/`, mantendo a identidade visual do site atual.

#### Scenario: Visitor views previous editions archive
- **WHEN** o visitante acessa "Edicoes Anteriores"
- **THEN** SHALL ver edicoes anteriores em cards ou blocos estruturados com numero da edicao, ano, tema, datas, local e links de materiais quando disponiveis

### Requirement: Previous editions de-duplication
A pagina "Edicoes Anteriores" SHALL eliminar conteudo duplicado sobre as mesmas edicoes e materiais.

#### Scenario: Duplicate edition data is collapsed
- **GIVEN** multiplas fontes legadas descrevem a mesma edicao
- **WHEN** a pagina "Edicoes Anteriores" e renderizada
- **THEN** SHALL exibir uma unica entrada consolidada para aquela edicao

### Requirement: Proceedings-derived edition metadata
As informacoes das edicoes anteriores SHALL ser enriquecidas a partir dos anais e referencias bibliograficas em `_legacy/cbnv/`.

#### Scenario: Local proceedings data is used
- **WHEN** houver metadados de edicao nos arquivos `_legacy/cbnv/Exported Items.json` ou `_legacy/cbnv/Exported Items/Exported Items.bib`
- **THEN** a pagina SHALL usar esses dados para preencher ou complementar a entrada da edicao correspondente

### Requirement: External event archive as supplemental source
O conteudo publico de `https://lapan.com.br/eventos/` MAY ser usado como fonte suplementar para preencher lacunas de edicoes anteriores, mas a renderizacao publica SHALL funcionar sem acesso de rede.

#### Scenario: External source unavailable
- **GIVEN** a fonte externa nao esta acessivel durante testes ou desenvolvimento local
- **WHEN** a pagina "Edicoes Anteriores" e renderizada
- **THEN** SHALL continuar exibindo os dados locais disponiveis sem erro
