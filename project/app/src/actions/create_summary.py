from project.app.src.domain.repositories.text_summary_repository import (
    Summary,
    TextSummaryRepository,
)
from sqlalchemy.orm import Session

from project.app.models.summary import TextSummary
from project.app.src.domain.text_summarizer import TextSummarizer


class CreateSummary:
    def __init__(self, text_summarizer: TextSummarizer, repo: TextSummaryRepository):
        self._text_summarizer = text_summarizer
        self._repo = repo

    def execute(self, url: str) -> str:
        original_text = self._fetch_text_from_url(url)

        text_summarized = self._text_summarizer.summarize(original_text)

        summary = Summary(url=url, summary=text_summarized)

        self._repo.save(summary)

        return summary.summary

    def _fetch_text_from_url(self, url: str) -> str:
        return "This is a placeholder text fetched from the URL."
