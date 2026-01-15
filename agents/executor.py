from __future__ import annotations

import uuid

from core.protocol import Action, Report


class ExecutorAgent:
    def execute(self, action: Action) -> Report:
        summary = "Simulated execution completed without inference."
        details = {
            "action_received": action.instructions,
            "execution_mode": "placeholder",
        }
        return Report(
            id=str(uuid.uuid4()),
            action_id=action.id,
            summary=summary,
            details=details,
            status="executed",
        )
