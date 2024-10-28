# schemas/user.py
from pydantic import BaseModel

class UserBase(BaseModel):
    full_name: str
    phone: str  # Используем строку для номера телефона
    email: str
    company: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True  # Включение поддержки ORM