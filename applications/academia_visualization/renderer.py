from __future__ import annotations

from dataclasses import asdict
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from typing import Any, Dict, Iterable, List

from core.protocol import Report

NOTICE_TEXT = (
    "Este relatório é descritivo e auditável.<br>"
    "Não contém recomendações, decisões ou inferências causais.<br>"
    "Decisões são externas ao sistema."
)

LABEL_HISTORICAL = "HISTÓRICO"
LABEL_SIMULATION = "SIMULAÇÃO (HIPÓTESE)"
LABEL_COMPARISON = "COMPARAÇÃO (DIFERENÇAS NUMÉRICAS)"


def render_academia_visualization(
    report_historical: Report,
    report_simulation: Report,
    output_dir: Path | str = "output",
    template_path: Path | None = None,
) -> Dict[str, str]:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if template_path is None:
        template_path = Path(__file__).with_name("template.html")

    template = template_path.read_text(encoding="utf-8")

    historical_section = _build_historical_section(report_historical)
    simulation_section = _build_simulation_section(report_simulation)
    comparison_section = _build_comparison_section(report_simulation)
    traceability_section = _build_traceability_section(report_historical, report_simulation)

    historical_html = _render_html(
        template,
        title="Academia — Relatório Histórico",
        sections=[traceability_section, historical_section],
    )
    simulation_html = _render_html(
        template,
        title="Academia — Relatório de Simulação",
        sections=[traceability_section, simulation_section],
    )
    combined_html = _render_html(
        template,
        title="Academia — Relatório Combinado",
        sections=[traceability_section, historical_section, simulation_section, comparison_section],
    )

    historical_file = output_path / "report_academia_historical.html"
    simulation_file = output_path / "report_academia_simulation.html"
    combined_file = output_path / "report_academia_combined.html"

    historical_file.write_text(historical_html, encoding="utf-8")
    simulation_file.write_text(simulation_html, encoding="utf-8")
    combined_file.write_text(combined_html, encoding="utf-8")

    return {
        "historical": str(historical_file),
        "simulation": str(simulation_file),
        "combined": str(combined_file),
    }


def _render_html(template: str, title: str, sections: Iterable[str]) -> str:
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    sections_html = "\n".join(sections)
    return (
        template.replace("{{title}}", escape(title))
        .replace("{{generated_at}}", escape(generated_at))
        .replace("{{notice}}", NOTICE_TEXT)
        .replace("{{sections}}", sections_html)
    )


def _build_historical_section(report: Report) -> str:
    metrics = _extract_metrics(report, "metrics")
    cards = _build_cards({"Total de registros": metrics.get("total_records", 0)})
    equipment_table = _build_table_from_mapping(
        "Contagem por equipamento",
        metrics.get("count_by_equipment", {}),
    )
    hour_table = _build_table_from_mapping(
        "Contagem por horário",
        metrics.get("count_by_hour", {}),
    )
    return _wrap_section(
        LABEL_HISTORICAL,
        [cards, equipment_table, hour_table],
    )


def _build_simulation_section(report: Report) -> str:
    simulated_metrics = _extract_metrics(report, "simulated_metrics")
    parameters = report.details.get("scenario_parameters", {})
    parameter_table = _build_table_from_mapping(
        "Parâmetros de simulação",
        parameters,
    )
    cards = _build_cards({"Total de registros": simulated_metrics.get("total_records", 0)})
    equipment_table = _build_table_from_mapping(
        "Contagem por equipamento",
        simulated_metrics.get("count_by_equipment", {}),
    )
    hour_table = _build_table_from_mapping(
        "Contagem por horário",
        simulated_metrics.get("count_by_hour", {}),
    )
    return _wrap_section(
        LABEL_SIMULATION,
        [parameter_table, cards, equipment_table, hour_table],
    )


def _build_comparison_section(report: Report) -> str:
    differences = report.details.get("factual_differences", {})
    total_records = differences.get("total_records", {})
    total_table = _build_table(
        "Diferença total de registros",
        [
            {
                "Histórico": total_records.get("historical", 0),
                "Simulação": total_records.get("simulated", 0),
                "Diferença": total_records.get("difference", 0),
            }
        ],
    )
    equipment_diff = _build_table_from_nested_mapping(
        "Diferença por equipamento",
        differences.get("count_by_equipment", {}),
    )
    hour_diff = _build_table_from_nested_mapping(
        "Diferença por horário",
        differences.get("count_by_hour", {}),
    )
    return _wrap_section(
        LABEL_COMPARISON,
        [total_table, equipment_diff, hour_diff],
    )


def _build_traceability_section(report_historical: Report, report_simulation: Report) -> str:
    rows = [
        {"Fonte": LABEL_HISTORICAL, "Report ID": report_historical.id},
        {"Fonte": LABEL_SIMULATION, "Report ID": report_simulation.id},
    ]
    table = _build_table("Rastreabilidade", rows)
    return _wrap_section("RASTREABILIDADE", [table])


def _build_cards(values: Dict[str, Any]) -> str:
    cards = []
    for label, value in values.items():
        cards.append(
            "<div class=\"card\">"
            f"<div class=\"meta\">{escape(str(label))}</div>"
            f"<div><strong>{escape(str(value))}</strong></div>"
            "</div>"
        )
    return f"<div class=\"cards\">{''.join(cards)}</div>"


def _build_table_from_mapping(title: str, mapping: Dict[str, Any]) -> str:
    rows = [{"Item": key, "Valor": mapping[key]} for key in sorted(mapping)]
    return _build_table(title, rows)


def _build_table_from_nested_mapping(title: str, mapping: Dict[str, Any]) -> str:
    rows: List[Dict[str, Any]] = []
    for key in sorted(mapping):
        entry = mapping[key] if isinstance(mapping[key], dict) else {}
        rows.append(
            {
                "Item": key,
                "Histórico": entry.get("historical", 0),
                "Simulação": entry.get("simulated", 0),
                "Diferença": entry.get("difference", 0),
            }
        )
    return _build_table(title, rows)


def _build_table(title: str, rows: List[Dict[str, Any]]) -> str:
    if not rows:
        rows = [{"Item": "", "Valor": ""}]
    headers = list(rows[0].keys())
    header_html = "".join(f"<th>{escape(str(header))}</th>" for header in headers)
    body_html = "".join(_build_row(headers, row) for row in rows)
    return (
        f"<h3>{escape(title)}</h3>"
        "<table>"
        f"<thead><tr>{header_html}</tr></thead>"
        f"<tbody>{body_html}</tbody>"
        "</table>"
    )


def _build_row(headers: List[str], row: Dict[str, Any]) -> str:
    cells = []
    for header in headers:
        value = row.get(header, "")
        cells.append(f"<td>{escape(str(value))}</td>")
    return f"<tr>{''.join(cells)}</tr>"


def _wrap_section(title: str, parts: Iterable[str]) -> str:
    content = "".join(part for part in parts if part)
    return f"<section class=\"section\"><h2>{escape(title)}</h2>{content}</section>"


def _extract_metrics(report: Report, key: str) -> Dict[str, Any]:
    payload = report.details.get(key, {})
    if isinstance(payload, dict):
        return payload
    if hasattr(payload, "to_dict"):
        return payload.to_dict()
    if hasattr(payload, "__dict__"):
        return asdict(payload)
    return {}
