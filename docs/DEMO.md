# Demonstração (CLI)

## Pré-requisitos

- Python disponível no ambiente.
- Executar os comandos na raiz do repositório.

## Passo a passo

1. **Self-test**
   ```bash
   python main.py selftest
   ```

2. **Executar aplicação histórica**
   ```bash
   python main.py run --app academia
   ```

3. **Executar simulação governada**
   ```bash
   python main.py run --app academia_simulation
   ```

4. **Gerar visualização governada**
   ```bash
   python main.py run --app academia_visualization
   ```

5. **Exibir logs append-only**
   ```bash
   python main.py show-logs
   ```

## Saídas esperadas (resumo)

- **Self-test**: confirmação de execução do protocolo e do fluxo de governança.
- **Academia (histórico)**: métricas agregadas em JSON no relatório.
- **Academia Simulation**: métricas simuladas e comparação numérica com histórico.
- **Academia Visualization**: arquivos HTML gerados em `output/`.
- **Show-logs**: linhas JSON correlacionadas por IDs.
