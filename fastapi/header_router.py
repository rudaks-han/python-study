from fastapi import APIRouter, Header, HTTPException

header_router = APIRouter(prefix="/header")


@header_router.get("/get-header/")
def read_header(x_my_header: str | None = Header(None)):
    return {"X-My-Header": x_my_header}


@header_router.get("/get-header-default/")
def read_header_with_default(x_my_header: str = Header("default_value")):
    return {"X-My-Header": x_my_header}


@header_router.get("/get-required-header/")
def read_required_header(x_my_header: str = Header(...)):
    return {"X-My-Header": x_my_header}


@header_router.get("/validate-header/")
def validate_header(x_my_header: str | None = Header(None)):
    if x_my_header != "expected_value":
        raise HTTPException(status_code=400, detail="Invalid header value")
    return {"X-My-Header": x_my_header}


@header_router.get("/api-key/")
def api_key_header(api_key: str | None = Header(None)):
    if api_key != "my_secret_key":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return {"message": "Access granted"}
