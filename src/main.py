from fastapi import FastAPI

from src.router import router as router_handler

app = FastAPI(
    title="Test_API"
)

app.include_router(router_handler)
