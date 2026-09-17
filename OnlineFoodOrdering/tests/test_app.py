from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_menu():
    client = app.test_client()
    response = client.get("/menu")
    assert response.status_code == 200

def test_order():
    client = app.test_client()
    response = client.get("/order")
    assert response.status_code == 200