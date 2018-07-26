from dbconnection import DBconnection

class AircraftService:
	_db = None

	def __init__(self):
		self._db = DBconnection()

	def searchForAircraft(self, model, manufacturer):
		modeldb = self.getModelByName(model)

		if(modeldb is None):
			manufacturerdb = self.getManufacturerByName(manufacturer)

			if(manufacturerdb is None):
				manufacturerdb = self.postManufacture(manufacturer)

			modeldb = self.postModel(model,manufacturerdb[0])

		return modeldb

	def getManufacturerByName(self, manufacturer):
		sql = "SELECT fabricante_id FROM fabricantes WHERE nome = '"+manufacturer+"'"
		return self._db.squery(sql)

	def getModelByName(self, model):
		sql = "SELECT modelo_id FROM modelos WHERE nome = '"+model+"'"
		return self._db.squery(sql)

	def postManufacture(self, manufacturer):
		sql = "INSERT INTO fabricantes (nome) VALUES  ('" + manufacturer + "') RETURNING *"
		return self._db.spquery(sql)

	def postModel(self, model, manufacturer):
		sql = "INSERT INTO modelos (nome, fabricante) VALUES ('" + model + "', " + str(manufacturer) + ") RETURNING *"
		return self._db.spquery(sql)