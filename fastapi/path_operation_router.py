from fastapi import APIRouter, Header, HTTPException

path_operation_router = APIRouter(prefix="/path_operation")


@path_operation_router.get(
    "/items/",
    tags=["items"],
    summary="Retrieve a list of items",
    response_description="A list of items",
)
def get_items():
    """
    add docstring
    Retrieve a list of items.

    This endpoint retrieves a list of all available items in the inventory.
    It supports pagination and filtering.
    """
    return {"items": ["item1", "item2"]}


@path_operation_router.get("/users/", tags=["users"])
def get_users():
    return {"users": ["user1", "user2"]}


@path_operation_router.get(
    "/old-endpoint/", deprecated=True, summary="Deprecated endpoint"
)
def old_endpoint():
    return {
        "message": "This endpoint is deprecated and will be removed in future versions."
    }
