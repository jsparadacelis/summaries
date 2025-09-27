from fastapi import FastAPI

from project.app.src.api.summaries import router

app = FastAPI()

app.include_router(router)
