from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass(frozen=True)
class Task:
    id: str
    objective: str
    constraints: List[str]
    context: str


@dataclass(frozen=True)
class Action:
    id: str
    task_id: str
    instructions: str


@dataclass(frozen=True)
class Report:
    id: str
    action_id: str
    summary: str
    details: Dict[str, Any]
    status: str
