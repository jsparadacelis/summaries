from typing import Generator
from unittest.mock import MagicMock, Mock, patch

import pytest

from project.app.src.infrastructure.summarizers.claude_summarizer import (
    ClaudeSummarizer,
)

@pytest.fixture
def mock_chat_openai() -> Generator[Mock, None, None]:
    with patch(
        "project.app.src.infrastructure.summarizers.claude_summarizer.ChatOpenAI"
    ) as mock:
        yield mock


@pytest.fixture
def mock_create_agent() -> Generator[Mock, None, None]:
    with patch(
        "project.app.src.infrastructure.summarizers.claude_summarizer.create_agent"
    ) as mock:
        mock_agent = MagicMock()
        mock.return_value = mock_agent
        yield mock


class TestClaudeSummarizer:
    def test_should_initialize_with_correct_model_config(
        self, mock_chat_openai: Mock
    ) -> None:
        ClaudeSummarizer()

        mock_chat_openai.assert_called_once_with(
            model="anthropic:claude-3-7-sonnet-latest", temperature=0.1, max_tokens=1000, timeout=30
        )

    def test_should_summarize_text(
        self, mock_chat_openai: Mock, mock_create_agent: Mock
    ) -> None:
        expected_summary = "Short summary."
        mock_agent = mock_create_agent.return_value
        mock_agent.run.return_value = expected_summary

        text_to_summarize = "This is a long text that needs to be summarized."
        summarizer = ClaudeSummarizer()
        result = summarizer.summarize(text_to_summarize)

        assert result == expected_summary
        mock_create_agent.assert_called_once_with(
            summarizer._model,
            agent_type="chat-conversational-react-description",
            verbose=False,
        )
        expected_prompt = (
            f"Summarize the following text in a concise manner:\n\n{text_to_summarize}"
        )
        mock_agent.run.assert_called_once_with(expected_prompt)
