from google.adk import Agent
from google.genai import types
import time


MODEL = "gemini-2.5-flash"

def handle_gce_question(question: str) -> dict:
    """
    Handles questions related to Compute Engine and answers after a 5 second delay.

    Args:
        question (str): The user's question about Compute Engine.

    Returns:
        dict: An acknowledgment message.
    """   
    time.sleep(5)
    print("I have waited for 5 seconds")

    return {
        "status": "success",
        "response": "Acknowledged. I will provide the answer after a 5 second delay.",
        "generate_content_config": types.GenerateContentConfig(
            temperature=1,
        )
    }


gce_agent = Agent(
    name="gce_agent",
    model=MODEL,
    description="Answer GCE related questions",
    instruction=
        "You are an expert in Compute Engine. "
        "Your primary goal is to provide factual information about Compute Engine concepts and features to the user. "
        "Have the LLM call the timer tool and print in the terminal 'I have waited for 5 seconds'"
        "After printing in the terminal that you have waited for 5 seconds, give the user the answer to their question.",
    tools=[handle_gce_question],
)