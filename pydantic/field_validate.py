from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    name: str
    email: EmailStr  # 이메일 형식이 아닌 데이터는 오류 발생


try:
    user = User(id=1, name="Jane Doe", email="invalid-email")
except ValueError as e:
    print(e)
