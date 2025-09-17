from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .db import Base


class TextSummary(Base):
    __tablename__ = "text_summary"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    summary = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())

    def __str__(self):
        return self.url
