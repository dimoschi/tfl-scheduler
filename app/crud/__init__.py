from .crud_job import job
from .crud_task import task
from .crud_task_result import task_result
from .lines.crud_disruption import line_disruption
from .lines.crud_line import line
from .lines.crud_mode import mode

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
