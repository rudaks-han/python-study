from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    name: str


class UserRdo(BaseModel):
    user_id: str
    name: str
