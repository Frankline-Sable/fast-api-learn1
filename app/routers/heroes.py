from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from app.models.hero import Hero
from app.utils.get_user import get_current_user


from ..database import get_session

router = APIRouter(
    prefix="/heroes",
    tags=["heroes"],
)

@router.post("/", response_model=Hero)
def create_hero(hero: Hero, session: Session = Depends(get_session), current_user: str = Depends(get_current_user)):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero

@router.get("/", response_model=List[Hero])
def read_heroes(session: Session = Depends(get_session)):
    return session.exec(select(Hero)).all()
