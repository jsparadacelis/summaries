from fastapi import APIRouter


router = APIRouter()


@router.post("/", status_code=201)
async def create_summary():
    return {"status": "OK"}