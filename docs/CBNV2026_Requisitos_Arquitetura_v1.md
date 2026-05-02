# XII CBNV 2026 — Documento de Requisitos e Arquitetura v1.0

**Projeto:** Website e plataforma digital do XII Congresso Brasileiro de Neurociências da Visão  
**Sigla:** CBNV 2026  
**Versão:** 1.0  
**Data:** 2026-05-01  
**Status:** Documento base para design, prototipação e implementação  
**Stack aprovada:** Django + Wagtail + PostgreSQL + Tailwind CSS + HTMX/Alpine.js  
**Decisão crítica:** Este documento passa a ser o *single source of truth* do projeto. 

---

## 1. Finalidade do documento

Este documento define os requisitos funcionais, não funcionais, editoriais, científicos, visuais e arquiteturais do novo site/plataforma digital do XII Congresso Brasileiro de Neurociências da Visão — CBNV 2026.

Ele deve orientar:

1. a prototipação visual no Google Stitch;
2. a implementação por agentes de codificação baseados em IA;
3. a tomada de decisão sobre escopo do MVP;
4. a modelagem de dados;
5. a estrutura do CMS;
6. o fluxo de submissão e avaliação de trabalhos;
7. a publicação de programação, palestrantes, anais e materiais pós-evento;
8. a prestação de contas e geração de indicadores.

Este documento deve ser lido antes de qualquer tarefa de design ou desenvolvimento. Em caso de divergência entre este documento e qualquer arquivo anterior, este documento prevalece.

---

## 2. Fontes consolidadas nesta versão

As decisões desta versão foram consolidadas a partir das seguintes fontes:

1. Termo/plano de trabalho FAPEMIG OET-00394-26.
2. PDF da programação preliminar do XII CBNV 2026.
3. Decisões explícitas do coordenador técnico do projeto nesta conversa.
4. Informações pontuais extraídas do site da 11ª edição apenas para migração da equipe e acervo histórico.

Fontes descontinuadas após esta versão:

1. Site legado Wix: não deve mais ser usado como referência de escopo, design ou implementação. Pode ser usado apenas como acervo histórico se houver necessidade controlada de migração posterior.

---

## 3. Descrição canônica do evento

**Nome formal:** XII Congresso Brasileiro de Neurociências da Visão  
**Nome curto:** CBNV 2026  
**Tema:** Neurovisão na Era da Inteligência Artificial  
**Formato:** Presencial com transmissão híbrida  
**Duração:** 3 dias  
**Datas:** 11 a 13 de novembro de 2026  
**Cidade:** Belo Horizonte, Minas Gerais  
**Local:** CAD-1 da UFMG, Campus Pampulha  
**Capacidade de referência:** aproximadamente 600 participantes  
**Abrangência:** nacional  
**Porte:** médio  
**Natureza:** evento técnico-científico consolidado, aberto ao público  
**Instituição executora/proponente:** UFMG  
**Instituição gestora:** FUNDEP  
**Parceiros institucionais/científicos previstos:** UFMG, FUNDEP, Sociedade Brasileira de Neurovisão, Hospital de Olhos de Minas Gerais/HOLHOS, UFRJ, USP, UFRN, UEMG e demais instituições científicas convidadas.

### 3.1 Posicionamento científico

O CBNV 2026 integra neurociência da visão, oftalmologia, psicofísica, eletrofisiologia, neuroimagem, ciência de dados, inteligência artificial, biomarcadores visuais, saúde digital e inovação clínica. O evento deve preservar a identidade histórica da neurociência da visão, mas apresentar a edição de 2026 como uma atualização científica voltada à inteligência artificial responsável, à neurovisão translacional e à integração entre pesquisa básica, prática clínica e tecnologia.

### 3.2 Promessa pública do site

O site deve comunicar rapidamente:

1. o que é o CBNV;
2. quando e onde será realizado;
3. qual é o tema central;
4. como participar;
5. como submeter trabalhos;
6. qual é a programação;
7. quem organiza;
8. quais são os produtos e registros pós-evento;
9. quais são os apoios institucionais;
10. como acessar materiais de edições anteriores e vídeos.

---

## 4. Objetivos do produto digital

O produto digital não é apenas uma landing page. Ele deve funcionar como infraestrutura pública e administrativa do congresso.

### 4.1 Objetivos principais

1. Divulgar o XII CBNV 2026 de forma moderna, confiável, acessível e cientificamente qualificada.
2. Centralizar informações sobre datas, local, tema, programação, palestrantes, submissões, inscrição e contato.
3. Permitir edição de conteúdo por um único usuário administrador central.
4. Gerenciar submissões científicas em fluxo bifásico.
5. Apoiar revisão, classificação e decisão de trabalhos.
6. Registrar dados necessários para anais, indicadores e relatório técnico-científico.
7. Publicar anais digitais e materiais pós-evento.
8. Integrar o acervo de vídeos via links para playlist/canal do YouTube do CBNV.
9. Reforçar menção obrigatória ao apoio da FAPEMIG em materiais pertinentes.
10. Ser simples e seguro de implementar com auxílio de agentes de codificação baseados em IA.

### 4.2 Objetivos de experiência

