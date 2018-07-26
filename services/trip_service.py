import requests
from dbconnection import DBconnection
from route_service import RouteService
from aircraft_service import AircraftService
from datetime import datetime
from datetime import timedelta

class TripService:
	_db = None

	def __init__(self):
		self._db = DBconnection()

	def postTripsOfAllRoutes(self):
		routes = RouteService().getAllRoutes()
		trips = []

		for route in routes:
			trips.append(self.postTripsByRoute(route[1], route[2]))

		return trips

	def postTripsByRoute(self, origin, dest):
		flights_schedules = self.getFlightSchedulesFromUrl(origin, dest)
		trips = []

		origin = str(flights_schedules['summary']['from']['iata'])
		dest = str(flights_schedules['summary']['to']['iata'])

		try:
			route_id = RouteService().getRouteID(origin = origin, dest = dest)

			if(route_id is None):
				raise ValueError('Route does not match any record in the database!')

		except Exception as error:
			print('Error: ' + repr(error))

		else: 
			for trip in flights_schedules['options']:
				model = str(trip['aircraft']['model'])
				manufacturer = str(trip['aircraft']['manufacturer'])
				aircraft = AircraftService().searchForAircraft(model, manufacturer)[0]
				trips.append(self.postTrip(str(trip['departure_time']), str(trip['arrival_time']), str(trip['fare_price']), aircraft, route_id[0]))

		return trips


	def postTrip(self, departure_time, arrival_time, fare_price, aircraft, route):
		sql = "INSERT INTO viagens (partida, chegada, preco, aeronave, rota) VALUES  "
		sql += "('" + departure_time + "','" + arrival_time + "', " + fare_price + ", " + str(aircraft) + ", " + str(route) + ") RETURNING *"

		return self._db.spquery(sql)

	def getFlightSchedulesFromUrl(self, origin, dest):
		departure_date = (datetime.now() + timedelta(days=40)).strftime("%Y-%m-%d")
		url = "http://stub.2xt.com.br/air/search/p7WxInwGGvwmuOupzrqEbqCqqrHrOvvY/"+origin+"/"+dest+"/"+departure_date
		r = requests.get(url, auth=('guilhermevf', 's4SxIn'))
		flights_schedules = r.json()

		return flights_schedules

	def getAllTrips(self):
		sql = "SELECT * FROM viagens"
		return self._db.mquery(sql)

	def updateAllPricePerKm(self):
		trips = self.getAllTrips()
		trips_updated = []

		for trip in trips:
			dist = RouteService().getDistanceRouteByID(trip[5])[0]
			price = trip[3]
			trips_updated.append(self.updatePricePerKm(trip[0], float(price)/dist))

		return trips_updated

	def updatePricePerKm(self, trip, price):
		sql = "UPDATE viagens SET preco_km = " + str(price) + " WHERE viagem_id = " + str(trip) + " RETURNING *"
		return self._db.spquery(sql)




