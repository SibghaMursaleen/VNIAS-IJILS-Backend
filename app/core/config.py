# app/core/config.py
from pydantic_settings import BaseSettings
from pydantic import Field
import sys

class Settings(BaseSettings):
    # Field(...) marks the variable as required. If missing in .env, Pydantic throws an error.
    db_url: str = Field(..., alias="DB_URL")
    redis_url: str = Field(..., alias="REDIS_URL")
    zeptomail_token: str = Field(..., alias="ZEPTOMAIL_TOKEN")
    secret_key: str = Field(..., alias="SECRET_KEY")
    allowed_origins: str = Field(..., alias="ALLOWED_ORIGINS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

# Instantiate settings immediately to trigger fail-fast startup checks
try:
    settings = Settings()
    print("[CONFIG] Environment variables successfully loaded and validated.")
except Exception as e:
    print(f"\nCRITICAL CONFIGURATION ERROR:\n{e}\n", file=sys.stderr)
    print("Application startup aborted due to missing or invalid .env parameters.", file=sys.stderr)
    raise e