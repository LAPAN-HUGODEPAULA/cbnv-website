# Contas e Autenticação (accounts-auth)

## Purpose
Gerenciar a identidade dos usuários, autenticação e papéis científicos (transactional roles) da plataforma, garantindo uma base sólida para fluxos de trabalho científicos.

## Requirements

### Requirement: Autenticação padrão do Django
A plataforma SHALL utilizar o model de User padrão do Django para autenticação de contas.

#### Scenario: User padrão permanece ativo
- **GIVEN** que os settings do Django estão carregados
- **WHEN** o model de usuário de autenticação é inspecionado
- **THEN** a plataforma SHALL usar o model User padrão do Django e SHALL NOT introduzir um model de usuário customizado nesta mudança.

### Requirement: Metadados de UserProfile
A plataforma SHALL armazenar metadados de usuário específicos do congresso em um model de perfil vinculado um-para-um com o User do Django. Campos do perfil:
- `institution` (CharField, Instituição)
- `country` (CharField, País com choices ISO)
- `position` (CharField, Vínculo/Cargo)
- `is_author` (BooleanField, Default=False)
- `is_reviewer` (BooleanField, Default=False)
- `is_chair` (BooleanField, Default=False)
- `consent_privacy` (BooleanField, Default=False)
- `consent_image` (BooleanField, Default=False)

#### Scenario: Perfil existe para usuário registrado
- **GIVEN** que um usuário se registra através do fluxo público de conta
- **WHEN** o registro é concluído
- **THEN** um `UserProfile` ou perfil equivalente SHALL existir para esse usuário.

#### Scenario: Perfil armazena metadados de instituição
- **GIVEN** que um usuário edita seu perfil
- **WHEN** instituição, país e cargo são salvos
- **THEN** esses valores SHALL ser armazenados no perfil, não em campos customizados do User.

### Requirement: Flags de papéis científicos independentes
O perfil SHALL suportar flags de papéis independentes para autor, revisor e chair/comitê científico.

#### Scenario: Usuário possui múltiplos papéis
- **GIVEN** um usuário que é simultaneamente autor e revisor
- **WHEN** seu perfil é inspecionado
- **THEN** ambas as flags de papel author e reviewer PODEM ser verdadeiras.

#### Scenario: Papel de Chair é privilegiado
- **GIVEN** que um usuário público se registra
- **WHEN** o formulário de registro é enviado
- **THEN** o usuário SHALL NOT ser capaz de conceder a si mesmo acesso de chair/comitê científico.

### Requirement: Mandatory role enforcement
Todo usuário SHALL possuir pelo menos um papel ativo entre os papéis transacionais (`is_author`, `is_reviewer`, `is_chair`) OU ser staff/superuser (`is_staff`, `is_superuser`). Esta validação SHALL ser implementada no método `UserProfile.clean()` (ou equivalente) e SHALL impedir a existência de usuários sem função no sistema.

#### Scenario: Admin creates user without any role
- **WHEN** um administrador tenta salvar um perfil sem marcar nenhum papel (is_author, is_reviewer, is_chair) e o usuário não é is_staff/is_superuser
- **THEN** o sistema SHALL rejeitar com um erro de validação: "Todo usuário deve ter pelo menos um papel atribuído."

#### Scenario: Registration auto-assigns Author role
- **WHEN** um visitante completa o registro
- **THEN** o perfil do usuário SHALL ser criado com `is_author=True`, satisfazendo automaticamente a validação de papel.

### Requirement: Role-based filtering capability
O perfil de usuário SHALL permitir filtragem eficiente de papéis via flags booleanas para uso futuro em submissões e revisões.

#### Scenario: Filtering for reviewers
- **WHEN** o sistema busca usuários para atribuição de revisão
- **THEN** SHALL ser possível filtrar via `UserProfile.objects.filter(is_reviewer=True)`

### Requirement: Wagtail admin user compatibility
O model de perfil SHALL ser compatível com Wagtail admin. Superusuários SHALL ter acesso ao Wagtail admin. Campos de perfil e flags de papéis SHALL ser editáveis via interface administrativa (Snippets ou Inline no User).

#### Scenario: Superuser can access Wagtail admin
- **WHEN** um superusuário faz login em `/admin/`
- **THEN** SHALL acessar o painel do Wagtail sem erro e visualizar/editar os campos do perfil do usuário.

