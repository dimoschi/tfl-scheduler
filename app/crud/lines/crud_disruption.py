from app.crud.base import CRUDBase
from app.models.lines import LineDisruption
from app.schemas.lines import LineDisruptionCreate, LineDisruptionUpdate


class CRUDTask(CRUDBase[LineDisruption, LineDisruptionCreate, LineDisruptionUpdate]):
    pass


line_disruption = CRUDTask(LineDisruption)
