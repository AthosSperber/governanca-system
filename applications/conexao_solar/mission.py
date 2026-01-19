from __future__ import annotations

import uuid
from datetime import datetime, timezone

from core.protocol import Task


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def create_conexao_solar_mission() -> Task:
    return Task(
        id=str(uuid.uuid4()),
        created_at=_utc_now_iso(),
        objective="análise histórica de desempenho de landing page",
        constraints=[
            "não inferir causa",
            "não recomendar ações",
            "não misturar histórico com simulação",
        ],
        context="conexao_solar",
    )
