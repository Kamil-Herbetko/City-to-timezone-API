from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class CommonSettings(BaseSettings):
    APP_NAME: str = "City to timezone API"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URI: str
    DB_NAME: str
    DB_CERTIFICATE_PATH: str


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()
