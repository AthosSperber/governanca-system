from __future__ import annotations

import json
from dataclasses import asdict

from core.governance import Governance
from applications.academia.mission import create_academia_mission


def main() -> None:
    governance = Governance()
    task = create_academia_mission()
    final_report = governance.run(task)
    print(json.dumps(asdict(final_report), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
