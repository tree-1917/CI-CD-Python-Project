import pytest
from fastapi.testclient import TestClient
from app.main import app  # Import the FastAPI app instance

# Initialize TestClient with your FastAPI app
client = TestClient(app)

def test_get_version():
    """Test the /version endpoint"""
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"Version": "V0.0.1"}

