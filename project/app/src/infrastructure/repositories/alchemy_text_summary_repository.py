from project.app.src.domain.repositories.text_summary_repository import Summary, TextSummaryRepository


class AlchemyTextSummaryRepository(TextSummaryRepository):

    def save(self, summary: Summary) -> None:
        return None