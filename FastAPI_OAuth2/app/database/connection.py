# app/database/connection.py
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Указываем URL базы данных SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Создание движка базы данных
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Создание фабрики сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Подключение к базе данных и получение списка таблиц
def get_tables_and_columns():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
        tables = result.fetchall()

        print("Таблицы в базе данных:")
        for table in tables:
            print(f"\nТаблица: {table[0]}")
            result = connection.execute(text(f"PRAGMA table_info({table[0]});"))
            columns = result.fetchall()

            print("Поля в таблице:")
            for column in columns:
                print(f"  - {column[1]} ({column[2]})")  # column[1] - название столбца, column[2] - тип данных

def get_users_and_tables():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM users;"))
        tables = result.fetchall()
        for table in tables:
            print(f"Users в таблице: {table}")
