# Persona Status Map - Round 1

## Metadata

- Change: `verify-cross-page-content-consistency`
- Reviewed commit: `d3044e5`
- Data profiles: empty/default and populated/custom.

## Preferred Status Vocabulary

- Public visitors: avoid internal workflow state names; use publication-facing states only.
- Authors: use action-oriented labels, e.g. `Rascunho`, `Enviado`, `Em avaliação`, `Aprovado - Oral`, `Materiais finais pendentes`, `Pronto para anais`, `Publicado nos anais`.
- Reviewers: use assignment/action states, e.g. `Avaliar`, `Avaliação enviada`, `Pendente`.
- Chairs/admin: may use operational terms, e.g. `Aceito - Oral`, `Atribuído a revisores`, `Revisões concluídas`, `Decisão pendente`, `Validados`, `Publicados`.
- Reports/exports: include either approved labels or paired `codigo` and `rotulo` fields.

## Submission and Decision Statuses

| Internal state | Public visitor | Author | Reviewer | Chair | Admin/staff | Intended asymmetry? | Notes |
|---|---|---|---|---|---|---|---|
| `draft` | Not visible | Rascunho | Not visible | Usually not listed | Rascunho | Yes | Author-only editing state. |
| `submitted` | Not visible | Enviado | Not visible | Enviado/submitted queue | Enviado | Yes | Chair may need operational queue naming. |
| `admin_screening` | Not visible | Em triagem | Not visible | Em triagem | Em triagem | Yes | Acceptable if the author-facing label stays understandable. |
| `assigned_to_reviewers` | Not visible | Em avaliação | Assignment visible when assigned | Atribuído a revisores | Atribuído a revisores | Yes | Current chair templates often call `status_label`, which collapses to author label; see CCR1-008. |
| `under_review` | Not visible | Em avaliação | Avaliar/Avaliação enviada | Em revisão | Em revisão | Yes | Reviewer view is assignment-focused rather than submission-status-focused. |
| `reviews_completed` | Not visible | Em avaliação | Avaliação enviada | Revisões concluídas | Revisões concluídas | Yes | Chair/report labels should avoid raw code. |
| `decision_pending` | Not visible | Em avaliação | No new action | Decisão pendente | Decisão pendente | Yes | Chair screen should make decision action explicit. |
| `accepted_oral` | Not visible | Aprovado - Oral | Not visible | Aceito - Oral / Solicitar materiais | Aceito - Oral | Yes | Author notification uses approved language; chair may need accepted language. |
| `accepted_poster` | Not visible | Aprovado - Pôster | Not visible | Aceito - Pôster / Solicitar materiais | Aceito - Pôster | Yes | Same issue as oral state. |
| `accepted_video` | Not visible | Aprovado - Vídeo | Not visible | Aceito - Vídeo / Solicitar materiais | Aceito - Vídeo | Yes | Same issue as oral state. |
| `rejected` | Not visible | Rejeitado | Not visible | Rejeitado | Rejeitado | No | Labels align. |

## Final-Material and Proceedings Statuses

| Internal state | Public visitor | Author | Reviewer | Chair | Admin/staff | Intended asymmetry? | Notes |
|---|---|---|---|---|---|---|---|
| `final_materials_pending` | Not visible | Materiais finais pendentes / Enviar materiais | Not visible | Materiais pendentes / Aguardando envio | Materiais pendentes | Yes | Request e-mail and form requirements need alignment; see CCR1-007. |
| `ready_for_proceedings` | Should not be public unless intentionally released | Pronto para anais | Not visible | Validados / Publicar | Pronto para anais | Yes | Public proceedings currently includes this state; see CCR1-005. |
| `published_in_proceedings` | Publicado nos anais | Publicado nos anais | Not visible | Publicados | Publicado nos anais | Yes | Public and author labels align. |
| `FinalMaterial.received_at` set | Not visible | Materiais enviados/recebidos | Not visible | Recebidos | Recebidos | Yes | Notification may duplicate on repeated upload; see CCR1-004. |
| `FinalMaterial.validated_at` set | Public only after publication decision | Pronto para anais | Not visible | Validados | Validados | Yes | Needs clear distinction from publication. |
| `FinalMaterial.publication_authorized = false` | Not visible | Autorização pendente | Not visible | Sem autorização | Sem autorização | Yes | Validation correctly blocks ready-for-proceedings without authorization. |

## Review Assignment Statuses

| Internal state | Public visitor | Author | Reviewer | Chair | Admin/staff | Intended asymmetry? | Notes |
|---|---|---|---|---|---|---|---|
| Assignment exists without review | Not visible | Em avaliação | Avaliar | Pendente / assigned reviewer | Pendente | Yes | Reviewer dashboard uses action label instead of raw assignment state. |
| Review submitted | Not visible | Em avaliação until decision | Avaliação enviada | Concluída | Concluída | Yes | Public author decision bundle excludes reviewer identity and confidential notes. |
| Recommendation `accept` | Not visible | Appears only after decision as approved state | Aceitar | Aceitar | Aceitar | Yes | Recommendation is advisory, not the decision. |
| Recommendation `corrections` | Not visible | May appear as reviewer feedback after decision | Aceitar com correções | Aceitar com correções | Aceitar com correções | Yes | Needs policy decision if exposed to authors. |
| Recommendation `reject` | Not visible | Appears only after decision as rejected state | Rejeitar | Rejeitar | Rejeitar | Yes | No reviewer identity exposed to author. |

## Unintentional Asymmetries

- `CCR1-006`: report/indicator rows expose raw machine status codes.
- `CCR1-008`: chair-facing templates reuse author-facing labels for accepted states.
- `CCR1-005`: public proceedings copy says published works while the query includes ready-for-proceedings items.
