import os
from typing import Set
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    db_url: str = Field(..., env='DATABASE_URL')

settings = Settings()

