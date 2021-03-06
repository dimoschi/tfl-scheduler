from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.lines import Line
from app.schemas.lines import LineCreate, LineUpdate


class CRUDTask(CRUDBase[Line, LineCreate, LineUpdate]):
    def create(self, db: Session, *, obj_in: LineCreate) -> Line:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


line = CRUDTask(Line)
