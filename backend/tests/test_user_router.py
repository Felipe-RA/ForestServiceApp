from fastapi.testclient import TestClient
from unittest.mock import patch
from sqlalchemy.orm import Session
from datetime import datetime
import pytest

# Import your FastAPI app
from app.main import app

# Setup TestClient for your FastAPI app
client = TestClient(app)

# Sample user data for testing
test_user_data = {
    "username": "testuser",
    "registered_at": datetime.now()
}

# Test for creating a user
@patch('app.crud.create_user')
def test_create_user(mock_create_user):
    mock_create_user.return_value = test_user_data
    response = client.post("/users/", json={"username": "testuser"})
    assert response.status_code == 200
    assert response.json() == test_user_data

# Test for getting a user
@patch('app.crud.get_user')
def test_get_user(mock_get_user):
    mock_get_user.return_value = test_user_data
    response = client.get("/users/testuser")
    assert response.status_code == 200
    assert response.json() == test_user_data

# Test for user not found scenario
@patch('app.crud.get_user')
def test_get_user_not_found(mock_get_user):
    mock_get_user.return_value = None
    response = client.get("/users/nonexistentuser")
    assert response.status_code == 404
