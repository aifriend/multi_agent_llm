from fastapi.testclient import TestClient

from src.agent_api import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_say_hello():
    response = client.get("/hello/Jose")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Jose"}


def test_unknown_route_is_404():
    assert client.get("/nope").status_code == 404
