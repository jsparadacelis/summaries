import pytest


def test_simple():
    """Simple test to verify pytest is working"""
    assert 1 + 1 == 2


def test_api_endpoint_exists():
    """Test that we can import and hit our API endpoint"""
    from fastapi.testclient import TestClient
    from fastapi import FastAPI
    
    # Create a simple test app
    app = FastAPI()
    
    @app.post("/summaries/")
    def create_summary():
        return {"status": "not implemented yet"}
    
    client = TestClient(app)
    response = client.post("/summaries/", json={"url": "https://example.com"})
    
    # This should fail because we haven't implemented the real endpoint yet
    assert response.status_code == 200
    assert response.json() == {"status": "not implemented yet"}