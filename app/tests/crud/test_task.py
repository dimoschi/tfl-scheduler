from datetime import datetime

from sqlalchemy.orm import Session

from app import crud
from app.schemas.task import TaskCreate, TaskUpdate
from app.tests.utils.utils import random_from_lines_list, random_lower_string


def test_create_task(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    schedule_time = datetime.now()
    lines = random_from_lines_list()
    task_in = TaskCreate(
        title=title, description=description, schedule_time=schedule_time, lines=lines
    )
    task = crud.task.create(db=db, obj_in=task_in)
    assert task.title == title
    assert task.description == description


def test_get_task(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    schedule_time = datetime.now()
    lines = random_from_lines_list()
    task_in = TaskCreate(
        title=title, description=description, schedule_time=schedule_time, lines=lines
    )
    task = crud.task.create(db=db, obj_in=task_in)
    stored_item = crud.task.get(db=db, id=task.id)
    assert stored_item
    assert task.id == stored_item.id
    assert task.title == stored_item.title
    assert task.description == stored_item.description


def test_update_task(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    schedule_time = datetime.now()
    lines = random_from_lines_list()
    task_in = TaskCreate(
        title=title, description=description, schedule_time=schedule_time, lines=lines
    )
    task = crud.task.create(db=db, obj_in=task_in)
    description2 = random_lower_string()
    task_update = TaskUpdate(description=description2)
    task2 = crud.task.update(db=db, db_obj=task, obj_in=task_update)
    assert task.id == task2.id
    assert task.title == task2.title
    assert task2.description == description2


def test_delete_task(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    schedule_time = datetime.now()
    lines = random_from_lines_list()
    task_in = TaskCreate(
        title=title, description=description, schedule_time=schedule_time, lines=lines
    )
    task = crud.task.create(db=db, obj_in=task_in)
    task2 = crud.task.remove(db=db, id=task.id)
    task3 = crud.task.get(db=db, id=task.id)
    assert task3 is None
    assert task2.id == task.id
    assert task2.title == title
    assert task2.description == description
