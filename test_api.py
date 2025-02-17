import requests

BASE_URL = "http://127.0.0.1:5000"

def test_register():
    response = requests.post(f"{BASE_URL}/register", json={"email": "test@example.com", "password": "1234"})
    assert response.status_code == 201
    assert response.json()["status"] == "success"
    print("✅ Тест реєстрації пройдено")

test_register()
