from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):  # User Model for SQL Database;
    __tablename__ = "users"  # SQL table name;
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, min_length=3, max_length=50)
    email: str = Field(unique=True, nullable=False)
    password: str = Field(nullable=False, min_length=8)
    is_active: bool = Field(default=False, nullable=False)
