# src/conf/config.py
import os
import sys
from typing import Any

from pydantic import ConfigDict, field_validator, EmailStr

from pydantic_settings import BaseSettings

# Додаємо шлях до кореневої папки проекту
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Settings(BaseSettings):
    DB_URL: str = "postgresql+asyncpg://postgres:123@localhost:5432/hw13"
    SECRET_KEY_JWT: str = "secret_key"
    ALGORITHM: str = "HS256"
    MAIL_USERNAME: str = "example@meta.ua"
    MAIL_PASSWORD: str = "secretPassword"
    MAIL_FROM: str = "example@meta.ua"
    MAIL_PORT: int = 465
    MAIL_SERVER: str = "smtp.meta.ua"
    REDIS_DOMAIN: str = 'localhost'
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str | None = None
    CLD_NAME: str = 'dcusbfyz7'
    CLD_API_KEY: int = 637918188437592
    CLD_API_SECRET: str = "secret"


    @field_validator("ALGORITHM")
    @classmethod
    def validate_algorithm(cls, v: Any):
        if v not in ["HS256", "HS512"]:
            raise ValueError("algorithm must be HS256 or HS512")
        return v


    model_config = ConfigDict(extra='ignore', env_file=".env", env_file_encoding="utf-8")  # noqa


config = Settings()
