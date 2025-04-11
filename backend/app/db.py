from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

# Replace with your actual database URL
DATABASE_URL = "postgresql://postgres:mypsqlpwd@db:5432/fastapi_db"

# Database connection
engine = create_engine(DATABASE_URL, echo=True)

# Function to create tables
def create_db_and_tables():
    with engine.begin() as conn:
        SQLModel.metadata.create_all(conn)

# Function to drop tables
def drop_db_and_tables():
    with engine.begin() as conn:
        SQLModel.metadata.drop_all(conn)

# Function to get a session
def get_session():
    with Session(engine) as session:
        yield session