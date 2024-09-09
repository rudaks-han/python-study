from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str = Field(..., example="Smartphone")
    price: float = Field(..., example=699.99)


print(Item.model_json_schema(by_alias=True))