1. Site centrado no usuário, não na estrutura administrativa.
2. Navegação clara para participantes, autores, revisores, palestrantes, patrocinadores e público geral.
3. Visual moderno, científico, responsivo e acessível.
4. Redução de carga cognitiva: CTAs claros, prazos visíveis, programação filtrável e linguagem objetiva.
5. Boa experiência mobile.
6. Boa experiência para pessoas com baixa visão, sensibilidade visual ou uso de tecnologias assistivas.
7. Separação clara entre conteúdo confirmado e conteúdo pendente.

---

## 5. Decisões fechadas

### 5.1 Stack tecnológica

A stack principal aprovada é:

1. **Django** como framework web principal.
2. **Wagtail** como CMS editorial.
3. **PostgreSQL** como banco de dados.
4. **Django templates** como camada de renderização server-side.
5. **Tailwind CSS** como sistema utilitário de estilos.
6. **HTMX** para interações leves sem SPA completa.
7. **Alpine.js** apenas quando necessário para microinterações locais.
8. **Docker Compose** para ambiente de desenvolvimento e deploy.
9. **Caddy** ou **Nginx** como reverse proxy com HTTPS.
10. **SMTP institucional ou provedor transacional** para e-mails.
11. **Armazenamento local protegido** no MVP, com possibilidade de migração futura para S3/Backblaze/MinIO.

Não usar Next.js + Strapi como stack principal desta versão.

### 5.2 Administração de conteúdo

O objetivo é ter **um usuário administrador editorial único** para evitar complexidade de RBAC. O sistema pode preservar permissões internas padrão de Django/Wagtail, mas o produto não deve depender de múltiplos perfis editoriais no MVP.

Papéis científicos (transactional roles) continuam existindo e devem ser implementados como **flags booleanas** no modelo de usuário para permitir que um único usuário acumule múltiplas funções (ex: autor e revisor simultaneamente):

1. `is_author` (Autor);
2. `is_reviewer` (Revisor);
3. `is_chair` (Chair/Comissão Científica).

O papel de **Admin técnico/organizador** é coberto pelas permissões `is_staff`/`is_superuser` padrão do Django.

### 5.3 Inscrição, certificados e credenciamento

Ficam fora do escopo da plataforma própria:

1. pagamento de inscrições;
2. QR code de credenciamento;
3. geração de certificados;
4. controle de check-in oficial, se fornecido por UFMG/FUNDEP/Sympla.

O site deve apenas exibir informações, categorias, prazos e botões/links externos para a entidade responsável. Os links externos devem ser editáveis no CMS.

### 5.4 Vídeos

O sistema não deve hospedar vídeos completos. Deve armazenar apenas links para vídeos ou playlists do YouTube do canal CBNV.

Campos recomendados para vídeos:

1. título;
2. descrição;
3. URL do YouTube;
4. ID do vídeo;
5. ID da playlist;
6. thumbnail;
7. sessão relacionada;
8. trabalho relacionado, se aplicável;
9. status: rascunho, público, oculto, arquivado.

### 5.5 Submissão de trabalhos

O fluxo de submissão é bifásico.

Fase 1 — submissão inicial:

1. cadastro/login do autor;
2. metadados do trabalho;
3. autores e afiliações;
4. resumo;
5. eixo temático;
6. palavras-chave;
7. upload de PDF para avaliação;
8. confirmação de ciência das regras.

Não exigir vídeo na submissão inicial.

Fase 2 — material final de trabalhos aprovados:

1. PDF final;
2. arquivo/arte de pôster, se aplicável;
3. link de vídeo, se aplicável;
4. autorização de publicação;
5. autorização de uso de imagem/material, se aplicável.

### 5.6 Programação

O PDF da programação preliminar é a fonte da verdade para estrutura de dias, sessões, temas e horários. Participantes ainda não confirmados devem ficar com status pendente e podem não aparecer no site.

### 5.7 Equipe

A equipe deve partir da equipe da 11ª edição e da equipe formal do projeto FAPEMIG, incorporando:

1. Prof. Hugo Bastos de Paula como cochair/subcoordenador;
2. Carla Stangherlim Neves;
3. Geovana Rafaela de Fátima.

---

## 6. Usuários e jornadas

### 6.1 Visitante público

Objetivo: entender o evento e decidir participar.

Precisa encontrar:

1. tema;
2. datas;
3. local;
4. formato;
5. programação;
6. palestrantes;
7. inscrição;
8. submissão de trabalhos;
9. contato;
10. acessibilidade e como chegar.

### 6.2 Participante inscrito

Objetivo: saber como chegar, acompanhar programação, acessar links externos e materiais.

Precisa encontrar:

1. link externo de inscrição/credenciamento;
2. informações sobre certificado;
3. programação por dia;
4. local;
5. mapa;
6. FAQs;
7. links de transmissão, se houver;
8. materiais e vídeos pós-evento.

### 6.3 Autor

Objetivo: submeter trabalho e acompanhar decisão.

Precisa fazer:

1. criar conta;
2. iniciar submissão;
3. salvar rascunho;
4. enviar submissão;
5. receber confirmação;
6. acompanhar status;
7. responder ressalvas;
8. enviar material final;
9. consultar decisão e modalidade final.

### 6.4 Revisor

Objetivo: avaliar trabalhos atribuídos.

Precisa fazer:

1. entrar no painel;
2. ver fila de trabalhos;
3. baixar PDF anonimizado;
4. declarar conflito de interesse;
5. preencher parecer;
6. recomendar decisão e modalidade;
7. revisar histórico da própria avaliação.

### 6.5 Chair/Comissão Científica

