# Travel Companion – Multi‑Agent Travel Planner

Tailored travel assistant that composes a destination summary, daily itinerary and illustrative images – all generated on‑the‑fly by a team of specialised agents running on Google ADK.

---

## Key Features

| Agent               | Responsibility                                                              |
| ------------------- | --------------------------------------------------------------------------- |
| `summary_agent`     | Fetches and cleans a concise description of the destination from Wikipedia  |
| `itinerary_agent`   | Builds a day‑by‑day plan according to trip length and user interests        |
| `image_agent`       | Retrieves royalty‑free image URLs representing the location                 |
| `file_writer_agent` | Compiles the above into a Markdown file (summary, itinerary, image gallery) |

The **root agent** (`travel_companion`) orchestrates the flow:

1. Receives *destination*, *days* and optional *comma‑separated interests*.
2. Delegates to the three specialised agents.
3. Returns a confirmation with the path to the generated `.md` file.

---

## Architecture

```
User ──► travel_companion (root)
          ├── summary_agent   ──► wikipedia_api
          ├── itinerary_agent ─► Gemini‑2.0‑Flash (Google Generative AI)
          ├── image_agent     ──► Unsplash / Wikimedia images
          └── file_writer_agent ─► Markdown file output
```

Agents communicate through ADK's `transfer_to_agent` mechanism; each agent is a standalone Python module under `travel_agent/agents`.

---

## Tech Stack

* Python 3.12
* Google ADK 1.5 – web server and agent runtime
* google‑generativeai – Gemini model access
* wikipedia‑api – lightweight Wikipedia scraper
* httpx / requests – outbound HTTP
* certifi – bundled CA certificates (handles Windows SSL issue)

---

## Quick Start

```bash
# Clone & enter
> git clone <repo_url>
> cd travel_agent

# Create virtual environment with Python 3.12
> py -3.12 -m venv .venv
> .venv\Scripts\activate

# Install dependencies and package
(.venv)> pip install -r requirements.txt
(.venv)> pip install -e .

# Add your API key(s)
(.venv)> copy .env.example .env
# → edit .env   (GOOGLE_API_KEY=...)

# Run locally
(.venv)> adk web --port 8080
# Open http://localhost:8080 and choose the Travel Companion app
```

### Docker (optional)

```bash
> docker build -t travel-companion .
> docker run -p 8080:8080 --env-file .env travel-companion
```

---

## Environment Variables

| Variable                                 | Description                                                                |
| ---------------------------------------- | -------------------------------------------------------------------------- |
| `GOOGLE_API_KEY`                         | Key for Gemini API (Google Generative AI)                                  |
| `SSL_CERT_FILE` and `REQUESTS_CA_BUNDLE` | Set automatically inside the virtual environment to certifi's `cacert.pem` |

---

## Repository Layout

```
travel_agent/
├─ agents/
│  ├─ root_travel_agent.py
│  ├─ summary_agent.py
│  ├─ itinerary_agent.py
│  └─ image_agent.py
├─ tools/
│  ├─ wiki_tools.py
│  ├─ itinerary_tools.py
│  └─ image_tools.py
├─ templates/
│  └─ output.md.jinja
├─ __init__.py   # exposes root_agent and fixes SSL env vars
└─ …
requirements.txt
setup.py
adk.yaml
README.md
```

---

## Usage Example

In the ADK UI send:

```
Destination: Barcelona
Days: 4
Interests: art, food, beaches
```

The system will reply with a confirmation and save `barcelona_4d.md` containing a destination overview, a four‑day plan and an image gallery with preview links.

---

## Development Notes

* Editable install (`pip install -e .`) lets you tweak agents without reinstalling.
* SSL certificates are copied automatically via `activate.bat`; on other operating systems simply rely on certifi.
* Tests can be added with `pytest`; mock external APIs for deterministic runs.

---

## License

MIT
