from google.adk import Agent
from google.genai import types
from google.adk.tools import google_search

MODEL = "gemini-2.5-flash"

search_agent = Agent(
    name="search_agent",
    model=MODEL,
    description="Agent that answers users questions through a google search",
    instruction= 
        "When prompted by the user to use a google search, answer the users question through a google search."
        "Include 'Google Search Called For: ' and then the answer",
    tools=[google_search],

)