# app/crud.py
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.models.user import User
from app.core.security import get_password_hash  # Импорт функции для хеширования паролей

def create_user(db: Session, user: UserCreate):
    # Создаем нового пользователя
    db_user = User(
        full_name=user.full_name,
        phone=user.phone,
        email=user.email,
        company=user.company,
        password=get_password_hash(user.password)  # Хешируем пароль перед сохранением
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    # Получаем пользователя по email
    return db.query(User).filter(email == User.email).first()

def entrance_user(db: Session, email: str, password: str):
    return db.query(User).filter(email == User.email, password == User.password).first()