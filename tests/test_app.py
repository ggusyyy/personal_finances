from typing import Generator
import pytest
from fastapi.testclient import TestClient

from app import app

@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client

def test_get_root_answers_with_200_and_message(client: TestClient):
    response = client.get("/")
    body = response.json()

    assert response.status_code == 200
    assert isinstance(body, dict)
    assert "message" in body
    assert isinstance(body["message"], str)