import sqlite3
from datetime import datetime

from backend.config import DB_PATH
from backend.models.history import HistoryEntry


def _get_connection():
    return sqlite3.connect(DB_PATH)


def _init_db():
    conn = _get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            help_type TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


_init_db()


def add_history_entry(course_name: str, help_type: str) -> None:
    conn = _get_connection()
    created_at = datetime.utcnow().isoformat(timespec="seconds")
    conn.execute(
        "INSERT INTO history (course_name, help_type, created_at) "
        "VALUES (?, ?, ?)",
        (course_name, help_type, created_at),
    )
    conn.commit()
    conn.close()


def get_recent_entries(limit: int = 5) -> list[HistoryEntry]:
    conn = _get_connection()
    cursor = conn.execute(
        """
        SELECT id, course_name, help_type, created_at
        FROM history
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,),
    )
    rows = cursor.fetchall()
    conn.close()

    return [
        HistoryEntry(
            id=row[0],
            course_name=row[1],
            help_type=row[2],
            created_at=row[3],
        )
        for row in rows
    ]