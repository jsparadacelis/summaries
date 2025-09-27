from typing import Generator
from unittest.mock import Mock, create_autospec

import pytest

from project.app.src.domain.repositories.text_summary_repository import (
    TextSummaryRepository,
)
from project.app.src.actions.create_summary import CreateSummary
from project.app.src.domain.text_summarizer import TextSummarizer


class TestCreateSummary:
    @pytest.fixture
    def mock_text_summarizer(self) -> Generator[TextSummarizer, None, None]:
        mock = create_autospec(TextSummarizer, instance=True, spec_set=True)
        yield mock

    @pytest.fixture
    def mock_text_summary_repository(self) -> Generator[TextSummarizer, None, None]:
        mock = create_autospec(TextSummaryRepository, instance=True, spec_set=True)
        yield mock

    def test_create_summary_succeesfully(
        self, mock_text_summarizer: Mock, mock_text_summary_repository: Mock
    ):
        mock_text_summarizer.summarize.return_value = "This is a summary."

        action = CreateSummary(
            text_summarizer=mock_text_summarizer, repo=mock_text_summary_repository
        )
        url = "https://example.com"
        summary = action.execute(url)

        assert summary == "This is a summary."

        mock_text_summarizer.assert_called()

        mock_text_summary_repository.assert_called()
