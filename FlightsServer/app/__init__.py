from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import API_KEY_2XT
from config import BASE_URL
from sqlalchemy.orm.exc import NoResultFound

# Import gateway(s)
# from app.airport.airport_gateway import airport

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Database connection
db = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# Database extensions
db.execute("CREATE EXTENSION IF NOT EXISTS postgis")

base = declarative_base()

# Entities
from app.state.state import State
from app.city.city import City
from app.airport.airport import Airport
from app.route.route import Route
from app.aircraft.aircraft import Manufacturer
from app.aircraft.aircraft import Aircraft
from app.trip.trip import Trip
from app.base_url import BaseUrl
from app.api_key import ApiKey

# Create all entities
base.metadata.create_all(db)

Session = sessionmaker(db)
session = Session()

try:
    session.query(BaseUrl).filter_by(base_url=BASE_URL).one()
except NoResultFound:
    session.add(BaseUrl(base_url=BASE_URL))
    session.commit()

try:
    session.query(ApiKey).filter_by(api_key=BASE_URL).one()
except NoResultFound:
    session.add(ApiKey(api_key=API_KEY_2XT))
    session.commit()

from app.airport.airport_controller import AirportController
airportController = AirportController()
#airportController.storeAirpotsDB()

from app.route.route_controller import RouteController
routeController = RouteController()
#routeController.createRoutes()

from app.trip.trip_controller import TripController
tripController = TripController()
#tripController.postAllTrips()
#tripController.updatePriceKm()

from app.aircraft.aircraft_controller import AircraftController
aircraftController = AircraftController()
#aircraftController.setAllAircraftSpeed()
aircraftController.setAllAircraftPriceKM()

# Register blueprint(s)
from app.airport.airport_gateway import airport
app.register_blueprint(airport)