from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey
from geoalchemy2 import Geometry
from app import base


class Airport(base):
    __tablename__ = 'airports'

    iata = Column(String(3), primary_key=True)
    city = Column(Integer, ForeignKey("cities.city_id"))
    geom = Column(Geometry(geometry_type='POINT', srid=4674))