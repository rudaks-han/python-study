from pydantic import BaseModel
from typing import List, Dict


class Item(BaseModel):
    name: str
    price: float


class ShoppingCart(BaseModel):
    items: List[Item]
    discounts: Dict[str, float]


cart = ShoppingCart(
    items=[Item(name="Laptop", price=1200), Item(name="Mouse", price=25)],
    discounts={"SUMMER_SALE": 0.1},
)
print(cart)