Objetivo: controlar triagem, revisão, decisão e preparação dos anais.

Precisa fazer:

1. visualizar submissões;
2. filtrar por eixo, status e modalidade;
3. atribuir revisores;
4. consultar pareceres;
5. decidir aceite, rejeição ou ressalvas;
6. classificar modalidade final;
7. exportar dados para anais;
8. exportar indicadores.

### 6.6 Admin editorial

Objetivo: centralizar edição do site.

Precisa fazer:

1. editar páginas;
2. publicar notícias;
3. atualizar programação;
4. atualizar palestrantes;
5. gerenciar patrocinadores;
6. inserir links externos;
7. publicar materiais e anais;
8. ocultar ou exibir conteúdo pendente.

---

## 7. Arquitetura da informação

### 7.1 Navegação principal

Menu principal recomendado:

1. Início
2. Sobre
3. Programação
4. Palestrantes
5. Submissões
6. Inscrição
7. Patrocínio
8. Edições anteriores
9. Contato

Em telas pequenas, usar menu mobile claro, com CTA fixo para “Submeter trabalho” ou “Inscreva-se”, conforme fase do congresso.

### 7.2 CTAs principais por fase

Antes da abertura de submissões:

1. “Conheça o congresso”
2. “Ver programação preliminar”
3. “Receba atualizações”

Durante submissões:

1. “Submeter trabalho”
2. “Consultar normas”
3. “Entrar na área do autor”

Após encerramento de submissões:

1. “Ver programação”
2. “Inscreva-se”
3. “Acessar área do autor”

Durante o evento:

1. “Ver programação de hoje”
2. “Como chegar”
3. “Acessar transmissão”
4. “Consultar trabalhos”

Pós-evento:

1. “Acessar anais”
2. “Ver vídeos”
3. “Baixar materiais”
4. “Ver resultados”

---

## 8. Páginas públicas

### 8.1 Início

Conteúdo obrigatório:

1. Hero com nome, tema, datas, local e formato.
2. CTAs: “Ver programação”, “Submeter trabalho”, “Inscrição”.
3. Cards rápidos: datas, local, formato, prazo de submissão, inscrição.
4. Seção “Por que participar”.
5. Destaque da programação.
6. Destaque de palestrantes confirmados.
7. Chamada de submissões.
8. Notícias ou avisos.
9. Apoios institucionais.
10. Rodapé com contato, redes, políticas e menção FAPEMIG quando aplicável.

A Home deve priorizar clareza. Evitar excesso de animações, parallax pesado ou elementos visuais que prejudiquem acessibilidade.

### 8.2 Sobre

Conteúdo:

1. descrição do CBNV;
2. histórico resumido;
3. objetivos científicos;
4. tema da edição 2026;
5. instituições envolvidas;
6. coordenação;
7. organização;
8. compromisso com ciência, sociedade e acessibilidade.

### 8.3 Programação

Requisitos:

1. visualização por dia;
2. filtros por tipo de atividade;
3. cards de sessão;
4. horários claros;
5. indicação de formato híbrido quando aplicável;
6. status de palestrante/participante;
7. opção de ocultar nomes pendentes;
8. versão mobile em timeline vertical;
9. versão desktop em timeline ou grade expandível.

Tipos de atividade:

1. recepção/credenciamento;
2. mesa solene;
3. conferência plenária;
4. palestra;
5. sessão temática;
6. sessão de pôsteres;
7. sessão oral;
8. mesa-redonda;
9. almoço/intervalo;
10. encerramento;
11. premiação.

### 8.4 Palestrantes

Requisitos:

1. cards com foto, nome, instituição, país, mini-bio, sessão relacionada;
2. status interno não necessariamente visível;
3. filtros por eixo/dia;
4. campo “a confirmar” para participantes de mesas ainda não definidos;
5. opção de ocultar palestrantes pendentes.

### 8.5 Submissões

Conteúdo público:

1. chamada para submissão;
2. prazos;
3. critérios de elegibilidade;
4. eixos temáticos;
5. normas de resumo;
6. normas de PDF;
7. fluxo de avaliação;
8. modalidades possíveis após avaliação: oral, pôster ou vídeo;
9. aviso explícito: vídeo não é exigido na submissão inicial;
10. botão “Submeter trabalho”;
11. FAQ.

### 8.6 Inscrição

Conteúdo:

1. inscrição será feita por plataforma externa;
2. categorias e valores, quando definidos;
3. prazos;
4. instruções;
5. certificado e credenciamento sob responsabilidade da entidade externa;
6. botão de inscrição;
7. link editável no CMS;
8. estado “em breve” se link não disponível.

### 8.7 Patrocínio

Conteúdo:

1. convite a apoiadores;
2. perfil do público;
3. contrapartidas;
4. modalidades de apoio;
5. contato institucional;
6. logos de patrocinadores e apoiadores confirmados.

### 8.8 Edições anteriores

Conteúdo:

1. acervo por edição;
2. anais;
3. vídeos/playlist;
4. fotos, se houver;
5. programação histórica;
6. links externos.

A 11ª edição deve ser preservada como acervo, mas não deve orientar o design ou escopo do novo site.

### 8.9 Contato

Conteúdo:

1. e-mail oficial;
2. formulário de contato simples;
3. localização;
4. redes sociais;
5. FAQ;
6. contato para submissões;
7. contato para patrocínio.

---

## 9. Área autenticada

### 9.1 Área do autor

