from __future__ import annotations

import uuid
from datetime import datetime, timezone

from core.protocol import Task


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def create_academia_visualization_mission() -> Task:
    return Task(
        id=str(uuid.uuid4()),
        created_at=_utc_now_iso(),
        objective="gerar visualização governada de relatórios históricos e simulados de academia",
        constraints=[
            "não recomendar ações",
            "não interpretar resultados",
            "não inferir causa",
            "não transformar visualização em argumento",
        ],
        context="academia_visualization",
    )
