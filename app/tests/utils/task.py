from datetime import datetime

from sqlalchemy.orm import Session
import random

from app import crud, models
from app.schemas.task import TaskCreate
from app.schemas.task_result import TaskResultCreate
from app.tests.utils.utils import random_from_lines_list, random_lower_string


def create_random_task(db: Session) -> models.Task:
    title = random_lower_string()
    description = random_lower_string()
    lines = random_from_lines_list()
    task_in = TaskCreate(
        title=title,
        description=description,
        id=id,
        schedule_time=datetime.now(),
        lines=lines,
    )
    return crud.task.create(db=db, obj_in=task_in)


def create_random_task_results(db: Session, task: models.Task) -> models.Task:
    task_in = TaskResultCreate(task_id=task.id, line_id=random.randint(1, 10))
    return crud.task_result.create(db=db, obj_in=task_in)
