from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


user_data = {
    "id": "123",  # 문자열로 제공된 숫자도 자동으로 변환됨
    "name": "John Doe",
    "email": "john.doe@example.com",
}

user = User(**user_data)
print(user)
