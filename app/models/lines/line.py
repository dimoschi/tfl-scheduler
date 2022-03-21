from sqlalchemy import ARRAY, Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.lines.mode import Mode


class Line(Base):
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    mode_id = Column(String, ForeignKey(Mode.id), nullable=False)
    # service_type_id = Column(String, ForeignKey(ServiceType.id), nullable=False)
    line_statuses = Column(ARRAY(String), nullable=True)
    route_sections = Column(ARRAY(String), nullable=True)
    disruptions = Column(ARRAY(String), nullable=True)
    created = Column(DateTime)
    modified = Column(DateTime)

    mode = relationship("Mode", back_populates="lines")
    # service_type = relationship("ServiceType", back_populates="lines")
