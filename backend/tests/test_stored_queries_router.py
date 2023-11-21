from fastapi.testclient import TestClient
from unittest.mock import patch
from sqlalchemy.orm import Session
import pytest

# Import your FastAPI app
from app.main import app

# Setup TestClient for your FastAPI app
client = TestClient(app)

# Sample saved query data for testing
test_saved_query_data = {
    "id": 1,
    "name": "Test Query",
    "query_text": "SELECT * FROM test_table",
    "username": "testuser",
    "comment": "Test Comment"
}

# Test for creating a saved query
@patch('app.crud.create_saved_query')
def test_create_saved_query(mock_create_saved_query):
    mock_create_saved_query.return_value = test_saved_query_data
    response = client.post("/queries/", json={
        "name": "Test Query",
        "query_text": "SELECT * FROM test_table",
        "username": "testuser",
        "comment": "Test Comment"
    })
    assert response.status_code == 200
    assert response.json() == test_saved_query_data

# Test for getting a saved query
@patch('app.crud.get_saved_query')
def test_get_saved_query(mock_get_saved_query):
    mock_get_saved_query.return_value = test_saved_query_data
    response = client.get("/queries/1")
    assert response.status_code == 200
    assert response.json() == test_saved_query_data

# Test for saved query not found scenario
@patch('app.crud.get_saved_query')
def test_get_saved_query_not_found(mock_get_saved_query):
    mock_get_saved_query.return_value = None
    response = client.get("/queries/2")
    assert response.status_code == 404
