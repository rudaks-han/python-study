import json
import threading
import traceback

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from openai import base_url
from starlette.responses import StreamingResponse

from fastapi import FastAPI, Query

load_dotenv()

app = FastAPI()

llm = ChatOpenAI(
    temperature=0, model_name="gpt-4o-mini", base_url="http://localhost:7777/v1"
)

template = "{query}"
prompt = PromptTemplate.from_template(template=template)


@app.get("/sync/chat")
def sync_chat(query: str):
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"query": query})


@app.get("/async/chat")
async def async_chat(query: str = Query(None)):
    chain = prompt | llm
    return await chain.ainvoke({"query": query})


@app.get("/streaming_sync/chat")
def streaming_sync_chat(query: str):
    chain = prompt | llm | StrOutputParser()

    def event_stream():
        try:
            for chunk in chain.stream({"query": query}):
                yield f"data: {chunk}\n\n"
        except Exception as e:
            yield f"data: error : {str(e)}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@app.get("/streaming_async/chat")
async def streaming_async(query: str = Query(None, min_length=3, max_length=50)):
    chain = prompt | llm | StrOutputParser()

    async def event_stream():
        try:
            async for chunk in chain.astream({"query": query}):
                if len(chunk) > 0:
                    yield f"data: {chunk}\n\n"
        except Exception as e:
            yield f"data: {str(e)}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
