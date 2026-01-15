from __future__ import annotations

import uuid
from datetime import datetime, timezone

from core.protocol import Task


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def create_academia_simulation_mission() -> Task:
    return Task(
        id=str(uuid.uuid4()),
        created_at=_utc_now_iso(),
        objective="simulação hipotética de capacidade em ambiente de academia",
        constraints=[
            "não inferir causa",
            "não recomendar ações",
            "não interpretar resultados",
            "não misturar simulação com histórico",
        ],
        context="academia_simulation",
    )
