from sqlalchemy.orm import Session

from project.app.models.summary import TextSummary
from project.app.src.domain.text_summarizer import TextSummarizer


class CreateSummary:
    def __init__(self, text_summarizer: TextSummarizer, db_session: Session):
        self._text_summarizer = text_summarizer
        self._db_session = db_session

    def execute(self, url: str) -> str:
        original_text = self._fetch_text_from_url(url)

        summary = self._text_summarizer.summarize(original_text)

        text_summary = TextSummary(url=url, summary=summary)
        self._db_session.add(text_summary)
        self._db_session.commit()
        self._db_session.refresh(text_summary)

        return summary

    def _fetch_text_from_url(self, url: str) -> str:
        return "This is a placeholder text fetched from the URL."
