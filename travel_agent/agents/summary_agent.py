from google.adk.agents import Agent
from travel_agent.tools.wiki_tools import get_wiki_summary
summary_agent = Agent(
    name="summary_agent",
    model="gemini-2.0-flash",
    description="Fetches a clean summary of the destination from Wikipedia.",
    instruction="Call get_wiki_summary(topic) and return the dict.",
    tools=[get_wiki_summary],
)
