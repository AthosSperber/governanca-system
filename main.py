from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from applications.academia.mission import create_academia_mission
from applications.academia_simulation.mission import create_academia_simulation_mission
from applications.academia_visualization.mission import (
    create_academia_visualization_mission,
)
from applications.conexao_solar.mission import create_conexao_solar_mission
from core.governance import Governance


def _run_app(app: str) -> None:
    governance = Governance()
    if app == "academia":
        task = create_academia_mission()
    elif app == "academia_simulation":
        task = create_academia_simulation_mission()
    elif app == "academia_visualization":
        task = create_academia_visualization_mission()
    elif app == "conexao_solar":
        task = create_conexao_solar_mission()
    else:
        raise ValueError(f"Aplicação não suportada: {app}")
    final_report = governance.run(task)
    print(json.dumps(asdict(final_report), ensure_ascii=False, indent=2))


def _show_logs() -> None:
    log_path = Path("memory") / "events.jsonl"
    if not log_path.exists():
        print("Nenhum log encontrado.")
        return
    with log_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            print(line.rstrip())


def _run_selftest() -> None:
    from core.selftest import run_selftests

    results = run_selftests()
    print(json.dumps(results, ensure_ascii=False, indent=2))


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Governança System CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Executar aplicação governada")
    run_parser.add_argument(
        "--app",
        required=True,
        choices=[
            "academia",
            "academia_simulation",
            "academia_visualization",
            "conexao_solar",
        ],
        help="Aplicação alvo",
    )

    subparsers.add_parser("show-logs", help="Exibir logs append-only")
    subparsers.add_parser("selftest", help="Executar auto-testes leves")

    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    if args.command == "run":
        _run_app(args.app)
    elif args.command == "show-logs":
        _show_logs()
    elif args.command == "selftest":
        _run_selftest()


if __name__ == "__main__":
    main()
