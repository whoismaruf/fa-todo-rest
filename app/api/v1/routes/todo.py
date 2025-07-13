from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.todo import ToDoCreate, ToDoRead, ToDoUpdate
from app.db.session import get_session
from app.services import todo as service

router = APIRouter(prefix="/todos", tags=["ToDos"])


@router.post("/", response_model=ToDoRead)
async def create(todo: ToDoCreate, session: AsyncSession = Depends(get_session)):
    return await service.create_todo_service(todo, session)


@router.get("/", response_model=List[ToDoRead])
async def read_all(session: AsyncSession = Depends(get_session)):
    return await service.get_all_todos_service(session)


@router.get("/{todo_id}", response_model=ToDoRead)
async def read_one(todo_id: int, session: AsyncSession = Depends(get_session)):
    return await service.get_todo_service(todo_id, session)


@router.put("/{todo_id}", response_model=ToDoRead)
async def update(
    todo_id: int, todo: ToDoUpdate, session: AsyncSession = Depends(get_session)
):
    return await service.update_todo_service(todo_id, todo, session)


@router.delete("/{todo_id}")
async def delete(todo_id: int, session: AsyncSession = Depends(get_session)):
    await service.delete_todo_service(todo_id, session)
    return {"message": "Deleted"}
