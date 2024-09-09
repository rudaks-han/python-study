from pydantic import BaseModel


class ConfigModel(BaseModel):
    setting_1: str
    setting_2: int

    model_config = {"validate_assignment": True}


from enum import Enum
from pydantic import BaseModel


class Status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class User(BaseModel):
    status: Status

    model_config = {
        "use_enum_values": True,
    }


user = User(status="active")
print(user.status)
