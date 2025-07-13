from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.todo import ToDoCreate, ToDoUpdate
from app.models.todo import ToDo
from app.repositories import todo as repo


async def create_todo_service(data: ToDoCreate, session: AsyncSession):
    model = ToDo(**data.model_dump())
    return await repo.create_todo(model, session)


async def get_todo_service(todo_id: int, session: AsyncSession):
    todo = await repo.get_todo(todo_id, session)
    if not todo:
        raise HTTPException(404, detail="ToDo not found")
    return todo


async def get_all_todos_service(session: AsyncSession):
    return await repo.get_all_todos(session)


async def update_todo_service(
    todo_id: int, update_data: ToDoUpdate, session: AsyncSession
):
    todo = await repo.get_todo(todo_id, session)
    if not todo:
        raise HTTPException(404, detail="ToDo not found")
    return await repo.update_todo(todo, update_data.dict(exclude_unset=True), session)


async def delete_todo_service(todo_id: int, session: AsyncSession):
    todo = await repo.get_todo(todo_id, session)
    if not todo:
        raise HTTPException(404, detail="ToDo not found")
    await repo.delete_todo(todo, session)
