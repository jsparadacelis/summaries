from abc import ABC


class TextSummarizer(ABC):
    @classmethod
    def summarize(cls, text: str) -> str: ...
