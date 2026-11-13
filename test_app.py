from app import app


def test_quote_returns_text():
    client = app.test_client()
    response = client.get("/quote")
    assert response.status_code == 200
    assert "quote" in response.get_json()


def test_health_is_ok():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_hello_message():
    client = app.test_client()
    response = client.get("/hello")
    assert response.status_code == 200
    assert "message" in response.get_json()