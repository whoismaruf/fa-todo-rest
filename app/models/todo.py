from typing import Optional
from sqlmodel import SQLModel, Field


class ToDo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    completed: bool = Field(default=False)
