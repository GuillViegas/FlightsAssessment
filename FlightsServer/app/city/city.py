from sqlalchemy import Column, String, Integer
from sqlalchemy.schema import ForeignKey
from app import base


class City(base):
    __tablename__ = 'cities'

    city_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    state_id = Column(Integer, ForeignKey("states.state_id"), nullable=False)

