import psycopg2


class DBconnection(object):
	'''docstring for Postgres'''
	_instance = None

	def __new__(cls):
		if cls._instance is None:

			cls._instance = object.__new__(cls)
			# normally the db_credenials would be fetched from a config file or the enviroment
			# meaning shouldn't be hardcoded as follow
			db_config = {'database': '2XT', 'host': 'localhost', 'password': '123456', 'user': 'postgres'}

			try:
				print('connecting to PostgreSQL database...')
				connection = DBconnection._instance.connection = psycopg2.connect(**db_config)
				cursor = DBconnection._instance.cursor = connection.cursor()
				cursor.execute('SELECT VERSION()')
				db_version = cursor.fetchone()

			except Exception as error:
				print('Error: connection not established {}'.format(error))
				DBconnection._instance = None

			else:
				print('connection established\n{}'.format(db_version[0]))

		return cls._instance

	def __init__(self):
		self.connection = self._instance.connection
		self.cursor = self._instance.cursor

	def query(self, query):
		try:
			self.cursor.execute(query)
			result = self.cursor
		except Exception as error:
			print('error executing query "{}", error: {}'.format(query, error))
			return None
		else:
			return result

	def squery(self, query):
		result = self.query(query)
		return result.fetchone()

	def spquery(self, query):
		result = self.query(query)
		self.connection.commit()
		return result.fetchone()

	def mquery(self, query):
		result = self.query(query)
		return result.fetchall()

	def __del__(self):
		self.connection.close()
		self.cursor.close()