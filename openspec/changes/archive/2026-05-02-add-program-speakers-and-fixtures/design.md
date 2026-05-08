## Context

O projeto XII CBNV 2026 já possui sua fundação técnica (Django/Wagtail), design system base (Tailwind CSS 4.2.4) e modelos editoriais (Proposal 03). Esta mudança foca na implementação da camada de dados e apresentação da programação científica e dos palestrantes.

## Goals / Non-Goals

**Goals:**
- Implementar modelos de dados normalizados para Dias, Sessões, Falas e Palestrantes como Snippets Wagtail.
- Criar `ProgramPage` que consome o componente `timeline.html` existente.
- Fornecer fixtures com a programação preliminar canônica (3 dias).
- Garantir que itens não confirmados sejam totalmente ocultos (sem slots vazios).

**Non-Goals:**
- Não criar `SpeakerIndexPage` — palestrantes aparecem inline na timeline.
- Não criar side-drawers, modais ou componentes JS customizados.
- Não implementar submissões de trabalhos.
- Não implementar painéis autenticados para autores ou revisores.

## Decisions

### D1: Modelagem no App `program`, 4 níveis
Modelos `ProgramDay`, `ProgramSession`, `ProgramTalk` e `Speaker` como Snippets no app `program`.
- **Rationale**: Mantém separação de domínios. Submissões futuras ligarão naturalmente a `ProgramTalk`.

### D2: Snippets Wagtail (não ModelAdmin)
Todos os modelos como Snippets. Em Wagtail 7, `ModelAdmin` foi removido. Snippets com FKs são a abordagem idiomática.
- **Rationale**: Admin funcional sem customização extra. Relações via FK nos panels.

### D3: Palestrantes Inline (sem SpeakerIndexPage)
Palestrantes aparecem apenas inline na timeline (nome + instituição + bio resumida). Sem página de perfil individual.
- **Rationale**: Menos código, menos manutenção. Usabilidade "less is more". Dados acessíveis no contexto da programação.

### D4: Zero Componentes JS Customizados
Sem side-drawers, modais Alpine.js, ou HTMX nesta fase. A timeline existente (`components/timeline.html`) é suficiente para exibir palestrantes inline.
- **Rationale**: Evitar complexidade de manutenção. O componente timeline já suporta `speaker`, `badge`, `description` por item.

### D5: Visibilidade Estrita — Confirmados Apenas
Itens com `status != confirmed` são totalmente omitidos do frontend. Sem slots vazios na timeline.
- **Rationale**: Slots vazios causam confusão. Se nada está confirmado para um horário, o horário simplesmente não aparece.

### D6: Layout Vertical Stack
Sessões paralelas renderizadas em pilha vertical (mesmo no desktop), cada uma com indicação de sala/local.
- **Rationale**: Simplicidade, responsividade, usabilidade > estética complexa.

### D7: Tipos de Atividade via ChoiceField
`ChoiceField` predefinido para tipos de atividade (plenária, palestra, sessão temática, pôsteres, oral, mesa-redonda, intervalo, etc.).
- **Rationale**: Estilo visual consistente (badges/cores) por tipo.

### D8: Fixture via Management Command
Dados preliminares carregados via management command (como `seed_cms.py`), não JSON fixture bruto.
- **Rationale**: Mais legível, mais fácil de atualizar quando dados mudarem. Relações FK resolvidas em código.

## Risks / Trade-offs

- **Relações FK em Snippets** → Admin é lista-based, não nested. Aceitável para volume esperado (~30 sessões, ~15 palestrantes).
- **Sem página de perfil do palestrante** → Se no futuro precisar de SEO individual, pode ser adicionado sem refactor nos dados.
