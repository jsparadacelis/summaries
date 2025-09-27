from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from project.app.models.summary import TextSummary


def test_returns_201(client: TestClient, db_session: Session):
    test_url = "https://example.com/test-article"

    response = client.post("/summaries/", json={"url": test_url})

    assert response.status_code == 201

    summary = db_session.query(TextSummary).filter(TextSummary.url == test_url).first()
    assert summary is not None
