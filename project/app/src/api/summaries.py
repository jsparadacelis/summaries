from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from project.app.models.db import get_db
from project.app.src.actions.create_summary import CreateSummary
from project.app.src.infrastructure.dummy_summarizer import DummyTextSummarizer


router = APIRouter(prefix="/summaries", tags=["summaries"])


class SummaryInput(BaseModel):
    url: str


@router.post("/", status_code=201)
async def create_summary(summary_input: SummaryInput, db: Session = Depends(get_db)):
    action = CreateSummary(text_summarizer=DummyTextSummarizer(), db_session=db)

    action.execute(url=summary_input.url)

    return {"status": "OK"}
