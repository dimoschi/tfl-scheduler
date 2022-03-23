from sqlalchemy import ARRAY, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.lines.mode import Mode


class Line(Base):
    id = Column(Integer, primary_key=True, index=True)
    tfl_id = Column(String, index=True)
    tfl_name = Column(String)
    mode_id = Column(String, ForeignKey(Mode.id), nullable=False)
    line_statuses = Column(ARRAY(String), nullable=True)
    route_sections = Column(ARRAY(String), nullable=True)
    disruptions = Column(ARRAY(String), nullable=True)
    created = Column(DateTime)
    modified = Column(DateTime)

    mode = relationship("Mode", back_populates="lines")