Telas mínimas:

1. Login/cadastro.
2. Dashboard do autor.
3. Lista de submissões.
4. Formulário de nova submissão.
5. Detalhes da submissão.
6. Upload de arquivos.
7. Histórico de status.
8. Resposta a ressalvas.
9. Envio de material final.
10. Confirmação de submissão.

### 9.2 Área do revisor

Telas mínimas:

1. Dashboard do revisor.
2. Lista de trabalhos atribuídos.
3. Detalhe do trabalho anonimizado.
4. Download do PDF.
5. Declaração de conflito de interesse.
6. Formulário de parecer.
7. Status da avaliação.

### 9.3 Área da comissão

Telas mínimas:

1. Dashboard geral.
2. Lista de submissões.
3. Triagem administrativa.
4. Atribuição de revisores.
5. Comparação de pareceres.
6. Decisão final.
7. Classificação de modalidade.
8. Exportações.
9. Indicadores.

### 9.4 Admin CMS

Usar Wagtail Admin e Django Admin conforme necessidade. O admin editorial central deve ter acesso ao painel de conteúdo. O admin técnico pode ter acesso ao Django Admin para dados transacionais, mas essa separação pode ser operacional, não necessariamente visível ao usuário final.

---

## 10. Programação canônica

### 10.1 Dia 1 — Fundamentos e Fronteiras da Neurociência da Visão

Foco: retina, circuitos visuais, percepção e cognição.

Atividades:

1. Recepção e credenciamento.
2. Mesa solene de abertura.
3. Conferência plenária de abertura.
4. Palestras sobre neurobiologia da visão, sincronização neuronal, pulvinar, movimento visual e temas associados.
5. Intervalo e sessão de pôsteres.
6. Palestra final do dia.

### 10.2 Dia 2 — Neurovisão Clínica e Translacional

Foco: aplicações clínicas e translacionais, eletrofisiologia da retina, biomarcadores visuais e condições neurológicas/psiquiátricas.

Atividades:

1. Palestra sobre córtex visual e Alzheimer.
2. Sessão temática de ERG clínica.
3. Sessão temática de biomarcadores visuais e visiomotores.
4. Sessão de pôsteres.
5. Palestra sobre rastreamento ocular.
6. Duas sessões paralelas de apresentação oral de trabalhos.

### 10.3 Dia 3 — Neurovisão, Inteligência Artificial e Inovação em Saúde

Foco: inteligência artificial, ciência de dados e tecnologias digitais aplicadas à pesquisa e prática clínica em neurovisão.

Atividades:

1. Palestra sobre IA no diagnóstico e triagem de doenças oculares.
2. Sessão temática sobre IA em neurociência da visão e oportunidades institucionais.
3. Palestra híbrida sobre modelos de redes neurais e visão biológica.
4. Mesa redonda sobre confiança em modelos de IA na prática clínica.
5. Conferência plenária de encerramento.
6. Encerramento oficial com premiação, agradecimentos e próximos encaminhamentos.

---

## 11. Modelagem de dados

### 11.1 Entidades editoriais

#### SiteSettings

Campos:

1. nome do evento;
2. edição;
3. tema;
4. datas;
5. local;
6. cidade;
7. formato;
8. e-mail de contato;
9. redes sociais;
10. link de inscrição;
11. link de transmissão;
12. link do canal YouTube;
13. texto de menção FAPEMIG;
14. logos institucionais.

#### Page

Gerenciada pelo Wagtail.

Tipos principais:

1. HomePage;
2. AboutPage;
3. ProgramPage;
4. SpeakerIndexPage;
5. SubmissionInfoPage;
6. RegistrationPage;
7. SponsorshipPage;
8. PreviousEditionsPage;
9. ContactPage;
10. NewsIndexPage;
11. NewsArticlePage.

#### NewsArticle

Campos:

1. título;
2. slug;
3. resumo;
4. imagem;
5. corpo;
6. categoria;
7. data de publicação;
8. status;
9. destaque na home;
10. autor/editor;
11. SEO title;
12. SEO description.

#### Speaker

Campos:

1. nome;
2. nome social/de exibição;
3. título;
4. instituição;
5. país;
6. mini-bio;
7. foto;
8. links;
9. status: confirmado, convidado, pendente, substituído, oculto;
10. permitir exibição pública;
11. ordem;
12. sessões relacionadas.

#### ProgramDay

Campos:

1. data;
2. título;
3. subtítulo;
4. descrição;
5. ordem.

#### ProgramSession

Campos:

1. dia;
2. horário início;
3. horário fim;
4. título;
5. tipo;
6. descrição;
7. sala;
8. formato: presencial, híbrido, online;
9. eixo temático;
10. status: rascunho, publicado, pendente, cancelado;
11. exibir no site;
12. ordem;
13. moderador;
14. observações internas.

#### ProgramTalk

Campos:

1. sessão;
2. horário início;
3. horário fim;
4. título;
5. descrição;
6. palestrante;
7. status do palestrante;
8. formato;
9. exibir palestrante publicamente;
10. ordem.

#### Sponsor

Campos:

1. nome;
2. categoria;
3. logo;
4. URL;
5. descrição;
6. status;
7. ordem.

#### Edition

Campos:

1. número da edição;
2. ano;
3. nome;
4. tema;
5. datas;
6. local;
7. descrição;
8. link dos anais;
9. link da playlist;
10. imagens;
11. status.

