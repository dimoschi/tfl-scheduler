from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel

from app.schemas.lines.mode import Mode


# Shared properties
class LineBase(BaseModel):
    id: str
    name: str
    line_statuses: Optional[List[Any]] = []
    route_sections: Optional[List[Any]] = []
    disruptions: Optional[List[Any]] = []
    created: datetime
    modified: datetime


# Properties to receive on task creation
class LineCreate(LineBase):
    pass


# Properties to receive on task update
class LineUpdate(LineBase):
    pass


# Properties shared by models stored in DB
class LineInDBBase(LineBase):
    id: str
    name: str
    line_statuses: Optional[List[Any]] = []
    route_sections: Optional[List[Any]] = []
    disruptions: Optional[List[Any]] = []
    created: datetime
    modified: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Line(LineInDBBase):
    mode: Mode


# Properties stored in DB
class LineInDB(LineInDBBase):
    mode_id: str
