from google.adk.agents import Agent
from travel_agent.tools.image_tools import get_destination_images
image_agent = Agent(
    name="image_agent",
    model="gemini-2.0-flash",
    description="Retrieves representative image URLs for the destination.",
    instruction="Call get_destination_images(topic, n) and return the dict.",
    tools=[get_destination_images],
)
