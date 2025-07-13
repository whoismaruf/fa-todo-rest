from dotenv import load_dotenv
from pydantic_settings import BaseSettings


# Manually load .env
load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str
    API_KEY: str = "your_api_key_here"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
