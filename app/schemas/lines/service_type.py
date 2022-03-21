from pydantic import BaseModel


# Shared properties
class ServiceTypeBase(BaseModel):
    id: str
    name: str


# Properties to receive on task creation
class ServiceTypeCreate(ServiceTypeBase):
    pass


# Properties to receive on task update
class ServiceTypeUpdate(ServiceTypeBase):
    pass


# Properties shared by models stored in DB
class ServiceTypeInDBBase(ServiceTypeBase):
    id: str
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class ServiceType(ServiceTypeInDBBase):
    pass


# Properties stored in DB
class ServiceTypeInDB(ServiceTypeInDBBase):
    pass