#### VideoResource

Campos:

1. título;
2. descrição;
3. edição;
4. sessão;
5. trabalho;
6. youtube_url;
7. youtube_video_id;
8. playlist_id;
9. thumbnail;
10. status.

---

## 12. Modelagem de submissões

### 12.1 User

Usar Django User customizado (`accounts.User`) herdando de `AbstractUser` desde o início.

Campos essenciais:

1. `email` (Username);
2. `full_name` (Nome completo);
3. `institution` (Instituição);
4. `country` (País - ISO 3166-1);
5. `position` (Vínculo/Cargo);
6. `is_author` (Boolean);
7. `is_reviewer` (Boolean);
8. `is_chair` (Boolean);
9. `consent_privacy` (Boolean);
10. `consent_image` (Boolean).

### 12.2 Submission

Campos:

1. código público;
2. título;
3. resumo;
4. palavras-chave;
5. eixo temático;
6. autor correspondente;
7. status;
8. modalidade final;
9. criado em;
10. atualizado em;
11. submetido em;
12. decisão em;
13. flags administrativas;
14. observações internas.

### 12.3 SubmissionAuthor

Campos:

1. submissão;
2. nome;
3. e-mail;
4. instituição;
5. país;
6. ORCID, se houver;
7. ordem de autoria;
8. autor correspondente;
9. apresentador.

### 12.4 SubmissionFile

Campos:

1. submissão;
2. tipo: PDF inicial, PDF revisado, PDF final, pôster final, material suplementar;
3. arquivo;
4. versão;
5. hash;
6. tamanho;
7. MIME type;
8. enviado por;
9. data;
10. aprovado para anais.

### 12.5 ReviewAssignment

Campos:

1. submissão;
2. revisor;
3. status;
4. data de atribuição;
5. prazo;
6. conflito declarado;
7. observações.

### 12.6 Review

Campos:

1. atribuição;
2. nota ou recomendação;
3. comentários para autores;
4. comentários internos;
5. recomendação de decisão;
6. recomendação de modalidade;
7. submetido em.

### 12.7 Decision

Campos:

1. submissão;
2. decisão: aceito, aceito com ressalvas, rejeitado;
3. modalidade final: oral, pôster, vídeo;
4. comentário aos autores;
5. observação interna;
6. decidido por;
7. data.

### 12.8 FinalMaterial

Campos:

1. submissão;
2. PDF final;
3. link de vídeo;
4. link de pôster, se houver;
5. autorização de publicação;
6. autorização de uso de imagem;
7. status de validação.

### 12.9 AuditLog

Campos:

1. usuário;
2. ação;
3. objeto;
4. antes;
5. depois;
6. IP;
7. user agent;
8. data.

---

## 13. Máquina de estados das submissões

Estados recomendados:

1. `draft`
2. `submitted`
3. `admin_screening`
4. `needs_admin_correction`
5. `assigned_to_reviewers`
6. `under_review`
7. `reviews_completed`
8. `decision_pending`
9. `revision_requested`
10. `revision_submitted`
11. `accepted_oral`
12. `accepted_poster`
13. `accepted_video`
14. `rejected`
15. `final_materials_pending`
16. `final_materials_received`
17. `ready_for_proceedings`
18. `published_in_proceedings`
19. `withdrawn`
20. `duplicate`
21. `desk_rejected`

A interface não precisa expor todos os nomes internos ao autor. Para autores, usar linguagem simples: “rascunho”, “submetido”, “em avaliação”, “correções solicitadas”, “aprovado”, “rejeitado”, “material final pendente”, “publicado nos anais”.

---

## 14. Requisitos funcionais

### RF-01 — CMS de páginas

O administrador deve conseguir criar, editar, publicar, despublicar e agendar páginas do site.

### RF-02 — Notícias

O administrador deve conseguir publicar notícias e avisos, com destaque opcional na Home.

### RF-03 — Programação editável

O administrador deve conseguir editar dias, sessões, horários, tipos, descrições, palestrantes e status de exibição.

### RF-04 — Palestrantes com status

O sistema deve permitir cadastrar palestrantes confirmados, convidados, pendentes, substituídos e ocultos.

### RF-05 — Inscrição externa

O sistema deve permitir cadastrar link externo de inscrição e exibir estado “em breve” se não houver link.

### RF-06 — Submissão inicial

Autores devem conseguir submeter trabalhos sem vídeo na fase inicial.

### RF-07 — Upload seguro

O sistema deve aceitar PDF e materiais finais com validação de tipo, tamanho e armazenamento protegido.

### RF-08 — Confirmação por e-mail

O autor deve receber confirmação de submissão.

### RF-09 — Painel do autor

O autor deve consultar o status de seus trabalhos.

### RF-10 — Revisão

Revisores devem avaliar trabalhos atribuídos e registrar pareceres.

### RF-11 — Decisão

A comissão deve registrar decisões e modalidades finais.

### RF-12 — Ressalvas

O sistema deve suportar “aceito com ressalvas” e reenvio.

### RF-13 — Material final

Trabalhos aprovados devem poder enviar material final, incluindo link de vídeo quando aplicável.

### RF-14 — Exportação

A comissão deve exportar dados para anais, indicadores e relatório técnico.

### RF-15 — Anais

O site deve publicar link ou página de anais digitais.

### RF-16 — Vídeos

O site deve publicar links para vídeos ou playlists do YouTube, sem hospedar vídeos completos.

