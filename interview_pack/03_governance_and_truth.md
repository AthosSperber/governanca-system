# Governança e Verdade

## Por que governança existe

Governança garante que o sistema produza saídas auditáveis, neutras e rastreáveis. Ela evita que o software apresente opinião ou conclusão implícita, preservando o caráter factual dos relatórios.

## Fato vs Hipótese

- **Fatos**: derivados de dados históricos observados.
- **Hipóteses**: derivados de datasets simulados, claramente rotulados.
- **Comparações**: numéricas e descritivas, sem inferência.

## Auditabilidade

- Cada evento é registrado em `memory/events.jsonl`.
- IDs correlacionáveis permitem rastrear Task → Action → Report.
- Auditoria é mecânica e verifica conformidade de linguagem, não semântica.

## Agentes como papéis institucionais

- **Executor** executa e registra.
- **Auditor** valida restrições de linguagem.
- **Creative** contribui com ideias sem inferência ou decisão.
