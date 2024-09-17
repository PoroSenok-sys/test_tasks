import asyncio
from time import monotonic

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="",
    tags=["Test"]
)


class TestResponse(BaseModel):
    elapsed: float


@router.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
    ts1 = monotonic()
#    ... организация вызовы функции work() ...
    task1 = asyncio.create_task(work())
    task2 = asyncio.create_task(work())
    task3 = asyncio.create_task(work())
    await task1
    await task2
    await task3
    ts2 = monotonic()
    return TestResponse(elapsed=ts2 - ts1)


async def work() -> None:
    await asyncio.sleep(3)
