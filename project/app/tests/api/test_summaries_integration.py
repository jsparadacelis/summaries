from project.app.models.summary import TextSummary
from project.app.tests.factories import TextSummaryFactory


def test_create_summary_creates_db_object(client, db_session):
    """Test that API endpoint actually creates object in database"""
    # Arrange
    test_url = "https://example.com/test-article"
    
    # Act - Make request to API
    response = client.post(
        "/summaries/",
        json={"url": test_url}
    )
    
    # Assert - Check API response
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["url"] == test_url
    assert "summary" in response_data
    assert "created_at" in response_data
    assert "id" in response_data
    
    # Assert - Check object was created in database
    db_object = db_session.query(TextSummary).filter(TextSummary.url == test_url).first()
    assert db_object is not None
    assert db_object.url == test_url
    assert db_object.summary == response_data["summary"]
    assert db_object.id == response_data["id"]


def test_create_summary_with_factory_boy(db_session):
    """Test Factory Boy setup"""
    # Create object using Factory Boy
    summary = TextSummaryFactory.create()
    
    # Verify it exists in database
    db_object = db_session.query(TextSummary).filter(TextSummary.id == summary.id).first()
    assert db_object is not None
    assert db_object.url == summary.url
    assert db_object.summary == summary.summary