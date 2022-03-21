from sqlalchemy import Column, String

from app.db.base_class import Base
from app.db.helpers import same_as


class ServiceType(Base):
    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, default=same_as("id"))

    # lines = relationship("Line", back_populates="service_type")
