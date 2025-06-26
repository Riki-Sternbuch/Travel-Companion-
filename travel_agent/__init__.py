from travel_agent.agents.root_travel_agent import root_travel_agent
root_agent = root_travel_agent
import os
import certifi
os.environ["SSL_CERT_FILE"] = certifi.where()
__all__ = ["root_travel_agent"]