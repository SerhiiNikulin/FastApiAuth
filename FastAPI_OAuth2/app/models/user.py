# app/models/user.py
from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    phone = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    company = Column(String, index=True)
    password = Column(String)  # Хранить хешированный пароль
    status = Column(Integer, default=0)
    isactive = Column(Integer, default=0)  # Даем активный статус по умолчанию






