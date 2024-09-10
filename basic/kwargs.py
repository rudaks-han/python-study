import json

from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    name: str

    @staticmethod
    def sample():
        return User(
            user_id="rudaks",
            name="루닥스"
        )

class UserRdo(BaseModel):
    user_id: str = None
    name: str = None
    address: str = None

    @staticmethod
    def sample():
        # sample = User.sample().model_dump_json()
        sample = json.loads(User.sample().model_dump_json())
        return UserRdo(
            **sample,
            address="서울시 강남구"
        )

    def to_json(self):
        return json.loads(self.sample().model_dump_json())
print(UserRdo.sample().to_json())



