## MODIFIED Requirements

### Requirement: Submission List for Authors
The system SHALL display a list of all submissions owned by the authenticated author in their dashboard.

#### Scenario: Author sees empty submission list
- **WHEN** an author with no submissions accesses the submissions list
- **THEN** they see an "Empty State" component with a "New Submission" CTA (even if disabled).

## ADDED Requirements

### Requirement: Protected submission file serving
Arquivos anexados a submissões (PDF, arquivos complementares) SHALL ser servidos exclusivamente via view autorizada do Django. A view SHALL verificar se o usuário autenticado é dono da submissão ou membro da equipe editorial (staff). O serving SHALL usar X-Accel-Redirect para delegar ao Nginx. A URL pública SHALL ser do tipo `/submissions/<id>/download/<file_id>/` e não SHALL expor o caminho real no sistema de arquivos.

#### Scenario: Author downloads own submission file
- **WHEN** o autor autenticado acessa `/submissions/<id>/download/<file_id>/` e é dono da submissão
- **THEN** o Django verifica permissão, retorna header `X-Accel-Redirect` para o Nginx e o arquivo é transmitido ao cliente

#### Scenario: Staff downloads any submission file
- **WHEN** um usuário staff acessa `/submissions/<id>/download/<file_id>/`
- **THEN** o arquivo SHALL ser servido independentemente de ser o dono

#### Scenario: Non-owner gets access denied
- **WHEN** um usuário autenticado que não é dono e não é staff acessa `/submissions/<id>/download/<file_id>/`
- **THEN** SHALL retornar HTTP 403 Forbidden

#### Scenario: Unauthenticated user gets redirected
- **WHEN** um usuário não autenticado acessa `/submissions/<id>/download/<file_id>/`
- **THEN** SHALL retornar HTTP 302 redirect para a página de login

#### Scenario: Direct media URL returns 404
- **WHEN** uma requisição é feita para `/media/submissions/<qualquer-caminho>`
- **THEN** o Nginx SHALL retornar HTTP 404
