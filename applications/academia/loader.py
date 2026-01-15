from __future__ import annotations

import csv
from pathlib import Path
from typing import List, Dict


def load_records(csv_path: str | Path) -> List[Dict[str, str]]:
    path = Path(csv_path)
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return [row for row in reader]
