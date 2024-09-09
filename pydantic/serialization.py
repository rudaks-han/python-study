from pydantic import BaseModel
from typing import List


class Item(BaseModel):
    name: str
    price: float


class ShoppingCart(BaseModel):
    items: List[Item]
    total_price: float


cart = ShoppingCart(
    items=[Item(name="Laptop", price=1200), Item(name="Mouse", price=25)],
    total_price=1225,
)

# Python 객체로 변환
cart_dict = cart.model_dump()
print(cart_dict)
print(type(cart_dict))

# JSON 문자열로 변환
cart_json = cart.model_dump_json()
print(cart_json)
print(type(cart_json))

cart_json = '{"items": [{"name": "Laptop", "price": 1200}], "total_price": 1200}'
cart_dict = {
    "items": [{"name": "Laptop", "price": 1200}],
    "total_price": 1200,
}
cart_raw = ShoppingCart.model_validate(cart_dict)
print(cart_raw)
print(type(cart_raw))  # <class '__main__.ShoppingCart'>


cart_raw = ShoppingCart.model_validate_json(cart_json)
print(cart_raw)
print(type(cart_raw))  # <class '__main__.ShoppingCart'>
