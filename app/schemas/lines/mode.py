from typing import Optional

from pydantic import BaseModel


# Shared properties
class ModeBase(BaseModel):
    id: str
    name: str
    is_tfl_service: Optional[bool] = None
    is_fare_paying: Optional[bool] = None
    is_scheduled_service: Optional[bool] = None


# Properties to receive on task creation
class ModeCreate(ModeBase):
    pass


# Properties to receive on task update
class ModeUpdate(ModeBase):
    pass


# Properties shared by models stored in DB
class ModeInDBBase(ModeBase):
    id: str
    name: str
    is_tfl_service: Optional[bool] = None
    is_fare_paying: Optional[bool] = None
    is_scheduled_service: Optional[bool] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Mode(ModeInDBBase):
    pass


# Properties stored in DB
class ModeInDB(ModeInDBBase):
    pass
