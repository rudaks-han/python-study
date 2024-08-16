from datetime import datetime, date, time, timedelta
from decimal import Decimal
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body

datatype_router = APIRouter(prefix="/datatype")

from pydantic import BaseModel, Field


class Item(BaseModel):
    id: UUID
    name: str


@datatype_router.post("/items/")
async def create_item(item: Item):
    return item


class Event(BaseModel):
    name: str
    # event_datetime: datetime
    event_date: date


@datatype_router.post("/events/")
async def create_event(event: Event):
    return event


class Schedule(BaseModel):
    name: str
    start_time: time


@datatype_router.post("/schedules/")
async def create_schedule(schedule: Schedule):
    return schedule


class Task(BaseModel):
    name: str
    duration: timedelta


@datatype_router.post("/tasks/")
async def create_task(task: Task):
    return task


class ItemCollection(BaseModel):
    tags: frozenset[str]


@datatype_router.post("/collections/")
async def create_collection(collection: ItemCollection):
    return collection


class FileData(BaseModel):
    file_name: str
    data: bytes


@datatype_router.post("/files/")
async def upload_file(file_data: FileData):
    return {"file_name": file_data.file_name, "data_length": len(file_data.data)}


class Product(BaseModel):
    name: str
    price: Decimal


@datatype_router.post("/products/")
async def create_product(product: Product):
    return product


@datatype_router.post("/items/{item_id}")
async def read_items(
    item_id: UUID,
    # start_datetime: Annotated[datetime, Body()],
    # end_datetime: Annotated[datetime, Body()],
    # process_after: Annotated[timedelta, Body()],
    # repeat_at: Annotated[time | None, Body()] = None,
    start_datetime: datetime = Body(),
    end_datetime: datetime = Body(),
    process_after: timedelta = Body(),
    repeat_at: time | None = Body(),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }
