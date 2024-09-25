from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from exception.custom_exception_handlers import (
    CustomException,
    custom_exception_handler,
    http_exception_handler,
    NotFoundException,
    not_found_exception_handler,
    validation_exception_handler,
)
from fastapi import FastAPI, HTTPException


app = FastAPI()

app.add_exception_handler(CustomException, custom_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(NotFoundException, not_found_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)


# @app.exception_handler(CustomException)
# async def custom_exception_handler(request: Request, exc: CustomException):
#     return JSONResponse(
#         status_code=400,
#         content={"message": f"An error occurred: {exc.name}"},
#     )


@app.get("/users")
async def find(
    user_id: str,
):
    if user_id == "not_found":
        raise HTTPException(status_code=404, detail="User not found")
    return user_id


@app.get("/users/{user_id}")
async def find_user(user_id: str):
    if user_id == "not_found":
        raise NotFoundException(user_id=user_id)
    return {"user_id": user_id}


@app.get("/custom_exception/{name}")
async def get_custom_exception(name: str):
    if name == "error":
        raise CustomException(name=name)
    return {"message": f"Hello, {name}"}
