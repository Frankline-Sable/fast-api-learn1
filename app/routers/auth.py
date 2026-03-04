from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session, select
from typing import List

from app.models.hero import Hero
from app.utils.auth import create_access_token, get_password_hash, verify_password
from app.utils.get_user import get_current_user
from app.models.user import User
from passlib.context import CryptContext


from ..database import get_session

router = APIRouter(
    tags=["auth"],
)

@router.post("/register")
def register_user(username: str, password: str, session: Session = Depends(get_session)):
    existing_user = session.exec(select(User).where(User.username == username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    

    new_user= User(username=username, hashed_password=get_password_hash(password))

    session.add(new_user)
    session.commit()
    return {"message": "User registered successfully"}


@router.post("/token")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    session: Session = Depends(get_session)
):
    # 1. Look up user in DB
    statement = select(User).where(User.username == form_data.username)
    user = session.exec(statement).first()
    
    # 2. Verify password
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    
    # 3. Create and return the token
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}