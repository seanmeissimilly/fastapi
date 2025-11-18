from typing import Optional
from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    username: str
    email: str

class User(UserBase, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    is_active: bool = Field(default=True)