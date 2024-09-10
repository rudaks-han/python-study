from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from schemas import *

app = FastAPI(
    title="DWorks AI Mock Server",
    version="0.5.0",
    description="DWorks AI Mock Server for test",
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat/completions", response_model=CreateChatCompletionResponse)
def create_chat_completion(request_body: CreateChatCompletionRequest):
    print("_______ create_chat_completion")
    res = CreateCompletionResponse(model="gpt-4o", object="text_completion")
    print(res)
    return res


@app.post("/completions", response_model=CreateCompletionResponse)
def create_completion(request_body: CreateCompletionRequest):
    print("_______ create_completion")
    # TODO: Implement the function to return the completion
    res = CreateCompletionResponse(model="gpt-3.5-turbo-0613", object="text_completion")
    return res
