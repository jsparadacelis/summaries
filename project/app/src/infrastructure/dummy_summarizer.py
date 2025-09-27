from project.app.src.domain.text_summarizer import TextSummarizer


class DummyTextSummarizer(TextSummarizer):
    def __init__(self) -> None: ...

    def summarize(self, text: str) -> str:
        return "summary"
