# Academia Visualization

Aplicação governada para visualização estática e auditável dos relatórios aprovados dos projetos Academia (histórico) e Academia Simulation (simulação).

## Como executar

```bash
python main.py run --app academia_visualization
```

## Saídas geradas

Os arquivos HTML são gerados em `output/`:

- `report_academia_historical.html`
- `report_academia_simulation.html`
- `report_academia_combined.html`

## Regras de visualização

- Sem recomendação, interpretação ou inferência causal.
- Seções explícitas: HISTÓRICO, SIMULAÇÃO (HIPÓTESE) e COMPARAÇÃO.
- Tabelas simples e cards informativos com texto neutro.
