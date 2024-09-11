import os
import sys

from starlette.responses import StreamingResponse

from fastapi import FastAPI

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from openai_dummy.openai_model import (
    CreateChatCompletionRequest,
    CreateChatCompletionResponse,
)

app = FastAPI()


def event_stream(completion: str):
    try:
        for i, chunk in enumerate(completion):
            print(i, len(completion))
            if i == len(completion) - 1:
                finish_reason = "stop"
            else:
                finish_reason = None
            yield f"{CreateChatCompletionResponse.sample_json(chunk, finish_reason)}\n\n"
    except Exception as e:
        yield f"data: {str(e)}\n\n"


def send_response(request_body: CreateChatCompletionRequest):
    prompt = request_body.messages[0].content
    if request_body.stream:  # streaming을 사용할 경우
        completion = prompt + "'s response"
        return StreamingResponse(
            event_stream(completion), media_type="text/event-stream"
        )
    else:  # streaming이 아닌 경우
        return CreateChatCompletionResponse.sample_json(prompt)


@app.post("/v1/chat/completions")
def create_chat_completion(request_body: CreateChatCompletionRequest):
    return send_response(request_body)
