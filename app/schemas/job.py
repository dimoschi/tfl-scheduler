import binascii

from pydantic import BaseModel


class ByteA:
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, bytes):
            raise ValueError(f"`bytes` expected not {type(v)}")
        return binascii.b2a_hex(v)


# Shared properties
class JobBase(BaseModel):
    next_run_time: int
    # job_state: ByteA


# Properties shared by models stored in DB
class JobInDBBase(JobBase):
    id: str
    next_run_time: int
    # job_state: ByteA

    class Config:
        orm_mode = True


# Properties to return to client
class Job(JobInDBBase):
    pass


# Properties stored in DB
class JobInDB(JobInDBBase):
    pass
