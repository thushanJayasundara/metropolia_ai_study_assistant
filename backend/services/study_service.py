from backend.ai.ai_service import generate_study_help
from backend.repositories.history_repository import (
    add_history_entry,
    get_recent_entries,
)


def process_study_request(course_name: str, content_type: str,
                          help_type: str, raw_text: str) -> dict:
    course_name = (course_name or "Unknown course").strip()
    content_type = (content_type or "General").strip()
    help_type = (help_type or "summary").strip()
    raw_text = (raw_text or "").strip()

    if not raw_text:
        return {"error": "Please paste some lecture notes or assignment text."}

    ai_output = generate_study_help(course_name, content_type, help_type, raw_text)

    add_history_entry(course_name, help_type)

    return {
        "course_name": course_name,
        "content_type": content_type,
        "help_type": help_type,
        "raw_text": raw_text,
        "ai_output": ai_output,
    }


def get_recent_history(limit: int = 5):
    return get_recent_entries(limit)