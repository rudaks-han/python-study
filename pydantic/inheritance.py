from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


class Admin(User):
    access_level: int


admin = Admin(id=1, name="Alice", access_level=5)
print(admin)
