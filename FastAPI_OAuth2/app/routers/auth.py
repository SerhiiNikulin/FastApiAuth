from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
from .. import crud, schemas, core
from app.database.connection import get_db

# Создаем роутер для авторизации
router = APIRouter()


@router.post("/login")
async def login_user(
        email: str = Form(...),
        password: str = Form(...),
        db: Session = Depends(get_db)
):
    # Ищем пользователя по email
    user = crud.get_user_by_email(db=db, email=email)

    # Если пользователь не найден, выбрасываем ошибку
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный email",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Проверяем пароль
    if not core.security.verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Если авторизация успешна, создаем токен
    access_token = core.security.create_access_token(data={"sub": user.email})

    return {
        "access_token": access_token,
        "token_type": "bearer",  # Указываем тип токена
        "message": {
            "id": user.id,
            "user": user.full_name,
            "email": user.email,
            "password": user.password,
        }
    }
