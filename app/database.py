import os

from sqlmodel import  Session, SQLModel, create_engine

# Use the credentials from your docker-compose
#DB_URL = "postgresql://user:password@localhost:5432/herodb"
DATABSE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")

engine = create_engine(DATABSE_URL)

# sqlite_url = "sqlite:///database.db"
# engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)  

def get_session():
    with Session(engine) as session:
        yield session 