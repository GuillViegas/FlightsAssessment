from sqlalchemy import Column, String, Integer
from geoalchemy2 import Geometry
from app import base


class State(base):
    __tablename__ = 'states'

    state_id = Column(Integer, primary_key=True)
    geom = Column(Geometry(geometry_type='MULTIPOLYGON', srid=4674))
    name = Column(String(50), nullable=False)
    region = Column(String(20))
    cod = Column(String(2))

