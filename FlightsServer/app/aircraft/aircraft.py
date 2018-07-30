from sqlalchemy import Column, String, Integer, DECIMAL
from sqlalchemy.schema import ForeignKey
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from app import base

class Manufacturer(base):
    __tablename__ = "manufacturers"

    manufacturer_id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)

class Aircraft(base):
    __tablename__ = 'aircrafts'
    aircraft_id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)
    manufacturer = Column(Integer, ForeignKey("manufacturers.manufacturer_id"), nullable=False)
    speed = Column(DOUBLE_PRECISION)
    price_km = Column(DECIMAL(5, 2))