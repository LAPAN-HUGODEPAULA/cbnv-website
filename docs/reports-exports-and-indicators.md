# Relatórios, Exportações e Indicadores — CBNV 2026

Este documento descreve as capacidades de monitoramento operacional e exportação de dados da plataforma XII CBNV 2026.

## Indicadores (Dashboard)

O painel de indicadores (`/relatorios/`) fornece uma visão em tempo real do estado do congresso:

### Submissões
- **Total de submissões**: Contagem geral de trabalhos criados.
- **Por status**: Distribuição de trabalhos por status do workflow (Rascunho, Enviado, Aceito, etc.).
- **Por eixo temático**: Distribuição de trabalhos pelos eixos científicos.
- **Por modalidade**: Distribuição pela modalidade final (Oral, Pôster, Vídeo).
- **Por país**: Distribuição baseada no país do perfil do submetedor.

### Avaliações (Revisões)
- **Total de atribuições**: Número de pares (Trabalho, Revisor) criados.
- **Concluídas**: Avaliações enviadas pelos revisores.
- **Pendentes**: Avaliações aguardando resposta.
- **Top Revisores**: Ranking dos revisores mais produtivos.

### Autores e Instituições
- **Total de autores**: Contagem de e-mails únicos na base de autores.
- **Instituições**: Contagem de nomes de instituições distintos.
- **Ranking de instituições**: Instituições com maior número de submissões associadas.

### Materiais Finais e Anais (Proceedings)
- **Total aceitos**: Trabalhos com decisão favorável.
- **Materiais entregues**: Trabalhos que já enviaram os arquivos finais.
- **Materiais pendentes**: Trabalhos aprovados que ainda não enviaram materiais.
- **Materiais validados**: Trabalhos com validação registrada pela comissão.
- **Sem autorização**: Trabalhos com material final, mas sem autorização de publicação.
- **Com vídeo**: Trabalhos que informaram URL do YouTube.
- **Na galeria**: Trabalhos associados a um recurso público de vídeo.
- **Publicados nos anais**: Trabalhos com status final de publicação.

## Filtros Disponíveis

O dashboard e as exportações suportam:
- **Eixo Temático**: Filtra todos os indicadores e exportações por um eixo específico.
- **Status**: Filtra pelo status de workflow da submissão.
- **Modalidade**: Filtra pela modalidade final (Oral, Pôster, Vídeo).
- **Instituição**: Filtra por instituição associada aos autores.
- **País**: Filtra pelo país do perfil do submetedor.
- **Materiais**: Filtra por pendentes, recebidos, validados ou sem autorização.
- **Anais**: Filtra por trabalhos prontos para anais ou publicados nos anais.
- **Período (Desde/Até)**: Filtra trabalhos pela data de criação.

Os links de exportação no dashboard preservam os filtros ativos.

## Exportações

Todos os dados podem ser exportados nos seguintes formatos:

| Relatório | Formato | Descrição |
|-----------|---------|-----------|
| **Indicadores** | CSV, XLSX, JSON | Resumo estatístico dos indicadores visíveis. |
| **Submissões** | CSV, XLSX, JSON | Lista detalhada de trabalhos, eixos, modalidades e autores. |
| **Revisões** | CSV, XLSX, JSON | Status das avaliações e recomendações dos revisores. |
| **Anais (Proceedings)** | CSV, XLSX, JSON | Dados para preparação do volume final (IDs, títulos, autores, vídeos). |
| **Autores** | CSV, XLSX, JSON | Lista completa de todos os autores associados a submissões. |
| **Instituições** | CSV, XLSX, JSON | Agregado de submissões e autores por instituição. |
| **Decisões** | CSV, XLSX | Lista focada em resultados (Aprovado/Reprovado) para comunicação. |

### Campos principais

- **Submissões**: ID, título, eixo, modalidade, status, submetedor, autores, data de criação e data de atualização.
- **Autores**: nome, e-mail, instituição, ordem, autor correspondente, apresentador, submissão, título, eixo e status. Como ainda não existe um campo separado de apresentador no modelo, o indicador de apresentador usa o autor correspondente como aproximação documentada.
- **Instituições**: instituição, total de autores e total de submissões.
- **Revisões**: revisor, instituição, submissão, título, recomendação e datas. O texto completo da avaliação e notas confidenciais não são exportados.
- **Anais (Proceedings)**: ID, título, resumo, palavras-chave, eixo, modalidade, status, autores, afiliações, URL de vídeo, autorização de publicação, recebimento e validação.

## Segurança e Privacidade

- **Acesso**: Restrito a usuários com papel de `Comissão Científica` (Chair) ou `Staff`.
- **Baixa sensibilidade**: contagens agregadas, status, eixos temáticos e modalidades.
- **Sensibilidade moderada**: títulos, nomes de autores, instituições e país.
- **Alta sensibilidade**: e-mails, identidade de revisores, texto de avaliações, notas de decisão, notas internas e arquivos protegidos.
- **Limites aplicados**:
    - E-mails de autores são exportados apenas em relatórios internos autorizados.
    - Identidade de revisores é protegida por permissão de comissão/staff; textos completos de avaliação e notas internas não são exportados nos resumos.
    - Arquivos protegidos (PDFs/apresentações) não têm caminhos nem URLs diretas expostas nos relatórios.
    - Dados de proceedings são internos para preparação; publicação pública continua controlada pelas telas públicas de anais.

## Observações Técnicas

- **Fuso Horário**: Todas as datas e horas seguem o padrão definido em `TIME_ZONE`.
- **Codificação**: CSVs utilizam `UTF-8 with BOM` para compatibilidade máxima com Microsoft Excel.
- **XLSX**: Gerado dinamicamente via biblioteca `openpyxl`.
