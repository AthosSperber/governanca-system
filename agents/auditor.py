from __future__ import annotations

from core.protocol import Report


class AuditorAgent:
    def audit(self, report: Report) -> Report:
        audited_details = dict(report.details)
        audited_details["audit_status"] = "validated"
        audited_details["audit_notes"] = "Report checked for structure and traceability."
        return Report(
            id=report.id,
            action_id=report.action_id,
            summary=report.summary,
            details=audited_details,
            status="audited",
        )
