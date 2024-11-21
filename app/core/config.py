from pydantic import BaseSettings

#Настройки приложения
class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
