from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

from project.app.config import Settings, get_settings


settings: Settings = get_settings()

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
