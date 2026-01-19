from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from applications.conexao_solar.loader import DEFAULT_DATA_PATH, load_records


def build_conexao_solar_metrics(
    csv_path: str | Path = DEFAULT_DATA_PATH,
) -> List[Dict[str, float | int | str]]:
    records = load_records(csv_path)
    total_page_views = sum(_to_int(row.get("page_views")) for row in records)
    total_leads = sum(_to_int(row.get("leads")) for row in records)
    total_conversions = sum(_to_int(row.get("conversions")) for row in records)
    avg_time = _average(
        [_to_int(row.get("avg_time_on_page_seconds")) for row in records]
    )
    conversion_rate = total_conversions / total_leads if total_leads else 0.0

    return [
        {
            "key": "leads_7d",
            "label": "Leads (7d)",
            "value": total_leads,
            "unit": "count",
        },
        {
            "key": "conversion_rate_7d",
            "label": "Conversion Rate (7d)",
            "value": round(conversion_rate, 4),
            "unit": "ratio",
        },
        {
            "key": "page_views_7d",
            "label": "Page Views (7d)",
            "value": total_page_views,
            "unit": "count",
        },
        {
            "key": "avg_time_on_page_7d",
            "label": "Avg Time on Page (7d)",
            "value": avg_time,
            "unit": "seconds",
        },
    ]


def _to_int(value: str | None) -> int:
    if value is None:
        return 0
    try:
        return int(value)
    except ValueError:
        return 0


def _average(values: List[int]) -> int:
    if not values:
        return 0
    return round(sum(values) / len(values))
