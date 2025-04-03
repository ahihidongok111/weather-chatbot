# import os
from langchain_core.tools import tool
from typing import Annotated
from services.weather import process_location
from langchain.agents import AgentType, initialize_agent

# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "<your-huggingface-token>"

from langchain_huggingface import HuggingFaceEndpoint


@tool
def get_weather_data(location: Annotated[str, "location to get weather data"]) -> Annotated[dict, "weather data in JSON format"]:
    """Input a location and returns its weather data in JSON format, including maximum, minimum temperature (in Celsius)
    and UV index for the next 7 days."""
    return process_location(location=location)


def load_agent():
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.2-3B-Instruct",
    )

    tools = [get_weather_data]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent


if __name__ == "__main__":
    print("Welcome to the Weather Chatbot! Type 'exit' to stop.")
    agent = load_agent()
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = agent.run(user_input)
        print("Bot:", response)