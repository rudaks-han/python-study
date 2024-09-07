from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel, to_pascal

from fastapi import FastAPI

app = FastAPI()


class User(BaseModel):
    user_id: int = Field(description="아이디")
    user_name: str = Field(description="이름")
    age: int = Field(description="나이")
    favorite_foods: list[str] = Field(description="음식 리스트")

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        # from_attributes=True,
    )


@app.get("/users/{user_id}")
def find_user(user_id: int):
    return User(
        user_id=user_id, user_name="홍길동", age=20, favorite_foods=["apple", "banana"]
    )


@app.post("/users/")
def find_user(user: User):
    return user
