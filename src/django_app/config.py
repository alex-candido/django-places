# django_app/config.py

import dj_database_url
import os
from pathlib import Path
from typing import List, Literal, Sequence
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / "envs/.env"

class ConfigService(BaseSettings):
    model_config = SettingsConfigDict(env_file=str(ENV_FILE), case_sensitive=True, extra="ignore")

    DJANGO_DEBUG: bool = True
    DJANGO_ENVIRONMENT: Literal["development", "production", "test"] = "test"
    DJANGO_SECRET_KEY: str = ""
    DJANGO_ALLOWED_HOSTS: List[str] = ["localhost"]
    DATABASE_URL: str = ""

    CORS_ALLOW_ALL_ORIGINS: bool = True 
    CORS_ALLOWED_ORIGINS: Sequence[str] = [] 

    @property
    def DATABASE_CONFIG(self) -> dj_database_url.DBConfig:
        if self.DJANGO_ENVIRONMENT.lower() == "test":
            return dj_database_url.parse(self.DATABASE_URL or "sqlite:///test_db.sqlite3")
        elif self.DJANGO_ENVIRONMENT:
            return dj_database_url.parse(self.DATABASE_URL)
        else:
            raise ValueError(
                f"DJANGO_ENVIRONMENT must be defined for the '{self.DJANGO_ENVIRONMENT}' environment."
            )
                                      