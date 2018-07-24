from dbconnection import DBconnection

class StateService:
	_db = None

	def __init__(self):
		self._db = DBconnection()

	def getStateByCod(self, cod):
		sql = "SELECT * FROM estados s WHERE s.sigla = '" + cod + "'"
		print(sql)
		return self._db.squery(sql)