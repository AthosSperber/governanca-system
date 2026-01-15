from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Literal

Status = Literal["ok", "approved", "rejected", "audited", "error"]

CONSTITUTION_VERSION = "1.1"
CONSTITUTION_PATH = "/constitution/GOVERNANCA_SYSTEM_CONSTITUTION.md"


@dataclass(frozen=True)
class Task:
    id: str
    created_at: str
    objective: str
    constraints: List[str]
    context: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class Action:
    id: str
    task_id: str
    created_at: str
    instructions: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class Report:
    id: str
    action_id: str
    created_at: str
    summary: str
    details: Dict[str, Any]
    status: Status

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
