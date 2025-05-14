from sqlmodel import SQLModel
from app.database import engine
from app.auth import model  # noqa: F401

SQLModel.metadata.create_all(engine)
