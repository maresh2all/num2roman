from pydantic import BaseSettings

class Settings(BaseSettings):
    API_KEY_HASHED : str
    API_SECRET : str
    API_KEY : str
    class Config:
        env_file = ".env"
