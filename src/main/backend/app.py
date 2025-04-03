from fastapi import FastAPI
from pydantic import BaseModel
from services.llm import load_agent
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

app = FastAPI()
agent = load_agent()

class Query(BaseModel):
    # Each query consists of a message
    message: str

@app.post("/chatbot/")
def get_response(query: Query) -> dict:
    # Get and process the query, return a JSON response.
    response = agent.run(query.message)
    print(type(response))
    return {'response': response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)