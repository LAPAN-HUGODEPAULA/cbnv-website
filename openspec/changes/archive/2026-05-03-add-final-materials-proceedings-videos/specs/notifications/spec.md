## ADDED Requirements

### Requirement: Final materials request notification
O sistema SHALL notificar o autor quando a comissão solicita materiais finais para seu trabalho aprovado.

#### Scenario: Chair requests materials
- **WHEN** a comissão solicita materiais finais para uma submissão aprovada
- **THEN** um email SHALL ser enviado ao autor correspondente com instruções de upload e prazo

### Requirement: Materials received notification
O sistema SHALL notificar o autor quando seus materiais finais são recebidos com sucesso.

#### Scenario: Author uploads materials
- **WHEN** o autor faz upload dos materiais finais
- **THEN** um email de confirmação SHALL ser enviado ao autor correspondente

### Requirement: Materials validated notification
O sistema SHALL notificar o autor quando a comissão valida seus materiais finais.

#### Scenario: Chair validates materials
- **WHEN** a comissão valida os materiais finais de uma submissão
- **THEN** um email SHALL ser enviado ao autor informando que os materiais foram aceitos

### Requirement: Proceedings publication notification
O sistema SHALL notificar o autor quando seu trabalho é publicado nos anais.

#### Scenario: Work published in proceedings
- **WHEN** a comissão publica um trabalho nos anais
- **THEN** um email SHALL ser enviado ao autor com link para a página pública dos anais
