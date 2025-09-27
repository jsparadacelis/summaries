from fastapi import APIRouter

from pydantic import BaseModel


router = APIRouter(prefix="/summaries", tags=["summaries"])


class SummaryInput(BaseModel):
    url: str


@router.post("/", status_code=201)
async def create_summary(summary_input: SummaryInput):
    return {"status": "OK"}