### RF-17 — Acervo

O site deve organizar edições anteriores, anais e vídeos por edição.

### RF-18 — Contato

O site deve oferecer canal claro para dúvidas gerais, submissões e patrocínio.

---

## 15. Requisitos não funcionais

### 15.1 Segurança

1. HTTPS obrigatório.
2. Senhas armazenadas com hashing seguro padrão Django.
3. Proteção CSRF ativa.
4. Proteção XSS via templates e sanitização de conteúdo.
5. ORM para evitar SQL injection.
6. Cabeçalhos de segurança configurados.
7. Upload de arquivos validado por extensão, MIME type, tamanho e, idealmente, varredura antivírus.
8. Arquivos de submissão não devem ficar públicos por URL direta.
9. Backups diários do banco e arquivos.
10. Logs de auditoria para ações críticas.
11. Variáveis sensíveis fora do repositório.
12. Rate limiting em login e formulários públicos.
13. Política de privacidade e termo de consentimento para submissões.

### 15.2 Acessibilidade

Critérios mínimos:

1. WCAG 2.2 AA como alvo.
2. Contraste adequado.
3. Navegação por teclado.
4. Foco visível.
5. Labels explícitos em formulários.
6. Mensagens de erro claras.
7. Estrutura semântica de headings.
8. Textos alternativos.
9. Evitar dependência exclusiva de cor.
10. Respeitar `prefers-reduced-motion`.
11. Componentes responsivos.
12. Leitura adequada por screen readers.
13. Linguagem clara para público acadêmico e leigo.
14. Conteúdo em português brasileiro.

### 15.3 Performance

1. Home deve carregar rapidamente em 4G.
2. Imagens otimizadas.
3. Evitar bibliotecas front-end pesadas.
4. SSR por padrão.
5. Cache para páginas públicas.
6. Lazy loading de imagens.
7. HTML semântico e CSS enxuto.

### 15.4 Manutenibilidade

1. Código modular.
2. Apps Django separados por domínio: core, cms, program, submissions, reviews, proceedings, videos.
3. Testes para fluxos críticos.
4. Seeds/fixtures para programação inicial.
5. README de instalação.
6. Scripts de backup e restore.
7. Documentação de variáveis de ambiente.
8. Estrutura compatível com agentes de codificação.

---

## 16. Direção visual

### 16.1 Identidade

A direção visual deve partir da identidade da programação preliminar:

1. azul-marinho profundo;
2. azul elétrico;
3. verde/neon associado ao contorno cerebral/onda visual;
4. estética científica;
5. elementos visuais inspirados em retina, campo visual, sinais, ondas, mapas corticais, grafos neurais e inteligência artificial.

A estética deve ser moderna e institucional, não excessivamente lúdica. O design deve transmitir ciência, precisão, confiança, interdisciplinaridade e inovação.

### 16.2 Tom visual

Palavras-chave:

1. científico;
2. translacional;
3. humano;
4. moderno;
5. acessível;
6. limpo;
7. profundo;
8. tecnológico;
9. brasileiro;
10. institucional.

Evitar:

1. visual de startup genérica;
2. excesso de neon;
3. animações que competem com o conteúdo;
4. textos longos na Home;
5. jargão sem contexto;
6. contraste baixo;
7. layout dependente de imagens pesadas.

### 16.3 Cores sugeridas

Paleta base:

1. `#081426` — azul-marinho profundo;
2. `#0E1E3A` — azul institucional escuro;
3. `#214BFF` — azul elétrico CBNV;
4. `#2FEA8B` — verde neuro/neon;
5. `#E7ECF7` — texto claro;
6. `#9AA8C7` — texto secundário;
7. `#FFFFFF` — superfície clara;
8. `#F5F7FB` — fundo claro;
9. `#111827` — texto em fundo claro;
10. `#F59E0B` — destaque/alerta moderado.

### 16.4 Tipografia

Usar uma combinação que gere confiança acadêmica e modernidade:

1. títulos: serifada elegante ou sans display sofisticada;
2. corpo: sans-serif altamente legível;
3. interface: sans-serif clara.

A escolha exata pode ser proposta no protótipo, mas deve preservar legibilidade.

### 16.5 Componentes

Componentes obrigatórios:

1. Header responsivo.
2. Hero com CTA.
3. Cards de informação.
4. Timeline de programação.
5. Cards de palestrante.
6. Badges de status.
7. Filtros.
8. Formulários.
9. Stepper de submissão.
10. Tabelas administrativas.
11. Alertas.
12. Modal/Drawer para detalhes de sessão.
13. Footer institucional.
14. Breadcrumbs em páginas internas.
15. Empty states.
16. Error states.
17. Loading states.

---

## 17. Conteúdo e tom editorial

### 17.1 Idioma

Português brasileiro. Inglês pode aparecer em nomes de instituições, títulos de palestras internacionais ou materiais específicos.

### 17.2 Tom

O tom deve ser:

1. institucional;
2. claro;
3. científico;
4. acolhedor, mas não promocional demais;
5. objetivo;
6. acessível para público leigo quando necessário.

### 17.3 Microcopy

Exemplos:

