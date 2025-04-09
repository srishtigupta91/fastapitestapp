from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import UserCreate, Token, LoginRequest
from app.models import User
from app.utils import create_refresh_token, create_access_token, pwd_context
from app.db import get_session

auth_router = APIRouter()

@auth_router.post("/register")
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    existing_user = session.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = pwd_context.hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password, email=user.email, refresh_token='')

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {"message": "User created successfully"}

@auth_router.post("/login", response_model=Token)
def login(request: LoginRequest, session: Session = Depends(get_session)):
    user = session.query(User).filter(User.username == request.username).first()
    if not user or not pwd_context.verify(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.username})
    refresh_token = create_refresh_token(data={"sub": user.username})
    user_details = {
        "username": user.username,
        "email": user.email
    }
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "user": user_details
    }


@auth_router.post("/logout")
def logout():
    return {"message": "Logout successful"}