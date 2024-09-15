import json
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
        for i, token in enumerate(completion):
            if i == len(completion) - 1:
                finish_reason = "stop"
            else:
                finish_reason = None
            res = CreateChatCompletionResponse.sample_streaming(token, finish_reason)
            yield f"data: {json.dumps(res)}\n\n"
        yield "data: [DONE]\n\n"
    except Exception as e:
        yield f"error occurred\n\n"
        yield f"data: {str(e)}\n\n"


# async def _resp_async_generator(text_resp: str):
#     tokens = text_resp.split(" ")
#
#     for i, token in enumerate(tokens):
#         chunk = {
#             "id": i,
#             "object": "chat.completion.chunk",
#             "created": time.time(),
#             "model": "blah",
#             "choices": [{"delta": {"content": token + " "}}],
#         }
#         yield f"data: {json.dumps(chunk)}\n\n"
#         # await asyncio.sleep(0.01)
#     yield "data: [DONE]\n\n"


def send_response(request_body: CreateChatCompletionRequest):
    prompt = request_body.messages[0].content
    completion = f"{prompt}의 응답 내용"
    print("request_body.stream", request_body.stream)
    if request_body.stream:  # streaming을 사용할 경우
        return StreamingResponse(
            event_stream(completion),
            media_type="application/x-ndjson",
        )

    else:  # streaming이 아닌 경우
        return CreateChatCompletionResponse.sample(completion)


@app.post("/v1/chat/completions")
def create_chat_completion(request_body: CreateChatCompletionRequest):
    return send_response(request_body)
