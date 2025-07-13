from typing import Optional
from pydantic import BaseModel, Field


class ToDoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=300)


class ToDoRead(ToDoCreate):
    id: int
    completed: bool


class ToDoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]
