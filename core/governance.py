from __future__ import annotations

import json
import os
import uuid
from datetime import datetime, timezone

from agents.auditor import AuditorAgent
from agents.executor import ExecutorAgent
from core.protocol import Action, Report, Task


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class Governance:
    def __init__(
        self, executor: ExecutorAgent | None = None, auditor: AuditorAgent | None = None
    ) -> None:
        self._executor = executor or ExecutorAgent()
        self._auditor = auditor or AuditorAgent()
        self._log_path = os.path.join("memory", "events.jsonl")
        os.makedirs(os.path.dirname(self._log_path), exist_ok=True)

    def run(self, task: Task) -> Report:
        self._validate_task(task)
        self._log_event(
            event_type="task_received",
            task_id=task.id,
            payload=task.to_dict(),
        )
        action = self._create_action(task)
        self._validate_action(action)
        self._log_event(
            event_type="action_created",
            task_id=task.id,
            action_id=action.id,
            payload=action.to_dict(),
        )
        report = self._executor.execute(action)
        self._validate_report(report)
        self._log_event(
            event_type="report_created",
            task_id=task.id,
            action_id=action.id,
            report_id=report.id,
            payload=report.to_dict(),
        )
        audited = self._auditor.audit(task, report)
        self._validate_report(audited)
        self._log_event(
            event_type="report_audited",
            task_id=task.id,
            action_id=action.id,
            report_id=audited.id,
            payload=audited.to_dict(),
        )
        return audited

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

    def _log_event(
        self,
        event_type: str,
        task_id: str | None = None,
        action_id: str | None = None,
        report_id: str | None = None,
        payload: dict | None = None,
    ) -> None:
        entry = {
            "event_id": str(uuid.uuid4()),
            "event_type": event_type,
            "timestamp": _utc_now_iso(),
            "task_id": task_id,
            "action_id": action_id,
            "report_id": report_id,
            "payload": payload or {},
        }
        with open(self._log_path, "a", encoding="utf-8") as handle:
            handle.write(json.dumps(entry, ensure_ascii=False) + "\n")

    def _validate_task(self, task: Task) -> None:
        if not task.id or not task.created_at or not task.objective:
            raise ValueError("Task schema invalid")

    def _validate_action(self, action: Action) -> None:
        if not action.id or not action.task_id or not action.created_at:
            raise ValueError("Action schema invalid")

    def _validate_report(self, report: Report) -> None:
        if not report.id or not report.action_id or not report.created_at:
            raise ValueError("Report schema invalid")
