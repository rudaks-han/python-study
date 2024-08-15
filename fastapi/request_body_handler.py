from fastapi import APIRouter

request_body = APIRouter(prefix="/request_body")

from pydantic import BaseModel


class Seller(BaseModel):
    name: str
    rating: float


class Item(BaseModel):
    name: str
    price: float
    # description: str = "No description provided"
    seller: Seller


@request_body.post("/items/")
def create_item(item: Item):
    # return {"name": item.name, "price": item.price}
    return item


@request_body.post("/categories/{category}/items/")
def create_item(category: str, item: Item, discount: float = 0.0):
    return {
        "category": category,
        "item": item,
        "discount": discount
    }