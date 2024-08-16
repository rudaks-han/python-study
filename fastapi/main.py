import logging
import time
from datetime import datetime
from enum import Enum
from typing import Optional, Annotated

from fastapi import FastAPI, Query, Path, Body, Form, Depends, Request, HTTPException
from pydantic import BaseModel

from cookie import cookie_router
from datatype import datatype_router
from field import field_router
from formdata_router import formdata_router
from header_router import header_router
from request_body_handler import request_body
from response_model_router import response_model_router
from sql_alchemy import models, database, crud, schemas
from sql_alchemy.database import engine, SessionLocal
from sql_alchemy.schemas import UserCreate, User
from sqlalchemy.orm import Session

app = FastAPI()
app.include_router(request_body)
app.include_router(field_router)
app.include_router(datatype_router)
app.include_router(cookie_router)
app.include_router(header_router)
app.include_router(response_model_router)
app.include_router(formdata_router)
# app.include_router(path_operation_router)


@app.get("/")
def home():
    return "home"


@app.get("/users/me")
def find_me():
    return "me"


@app.get("/users/{user_id}")
def find_path_parameter(user_id):
    return f"path parameter: {user_id}"


@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: int):
    return {"user_id": user_id, "item_id": item_id}


class FruitName(str, Enum):
    apple = "apple"
    pear = "pear"
    banana = "banana"


@app.get("/fruits/{fruit_name}")
def get_fruit(fruit_name: FruitName):
    return {"fruit_name": fruit_name}


class ItemQuery(BaseModel):
    name: str
    category: str = "general"


# @app.get("/items")
# def read_items(query: ItemQuery):
#     return query.dict()


# @app.get("/items/")
# async def read_items(name: str = Query(..., min_length=3, max_length=50)):
#     return {"name": name}


@app.get("/search/")
async def search_items(query: Optional[str] = Query(None, min_length=3, max_length=50)):
    return {"query": query}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: int = Path(..., title="The ID of the item to update"),
    q: str | None = Query(None, max_length=50),
    item: Item = Body(..., embed=True),
):
    results = {"item_id": item_id, "item": item}
    if q:
        results.update({"q": q})
    return results


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}


# @app.get("/items/", response_description="모든 item 목록")
# def get_items():
#     return {
#         "items": [
#             {"name": "item1", "description": "샘플 아이템"},
#             {"name": "item2", "description": "또 다른 샘플 아이템"},
#         ]
#     }


@app.get("/users/", tags=["users"])
def get_users():
    return {"users": ["user1", "user2"]}


@app.get("/old-endpoint/", deprecated=True, summary="삭제될 예정입니다.")
def old_endpoint():
    return {
        "message": "This endpoint is deprecated and will be removed in future versions."
    }


class Item(BaseModel):
    name: str
    price: float
    created_at: datetime


# @app.post("/items/", response_model=Item)
# async def create_item(item: Item):
#     # json_compatible_item_data = jsonable_encoder(item)
#     # return json_compatible_item_data
#     return item
#
#
# @app.post("/items2/", response_model=Item)
# async def create_item(item: Item):
#     json_compatible_item_data = jsonable_encoder(item)
#     print("type(item)", type(item))  # Item
#     print("type(json_compatible_item_data)", type(json_compatible_item_data))  # dict
#     return item


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/request")
async def request():
    return "ok"


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


logging.basicConfig(level=logging.DEBUG)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"Request URL: {request.url.path}")
    response = await call_next(request)
    logging.info(f"Response status code: {response.status_code}")
    return response


# 데이터베이스와 연결을 설정
models.Base.metadata.create_all(bind=engine)


# 의존성 주입: 요청마다 데이터베이스 세션을 생성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
