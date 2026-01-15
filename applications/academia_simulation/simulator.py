from __future__ import annotations

import csv
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Dict, List

from applications.academia.loader import load_records
from applications.academia.metrics import DEFAULT_DATA_PATH, build_academia_metrics


def run_academia_simulation(
    csv_path: str | Path = DEFAULT_DATA_PATH,
    capacity_increment: int = 2,
) -> Dict[str, object]:
    historical_metrics = build_academia_metrics(csv_path)
    records = load_records(csv_path)
    equipment_names = _collect_equipment_names(records)
    capacity_adjustments = {name: capacity_increment for name in equipment_names}
    simulated_records = _build_simulated_records(records, capacity_adjustments)
    simulated_metrics = _build_metrics_from_records(simulated_records)
    factual_differences = _build_factual_differences(
        historical_metrics, simulated_metrics
    )
    scenario_parameters = {
        "capacity_increment": capacity_increment,
        "capacity_adjustments": capacity_adjustments,
        "simulation_dataset": "registros sintéticos com timestamp vazio",
    }
    return {
        "scenario_parameters": scenario_parameters,
        "historical_metrics": historical_metrics,
        "simulated_metrics": simulated_metrics,
        "factual_differences": factual_differences,
    }


def _collect_equipment_names(records: List[Dict[str, str]]) -> List[str]:
    names = {record.get("equipment") or "unknown" for record in records}
    return sorted(names)


def _build_simulated_records(
    records: List[Dict[str, str]],
    adjustments: Dict[str, int],
) -> List[Dict[str, str]]:
    simulated = list(records)
    for equipment, increment in adjustments.items():
        for _ in range(max(increment, 0)):
            simulated.append({"timestamp": "", "equipment": equipment})
    return simulated


def _build_metrics_from_records(
    records: List[Dict[str, str]],
) -> Dict[str, Dict[str, int] | int]:
    with NamedTemporaryFile("w", delete=False, encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["timestamp", "equipment"])
        writer.writeheader()
        writer.writerows(records)
        temp_path = Path(handle.name)
    try:
        return build_academia_metrics(temp_path)
    finally:
        temp_path.unlink(missing_ok=True)


def _build_factual_differences(
    historical: Dict[str, Dict[str, int] | int],
    simulated: Dict[str, Dict[str, int] | int],
) -> Dict[str, object]:
    return {
        "total_records": _diff_scalar(
            historical.get("total_records", 0),
            simulated.get("total_records", 0),
        ),
        "count_by_equipment": _diff_mapping(
            historical.get("count_by_equipment", {}),
            simulated.get("count_by_equipment", {}),
        ),
        "count_by_hour": _diff_mapping(
            historical.get("count_by_hour", {}),
            simulated.get("count_by_hour", {}),
        ),
    }


def _diff_scalar(historical: object, simulated: object) -> Dict[str, int]:
    historical_value = int(historical or 0)
    simulated_value = int(simulated or 0)
    return {
        "historical": historical_value,
        "simulated": simulated_value,
        "difference": simulated_value - historical_value,
    }


def _diff_mapping(
    historical: object,
    simulated: object,
) -> Dict[str, Dict[str, int]]:
    historical_map = dict(historical) if isinstance(historical, dict) else {}
    simulated_map = dict(simulated) if isinstance(simulated, dict) else {}
    keys = sorted(set(historical_map) | set(simulated_map))
    return {
        key: _diff_scalar(historical_map.get(key, 0), simulated_map.get(key, 0))
        for key in keys
    }
