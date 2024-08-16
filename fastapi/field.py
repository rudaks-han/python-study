from typing import Annotated

from fastapi import APIRouter, Body

field_router = APIRouter(prefix="/field")

from pydantic import BaseModel, Field


# class Item(BaseModel):
#     name: str = Field(..., example="Apple MacBook Pro")
#     description: str | None = Field(None, example="A high-end laptop from Apple")
#     price: float = Field(..., example=1999.99)
#     tax: float | None = Field(None, example=19.99)


class Item(BaseModel):
    name: str = Field(...)
    description: str | None = Field(None)
    price: float = Field(...)
    tax: float | None = Field(None)

    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "name": "Foo",
    #                 "description": "A very nice Item",
    #                 "price": 35.4,
    #                 "tax": 3.2,
    #             }
    #         ]
    #     }
    # }


@field_router.post("/items/")
async def create_item(
    item: Annotated[
        Item,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            }
        ),
    ]
):
    return item


@field_router.post("/categories/{category}/items/")
def create_item(category: str, item: Item, discount: float = 0.0):
    return {"category": category, "item": item, "discount": discount}
