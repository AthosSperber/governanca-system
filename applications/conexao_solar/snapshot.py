from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Dict, List


def render_conexao_solar_snapshot(
    metrics: List[Dict[str, float | int | str]],
    generated_at: str,
    output_dir: str | Path = "output",
) -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    snapshot = {
        "schema_version": "0.1",
        "domain": "conexao_solar",
        "nature": "historical",
        "generated_at": generated_at,
        "source": {
            "repo": "AthosSperber/governanca-system",
            "commit": _resolve_commit_sha(),
            "events_log": "memory/events.jsonl",
        },
        "metrics": metrics,
        "notes": [
            "Reference domain: values are mock/demo",
            "Historical and simulation must never be mixed; comparisons are numeric-only",
        ],
        "links": {
            "report_html": "",
            "repo_consumer": "AthosSperber/ConexaoSolar",
        },
    }
    snapshot_path = output_path / "governed_snapshot_conexao_solar.json"
    snapshot_path.write_text(
        json.dumps(snapshot, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return snapshot_path


def _resolve_commit_sha() -> str:
    env_sha = os.getenv("GITHUB_SHA") or os.getenv("GIT_SHA")
    if env_sha:
        return env_sha
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"
    return result.stdout.strip() or "unknown"
