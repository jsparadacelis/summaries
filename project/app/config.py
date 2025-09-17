import logging
import os
from functools import lru_cache

from pydantic import AnyUrl, BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.environ.get(
        "DATABASE_URL", "postgresql+psycopg2://user:pass@db:5432/postgres"
    )


@lru_cache()
def get_settings() -> BaseSettings:
    print("Hola mundo...")
    log.info("Loading config settings from the environment...")
    return Settings()
