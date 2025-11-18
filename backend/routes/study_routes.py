from flask import Blueprint, render_template, request

from backend.services.study_service import (
    process_study_request,
    get_recent_history,
)

study_bp = Blueprint("study", __name__)


@study_bp.get("/")
def index():
    history = get_recent_history()
    return render_template("index.html", history=history)


@study_bp.post("/analyze")
def analyze():
    course_name = request.form.get("course_name", "")
    content_type = request.form.get("content_type", "")
    help_type = request.form.get("help_type", "")
    raw_text = request.form.get("raw_text", "")

    result = process_study_request(course_name, content_type, help_type, raw_text)

    if "error" in result:
        history = get_recent_history()
        return render_template(
            "index.html",
            history=history,
            error=result["error"],
            previous_form={
                "course_name": course_name,
                "content_type": content_type,
                "help_type": help_type,
                "raw_text": raw_text,
            },
        )

    return render_template("result.html", **result)