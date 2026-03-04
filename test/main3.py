from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI()

# Define the Data Model (Table)
class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = None


# Set up the database engine
sqlite_url = "sqlite:///heroes.db"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

# Create the tables on startup
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)   


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# Create dependency to get a database session
def get_session():
    with Session(engine) as session:
        yield session 


# Routes
@app.post("/heroes/", response_model=Hero)
def create_hero(hero: Hero, session: Session = Depends(get_session)):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero

@app.get("/heroes/", response_model=List[Hero])
def read_heroes(session: Session = Depends(get_session)):
    heroes = session.exec(select(Hero)).all()
    return heroes