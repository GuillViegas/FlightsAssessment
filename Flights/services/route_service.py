from Filghts.service.dbconnection import DBconnection
from Filghts.service.airport_service import AirportService
from Flights.utils.haversine import haversine

class RouteService:
	_db = None

	def __init__(self):
		self._db = DBconnection()

	def createRoutes(self):
		ars1 = AirportService().getAllAirportsIata()
		routes = []

		while(len(ars1) != 0):
			origin = ars1[0][0]
			ars1.remove(ars1[0])

			for dest in ars1:
				dest = dest[0]
				dist = self.calcDistanceKm(origin, dest)
				routes.append(self.postRoute(origin, dest, dist))
				routes.append(self.postRoute(dest, origin, dist))

		return routes
				
	def calcDistanceKm(self, origin, dest):
		origin = AirportService().getAirportCoord(origin)
		dest = AirportService().getAirportCoord(dest)

		return haversine(origin, dest)

	def calcDistanceDegree(self, origin, dest):
		sql = "SELECT ST_Distance(o.geom, d.geom) FROM aeroportos o, aeroportos d"
		sql += " WHERE o.iata = '"+origin+"'"
		sql += " AND d.iata = '"+dest+"'"

		return self._db.squery(sql)

	def postRoute(self, origin, dest, dist):
		sql = "INSERT INTO rotas (origem, destino, distancia) VALUES  "
		sql += "('" + origin+"', '"+dest+"', "+str(dist)+") RETURNING *"

		return self._db.spquery(sql)

	def getRouteID(self, origin, dest):
		sql = "SELECT rota_id FROM rotas WHERE origem = '" + origin + "' AND destino = '" + dest + "'"
		return self._db.squery(sql)

	def getAllRoutes(self):
		sql = "SELECT * FROM rotas"
		return self._db.mquery(sql)

	def getDistanceRouteByID(self, route):
		sql = "SELECT distancia FROM rotas WHERE rota_id = " + str(route)
		return self._db.squery(sql)