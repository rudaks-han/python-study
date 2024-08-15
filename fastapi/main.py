from enum import Enum
from typing import Optional

from fastapi import FastAPI, Query
from pydantic import BaseModel

from request_body_handler import request_body

app = FastAPI()
app.include_router(request_body)


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

@app.get("/items/")
async def read_items(name: str = Query(..., min_length=3, max_length=50)):
    return {"name": name}

@app.get("/search/")
async def search_items(query: Optional[str] = Query(None, min_length=3, max_length=50)):
    return {"query": query}