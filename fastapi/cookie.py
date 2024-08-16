from typing import Annotated

from fastapi import APIRouter, Body, Cookie, HTTPException

cookie_router = APIRouter(prefix="/cookie")


@cookie_router.get("/get-cookie/")
def read_cookie(token: Annotated[str | None, Cookie()] = None):
    return {"token": token}


@cookie_router.get("/get-cookies/")
def read_cookies(
    cookie1: Annotated[str | None, Cookie()] = None,
    cookie2: Annotated[str | None, Cookie()] = None,
):
    return {"cookie1": cookie1, "cookie2": cookie2}


@cookie_router.get("/get-cookie-default/")
def read_cookie_with_default(my_cookie: Annotated[str, Cookie()] = "default_value"):
    return {"my_cookie": my_cookie}


@cookie_router.get("/validate-cookie/")
def validate_cookie(my_cookie: Annotated[str, Cookie()]):
    if my_cookie is None or not my_cookie.startswith("valid_"):
        raise HTTPException(status_code=400, detail="Invalid cookie value")
    return {"my_cookie": my_cookie}
