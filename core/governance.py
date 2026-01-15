from __future__ import annotations

import uuid

from core.protocol import Task, Action, Report
from agents.executor import ExecutorAgent
from agents.auditor import AuditorAgent


class Governance:
    def __init__(self, executor: ExecutorAgent | None = None, auditor: AuditorAgent | None = None) -> None:
        self._executor = executor or ExecutorAgent()
        self._auditor = auditor or AuditorAgent()

    def run(self, task: Task) -> Report:
        action = self._create_action(task)
        report = self._executor.execute(action)
        audited = self._auditor.audit(report)
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
            instructions=instructions,
        )
