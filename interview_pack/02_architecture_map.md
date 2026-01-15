# Mapa de Arquitetura

## Núcleo

- **Protocol** (`core/protocol.py`): modelos estáveis para Task / Action / Report.
- **Governance** (`core/governance.py`): orquestração do fluxo e logging append-only.
- **Agents** (`agents/*.py`): papéis institucionais (Executor, Auditor, Creative).

## Aplicações

- **academia**: métricas históricas básicas.
- **academia_simulation**: simulação hipotética com comparação numérica.
- **academia_visualization**: HTML estático com histórico, simulação e comparação.

## Fluxo

1. **Task** define objetivo, restrições e contexto.
2. **Action** consolida instruções operacionais.
3. **Report** registra execução e auditoria.
4. **Governance** grava eventos append-only em `memory/events.jsonl`.

## Fatos vs Hipóteses

- Histórico e simulação não são misturados.
- Comparações são numéricas, sem interpretação.
