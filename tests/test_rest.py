from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_list_articles():
    response = client.get("/articles")
    assert response.status_code == 200
    assert response.json() == [
        {
            "author": "user1",
            "title": "default",
            "contents": "default content"
        }
    ]

def test_read_article():
    response = client.get("/articles/0")
    assert response.status_code == 200
    assert response.json() == {
        "author": "user1",
        "title": "default",
        "contents": "default content"
    }
    
    
def test_create_article():
    response = client.post(
        "/articles",
        json={"author": "user1", "title": "default", "contents": "test"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Title aleady exists!"}