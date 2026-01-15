from __future__ import annotations

from typing import Any, Iterable

from core.protocol import CONSTITUTION_PATH, CONSTITUTION_VERSION, Report, Task


class AuditorAgent:
    def __init__(self) -> None:
        self._forbidden_terms = [
            "recomendo",
            "sugiro",
            "deveria",
            "faça",
            "porque",
            "causa",
            "motivo",
            "razão",
            "melhor",
            "pior",
            "eficiente",
            "ruim",
        ]

    def audit(self, task: Task, report: Report) -> Report:
        violations = self._find_violations(report)
        audited_details = dict(report.details)
        audited_details["constitution"] = {
            "version": CONSTITUTION_VERSION,
            "path": CONSTITUTION_PATH,
        }
        if violations:
            audited_details["violations"] = violations
            status = "rejected"
        else:
            audited_details["audit"] = "approved"
            status = "approved"
        return Report(
            id=report.id,
            action_id=report.action_id,
            created_at=report.created_at,
            summary=report.summary,
            details=audited_details,
            status=status,
        )

    def _find_violations(self, report: Report) -> list[dict[str, Any]]:
        violations: list[dict[str, Any]] = []
        for path, value in self._walk("summary", report.summary):
            violations.extend(self._match_terms(path, value))
        for path, value in self._walk("details", report.details):
            violations.extend(self._match_terms(path, value))
        return violations

    def _walk(self, path: str, value: Any) -> Iterable[tuple[str, Any]]:
        if isinstance(value, dict):
            for key, item in value.items():
                yield from self._walk(f"{path}.{key}", item)
        elif isinstance(value, list):
            for index, item in enumerate(value):
                yield from self._walk(f"{path}[{index}]", item)
        else:
            yield path, value

    def _match_terms(self, path: str, value: Any) -> list[dict[str, Any]]:
        if not isinstance(value, str):
            return []
        lowered = value.lower()
        matches = []
        for term in self._forbidden_terms:
            if term in lowered:
                matches.append({"term": term, "path": path, "value": value})
        return matches
