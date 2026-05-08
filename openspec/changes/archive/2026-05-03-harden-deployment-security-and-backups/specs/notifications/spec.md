## MODIFIED Requirements

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

## ADDED Requirements

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
