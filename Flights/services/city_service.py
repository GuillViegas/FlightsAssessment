from Filghts.service.dbconnection import DBconnection

class CityService:
	_db = None

	def __init__(self):
		self._db = DBconnection()

	def getCityByName(self, name):
		sql = "SELECT * FROM cidades c WHERE c.nome = '" + name + "'"
		return self._db.squery(sql)

	def postCity(self, city, state):
		sql = "INSERT INTO cidades (nome, estado_id) VALUES  ('" + city + "', "+str(state)+") RETURNING *"
		return self._db.spquery(sql)
