import os
from fastapi import Depends
from typing import Annotated
from datetime import datetime, timezone
from sqlmodel import create_engine, Session


def utcnow():
    return datetime.now(tz=timezone.utc)


DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sqlite.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def get_db():  # DB Seesion Dependency;
    with Session(engine) as session:
        yield session


SessDB = Annotated[Session, Depends(get_db)]
