from Filghts.service.dbconnection import DBconnection

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

	def getAllModels(self):
		sql = "SELECT * FROM modelos"
		return self._db.mquery(sql)

	def updateAllModelsSpeed(self):
		sql = "SELECT m.modelo_id, SUM(r.distancia), SUM(v.duracao) FROM rotas r, viagens v, modelos m WHERE "
		sql += "v.aeronave = m.modelo_id AND v.rota = r.rota_id GROUP BY m.modelo_id"
		models = self._db.mquery(sql)
		models_updated = []

		for model in models:
			speed = model[1]/float(model[2].total_seconds())*3600
			models_updated.append(self.updateModelSpeed(model[0], speed))

		return models_updated

	def updateModelSpeed(self, model, speed):
		sql = "UPDATE modelos SET velocidade = " + str(speed) + " WHERE modelo_id = " + str(model) + " RETURNING *"
		return self._db.spquery(sql)


