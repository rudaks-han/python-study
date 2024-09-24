from typing import Annotated
from urllib.request import Request

from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from error_handlings.custom_exception_handlers import (
    ResourceNotFoundException,
    CustomException,
)
from fastapi import FastAPI, Query

app = FastAPI()


# app.add_exception_handler(RuntimeError, my_handler_for_runtime_error)
@app.exception_handler(CustomException)
async def uvicorn_exception_handler(request: Request, exc: CustomException):
    content = {
        "error": exc.error,
        "code": exc.code,
        "message": exc.message,
        "module": exc.module,
    }

    if exc.detail_message:
        content["detailMessage"] = exc.detail_message

    return JSONResponse(
        status_code=exc.status_code,
        content=content,
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(exc)
    return JSONResponse(
        status_code=400,
        content="value error....",
    )


@app.get("/users/{user_id}")
def find(
    user_id: str,
    name: Annotated[str, Query(description="검색어", min_length=1, max_length=512)],
):  # processed sequentially

    if user_id == "unknown":
        # raise HTTPException(status_code=400, detail="user unknown")
        raise RuntimeError("error 발생")
    elif user_id == "resourceNotFound":
        # raise HTTPException(status_code=400, detail="user unknown")
        # raise ResourceNotFoundException(
        #     status_code=400, resource_id="user1", detail_message="detail...."
        # )
        raise ResourceNotFoundException(
            "user not found",
        )
    return "ok"
