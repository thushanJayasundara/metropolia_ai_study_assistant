from dataclasses import dataclass


@dataclass
class HistoryEntry:
    id: int
    course_name: str
    help_type: str
    created_at: str