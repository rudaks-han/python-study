from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "Anonymous"  # 기본값 설정
    age: Optional[int] = None  # 선택적 필드


user = User(id=2)
print(user)
