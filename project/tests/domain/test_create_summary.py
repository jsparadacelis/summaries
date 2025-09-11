from typing import Generator
from unittest.mock import Mock, create_autospec
import pytest
from app.actions.create_summary import CreateSummary
from app.domain.text_summarizer import TextSummarizer


class TestCreateSummary:
    @pytest.fixture
    def mock_text_summarizer(self) -> Generator[TextSummarizer, None, None]:
        mock = create_autospec(TextSummarizer, instance=True, spec_set=True)
        yield mock

    def test_create_summary_succeesfully(self, mock_text_summarizer: Mock):
        mock_text_summarizer.summarize.return_value = "This is a summary."

        action = CreateSummary(mock_text_summarizer)
        url = "https://example.com"
        summary = action.execute(url)

        assert summary == "This is a summary."
