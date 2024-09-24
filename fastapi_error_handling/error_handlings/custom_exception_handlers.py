from typing import Optional


class CustomException(Exception):
    def __init__(
        self,
        status_code: int,
        error: bool,
        code: int,
        message: str,
        detail_message: str,
        module: str,
    ):
        self.status_code = status_code
        self.error = error
        self.code = code
        self.message = message
        self.detail_message = detail_message
        self.module = module


class ResourceNotFoundException(CustomException):
    """
    조회시 키값에 해당하는 데이터가 없는 경우 발생하는 예외
    """

    code: int = 400201
    error: bool = True
    message: str = (
        "The resource identified with the request's ``resourceId`` parameter cannot be found."
    )
    detail_message: str
    module: str = "aiadapter"

    def __init__(self, message: str, detail_message: Optional[str] = None):
        self.status_code = 400
        self.message = message
        self.detail_message = detail_message
