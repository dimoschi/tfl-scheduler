from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.task import create_random_task


def test_create_task(client: TestClient, db: Session) -> None:
    data = {
        "title": "Foo",
        "description": "Fighters",
        "schedule_time": "2025-01-01T00:00:01.000Z",
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
    assert content["job"] is not None
    assert "id" in content


def test_create_task_without_schedule_time(client: TestClient, db: Session) -> None:
    data = {
        "title": "Foo",
        "description": "Fighters",
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
    assert content["job"] is None
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


def test_read_task_not_found(client: TestClient, db: Session) -> None:
    task = create_random_task(db)
    task_id = task.id + 1000
    response = client.get(
        f"{settings.API_V1_STR}/tasks/{task_id}",
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Task not found"


def test_update_task(client: TestClient, db: Session) -> None:
    task = create_random_task(db)
    new_title = "new_" + task.title
    response = client.put(
        f"{settings.API_V1_STR}/tasks/{task.id}", data={"title": new_title}
    )
    assert response.status_code == 422
    content = response.json()
    assert content["title"] != task.title
    assert content["description"] == task.description
    assert content["id"] == task.id
