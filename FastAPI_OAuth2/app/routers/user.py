# app/routers/user.py
from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database.connection import get_db

router = APIRouter()

@router.post("/register")
async def register_user(
    full_name: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    company: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # Проверяем, существует ли пользователь с таким email
    existing_user = crud.get_user_by_email(db=db, email=email)
    if existing_user:
        return {
            "message": "Пользователь уже зарегистрирован.",
            "user": {
                "full_name": existing_user.full_name,
                "phone": existing_user.phone,
                "email": existing_user.email,
                "company": existing_user.company,
                "id": existing_user.id,
            }
        }

    # Если пользователя нет, создаем нового
    user_data = schemas.UserCreate(
        full_name=full_name,
        phone=phone,
        email=email,
        company=company,
        password=password
    )

    # Создание нового пользователя
    crud.create_user(db=db, user=user_data)

    return {
        "message": "Пользователь успешно зарегистрирован!",
        "new_user": {
            "full_name": full_name,
            "phone": phone,
            "email": email,
            "company": company
        }
    }
