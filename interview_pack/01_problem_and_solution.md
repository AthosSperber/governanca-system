# Problema & Solução

## Problema

- Sistemas analíticos frequentemente misturam fatos históricos com hipóteses, gerando confusão sobre o que é observação versus simulação.
- Visualizações e relatórios podem introduzir linguagem interpretativa, gerando conclusões implícitas.
- Sem um protocolo explícito, o histórico de decisões e resultados é difícil de auditar.

## Solução

- **Protocolo canônico (Task / Action / Report)** com IDs e timestamps para rastreabilidade completa.
- **Governança append-only** em `memory/events.jsonl`, mantendo cadeia de eventos correlacionável.
- **Separação epistêmica**: histórico (Projeto 1), simulação (Projeto 2) e visualização governada (Projeto 3) são outputs isolados.
- **Agentes como papéis institucionais**: Executor, Auditor e Creative, sem “decidir” ou recomendar.

## Resultado esperado

Transparência operacional, auditabilidade de ponta a ponta e comunicação clara entre fatos e hipóteses.
