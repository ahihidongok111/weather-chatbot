from langchain_core.tools import tool
from typing import Annotated
from services.weather import process_location
from langchain.agents import AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import LLMChain

@tool
def get_weather_data(location: Annotated[str, "location to get weather data"]) -> Annotated[dict, "weather data in JSON format"]:
    """Input a location and returns its weather data in JSON format, including maximum, minimum temperature (in Celsius)
    and UV index for the next 7 days.
    When parsing the input, the agent must parse the city or the country name (not both).
    Do not try to use other tools for extracting information from the JSON output."""
    try:
        return process_location(location=location)
    except Exception:
        return {}


def load_agent():
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.2-3B-Instruct",
        task='text-generation'
    )

    tools = [get_weather_data]

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Use conversational agent type
        memory=memory,  # Add memory to agent
        verbose=False
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