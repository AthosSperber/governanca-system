from __future__ import annotations

from core.protocol import Task


class CreativeAgent:
    def ideate(self, task: Task) -> list[str]:
        return [
            f"Idea 1 for context '{task.context}': preserve raw historical logs.",
            "Idea 2: visualize equipment timelines without conclusions.",
        ]
