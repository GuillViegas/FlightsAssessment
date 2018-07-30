from sqlalchemy import Column, String, Integer
from sqlalchemy.schema import ForeignKey
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from app import base


class Route(base):
    __tablename__ = 'routes'

    route_id = Column(Integer, primary_key=True)
    origin = Column(String(3), ForeignKey("airports.iata"), nullable=False)
    destination = Column(String(3), ForeignKey("airports.iata"), nullable=False)
    distance = Column(DOUBLE_PRECISION)