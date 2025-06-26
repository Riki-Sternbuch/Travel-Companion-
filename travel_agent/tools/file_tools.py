import os
from datetime import datetime
from typing import List
from jinja2 import Environment, FileSystemLoader


def _template():
    here = os.path.dirname(os.path.abspath(__file__))
    tmpl_dir = os.path.abspath(os.path.join(here, "..", "templates"))
    env = Environment(loader=FileSystemLoader(tmpl_dir), autoescape=False)
    return env.get_template("answer.md.jinja")


def save_to_file(topic: str,
                 wiki_summary: dict,
                 itinerary: dict,
                 images: List[str]) -> dict:
    """
    Render markdown via templates/answer.md.jinja and save to texts/<topic>.md
    """
    try:
        md = _template().render(
            title=wiki_summary.get("title", topic.title()),
            overview=wiki_summary.get("summary", ""),
            itinerary=itinerary.get("itinerary", ""),
            images=images,
        )

        root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        out_dir = os.path.join(root, "texts")
        os.makedirs(out_dir, exist_ok=True)
        fname = os.path.join(
            out_dir, f"{topic.lower().replace(' ', '_')}.md"
        )

        with open(fname, "w", encoding="utf-8") as fp:
            fp.write(f"<!-- Generated {datetime.utcnow().isoformat()}Z -->\n\n")
            fp.write(md)

        return {"status": "success", "filename": fname}
    except Exception as exc:
        return {"status": "error", "error_message": str(exc)}
