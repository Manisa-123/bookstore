from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./bookstore.db"

    class Config:
        env_file = ".env"


settings = Settings()
