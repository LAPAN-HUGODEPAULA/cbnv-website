# Notificações (notifications)

## Purpose
Gerenciar templates e envio de emails transacionais da plataforma, incluindo notificações de criação de conta e atribuição de papéis.

## Requirements

### Requirement: Account Creation Notification
The system SHALL send a confirmation email to the user upon successful registration.

#### Scenario: User receives welcome email
- **WHEN** a new account is created
- **THEN** an email is sent to the registered address with a welcome message and login instructions.

### Requirement: Role Assignment Notification
The system SHALL notify users when a new scientific role (Reviewer, Chair) is assigned to them by an administrator.

#### Scenario: Reviewer is notified of role change
- **WHEN** an administrator sets `is_reviewer=True` for an existing user
- **THEN** the user receives a notification informing them of their new responsibilities.

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

### Requirement: Reviewer assignment notification
The system SHALL notify reviewers via email when a new work is assigned to them for review.

#### Scenario: Notifying reviewer
- **WHEN** a reviewer is assigned to a work
- **THEN** an email containing the work title and link to the reviewer portal SHALL be sent

### Requirement: Decision notification for authors
Authors SHALL be notified via email when a final decision (Accept/Reject) or a request for corrections is issued.

#### Scenario: Notifying author of corrections
- **WHEN** the commission issues an "Accepted with Corrections" decision
- **THEN** an email with the reviewer comments and instructions for revision SHALL be sent to the corresponding author

### Requirement: SMTP configuration in production
O Django SHALL configurar email via SMTP com TLS em staging e produção usando as variáveis de ambiente `SMTP_HOST`, `SMTP_PORT`, `SMTP_USE_TLS`, `SMTP_USER`, `SMTP_PASSWORD` e `DEFAULT_FROM_EMAIL`. Em desenvolvimento, SHALL usar `console.EmailBackend`. A configuração SHALL ser feita em `settings/production.py`.

#### Scenario: Production sends email via SMTP
- **WHEN** o Django está em modo produção e um email transacional precisa ser enviado
- **THEN** SHALL usar SMTP com TLS para o host configurado em `SMTP_HOST`

#### Scenario: Development uses console backend
- **WHEN** o Django está em modo desenvolvimento
- **THEN** SHALL usar `django.core.mail.backends.console.EmailBackend` e imprimir emails no stdout

### Requirement: Email failure logging
Falhas no envio de emails transacionais SHALL ser logadas em nível `ERROR` com detalhes do destinatário e motivo da falha. A falha SHALL NOT propagar como exceção que interrompa o fluxo principal do usuário (ex: registro de conta deve completar mesmo se o email falhar).

#### Scenario: Email failure is logged
- **WHEN** o envio de um email falha (SMTP indisponível, autenticação falhou)
- **THEN** SHALL ser emitido log em nível `ERROR` com destinatário e mensagem de erro

#### Scenario: User flow continues after email failure
- **WHEN** um email transacional falha durante um fluxo do usuário
- **THEN** o fluxo principal SHALL completar normalmente e o usuário SHALL receber feedback adequado

### Requirement: Submission status change notification
O sistema SHALL enviar email ao autor quando o status da sua submissão mudar para estados finais: `accepted_oral`, `accepted_poster`, `accepted_video` ou `rejected`.

#### Scenario: Author notified of acceptance
- **WHEN** uma decisão é registrada para uma submissão e o status muda para `accepted_oral`
- **THEN** o autor SHALL receber email com o resultado e instruções para próximas etapas

#### Scenario: Author notified of rejection
- **WHEN** uma decisão é registrada para uma submissão e o status muda para `rejected`
- **THEN** o autor SHALL receber email com o resultado
