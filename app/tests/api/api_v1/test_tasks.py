from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.task import create_random_task


def test_create_task(client: TestClient, db: Session) -> None:
    data = {
        "title": "Foo",
        "description": "Fighters",
        "schedule_time": "2022-03-20T18:19:24.157Z",
        "lines": ["victoria"],
    }
    response = client.post(
        f"{settings.API_V1_STR}/tasks/",
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content


def test_read_task(client: TestClient, db: Session) -> None:
    task = create_random_task(db)
    response = client.get(
        f"{settings.API_V1_STR}/tasks/{task.id}",
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == task.title
    assert content["description"] == task.description
    assert content["id"] == task.id
