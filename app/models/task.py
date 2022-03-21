from sqlalchemy import ARRAY, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from .job import Job


class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    schedule_time = Column(DateTime)
    lines = Column(ARRAY(String))
    job_id = Column(String(191), ForeignKey(Job.id, ondelete="SET NULL"), nullable=True)
    job = relationship("Job", back_populates="task", lazy="select")
