import requests


def get_destination_images(topic: str, n: int = 4, lang: str = "en") -> dict:
    """
    Get up to `n` representative image URLs for `topic`.
    Falls back to Unsplash source if Wikipedia has none.
    """
    try:
        url = f"https://{lang}.wikipedia.org/api/rest_v1/page/media/{topic}"
        resp = requests.get(url, timeout=10)
        pics = []
        if resp.status_code == 200:
            for item in resp.json().get("items", []):
                if item.get("type") == "image" and "src" in item:
                    pics.append(item["src"])
                if len(pics) >= n:
                    break
        if not pics:  # graceful fallback
            pics.append(f"https://source.unsplash.com/featured/?{topic}")
        return {"status": "success", "images": pics[:n]}
    except Exception as exc:
        return {"status": "error", "error_message": str(exc)}
