# app/core/settings.py
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"  # Убедитесь, что у вас есть .env файл с нужными переменными

settings = Settings()