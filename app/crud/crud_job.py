from app.crud.base import CRUDBase
from app.models.job import Job


class CRUDTaskResult(CRUDBase[Job, None, None]):
    pass


job = CRUDTaskResult(Job)
