from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import BYTEA, DOUBLE_PRECISION
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Job(Base):
    __tablename__ = "apscheduler_jobs"
    __table_args__ = {"info": {"skip_autogenerate": True}}

    id = Column(String(191), primary_key=True)
    next_run_time = Column(DOUBLE_PRECISION, index=True)
    job_state = Column(BYTEA, nullable=False)
    task = relationship("Task", back_populates="job", lazy="select")
