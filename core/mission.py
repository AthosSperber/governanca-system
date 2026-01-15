from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MissionSpec:
    name: str
    description: str