1. “Submissões abertas em breve.”
2. “O vídeo será solicitado apenas na etapa final para trabalhos aprovados, quando aplicável.”
3. “Participantes da mesa a confirmar.”
4. “Inscrição realizada em plataforma externa.”
5. “Certificados e credenciamento serão emitidos pela entidade responsável pela inscrição.”
6. “Trabalho submetido com sucesso. Você receberá uma confirmação por e-mail.”
7. “Material final pendente.”
8. “Aguardando parecer da Comissão Científica.”

---

## 18. Equipe

### 18.1 Equipe formal já consolidada no projeto

Nomes formalizados no projeto FAPEMIG e/ou incorporados ao escopo do 12º CBNV:

1. Jerome Paul Armand Laurent Baron — Coordenador.
2. Hugo Bastos de Paula — Cochair/Subcoordenador.
3. Maria Lucia Machado Duarte — Colaboradora.
4. Ricardo Queiroz Guimarães — Colaborador.
5. Marcia Fernanda da Costa Reis Guimarães — Colaboradora.
6. Theo Rolla Paula Mota — Colaborador.
7. Danilo Barbosa Melges — Presidente da Comissão Científica/Colaborador.
8. Alice Timponi França Magalhães — Colaboradora.
9. Clara Amaral Peçanha e Silva — Colaboradora.
10. Lívia Stemler de Godoi Quintão — Colaboradora.
11. Anderson Rodrigues de Oliveira — Colaborador.
12. Victor Soares Sousa — Colaborador.
13. Luiza Furtado Goulart Rodrigues — Colaboradora.
14. Geovana de Fátima Sousa Gonçalves — Colaboradora.
15. Pedro Brandão Belisário — Colaborador.
16. Izabela Cecília Silva Barbosa — Colaboradora.
17. Samuel dos Santos Alves — Colaborador.
18. Daniela Reis Passos Sana Morais — Colaboradora.

### 18.2 Equipe migrada da 11ª edição e acréscimos identificados

A equipe do 11º CBNV deve ser migrada para o 12º CBNV, com revisão editorial de nomes, fotos e mini-bios antes da publicação. Entre os nomes que exigiam resolução e agora ficam resolvidos:

1. Carla Stangherlim Neves.
2. Geovana Rafaela de Fátima.

Outros nomes visíveis no acervo da 11ª edição que podem exigir confirmação editorial para exibição no site do 12º CBNV:

1. Letícia de Senna.
2. Tiago Lopes.
3. Victor Cesar.
4. Vinicius Borges.
5. Cláudia de Almeida Diniz.
6. Estêvão Carlos Lima.
7. Cíntia Aparecida de Souza G. Piton.

Regra: membros podem existir no banco como equipe organizadora, comissão científica ou apoio, com status de exibição pública controlado pelo admin.

---

## 19. Produtos e indicadores

O sistema deve permitir a consolidação de dados para:

1. 80 apresentações científicas em congresso;
2. 80 resumos publicados;
3. 1 edição eletrônica dos anais digitais;
4. 1 relatório técnico-científico final;
5. 1 pitch de divulgação dos resultados;
6. 3 materiais didático-pedagógicos;
7. capacitação de 12 membros da equipe;
8. 1 vídeo-filme ou registro audiovisual;
9. processo/metodologia/procedimento de organização e avaliação do CBNV.

Indicadores mínimos:

1. número de inscritos;
2. número de submissões;
3. número de trabalhos aceitos;
4. número de trabalhos rejeitados;
5. número de trabalhos por eixo;
6. número de trabalhos por modalidade final;
7. instituições participantes;
8. estados/países representados;
9. número de autores;
10. número de revisores;
11. prazo médio de avaliação;
12. número de materiais publicados;
13. número de vídeos/links publicados;
14. métricas básicas de acesso ao site, se disponíveis.

---

## 20. Arquitetura técnica

### 20.1 Visão geral

Aplicação monolítica modular:

1. Django project;
2. Wagtail CMS;
3. PostgreSQL;
4. Redis opcional para cache/fila;
5. Celery opcional para e-mails e tarefas assíncronas;
6. Caddy/Nginx como reverse proxy;
7. Docker Compose.

### 20.2 Apps Django sugeridos

1. `core` — configurações globais, site settings, utilitários.
2. `pages` — tipos de páginas Wagtail.
3. `program` — programação, sessões, palestrantes.
4. `submissions` — submissões, autores, arquivos.
5. `reviews` — revisões, pareceres, decisões.
6. `proceedings` — anais, exportações.
7. `videos` — links YouTube e acervo.
8. `sponsors` — patrocinadores.
9. `accounts` — usuários e papéis.
10. `reports` — indicadores e exports.
11. `notifications` — e-mails transacionais/outbox.

### 20.3 Ambientes

1. Local/development.
2. Staging.
3. Production.

### 20.4 Variáveis de ambiente

1. `DJANGO_SECRET_KEY`
2. `DATABASE_URL`
3. `ALLOWED_HOSTS`
4. `CSRF_TRUSTED_ORIGINS`
5. `EMAIL_HOST`
6. `EMAIL_PORT`
7. `EMAIL_HOST_USER`
8. `EMAIL_HOST_PASSWORD`
9. `DEFAULT_FROM_EMAIL`
10. `MEDIA_ROOT`
11. `STATIC_ROOT`
12. `BACKUP_PATH`
13. `SENTRY_DSN` ou equivalente opcional.

### 20.5 Backups

1. dump diário do PostgreSQL;
2. backup diário de media files;
3. retenção mínima: 30 dias;
4. teste de restore antes de abertura de submissões;
5. cópia externa semanal.

