from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class LineDisruptionBase(BaseModel):
    category: str
    category_description: str
    type: str
    description: str
    affected_routes: Optional[List[str]] = []
    affected_stops: Optional[List[str]] = []
    closure_text: str


# Properties to receive on task creation
class LineDisruptionCreate(LineDisruptionBase):
    pass


# Properties to receive on task update
class LineDisruptionUpdate(LineDisruptionBase):
    pass


# Properties shared by models stored in DB
class LineDisruptionInDBBase(LineDisruptionBase):
    id: int
    category: str
    category_description: str
    type: str
    description: str
    affected_routes: Optional[List[str]] = []
    affected_stops: Optional[List[str]] = []
    closure_text: str

    class Config:
        orm_mode = True


# Properties to return to client
class LineDisruption(LineDisruptionInDBBase):
    pass


# Properties stored in DB
class LineDisruptionInDB(LineDisruptionInDBBase):
    mode_id: str
