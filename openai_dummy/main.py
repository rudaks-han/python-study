from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from schemas import *

app = FastAPI(
    title="DWorks AI Mock Server",
    version="0.5.0",
    description="DWorks AI Mock Server for test",
)

response_json = {
    "id": "dummy-id",
    "object": "chat.completion",
    "created": 1234567890,
    "model": "gpt-3.5-turbo",
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": f"Dummy response",
            },
            "finish_reason": "stop",
            "index": 0,
        }
    ],
    "usage": {"prompt_tokens": 10, "completion_tokens": 10, "total_tokens": 20},
}


@app.post("/v1/chat/completions")
def create_chat_completion(request_body: CreateChatCompletionRequest):
    print("_______ create_chat_completion")
    return response_json


@app.post("/completions")
def create_completion(request_body: CreateCompletionRequest):
    print("_______ create_completion")
    # TODO: Implement the function to return the completion
    res = CreateCompletionResponse(model="gpt-3.5-turbo-0613", object="text_completion")
    return res
