import os
import certifi
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
os.environ["SSL_CERT_FILE"] = certifi.where()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
_llm = genai.GenerativeModel("gemini-2.0-flash")


def build_itinerary(topic: str, days: int = 3, interests=None) -> dict:
    """
    Build a markdown itinerary via Gemini. `interests` = list[str] or None.
    """
    interests = interests or []
    prompt = (
        f"Create a {days}-day itinerary for {topic}. "
        f"Focus on: {', '.join(interests) if interests else 'general sightseeing'}. "
        "Balance active & relaxed time, include transport tips and recommended food. "
        "Answer in simple Hebrew using markdown; start each day with '### Day X'."
    )
    try:
        res = _llm.generate_content(prompt)
        return {"status": "success", "itinerary": res.text}
    except Exception as exc:
        return {"status": "error", "error_message": str(exc)}
