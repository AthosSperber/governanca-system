from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

from agents.auditor import AuditorAgent
from core.governance import Governance
from core.protocol import Action, Report, Task


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _build_task() -> Task:
    return Task(
        id=str(uuid.uuid4()),
        created_at=_utc_now_iso(),
        objective="teste de governança",
        constraints=["não inferir causa", "não recomendar ações", "não interpretar dados"],
        context="academia",
    )


def _build_action(task: Task) -> Action:
    return Action(
        id=str(uuid.uuid4()),
        task_id=task.id,
        created_at=_utc_now_iso(),
        instructions="Objective: teste. Constraints: neutro. Context: academia.",
    )


def _build_report(action: Action, summary: str, details: Dict[str, Any]) -> Report:
    return Report(
        id=str(uuid.uuid4()),
        action_id=action.id,
        created_at=_utc_now_iso(),
        summary=summary,
        details=details,
        status="ok",
    )


def run_selftests() -> Dict[str, Any]:
    results: Dict[str, Any] = {
        "auditor_rejects_forbidden": False,
        "auditor_approves_neutral": False,
        "governance_logs": False,
        "full_flow": False,
    }

    auditor = AuditorAgent()
    task = _build_task()
    action = _build_action(task)

    forbidden_report = _build_report(
        action,
        summary="Resumo neutro.",
        details={"note": "Recomendo atenção ao histórico."},
    )
    rejected = auditor.audit(task, forbidden_report)
    results["auditor_rejects_forbidden"] = rejected.status == "rejected" and "violations" in rejected.details

    neutral_report = _build_report(
        action,
        summary="Resumo neutro.",
        details={"note": "Registro histórico coletado."},
    )
    approved = auditor.audit(task, neutral_report)
    results["auditor_approves_neutral"] = approved.status == "approved" and approved.details.get("audit") == "approved"

    governance = Governance()
    final_report = governance.run(task)
    results["full_flow"] = final_report.status in {"approved", "rejected"}

    log_path = Path("memory") / "events.jsonl"
    if log_path.exists():
        with log_path.open("r", encoding="utf-8") as handle:
            lines = [json.loads(line) for line in handle if line.strip()]
        results["governance_logs"] = any(entry.get("task_id") == task.id for entry in lines)

    return results
