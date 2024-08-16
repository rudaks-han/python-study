from typing import Optional

from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel, EmailStr

response_model_router = APIRouter(prefix="/response_model")


class User(BaseModel):
    id: int
    name: str
    # email: str
    # email: EmailStr
    email: Optional[str] = None

    # id: int = Field(description="The unique identifier of the user", example=123)
    # name: str = Field(..., description="The name of the user", example="John Doe")
    # email: str = Field(
    #     ..., description="The email address of the user", example="john.doe@example.com"
    # )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"id": 123, "name": "John Doe", "email": "john.doe@example.com"}
            ]
        }
    }


@response_model_router.get(
    "/user/{user_id}", response_model=User, response_model_exclude_unset=True
)
def get_user(user_id: int):
    # return {"id": user_id, "name": "John Doe", "email": "john.doe@example.com"}
    return {"id": user_id, "name": "John Doe"}
