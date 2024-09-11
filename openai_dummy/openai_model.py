import json
from typing import List, Union, Optional

from pydantic import BaseModel


class ChatCompletionRequestMessage(BaseModel):
    content: str
    role: str
    name: str = None


class CreateChatCompletionRequest(BaseModel):
    messages: List[ChatCompletionRequestMessage]
    model: Union[str, List[str]] = "gpt-4o"
    temperature: Optional[float] = 1
    stream: Optional[bool] = False


class Choice(BaseModel):
    text: str = "This is a test."
    finish_reason: str = "stop"
    index: int = 0


class CompletionUsage(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int


class CreateChatCompletionResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[Choice]
    usage: CompletionUsage

    @staticmethod
    def sample(content: str, finish_reason: str = None):
        return {
            "id": "chatcmpl-abc123",
            "object": "chat.completion",
            "created": 1677858242,
            "model": "gpt-4o",
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": content,
                    },
                    "finish_reason": finish_reason,
                    "index": 0,
                }
            ],
            "usage": {
                "prompt_tokens": 10,
                "completion_tokens": 10,
                "total_tokens": 20,
            },
        }
