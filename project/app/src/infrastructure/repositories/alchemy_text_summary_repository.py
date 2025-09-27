from sqlalchemy.orm import Session

from project.app.models.summary import TextSummary
from project.app.src.domain.repositories.text_summary_repository import (
    Summary,
    TextSummaryRepository,
)


class AlchemyTextSummaryRepository(TextSummaryRepository):
    def __init__(self, db_session: Session):
        self._db_session = db_session

    def save(self, summary: Summary) -> None:
        text_summary = TextSummary(url=summary.url, summary=summary.summary)

        self._db_session.add(text_summary)
        self._db_session.commit()
        self._db_session.refresh(text_summary)
