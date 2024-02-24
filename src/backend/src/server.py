"""server.py
"""
from typing import Text, Dict, List
from fastapi import FastAPI
import uvicorn
from openai_utils import construct_messages, get_chat_completion
from constants import GPT_3DOT5_TURBO
app = FastAPI()


@app.get("/")
def hello():
    return "Hello,chatbot python backend"


@app.post("/chat/openai")
def chat_openai(messages: List[Dict], model: Text = GPT_3DOT5_TURBO) -> Text:
    """chat with openai api

    Args:
        query: _description_

    Returns:
        _description_
    """
    response = get_chat_completion(messages=messages, model=model)
    return response


def run_server(host="0.0.0.0", port=7861):
    uvicorn.run(app, host=host, port=port, log_level="info")
