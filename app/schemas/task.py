from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from app.schemas.job import Job


# Shared properties
class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    lines: List[str] = []


# Properties to receive on task creation
class TaskCreate(TaskBase):
    title: str
    schedule_time: Optional[datetime] = None
    lines: List[str]


# Properties to receive on task update
class TaskUpdate(TaskBase):
    pass


class TaskUpdateInternal(TaskUpdate):
    job_id: Optional[str] = None


# Properties shared by models stored in DB
class TaskInDBBase(TaskBase):
    id: int
    description: str
    title: str
    schedule_time: Optional[datetime]
    lines: List[str]
    job: Optional[Job]

    class Config:
        orm_mode = True


# Properties to return to client
class Task(TaskInDBBase):
    pass


# Properties stored in DB
class TaskInDB(TaskInDBBase):
    pass
