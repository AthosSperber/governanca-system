# Roadmap v0.2 — Controlled Evolution

## Issue principal

- **Issue**: Roadmap v0.2 — Controlled Evolution
- **Milestone**: v0.2

## Issues filhas (propostas)

1. **Schema validation for governed snapshots**
   - Validação automática do schema JSON (contrato mínimo + campos opcionais).
2. **Multi-domain publishing**
   - Publicar múltiplos snapshots governados sem conflitar com o Pages.
3. **Signed artifacts**
   - Assinatura/verificação de artefatos JSON e HTML.
4. **Review signals UI**
   - Expor sinais de revisão em páginas estáticas do Pages.
5. **Simulation domain hardening**
   - Reforçar limites de simulação e proibir mistura com histórico.

---

## InsureRoadmap v2

### Critérios de aceite (verificáveis)

- JSON governado publicado no GitHub Pages.
- Consumer app renderiza o snapshot sem quebrar o build.
- Histórico ≠ simulação (separação explícita em artefatos).
- Eventos append-only registrados em `memory/events.jsonl`.
- Documentação atualizada com links e comandos de geração.

### Sinais de revisão

- Verificar `docs/REVIEW_SIGNALS.md` para checklist de revisão e sinais críticos.

### Non-goals v0.2

- Não criar backend/API.
- Não introduzir decisões automatizadas.
- Não criar dashboards prescritivos.
