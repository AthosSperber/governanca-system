# governanca-system

![CI](https://github.com/AthosSperber/governanca-system/actions/workflows/ci.yml/badge.svg) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

O governanca-system é um sistema de governança com protocolo explícito e rastreabilidade por eventos.
Ele existe para garantir fluxo canônico (Task → Action → Report) e separar dados históricos de simulações.
As saídas são descritivas e auditáveis, mantendo linguagem neutra e comparações numéricas.
O objetivo é oferecer clareza operacional com rigor técnico, sem alterar fatos por hipótese.

Para navegação de documentos, veja o [Índice de Documentação](docs/README.md).

## Demo (no install)

GitHub Pages Demo: https://athossperber.github.io/governanca-system/

## Consumer App Example: Conexão Solar (React/TS)

- Repo consumidor: https://github.com/AthosSperber/ConexaoSolar
- Snapshot JSON (Pages): https://athossperber.github.io/governanca-system/governed_snapshot_conexao_solar.json
- Demo Pages: https://athossperber.github.io/governanca-system/

## What you can verify in 60 seconds

1. Abrir o link do demo.
2. Abrir o relatório Combined (domínio de referência: Academia).
3. Ver rótulos de separação explícita e a seção de comparação numérica.

## How to adopt this framework

- docs/FRAMEWORK.md
- docs/ADDING_A_DOMAIN.md
- docs/PROCESS.md
- docs/GOVERNANCE_GUARANTEES.md
- docs/REVIEW_SIGNALS.md

## Quickstart

> Dependências de runtime: nenhuma. O `requirements.txt` contém apenas `ruff` para lint.

```bash
python -m venv .venv
pip install -r requirements.txt
python main.py selftest
python main.py run --app academia
python main.py run --app academia_simulation
python main.py run --app academia_visualization
python main.py run --app conexao_solar
```

Os relatórios HTML são gerados em `output/`.

## What you get

- JSON de relatório no terminal.
- Log append-only em `memory/events.jsonl`.
- Relatórios HTML em `output/`.
- Snapshot governado em `output/governed_snapshot_conexao_solar.json`.

## Arquitetura em um olhar

```
Task -> Action -> Report
          |
          v
Governance (append-only) -> memory/events.jsonl

Agents: Executor | Auditor | Creative
Applications: academia | academia_simulation | academia_visualization | conexao_solar
```

## Projetos

- **Project 1 = Historical (Academia)**
- **Project 2 = Governed Simulation**
- **Project 3 = Governed Visualization**

Separação explícita: histórico ≠ simulação, comparação apenas numérica.

## Constitutional Authority

A autoridade máxima é a Constituição em `/constitution/GOVERNANCA_SYSTEM_CONSTITUTION.md`.
Qualquer artefato deve seguir a ordem de prioridade: Constituição → Regras de Negócio → UX → Implementação Técnica.

## Referências

- Edward Tufte — *The Visual Display of Quantitative Information*
- Martin Kleppmann — *Designing Data-Intensive Applications*
- Robert C. Martin — *Clean Architecture*
- Edsger Dijkstra — Separation of Concerns
- GoF — Command / Message Pattern
- Michael Wooldridge — Multi-Agent Systems

## Non-goals

- Não é um decisor automático.
- Não é um sistema prescritivo.
- Não é um motor preditivo.
- Não é um produto dashboard-first.
