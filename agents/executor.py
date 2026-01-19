from __future__ import annotations

import uuid
from datetime import datetime, timezone

from applications.academia.metrics import build_academia_metrics
from applications.academia.mission import create_academia_mission
from applications.academia_simulation.mission import create_academia_simulation_mission
from applications.academia_simulation.simulator import run_academia_simulation
from applications.academia_visualization.renderer import render_academia_visualization
from applications.conexao_solar.metrics import build_conexao_solar_metrics
from applications.conexao_solar.snapshot import render_conexao_solar_snapshot
from agents.auditor import AuditorAgent
from core.protocol import CONSTITUTION_PATH, CONSTITUTION_VERSION, Action, Report, Task


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class ExecutorAgent:
    def execute(self, action: Action) -> Report:
        context = self._extract_context(action.instructions)
        details = {
            "action_id": action.id,
            "task_id": action.task_id,
            "context": context,
            "execution_mode": "neutral",
            "constitution": {
                "version": CONSTITUTION_VERSION,
                "path": CONSTITUTION_PATH,
            },
        }
        report_status = "ok"
        report_created_at = _utc_now_iso()
        if context == "academia":
            details["context_route"] = "academia"
            details["metrics"] = build_academia_metrics()
        elif context == "academia_simulation":
            details["context_route"] = "academia_simulation"
            details.update(run_academia_simulation())
        elif context == "academia_visualization":
            details["context_route"] = "academia_visualization"
            auditor = AuditorAgent()
            historical_task = create_academia_mission()
            simulation_task = create_academia_simulation_mission()
            historical_action = self._create_action(historical_task)
            simulation_action = self._create_action(simulation_task)
            historical_report = self.execute(historical_action)
            simulation_report = self.execute(simulation_action)
            audited_historical = auditor.audit(historical_task, historical_report)
            audited_simulation = auditor.audit(simulation_task, simulation_report)
            details["source_reports"] = {
                "historical_report_id": audited_historical.id,
                "simulation_report_id": audited_simulation.id,
            }
            details["audit_status"] = {
                "historical": audited_historical.status,
                "simulation": audited_simulation.status,
            }
            details["labels"] = [
                "HISTÓRICO",
                "SIMULAÇÃO (HIPÓTESE)",
                "COMPARAÇÃO (DIFERENÇAS NUMÉRICAS)",
            ]
            if (
                audited_historical.status == "approved"
                and audited_simulation.status == "approved"
            ):
                details["output_paths"] = render_academia_visualization(
                    audited_historical,
                    audited_simulation,
                )
            else:
                details["output_paths"] = {}
                details["visualization_status"] = "rejected"
        elif context == "conexao_solar":
            details["context_route"] = "conexao_solar"
            details["metrics"] = build_conexao_solar_metrics()
            snapshot_path = render_conexao_solar_snapshot(
                details["metrics"],
                generated_at=report_created_at,
            )
            details["output_paths"] = {
                "governed_snapshot": str(snapshot_path),
            }
        summary = "Execution completed with neutral reporting."
        return Report(
            id=str(uuid.uuid4()),
            action_id=action.id,
            created_at=report_created_at,
            summary=summary,
            details=details,
            status=report_status,
        )

    def _extract_context(self, instructions: str) -> str:
        lowered = instructions.lower()
        if "context:" not in lowered:
            return "unknown"
        after = lowered.split("context:", 1)[1].strip()
        context = after.split(".", 1)[0].strip()
        return context or "unknown"

    def _create_action(self, task: Task) -> Action:
        instructions = (
            f"Objective: {task.objective}. "
            f"Constraints: {', '.join(task.constraints)}. "
            f"Context: {task.context}."
        )
        return Action(
            id=str(uuid.uuid4()),
            task_id=task.id,
            created_at=_utc_now_iso(),
            instructions=instructions,
        )
