from urllib.request import Request

from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from fastapi import HTTPException


class CustomException(Exception):
    def __init__(self, name: str):
        self.name = name


class NotFoundException(Exception):
    def __init__(self, user_id: str):
        self.user_id = user_id


async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=400,
        content={"message": f"An error occurred: {exc.name}"},
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code, content={"detail": f"Oops! {exc.detail}"}
    )


async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404, content={"message": f"User with ID {exc.user_id} not found"}
    )


async def validation_exception_handler(request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400, content={"message": f"Value Error", "detail": str(exc)}
    )
