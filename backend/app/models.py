from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    __tablename__ = "users"
    id: int = Field(primary_key=True)
    username: str
    email: str
    hashed_password: str
    refresh_token: str = Field(default=None)