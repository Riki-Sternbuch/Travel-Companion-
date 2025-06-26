from google.adk.agents import Agent
from travel_agent.tools.file_tools import save_to_file
file_writer_agent = Agent(
    name="file_writer_agent",
    model="gemini-2.0-flash",
    description="Compiles summary, itinerary & images into a Markdown file.",
    instruction=(
        "Receive: topic, wiki_summary (dict), itinerary (dict), images (list[str]). "
        "Call save_to_file(...) and return its status dict."
    ),
    tools=[save_to_file],
)
