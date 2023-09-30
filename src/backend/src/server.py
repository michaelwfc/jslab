"""server.py
"""
from typing import Text
from fastapi import FastAPI
import uvicorn
from openai_utils import construct_messages, get_chat_completion

app = FastAPI()


@app.get("/")
def hello():
    return "Hello,chatbot python backend"


@app.post("/chat/openai")
def chat_openai(query: str) -> Text:
    """chat with openai api

    Args:
        query: _description_

    Returns:
        _description_
    """
    messages = construct_messages(query=query)
    response = get_chat_completion(messages=messages)
    return response


def run_server(host="0.0.0.0", port=7861):
    uvicorn.run(app, host=host, port=port, log_level="info")
