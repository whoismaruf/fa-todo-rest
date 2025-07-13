import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Debug print: see where you're running the app from
print("🔍 CWD:", os.getcwd())

# Manually load .env
load_dotenv()
print("🔍 ENV VAR (os):", os.getenv("DATABASE_URL"))


class Settings(BaseSettings):
    DATABASE_URL: str
    API_KEY: str = "your_api_key_here"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()

# Debug print: show what's actually loaded into Pydantic
print("✅ settings.DATABASE_URL:", settings.DATABASE_URL)