### Requirement: Dashboard shell for authenticated areas
As telas de área do autor e revisor SHALL herdar de `templates/layouts/dashboard.html`, fornecendo uma interface de navegação focada em tarefas, separada do site institucional. O dashboard SHALL exibir estados vazios (Empty States) amigáveis quando o usuário não possuir submissões ou revisões pendentes.

#### Scenario: Author dashboard layout
- **WHEN** um autor faz login e acessa seu painel
- **THEN** SHALL ser apresentado com o shell de dashboard contendo navegação lateral para suas submissões e um estado vazio se não houver submissões.

#### Scenario: Role-based Dashboard Access
- **WHEN** um usuário com apenas `is_author=True` tenta acessar o dashboard de revisor
- **THEN** o sistema SHALL redirecionar para o dashboard de autor ou exibir uma página de acesso negado (403).

### Requirement: Dynamic sidebar navigation
A navegação lateral do dashboard SHALL exibir links condicionalmente baseados nos papéis do usuário autenticado. Todos os usuários veem "Painel"; seções adicionais aparecem apenas se o usuário tiver o papel correspondente no perfil.

#### Scenario: Author sees only relevant links
- **WHEN** um usuário com `is_author=True` (mas não is_reviewer/is_chair) acessa o dashboard
- **THEN** a sidebar SHALL exibir apenas "Painel" e "Submissões". "Revisões" e "Indicadores" SHALL ser ocultos.

#### Scenario: Chair sees all sections
- **WHEN** um usuário com `is_chair=True` acessa o dashboard
- **THEN** a sidebar SHALL exibir todas as seções: "Painel", "Submissões", "Revisões" e "Indicadores".

### Requirement: Mobile-responsive dashboard
O shell do dashboard SHALL ser totalmente responsivo em dispositivos móveis. SHALL incluir um menu hamburger usando Alpine.js para alternar a visibilidade da navegação lateral, seguindo o mesmo padrão estabelecido em `templates/components/header.html` (x-data toggle, x-show, x-transition, escape para fechar).

#### Scenario: Mobile navigation toggle
- **WHEN** um usuário acessa o dashboard em um dispositivo móvel (< lg breakpoint)
- **THEN** a sidebar SHALL estar oculta por padrão e SHALL ser revelada ao tocar no botão hamburger.
- **THEN** o menu SHALL fechar ao pressionar Escape ou ao clicar em um link.

### Requirement: Fluxo de Registro de Participante
O sistema SHALL fornecer um fluxo de registro público onde os usuários podem criar uma conta e ganhar automaticamente o papel de 'Autor' (`is_author=True`). O registro SHALL NOT exigir verificação de e-mail — os usuários são logados imediatamente após o registro bem-sucedido.

#### Scenario: Registro bem-sucedido
- **WHEN** um visitante completa o formulário de registro com dados válidos e consentimentos obrigatórios
- **THEN** uma nova conta de usuário é criada com `is_author=True` em seu perfil, ele é logado e redirecionado para o Dashboard do Autor.

#### Scenario: Formulário de registro coleta nome e sobrenome
- **WHEN** o formulário de registro é exibido
- **THEN** ele SHALL apresentar campos separados para `first_name` e `last_name` (não um campo full_name combinado).

### Requirement: Views de Autenticação
O sistema SHALL fornecer views de autenticação padrão, incluindo Login, Logout e Redefinição de Senha, estilizadas de acordo com o Design System.

#### Scenario: Login de Usuário
- **WHEN** um usuário registrado fornece credenciais corretas
- **THEN** ele é redirecionado para seu dashboard primário baseado em seu papel mais alto (Chair > Revisor > Autor).

#### Scenario: Redefinição de Senha
- **WHEN** um usuário solicita uma redefinição de senha
- **THEN** ele recebe um e-mail com um link seguro para definir uma nova senha, seguindo o fluxo de redefinição de senha integrado do Django.

### Requirement: Estilização de formulários de perfil e submissão
Componentes de formulário (`accessible_input`, `primary_button`) SHALL ser usados em todas as telas de autenticação e perfil para manter a consistência visual.

#### Scenario: Consistência do formulário de edição de perfil
- **WHEN** um usuário edita seu perfil
- **THEN** os inputs SHALL seguir o padrão visual definido no Design System

#### Scenario: Edição de perfil usa first_name/last_name
- **WHEN** um usuário edita seu perfil
- **THEN** SHALL editar `first_name` e `last_name` do User separadamente, não um campo combinado.
