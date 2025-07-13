from fastapi import FastAPI
from app.api.v1.routes import todo
from app.core.init_db import init_db


app = FastAPI(title="ToDo API - Pro Setup")


@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(todo.router)
