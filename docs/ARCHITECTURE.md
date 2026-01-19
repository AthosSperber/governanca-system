# Visão Geral da Arquitetura

## Visão geral do fluxo

O sistema opera com um protocolo canônico que organiza toda execução em três artefatos:

1. **Task** — define objetivo, restrições e contexto.
2. **Action** — consolida instruções operacionais derivadas da Task.
3. **Report** — registra o resultado executado e auditado.

A governança coordena esse fluxo e mantém rastreabilidade ponta a ponta.

## Mapa de componentes

- **Protocol** (`core/protocol.py`): modelos estáveis para Task / Action / Report.
- **Governance** (`core/governance.py`): orquestração e logging append-only.
- **Agents** (`agents/*.py`): papéis institucionais (Executor, Auditor, Creative).
- **Applications**:
  - `academia` — métricas históricas básicas.
  - `academia_simulation` — simulação hipotética com comparação numérica.
  - `academia_visualization` — HTML estático com histórico, simulação e comparação.
  - `conexao_solar` — snapshot governado em JSON para consumo externo.

## Traceability e audit trail

- Cada execução gera eventos correlacionados por IDs.
- Os eventos são registrados de forma append-only em `memory/events.jsonl`.
- O relatório é produzido e auditado no mesmo fluxo, preservando origem e contexto.

## Regras de separação epistêmica (histórico vs simulação)

- **Histórico** contém apenas dados observados (fato).
- **Simulação** contém apenas hipóteses controladas, nunca evidência.
- Não há mistura de dados históricos com simulados.
- A comparação é **numérica** e descritiva, sem interpretação ou decisão.

## Diagrama resumido

```
Task -> Action -> Report
          |
          v
Governance (append-only) -> memory/events.jsonl

Agents: Executor | Auditor | Creative
Applications: academia | academia_simulation | academia_visualization | conexao_solar
```
