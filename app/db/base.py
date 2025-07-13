from sqlmodel import SQLModel
# from app.models.todo import ToDo


def get_metadata():
    return SQLModel.metadata
