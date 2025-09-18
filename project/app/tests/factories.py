import factory
from factory.alchemy import SQLAlchemyModelFactory
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from models.summary import TextSummary
from models.db import SessionLocal


class TextSummaryFactory(SQLAlchemyModelFactory):
    class Meta:
        model = TextSummary
        sqlalchemy_session = SessionLocal()
        sqlalchemy_session_persistence = "commit"

    id = factory.Sequence(lambda n: n)
    url = factory.Faker("url")
    summary = factory.Faker("text", max_nb_chars=200)
    created_at = factory.LazyFunction(datetime.now)