from __future__ import annotations

import uuid
from datetime import datetime, timezone

from applications.academia.metrics import build_academia_metrics
from applications.academia_simulation.simulator import run_academia_simulation
from core.protocol import Action, Report


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
        }
        if context == "academia":
            details["context_route"] = "academia"
            details["metrics"] = build_academia_metrics()
        elif context == "academia_simulation":
            details["context_route"] = "academia_simulation"
            details.update(run_academia_simulation())
        summary = "Execution completed with neutral reporting."
        return Report(
            id=str(uuid.uuid4()),
            action_id=action.id,
            created_at=_utc_now_iso(),
            summary=summary,
            details=details,
            status="ok",
        )

    def _extract_context(self, instructions: str) -> str:
        lowered = instructions.lower()
        if "context:" not in lowered:
            return "unknown"
        after = lowered.split("context:", 1)[1].strip()
        context = after.split(".", 1)[0].strip()
        return context or "unknown"
