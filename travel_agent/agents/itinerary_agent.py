from google.adk.agents import Agent
from travel_agent.tools.itinerary_tools import build_itinerary

itinerary_agent = Agent(
    name="itinerary_agent",
    model="gemini-2.0-flash",
    description="Creates a daily travel plan tailored to trip length & interests.",
    instruction=(
        "Expect input keys: topic, days, interests (list[str]). "
        "Return build_itinerary(...) output unchanged."
    ),
    tools=[build_itinerary],
)
