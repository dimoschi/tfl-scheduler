from sqlalchemy import ARRAY, Column, Integer, String

from app.db.base_class import Base


class LineDisruption(Base):
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    category_description = Column(String)
    type = Column(String)
    description = Column(String)
    affected_routes = Column(ARRAY(String), nullable=True)
    affected_stops = Column(ARRAY(String), nullable=True)
    closure_text = Column(String)
