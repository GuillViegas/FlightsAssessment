from sqlalchemy import Column, Integer, Interval, TIMESTAMP, DECIMAL
from sqlalchemy.schema import ForeignKey
from app import base


class Trip(base):
    __tablename__ = 'trips'

    trip_id = Column(Integer, primary_key=True)
    departure_time = Column(TIMESTAMP, nullable=False)
    arrival_time = Column(TIMESTAMP, nullable=False)
    price = Column(DECIMAL(7,2), nullable=False)
    aircraft = Column(Integer, ForeignKey("aircrafts.aircraft_id"), nullable=False)
    route = Column(Integer, ForeignKey("routes.route_id"), nullable=False)
    price_km = Column(DECIMAL(5,2))
    duration = Column(Interval)
    search_url = Column(Integer, ForeignKey("search_urls.route_id"), nullable=False)


