# Notification Trigger Consistency - Round 1

## Metadata

- Change: `verify-cross-page-content-consistency`
- Reviewed commit: `d3044e5`
- Review basis: `notifications/services.py`, notification templates, `submissions/views.py`, `reviews/views.py`, `proceedings/views.py`.

## Trigger Matrix

| Notification type | Trigger | Pre-state | Post-state | Recipient | Subject terminology | Body terminology | Dashboard state after trigger | Duplicate-send risk | Status |
|---|---|---|---|---|---|---|---|---|---|
| Account welcome | `post_save(User)` on create | User absent | User created | User e-mail | `Bem-vindo(a) ao CBNV 2026` | Hardcoded full event name and panel URL | Dashboard redirect by role | Low; only create signal | Pass with hardcoded URL risk |
| Role assignment | `notify_role_assignment` helper | User exists | Role assigned externally | User e-mail | `Novo papel atribuído` | Role labels `Revisor(a)`/`Membro da Comissão Científica` | Reviewer/chair dashboard by role | Unknown; helper has no durable sent marker | Needs workflow confirmation |
| Submission confirmation | `wizard_step3` after `submission.submit()` | `draft` | `submitted` | Corresponding author | `Submissão recebida` | Uses `status_label`, says initial video is not required | Author dashboard shows `Enviado` | Medium; repeat POST after state change redirects without send, but no durable sent marker if exception/retry | Partial: CCR1-004 |
| Reviewer assignment | `assign_reviewers` after assignments created | Usually `admin_screening` or submitted queue | `assigned_to_reviewers` only from `admin_screening` | Selected reviewers | `Nova atribuição de revisão` | Provides ID/title/eixo and panel instruction | Reviewer dashboard lists assignment | Medium; sends to selected reviewers with assignments, but no explicit sent flag | Partial: CCR1-004 |
| Decision notification | `issue_decision` after transition to accepted/rejected | `decision_pending` or reviews completed | accepted/rejected state | Corresponding author | `Decisão da submissão` | Uses author-facing status label; includes public review comments, excludes confidential notes and identities | Author dashboard shows final decision | Low; transition prevents repeated same decision in normal flow | Pass |
| Final-material request | `request_materials` after transition | accepted oral/poster/video | `final_materials_pending` | Corresponding author | `Materiais finais solicitados` | Lists PDF final, presentation and optional YouTube link | Author dashboard shows upload action | Low/medium; transition prevents repeat but no sent marker | Partial: CCR1-007 |
| Final-material received | Author upload valid POST | `final_materials_pending` | Still `final_materials_pending`; `received_at` updated | Corresponding author | `Materiais finais recebidos` | Says committee will validate | Author upload page stays open; chair sees received timestamp | High; every valid re-upload can resend | Fail: CCR1-004 |
| Final-material validated | Chair validates materials | `final_materials_pending`, final PDF + authorization | `ready_for_proceedings` | Corresponding author | `Materiais finais validados` | Says ready for proceedings, await official publication | Author dashboard shows `Pronto para anais` | Low; transition prevents repeat | Pass |
| Proceedings published | Chair publishes | `ready_for_proceedings` | `published_in_proceedings` | Corresponding author | `Publicado nos anais` | Links to `/anais/<submission_id>/` | Public detail/download available | Low; transition prevents repeat | Pass |

## Findings

- `CCR1-003`: event facts in notification templates are hardcoded instead of coming from canonical settings.
- `CCR1-004`: several notification types lack durable idempotence markers; final-material received is the highest duplicate-send risk.
- `CCR1-007`: final-material request copy and upload validation do not agree on whether presentation upload is strictly required.

## Recommended Future Checks

- Unit test that every notification template receives canonical event context.
- Unit test that final-material received notification is not sent twice for repeated uploads unless the product explicitly wants a new confirmation per replacement.
- Unit test that decision e-mails never include reviewer identity or confidential notes.
