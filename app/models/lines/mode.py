from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.helpers import same_as


class Mode(Base):
    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, default=same_as("id"))
    is_tfl_service = Column(Boolean, nullable=False)
    is_fare_paying = Column(Boolean, nullable=False)
    is_scheduled_service = Column(Boolean, nullable=False)

    lines = relationship("Line", back_populates="mode")
