# governanca-system

Sistema de governança com protocolo explícito, rastreabilidade por eventos e agentes com papéis institucionais.

## What is Governance System

Governanca-system é um núcleo operacional que assegura fluxo, restrições e rastreabilidade para aplicações que operam sob um protocolo canônico de mensagens.

## Core Architecture

- **Protocol**: mensagens estáveis (Task / Action / Report) com IDs e timestamps.
- **Governance**: orquestração do fluxo e logging append-only.
- **Agents**: papéis institucionais (Executor, Auditor, Creative) sem decisão ou recomendação.
- **Applications**: módulos contextuais conectados via Executor.

## Protocol (Task / Action / Report)

- **Task**: descreve objetivo, restrições e contexto.
- **Action**: consolida instruções operacionais a partir da Task.
- **Report**: registra o resultado executado e auditado.

## Agents as Institutional Roles

- **Executor**: produz saídas estruturadas e neutras.
- **Auditor**: valida constraints com auditoria mecânica.
- **Creative**: gera ideias em contexto sem inferência.

## Append-only Audit Logs

A governança grava eventos em `memory/events.jsonl`, mantendo histórico contínuo e correlacionável por IDs.

## Application Example: Academia

A aplicação `academia` carrega um CSV simples e produz métricas históricas básicas (total de registros, contagem por equipamento e por horário).

## Roadmap

- **Project 2: Simulation**
- **Project 3: Visualization**

## Architectural Foundations & References

- Clean Architecture — Robert C. Martin
- Separation of Concerns — Edsger Dijkstra
- Event Logs / Data Lineage — Martin Kleppmann
- Command / Message Pattern — GoF
- Multi-Agent Systems (roles, not intelligence) — Wooldridge

## What This System Is NOT

- Not an AI decision maker
- Not a recommender system
- Not a predictive engine
- Not a dashboard-first product
