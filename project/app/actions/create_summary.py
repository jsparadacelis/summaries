from app.domain.text_summarizer import TextSummarizer


class CreateSummary:
    def __init__(self, text_summarizer: TextSummarizer):
        self._text_summarizer = text_summarizer

    def execute(self, url: str) -> str:
        original_text = self._fetch_text_from_url(url)

        return self._text_summarizer.summarize(original_text)

    def _fetch_text_from_url(self, url: str) -> str:
        return "This is a placeholder text fetched from the URL."
        