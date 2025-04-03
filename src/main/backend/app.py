from fastapi import FastAPI
from pydantic import BaseModel
from services.llm import load_agent

app = FastAPI()
agent = load_agent()

class Query(BaseModel):
    # Each query consists of a message
    message: str

@app.post("/chatbot/")
def get_response(query: Query) -> dict:
    # Get and process the query, return a JSON response.
    response = agent.run(query.message)
    return {'response': response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)