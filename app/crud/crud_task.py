from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class CRUDTask(CRUDBase[Task, TaskCreate, TaskUpdate]):
    def create(self, db: Session, *, obj_in: TaskCreate, job_id: str = None) -> Task:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, job_id=job_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


task = CRUDTask(Task)
