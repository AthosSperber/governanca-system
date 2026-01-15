from __future__ import annotations

import uuid

from core.protocol import Task


def create_academia_mission() -> Task:
    return Task(
        id=str(uuid.uuid4()),
        objective="análise histórica de equipamentos",
        constraints=[
            "não inferir causa",
            "não recomendar ações",
            "não interpretar dados",
        ],
        context="academia",
    )
