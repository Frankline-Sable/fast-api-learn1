from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from ..models import Hero
from ..database import get_session

router = APIRouter(
    prefix="/heroes",
    tags=["heroes"],
)

@router.post("/", response_model=Hero)
def create_hero(hero: Hero, session: Session = Depends(get_session)):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero

@router.get("/", response_model=List[Hero])
def read_heroes(session: Session = Depends(get_session)):
    return session.exec(select(Hero)).all()
