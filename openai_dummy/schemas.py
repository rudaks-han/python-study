from typing import List, Optional, Union, Any
from pydantic import BaseModel
from datetime import datetime


class CompletionUsage(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int


class LogProbs(BaseModel):
    pass


class Choice(BaseModel):
    text: str = "This is a test."
    finish_reason: str = "stop"
    index: int = 0
    logprobs: LogProbs = None


class ChatCompletionRequestMessage(BaseModel):
    content: str
    role: str
    name: str = None


class FunctionObject(BaseModel):
    description: str = None
    name: str
    parameters: str = None


class ChatCompletionTool(BaseModel):
    type: str
    function: FunctionObject


class ChatCompletionToolChoiceOption(BaseModel):
    pass


class ChatCompletionFunctions(BaseModel):
    description: str = None
    name: str
    parameters: Any = None


class CreateChatCompletionRequest(BaseModel):
    messages: List[ChatCompletionRequestMessage] = [
        {"content": "Hello", "role": "system"}
    ]
    model: Union[str, List[str]] = "gpt-4o"
    frequency_penalty: Optional[float] = 0
    logit_bias: Optional[dict[int, int]] = None
    logprobs: Optional[bool] = False
    top_logprobs: Optional[int] = None
    max_tokens: Optional[int] = None
    n: Optional[int] = 1
    presence_penalty: Optional[float] = 0
    response_format: Optional[dict[str, str]] = None
    seed: Optional[int] = None
    stop: Optional[Union[str, List[str]]] = None
    stream: Optional[bool] = False
    temperature: Optional[float] = 1
    top_p: Optional[float] = 1
    tools: Optional[List[ChatCompletionTool]] = None
    tool_choice: Optional[ChatCompletionToolChoiceOption] = None
    user: Optional[str] = None  # TODO: Replace with the actual schema
    function_call: Optional[bool] = None
    functions: Optional[List[ChatCompletionFunctions]] = None


class CreateChatCompletionResponse(BaseModel):
    id: str
    choices: List[Choice] = [
        {"text": "This is a test.", "finish_reason": "stop", "index": 0}
    ]
    created: int
    model: str
    system_fingerprint: str
    object: str
    usage: CompletionUsage


class CreateCompletionRequest(BaseModel):
    model: Union[str, List[str]]
    prompt: Union[str, List[str], List[int], List[List[int]]] = ""
    best_of: Optional[int] = 1
    echo: Optional[bool] = False
    frequency_penalty: Optional[float] = 0
    logit_bias: Optional[dict] = None
    logprobs: Optional[int] = None
    max_tokens: Optional[int] = 16
    n: Optional[int] = 1
    presence_penalty: Optional[float] = 0
    seed: Optional[int] = None
    stop: Optional[Union[str, List[str]]] = None
    stream: Optional[bool] = False
    suffix: Optional[str] = None
    temperature: Optional[float] = 1
    top_p: Optional[float] = 1
    user: Optional[str] = None


class CreateCompletionResponse(BaseModel):
    id: str = "cmpl-8oiZRYUm7TUCwqSj4lv8vABmoiBTy"
    choices: list[Choice] = [Choice()]
    created: float = 12345
    model: str = "gpt-4o"
    system_fingerprint: str = ""
    object: str = "chat.completion"
    usage: CompletionUsage = CompletionUsage(
        prompt_tokens=5, completion_tokens=6, total_tokens=11
    )
