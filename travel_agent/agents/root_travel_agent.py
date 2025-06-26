from google.adk.agents import Agent
from travel_agent.agents.summary_agent import summary_agent
from travel_agent.agents.itinerary_agent import itinerary_agent
from travel_agent.agents.image_agent import image_agent
from travel_agent.agents.file_writer_agent import file_writer_agent
root_travel_agent = Agent(
    name="travel_companion",
    model="gemini-2.0-flash",
    description="Tailored travel companion: summary + itinerary + images.",
    instruction=(
        "Receive from the user: destination, trip length in days, "
        "and optional comma-separated interests.\n"
        "1. Call summary_agent.\n"
        "2. Call itinerary_agent with destination, days & interests.\n"
        "3. Call image_agent for illustrative images.\n"
        "4. Send everything to file_writer_agent.\n"
        "Finally, reply with a short confirmation and the file path."
    ),
    sub_agents=[summary_agent, itinerary_agent, image_agent, file_writer_agent],
)
