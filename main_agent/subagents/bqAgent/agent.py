from google.adk import Agent
from google.genai import types
import time
from google.adk.tools.agent_tool import AgentTool
from ..search_agent import search_agent

MODEL = "gemini-2.5-flash"

def handle_bigquery_question(question: str) -> dict:
    """
    Waits for 5 seconds and answers the user's question about BigQuery.

    Args:
        question (str): The user's question about BigQuery.

    Returns:
        dict: A dictionary containing an acknowledgment message.
    """   
    wait(5)
    print("I have waited for 5 seconds")

    return {
        "status": "success",
        "message": "Acknowledged. I will provide the answer after a 5 second delay.",
        "generate_content_config": types.GenerateContentConfig(
            temperature=1,
        )
    }

def wait(seconds: int):
    print("waiting...")
    time.sleep(seconds)
    print("done waiting")


bq_agent = Agent(
    name="bq_agent",
    model=MODEL,
    description="Answer BQ related questions",
    instruction=
        "You are an expert in Big Query. "
        "Your primary goal is to provide factual information about Big Query concepts and features to the user. "
        "Have the LLM call the timer tool and print in the terminal 'I have waited for 5 seconds'"
        "After printing in the terminal that you have waited for 5 seconds, give the user the answer to their question."
        "If the user indicates they want the answer using a Google Search, or if you are insufficient in the knowledge, perform a Google Search and indicate that you did so in your response."
        "Be sure to include 'I have waited 5 seconds' in your answer",

    tools=[handle_bigquery_question, 
        AgentTool(search_agent)],

)
