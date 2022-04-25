from fastapi import testclient
from main import app


client = testclient.TestClient(app)


def test_livecheck():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.text == '"Hello from the webscraper!"'


def test_nonexistent_endpoint():
    resp = client.get("/wrong")
    assert resp.status_code == 404
    assert resp.json() == {"detail": "Not Found"}
