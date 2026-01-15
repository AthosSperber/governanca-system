from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List

from applications.academia.loader import load_records

DEFAULT_DATA_PATH = Path(__file__).with_name("data.csv")


def build_academia_metrics(csv_path: str | Path = DEFAULT_DATA_PATH) -> Dict[str, Dict[str, int] | int]:
    records = load_records(csv_path)
    total_records = len(records)
    count_by_equipment = _count_by_key(records, "equipment")
    count_by_hour = _count_by_hour(records)
    return {
        "total_records": total_records,
        "count_by_equipment": count_by_equipment,
        "count_by_hour": count_by_hour,
    }


def _count_by_key(records: List[Dict[str, str]], key: str) -> Dict[str, int]:
    counts: Dict[str, int] = defaultdict(int)
    for record in records:
        value = record.get(key) or "unknown"
        counts[value] += 1
    return dict(counts)


def _count_by_hour(records: List[Dict[str, str]]) -> Dict[str, int]:
    counts: Dict[str, int] = defaultdict(int)
    for record in records:
        raw = record.get("timestamp") or ""
        hour = _parse_hour(raw)
        counts[hour] += 1
    return dict(counts)


def _parse_hour(raw: str) -> str:
    if not raw:
        return "unknown"
    try:
        parsed = datetime.fromisoformat(raw)
    except ValueError:
        return "unknown"
    return f"{parsed.hour:02d}:00"
