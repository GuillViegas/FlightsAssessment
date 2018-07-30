from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

# Create all entities
base.metadata.create_all(db)

Session = sessionmaker(db)
session = Session()

from app.airport.airport_controller import AirportController
airportController = AirportController()
#airportController.storeAirpotsDB()

from app.route.route_controller import RouteController
routeController = RouteController()
#routeController.createRoutes()

from app.trip.trip_controller import TripController
tripController = TripController()
#tripController.updatePriceKm()
#tripController.updateTripsDuration()
#tripController.postAllTrips()

from app.aircraft.aircraft_controller import AircraftController
aircraftController = AircraftController()
#aircraftController.setAllAircraftSpeed()

# Register blueprint(s)
from app.airport.airport_gateway import airport
app.register_blueprint(airport)