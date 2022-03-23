from datetime import datetime

from sqlalchemy.orm import Session
import random

from app import crud, models
from app.schemas.lines.line import LineCreate
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


def create_random_line(db: Session) -> models.Line:
    line = random_from_lines_list()[0]
    line_in = LineCreate(
        tfl_id=line,
        tfl_name=line,
        mode_id="tube",
        created=datetime.now(),
        modified=datetime.now(),
    )

    return crud.line.create(db=db, obj_in=line_in)


def create_random_task_results(
    db: Session, task: models.Task, line: models.Line
) -> models.TaskResult:
    task_in = TaskResultCreate(task_id=task.id, line_id=line.id)
    return crud.task_result.create(db=db, obj_in=task_in)
