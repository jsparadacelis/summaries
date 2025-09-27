import factory
from factory.alchemy import SQLAlchemyModelFactory
from datetime import datetime

from project.app.models.summary import TextSummary


class TextSummaryFactory(SQLAlchemyModelFactory):
    class Meta:
        model = TextSummary
        sqlalchemy_session_persistence = "commit"

    id = factory.Sequence(lambda n: n)
    url = factory.Faker("url")
    summary = factory.Faker("text", max_nb_chars=200)
    created_at = factory.LazyFunction(datetime.now)
