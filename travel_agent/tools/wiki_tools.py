import requests
import wikipediaapi


def get_wiki_summary(topic: str, lang: str = "en", max_images: int = 3) -> dict:
    """
    Retrieve a short summary paragraph and up to `max_images` image URLs
    from Wikipedia (tries lang → fallback to he/en).
    """
    try:
        wiki = wikipediaapi.Wikipedia(lang)
        page = wiki.page(topic)
        if not page.exists():
            # try the other language
            alt = "he" if lang == "en" else "en"
            wiki = wikipediaapi.Wikipedia(alt)
            page = wiki.page(topic)
            if not page.exists():
                return {"status": "error", "error_message": f'"{topic}" not found'}

        media_api = f"https://{lang}.wikipedia.org/api/rest_v1/page/media/{page.title}"
        imgs, grabbed = [], requests.get(media_api, timeout=10)
        if grabbed.status_code == 200:
            for item in grabbed.json().get("items", []):
                if item.get("type") == "image" and "src" in item:
                    imgs.append(item["src"])
                if len(imgs) >= max_images:
                    break

        return {
            "status": "success",
            "title": page.title,
            "summary": page.summary,
            "images": imgs,
        }
    except Exception as exc:
        return {"status": "error", "error_message": str(exc)}
