from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List

DEFAULT_DATA_PATH = Path(__file__).with_name("data.csv")


def load_records(csv_path: str | Path = DEFAULT_DATA_PATH) -> List[Dict[str, str]]:
    path = Path(csv_path)
    with path.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [row for row in reader]
