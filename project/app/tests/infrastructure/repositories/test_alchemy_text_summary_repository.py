from project.app.models.summary import TextSummary
from sqlalchemy.orm import Session

from project.app.src.infrastructure.repositories.alchemy_text_summary_repository import AlchemyTextSummaryRepository
from project.app.tests.domain.summary_builder import SummaryBuilder


class TestAlchemyTextSummaryRepository:

    def test_should_save_summary(self, db_session: Session) -> None:
        summary_to_save = SummaryBuilder().build()

        repo = AlchemyTextSummaryRepository()
        repo.save(summary=summary_to_save)

        summary = db_session.query(TextSummary).filter(TextSummary.url == summary_to_save.url).first()
        assert summary is not None