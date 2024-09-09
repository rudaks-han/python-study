from pydantic import BaseModel


class UserORM:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class User(BaseModel):
    id: int
    name: str

    model_config = {"from_attributes": True}


user_orm = UserORM(id=1, name="Bob")
user = User.model_validate(user_orm)
print(user.model_dump())
