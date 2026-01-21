from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    prometheus_host: str = "localhost"
    prometheus_port: int = 9090

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
