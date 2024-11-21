from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

#Тестирование регистрации пользователя
def test_register_user():

    response = client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
