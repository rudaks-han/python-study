import asyncio
import time
from functools import wraps
from typing import Annotated

from pydantic import BaseModel, Field
from pydantic.alias_generators import to_camel, to_snake

from fastapi import FastAPI, Query


def elapsed_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print("Sync execution time:", (end_time - start_time))
        return result

    return wrapper


def elapsed_time_async(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        print("Async execution time:", (end_time - start_time))
        return result

    return wrapper


app = FastAPI()

"""
main thread에서 실행
await를 사용할 수 없고 pause될 수 없다.
순차적으로 실행
Request 1
    start
    end
Request 2
    start
    end
"""


@app.get("/async_sync")
@elapsed_time_async
async def async_sync():  # processed sequentially
    print("start")
    time.sleep(3)  # Blocking I/O Operation, cannot be await
    # Function execution cannot be paused
    print("end")
    return "ok"


"""
main thread에서 실행
await를 사용할 수 있고 paused될 수 있다.
Request 1
    start
Request 2
    start
Request 1
    end
Request 2
    end
"""


@app.get("/async_async")
@elapsed_time_async
async def async_async():  # processed concurrently
    print("start")
    await asyncio.sleep(3)  # Non-blocking I/O Operation
    # Function execution paused
    print("end")
    return "ok"


"""
개발 thread에서 실행, 병렬로 실행되어야 함.
"""


@app.get("/sync")
@elapsed_time
def sync_sync():  # processed concurrently
    print("start")
    time.sleep(3)
    print("end")
    return "ok"


# Uvicorn > Main Thread
# Uvicorn을 실행하면 하나의 쓰레드로 실행한다. main thread라고 한다.
# async를 사용하는 Coroutines은 main thread의 event loop에서 실행된다.


"""
BEST PRACITCE
1. non-blocking I/O operation에서는 async를 사용하자.
2. blocking I/O operation에서는 async를 사용하지 말자.
3. blocking I/O operation에서는 기본 함수를 사용하자. (예: await를 지원하지 않는 DB 라이브러리, time.sleep)
"""



class UserCdo(BaseModel):
    # user_id: str = Field(..., alias='userId')
    user_id: Annotated[str, Field(alias="userId")]
    name: str

    class Config:
        alias_generator = to_snake
        populate_by_name = True  # 필드 이름을 사용해 값 할당 허용

class User(BaseModel):
    user_id: str
    name: str

class UserRdo(BaseModel):
    # user_id: str
    user_id: str = Field(description="Bot 아이디", alias="userId")
    name: str

    class Config:
        alias_generator = to_camel
        populate_by_name = True  # 필드 이름을 사용해 값 할당 허용


@app.get("/camelcase")
def camelcase():
    user = User(user_id="rudaks", name="루닥스")
    user_rdo = UserRdo(user_id=user.user_id, name=user.name)
    # user_rdo = UserRdo(user)

    return user_rdo

@app.post("/camelcase")
def camelcase(
        user_cdo: UserCdo
):
    print(user_cdo)
    print("user_id:", user_cdo.user_id)



@app.get("/users/{user_id}")
def find_user(user_id: int):
    return {"user_id": user_id}
