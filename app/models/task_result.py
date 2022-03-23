from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from .lines.disruption import LineDisruption
from .lines.line import Line
from .task import Task


class TaskResult(Base):
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey(Task.id))
    line_id = Column(Integer, ForeignKey(Line.id))
    line_disruption_id = Column(Integer, ForeignKey(LineDisruption.id))

    task = relationship("Task", back_populates="result", lazy="select")
    line = relationship("Line")
    line_disruption = relationship("LineDisruption")
