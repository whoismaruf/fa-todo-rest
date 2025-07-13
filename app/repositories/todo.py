from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from app.models.todo import ToDo


async def create_todo(data: ToDo, session: AsyncSession) -> ToDo:
    session.add(data)
    await session.commit()
    await session.refresh(data)
    return data


async def get_todo(id: int, session: AsyncSession) -> ToDo:
    result = await session.execute(select(ToDo).where(ToDo.id == id))
    return result.scalar_one_or_none()


async def get_all_todos(session: AsyncSession):
    result = await session.execute(select(ToDo))
    return result.scalars().all()


async def update_todo(existing: ToDo, data: dict, session: AsyncSession) -> ToDo:
    for key, value in data.items():
        setattr(existing, key, value)
    await session.commit()
    await session.refresh(existing)
    return existing


async def delete_todo(todo: ToDo, session: AsyncSession):
    await session.delete(todo)
    await session.commit()
