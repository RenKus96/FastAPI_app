from fastapi.testclient import TestClient

from main import app


client = TestClient(app)

user_in = {
    "name": "user2",
    "email": "email2@test.com",
    "password": "password"
}

user_out = {
    "name": "user2",
    "email": "email2@test.com",
    "full_name": None,
    "is_active": True,
    "is_superuser": False
}

user_1 = {
  "name": "user1",
  "email": "user1@mail.com",
  "full_name": None,
  "is_active": True,
  "is_superuser": False
}

user_id = {"id": 1}


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_create_user():
    response = client.post("/create-user/", json=user_in)
    assert response.status_code == 200 and response.json() == user_out or\
           response.status_code == 400 and (response.json() == {"detail": "Login already registered"} or
                                            response.json() == {"detail": "Email already registered"})


def test_user():
    response = client.post("/user/", json=user_id)
    assert response.status_code == 200 and response.json() == user_1 or \
           response.status_code == 404 and response.json() == {"detail": "User not found"}

