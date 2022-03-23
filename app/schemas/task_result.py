from typing import Optional

from pydantic import BaseModel

from app.schemas.lines.disruption import LineDisruption
from app.schemas.lines.line import Line
from app.schemas.task import Task


# Shared properties
class TaskResultBase(BaseModel):
    task_id: int
    line_id: int
    line_disruption_id: Optional[int] = None


# Properties to receive on task creation
class TaskResultCreate(TaskResultBase):
    pass


# Properties to receive on task update
class TaskResultUpdate(TaskResultBase):
    pass


# Properties shared by models stored in DB
class TaskResultInDBBase(TaskResultBase):
    id: int
    task_id: int
    line_id: int
    line_disruption_id: Optional[int] = None

    class Config:
        orm_mode = True


# Properties to return to client
class TaskResult(TaskResultInDBBase):
    task: Task
    line: Optional[Line]
    line_disruption: Optional[LineDisruption] = None


# Properties stored in DB
class TaskResultInDB(TaskResultInDBBase):
    pass
