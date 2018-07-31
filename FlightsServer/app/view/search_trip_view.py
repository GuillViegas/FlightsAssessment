from sqlalchemy import Table, Column, Integer, String, DECIMAL, MetaData
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql import text
from sqlalchemy_views import CreateView
from app import base, db

metadata = MetaData()

search_trip_view = Table('search_trip', metadata)
definition = text('''SELECT t.trip_id, r.origin, r.destination, r.distance, t.price, a.name aircraft FROM routes r, trips t, aircrafts a 
                     WHERE t.trip_id IN 
                        (SELECT DISTINCT ON (t.route) t.trip_id FROM trips t ORDER BY t.route, t.price) 
                     AND t.route = r.route_id 
                     AND t.aircraft = a.aircraft_id''')

search_trip_view = CreateView(search_trip_view, definition, or_replace=True)
db.execute(search_trip_view)

class SearchTripView(base):
        __table__ = Table('search_trip', base.metadata,
                          Column('trip_id', Integer, primary_key=True),
                          Column('origin', String(3), ForeignKey("airports.iata")),
                          Column('destination', String(3), ForeignKey("airports.iata")),
                          Column('distance', DOUBLE_PRECISION),
                          Column('price', DECIMAL(5,2)),
                          Column('aircraft', String(15)), autoload=True, autoload_with=db)