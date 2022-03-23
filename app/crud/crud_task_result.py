from typing import Any, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.task_result import TaskResult
from app.schemas.task_result import TaskResultCreate, TaskResultUpdate


class CRUDTaskResult(CRUDBase[TaskResult, TaskResultCreate, TaskResultUpdate]):
    def get_by_task_id(self, db: Session, task_id: Any) -> Optional[TaskResult]:
        return db.query(TaskResult).filter(TaskResult.task_id == task_id).all()


task_result = CRUDTaskResult(TaskResult)
