import requests
from app import session
from app.route.route import Route
from trip import Trip
from app.search_url.search_url_controller import SearchUrlController
from config import BASE_URL, API_KEY_2XT, CREDENCIAL_2XT
from app.aircraft.aircraft_controller import AircraftController
from datetime import datetime, timedelta
from sqlalchemy.sql import func


class TripController:
    def postAllTrips(self):
        routes = session.query(Route).all()
        trips = []

        for route in routes:
            trips.append(self.postTripsByRoute(route.origin, route.destination))

        return trips

    def postTripsByRoute(self, origin, dest):
        flights_schedules, searchUrl = self.getFlightSchedulesFromUrl(origin, dest)
        trips = []

        origin = str(flights_schedules['summary']['from']['iata'])
        dest = str(flights_schedules['summary']['to']['iata'])

        try:
            route = session.query(Route).filter_by(origin=origin, destination=dest).one()

        except Exception as error:
            print('Error: ' + repr(error))

        else:
            for trip in flights_schedules['options']:
                aircraft_model = str(trip['aircraft']['model'])
                aircraft_manufacturer = str(trip['aircraft']['manufacturer'])
                aircraft = AircraftController.searchForAircraft(aircraft=aircraft_model, manufacturer=aircraft_manufacturer)
                arrival_time = datetime.strptime(trip['arrival_time'], "%Y-%m-%dT%H:%M:%S")
                departure_time = datetime.strptime(trip['departure_time'], "%Y-%m-%dT%H:%M:%S")
                duration = arrival_time - departure_time
                trip = Trip(route=route.route_id, departure_time=str(trip['departure_time']),
                                 arrival_time=str(trip['arrival_time']), price=str(trip['fare_price']),
                            aircraft=aircraft.aircraft_id, duration=duration, search_url=searchUrl.search_url_id)
                session.add(trip)
                trips.append(trip)

            session.commit()

        return trips

    def getFlightSchedulesFromUrl(self, origin, dest):
        departure_date = (datetime.now() + timedelta(days=40)).strftime("%Y-%m-%d")
        searchUrl = SearchUrlController().postSearchUrl(base_url=BASE_URL, api_key=API_KEY_2XT, departure_airport=origin,
                                                        arrival_airport=dest, departure_date=departure_date)

        params = {'base_url': searchUrl.base_url, 'api_key': searchUrl.api_key, 'origin': searchUrl.departure_airport, 'dest': searchUrl.arrival_airport, 'departure_date': searchUrl.departure_date}
        url = "%(base_url)s/%(api_key)s/%(origin)s/%(dest)s/%(departure_date)s" % params
        r = requests.get(url, auth=CREDENCIAL_2XT)
        flights_schedules = r.json()

        return flights_schedules, searchUrl

    def updateTripsDuration(self):
        trips = session.query(Trip).all()

        for trip in trips:
            trip.duration = trip.arrival_time - trip.departure_time

        session.commit()

    def updatePriceKm(self):
        trips = session.query(Trip).all()

        for trip in trips:
            dist = session.query(Route).filter_by(route_id=trip.route).one().distance
            trip.price_km = float(trip.price)/dist

        session.commit()

    def longestFlightDuration(self):
        duration = session.query(func.max(Trip.duration)).one()
        trips = session.query(Trip).filter_by(duration=duration).all()
        r = []

        for trip in trips:
            route = session.query(Route).filter_by(route_id=trip.route).one()
            r.append({ 'origin': route.origin,
                 'destination': route.destination,
                 'departure_time': str(trip.departure_time),
                 'arrival_time': str(trip.arrival_time),
                 'duration': str(trip.duration)})

        return r