---

## 21. Testes e critérios de aceite

### 21.1 Testes mínimos

1. criação/edição/publicação de páginas;
2. submissão de trabalho;
3. upload de PDF;
4. envio de e-mail de confirmação;
5. atribuição de revisor;
6. envio de parecer;
7. decisão final;
8. solicitação de ressalvas;
9. envio de material final;
10. exportação CSV;
11. publicação de programação;
12. responsividade mobile;
13. navegação por teclado;
14. contrastes principais;
15. backup/restore.

### 21.2 Critérios de aceite do MVP

O MVP só é aceitável se:

1. Home, Sobre, Programação, Submissões, Inscrição e Contato estiverem publicáveis.
2. Admin único conseguir editar conteúdo essencial.
3. Programação puder ser atualizada sem código.
4. Palestrantes pendentes puderem ficar ocultos.
5. Inscrição externa puder ser configurada por link.
6. Autor conseguir submeter trabalho sem vídeo.
7. Comissão conseguir visualizar e exportar submissões.
8. Sistema enviar confirmação por e-mail.
9. Arquivos de submissão não forem públicos por URL direta.
10. Site for responsivo e acessível em nível básico.
11. Rodapé e materiais obrigatórios incluírem menção FAPEMIG quando aplicável.

---

## 22. Escopo fora do MVP

Fora do MVP:

1. pagamento online próprio;
2. emissão própria de certificados;
3. QR code de credenciamento próprio;
4. aplicativo mobile nativo;
5. streaming de vídeo próprio;
6. hospedagem interna de vídeos completos;
7. RBAC editorial complexo;
8. gamificação;
9. agenda personalizada avançada;
10. integração automática com Sympla/UFMG/FUNDEP, salvo link externo;
11. tradução completa para inglês;
12. recomendação automática por IA;
13. chatbot público;
14. revisão totalmente duplo-cega automatizada sem triagem humana.

---

## 23. Prioridades

### P0 — Preparação

1. Aprovar este documento.
2. Prototipar telas no Stitch.
3. Definir identidade visual final.
4. Definir domínio e hospedagem.
5. Definir link/plataforma externa de inscrição, se já disponível.
6. Definir calendário de submissões.
7. Confirmar lista pública de equipe e palestrantes.

### P1 — MVP público e submissão inicial

1. CMS.
2. Site público.
3. Programação.
4. Submissões.
5. Login de autor.
6. Upload.
7. E-mails.
8. Export CSV básico.

### P2 — Revisão científica

1. Revisor.
2. Parecer.
3. Comissão.
4. Decisão.
5. Ressalvas.
6. Material final.
7. Export para anais.

### P3 — Pós-evento

1. Anais digitais.
2. Indicadores.
3. Relatório técnico.
4. Materiais de divulgação.
5. Vídeos/YouTube.
6. Acervo.

---

## 24. Orientações para agentes de codificação

1. Priorizar simplicidade sobre abstração prematura.
2. Usar Django idiomático.
3. Evitar SPA complexa.
4. Usar HTMX apenas onde houver ganho claro.
5. Manter templates legíveis.
6. Criar modelos e migrations incrementais.
7. Escrever testes para fluxos críticos.
8. Não implementar RBAC editorial complexo.
9. Não implementar pagamento.
10. Não implementar certificado ou QR code próprio.
11. Não hospedar vídeos.
12. Criar fixtures da programação preliminar.
13. Manter componentes Tailwind reutilizáveis.
14. Documentar decisões no README.
15. Gerar seed de SiteSettings.
16. Validar acessibilidade antes de aceitar páginas.

---

## 25. Orientações para o Stitch

Ao usar o Stitch, anexar este documento como referência principal. Não anexar Notion export nem site legado como documentos de referência para decisão. Usar o prompt mestre separado.

Objetivo do protótipo:

1. explorar alternativas de design;
2. validar a experiência pública;
3. definir sistema visual;
4. obter telas exportáveis para orientar implementação;
5. não tratar o output do Stitch como especificação funcional final.

O Stitch deve focar primeiro em:

1. Home;
2. Programação;
3. Submissões;
4. Área do autor;
5. Palestrantes;
6. Sobre/Local;
7. Admin/Comissão em baixa prioridade visual.

---

## 26. Questões abertas

1. Domínio definitivo do site.
2. Plataforma externa de inscrição.
3. Categorias e valores de inscrição.
4. Datas exatas de abertura/fechamento de submissões.
5. E-mail oficial.
6. Política final de revisão: simples-cega, duplo-cega ou revisão não-cega com PDF anonimizado.
7. Tamanho máximo dos arquivos.
8. Template oficial de resumo/PDF.
9. Lista pública final de equipe.
10. Lista final de palestrantes confirmados.
11. Link do canal/playlist YouTube.
12. Logos oficiais em alta resolução.
13. Texto final de apoio FAPEMIG.
14. Política de privacidade.
15. Política de uso de imagem.

---

## 27. Conclusão

O projeto deve ser implementado como uma plataforma monolítica modular em Django/Wagtail, com design moderno, acessível e responsivo. A prioridade é entregar uma experiência pública clara e uma infraestrutura robusta para submissões, revisão, anais e indicadores, evitando complexidade desnecessária. O sistema deve ser suficientemente simples para ser implementado com agentes de codificação, mas estruturado o bastante para sustentar a produção científica e a prestação de contas do CBNV 2026.
