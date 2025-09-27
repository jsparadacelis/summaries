from datetime import datetime
from project.app.src.domain.repositories.text_summary_repository import Summary


class SummaryBuilder:
    def __init__(self):
        self._summary = Summary(
            url="http://my-summary", summary="my-summary", created_at=datetime.now()
        )

    def build(self) -> Summary:
        return self._summary
