import requests
from dbconnection import DBconnection
from city_service import CityService
from state_service import StateService

class AirportService:
	_db = None

	def __init__(self):
		self._db = DBconnection()

	def getAirportsFromUrl(self):
		r = requests.get('http://stub.2xt.com.br/air/airports/p7WxInwGGvwmuOupzrqEbqCqqrHrOvvY', auth=('guilhermevf', 's4SxIn'))
		airports = r.json()

		return airports

	def storeAirportsDB(self, airports):
		for airport in airports:
			iata = airports[airport]['iata']
			airportdb = self.getAirportByIata(iata)
			print(airportdb)

			if(airportdb is None):
				city_name = airports[airport]['city']
				city = CityService().getCityByName(city_name)
				print(city)

				if(city is None):
					try:
						state_cod = airports[airport]['state']
						state = StateService().getStateByCod(state_cod.strip())

						if(state is None):
							raise ValueError('State does not match any record in the database!')

					except Exception as error:
						print('Error +: ' + repr(error))

					else:
						city = CityService().postCity(city_name ,state[0])
						print(city)

				airportdb = self.postAirport(iata, city[0], state[0], airports[airport]['lat'], airports[airport]['lon'])

	def postAirport(self, iata, city_id, state_id, lat, lon):
		sql = "INSERT INTO aeroportos (iata, cidade, estado, geom) VALUES "
		sql += "('" + iata + "', "+str(city_id)+", "+str(state_id)+", "
		sql += "GeomFromEWKT('SRID=4326;POINT("+str(lon)+" "+str(lat)+")') ) RETURNING *"
		return self._db.pquery(sql)	


	def getAirportByIata(self, iata):
		sql = "SELECT * FROM aeroportos a WHERE a.iata = '" + iata + "'"
		return self._db.squery(sql)
