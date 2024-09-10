from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    # app_name: str
    # admin_email: str
    # items_per_user: int
    secret_key: str

    # class Config:
    #     env_file = "../.env"  # 환경 변수를 정의한 파일 지정
    model_config = {
        "env_prefix": "MYAPP_"
    }

config = AppConfig(_env_file="../.env")
# print(config.app_name)
# print(config.admin_email)
# print(config.items_per_user)
print(config.secret_key)
