from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

current_directory = Path(__file__).parent
dotenv_path = current_directory / ".env"
load_dotenv(dotenv_path=dotenv_path)


class Settings(BaseSettings):
    KUBEFLOW_ENDPOINT: str
    KUBEFLOW_USERNAME: str
    KUBEFLOW_PASSWORD: str
    KUBEFLOW_NAMESPACE: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
