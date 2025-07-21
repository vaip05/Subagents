from google.adk import Agent
from google.genai import types
import time

MODEL = "gemini-2.5-flash"

def handle_sql_question(question: str) -> dict:
    """
    Handles questions related to Cloud SQL and answers after a 5 second delay.

    Args:
        question (str): The user's question about Cloud SQL.

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

sql_agent = Agent(
    name="sql_agent",
    model=MODEL,
    description="Answer SQL related questions",
    instruction=
        "You are an expert in Cloud SQL. "
        "Your primary goal is to provide factual information about Cloud SQL concepts and features to the user. "
        "Have the LLM call the timer tool and print in the terminal 'I have waited for 5 seconds'"
        "After printing in the terminal that you have waited for 5 seconds, give the user the answer to their question.",
    tools=[handle_sql_question],
)