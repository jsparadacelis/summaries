from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Summary:
    url: str
    summary: str
    created_at: datetime | None = datetime.now()


class TextSummaryRepository(ABC):
    @abstractmethod
    def save(self, summary: Summary) -> None: ...
