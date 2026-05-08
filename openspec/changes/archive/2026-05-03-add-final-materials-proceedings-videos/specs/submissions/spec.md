## MODIFIED Requirements

### Requirement: Submission status machine (MODIFIED)
A máquina de estados da submissão SHALL implementar as transições finais:
- `accepted_oral` / `accepted_poster` / `accepted_video` → `final_materials_pending` (quando a comissão solicita materiais finais)
- `final_materials_pending` → `ready_for_proceedings` (quando a comissão valida materiais)
- `ready_for_proceedings` → `published_in_proceedings` (quando a comissão publica nos anais)

#### Scenario: Chair requests final materials
- **WHEN** a comissão solicita materiais finais para um trabalho aprovado
- **THEN** a submissão SHALL transitar para `final_materials_pending` e uma notificação SHALL ser enviada ao autor

#### Scenario: Author uploads materials
- **WHEN** o autor faz upload dos materiais finais para uma submissão em `final_materials_pending`
- **THEN** os materiais SHALL ser armazenados e uma confirmação SHALL ser enviada ao autor

#### Scenario: Author cannot upload for wrong status
- **GIVEN** uma submissão com status diferente de `final_materials_pending`
- **WHEN** o autor tenta acessar a página de upload de materiais
- **THEN** o sistema SHALL exibir uma mensagem informando que materiais não são necessários

### Requirement: Author final materials page (ADDED)
O autor SHALL ter uma página dedicada para upload de materiais finais quando sua submissão está em `final_materials_pending`.

#### Scenario: Author accesses materials page
- **WHEN** o autor acessa a página de materiais finais para sua submissão aprovada
- **THEN** SHALL ver o formulário de upload com campos para PDF final, apresentação e link de vídeo (quando aplicável)

#### Scenario: Author re-uploads materials
- **GIVEN** uma submissão em `final_materials_pending` com materiais já enviados
- **WHEN** o autor faz upload de novos materiais
- **THEN** os materiais anteriores SHALL ser substituídos e `received_at` SHALL ser atualizado
