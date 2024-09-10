from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.language_models import FakeListLLM, FakeStreamingListLLM
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from starlette.responses import StreamingResponse

from fastapi import FastAPI, Query

load_dotenv()

app = FastAPI()

fake_responses = [
    "서울은 대한민국의 수도입니다. 대한민국의 정치, 경제, 문화의 중심지로서 중요한 역할을 하고 있습니다. 추가로 궁금한 사항이 있으시면 말씀해 주세요!"
]

llm = FakeListLLM(
    responses=fake_responses,
)
llm_streaming = FakeStreamingListLLM(responses=fake_responses)

template = "아래 질문에 대한 답변을 해주세요. \n{query}"
prompt = PromptTemplate.from_template(template=template)
chain = prompt | llm | StrOutputParser()
chain_streaming = prompt | llm_streaming | StrOutputParser()


@app.get("/sync/chat")
def sync_chat(query: str = Query(None, min_length=3, max_length=50)):
    response = chain.invoke({"query": query})
    return response


@app.get("/async/chat")
async def async_chat(query: str = Query(None, min_length=3, max_length=50)):
    response = await chain.ainvoke({"query": query})
    return response


@app.get("/streaming_sync/chat")
def streaming_sync_chat(query: str = Query(None, min_length=3, max_length=50)):
    def event_stream():
        try:
            for chunk in chain_streaming.stream({"query": query}):
                if len(chunk) > 0:
                    yield f"data: {chunk}\n\n"
        except Exception as e:
            yield f"data: {str(e)}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@app.get("/streaming_async/chat")
async def streaming_async(query: str = Query(None, min_length=3, max_length=50)):
    async def event_stream():
        try:
            async for chunk in chain_streaming.astream({"query": query}):
                if len(chunk) > 0:
                    yield f"data: {chunk}\n\n"
        except Exception as e:
            yield f"data: {str(e)}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
