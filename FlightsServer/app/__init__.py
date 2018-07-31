from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import API_KEY_2XT, BASE_URL, STATES_DATA_FILE
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
from app.search_url.search_url import ApiKey, BaseUrl
from app.search_url.search_url import SearchUrl
from app.trip.trip import Trip

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
    session.query(ApiKey).filter_by(api_key=API_KEY_2XT).one()
except NoResultFound:
    session.add(ApiKey(api_key=API_KEY_2XT))
    session.commit()

db.execute(text("COPY states FROM '%s' WITH (FORMAT csv)" % STATES_DATA_FILE).execution_options(autocommit=True))

from app.airport.airport_controller import AirportController
airportController = AirportController()
airportController.storeAirpotsDB()

from app.route.route_controller import RouteController
routeController = RouteController()
routeController.createRoutes()

from app.trip.trip_controller import TripController
tripController = TripController()
tripController.postAllTrips()
tripController.updatePriceKm()

from app.aircraft.aircraft_controller import AircraftController
aircraftController = AircraftController()
aircraftController.setAllAircraftSpeed()
aircraftController.setAllAircraftPriceKM()

# Views
from app.view.search_trip_view import SearchTripView

# Register blueprint(s)
from app.airport.airport_gateway import airport
app.register_blueprint(airport)

from app.route.route_gateway import route
app.register_blueprint(route)

from app.trip.trip_gateway import trip
app.register_blueprint(trip)

from app.state.state_gateway import state
app.register_blueprint(state)