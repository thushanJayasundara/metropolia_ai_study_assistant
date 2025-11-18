from textwrap import dedent

from openai import OpenAI
from backend import config


API_KEY = config.OPENAI_API_KEY
MODEL_NAME = config.OPENAI_MODEL
TEMPERATURE = config.TEMPERATURE
SYSTEM_MESSAGE = config.SYSTEM_MESSAGE


def build_prompt(course_name: str, content_type: str,
                 help_type: str, raw_text: str) -> str:
    base_context = f"""
    You are an AI study assistant for Metropolia University of Applied Sciences.
    Course: {course_name}
    Content type: {content_type}
    """

    if help_type == "summary":
        help_instructions = """
        Task: Create a concise summary with 5–10 bullet points.
        Focus on key concepts and definitions.
        """
    elif help_type == "explain":
        help_instructions = """
        Task: Explain the content to a beginner.
        Use simple language, short paragraphs, and examples.
        """
    elif help_type == "questions":
        help_instructions = """
        Task: Create 5–10 practice questions (mix of multiple-choice and
        open-ended) and then provide a short answer key.
        """
    elif help_type == "plan":
        help_instructions = """
        Task: Treat this as an assignment or project description and create
        a 7–14 day step-by-step study / implementation plan.
        """
    else:
        help_instructions = """
        Task: Provide a structured summary of the key ideas.
        """

    user_content = f"""
    STUDENT TEXT:
    \"\"\"{raw_text}\"\"\"
    """

    prompt = dedent(base_context + help_instructions + user_content)
    return prompt.strip()


def _call_openai_model(prompt: str) -> str:
    if not API_KEY:
        raise RuntimeError("OPENAI_API_KEY is not configured in backend/config.py")

    client = OpenAI(api_key=API_KEY)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": prompt},
        ],
        temperature=TEMPERATURE,
    )

    return response.choices[0].message.content.strip()


def _mock_ai_response(help_type: str, raw_text: str) -> str:
    preview = raw_text[:250].replace("\n", " ")
    if len(raw_text) > 250:
        preview += "..."

    return (
        "⚠️ Demo mode (no real AI key configured or API call failed).\n\n"
        f"Help type: {help_type}\n\n"
        f"Preview of your text:\n{preview}\n\n"
        "In a real deployment this would be a full AI-generated response."
    )


def generate_study_help(course_name: str, content_type: str,
                        help_type: str, raw_text: str) -> str:
    prompt = build_prompt(course_name, content_type, help_type, raw_text)
    try:
        return _call_openai_model(prompt)
    except Exception as exc:

        print("[AI ERROR]", exc)
        return _mock_ai_response(help_type, raw_text)