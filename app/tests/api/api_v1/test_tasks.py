from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.task import (
    create_random_task,
    create_random_task_results,
    create_random_line,
)


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
    assert content["job_id"] is not None
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
    assert content["job_id"] is None
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
    data = {"title": new_title}
    response = client.patch(f"{settings.API_V1_STR}/tasks/{task.id}", json=data)
    assert response.status_code == 200
    content = response.json()
    assert content["title"] != task.title
    assert content["description"] == task.description
    assert content["id"] == task.id


def test_update_task_not_found(client: TestClient, db: Session) -> None:
    task = create_random_task(db)
    new_title = "new_" + task.title
    data = {"title": new_title}
    task_id = task.id + 1000
    response = client.patch(f"{settings.API_V1_STR}/tasks/{task_id}", json=data)
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Task not found"


def test_get_tasks(client: TestClient, db: Session) -> None:
    task1 = create_random_task(db)
    task2 = create_random_task(db)
    response = client.get(
        f"{settings.API_V1_STR}/tasks",
    )
    assert response.status_code == 200
    content = response.json()
    assert content[0]["title"] != task1.title
    assert content[1]["title"] != task2.title
    assert content[0]["id"] != task1.id
    assert content[1]["id"] != task2.id


def test_read_task_results(client: TestClient, db: Session) -> None:
    task = create_random_task(db)
    line = create_random_line(db)
    task_result = create_random_task_results(db, task=task, line=line)
    response = client.get(
        f"{settings.API_V1_STR}/tasks/results/{task.id}",
    )
    assert response.status_code == 200
    content = response.json()
    assert isinstance(content, list)
    assert len(content) > 0
    assert content[0]["id"] == task_result.id
    assert content[0]["task_id"] == task.id


def test_read_task_results_task_not_found(client: TestClient, db: Session) -> None:
    task = create_random_task(db)
    line = create_random_line(db)
    create_random_task_results(db, task=task, line=line)
    task_id = task.id + 1000
    response = client.get(
        f"{settings.API_V1_STR}/tasks/results/{task_id}",
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Task not found"


def test_delete_task(client: TestClient, db: Session) -> None:
    task = create_random_task(db)
    response = client.delete(f"{settings.API_V1_STR}/tasks/{task.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == task.title
    assert content["description"] == task.description
    assert content["id"] == task.id


def test_delete_task_not_found(client: TestClient, db: Session) -> None:
    task = create_random_task(db)
    task_id = task.id + 1000
    response = client.delete(f"{settings.API_V1_STR}/tasks/{task_id}")
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Task not found"
