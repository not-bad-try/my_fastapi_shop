from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, Token
from app.db.session import get_db
from app.core.security import hash_password, verify_password

router = APIRouter()

@router.post("/register", response_model=Token)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    # Добавление пользователя в базу данных (пример)
    return {"access_token": "fake_token", "token_type": "bearer"}

@router.post("/login", response_model=Token)
async def login(user: UserCreate, db: Session = Depends(get_db)):
    # Логика аутентификации
    if not verify_password(user.password, "hashed_password_from_db"):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": "fake_token", "token_type": "bearer"}