from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from ..models import villain
from ..database import get_session

router = APIRouter(
    prefix="/villaines",
    tags=["villaines"],
)

@router.post("/", response_model=villain)
def create_villain(villain: villain, session: Session = Depends(get_session)):
    session.add(villain)
    session.commit()
    session.refresh(villain)
    return villain

@router.get("/", response_model=List[villain])
def read_villaines(session: Session = Depends(get_session)):
    return session.exec(select(villain)).all()
