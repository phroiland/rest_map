import pymysql
import dbconfig
import datetime

class DBHelper:
	def connect(self, database='rest_map'):
		return pymysql.connect(host='localhost', user=dbconfig.db_user,
								passwd=dbconfig.db_password, db=database)

	def clear_all(self):
		conn = self.connect()
		try:
			query = 'DELETE FROM restaurants;'
			with conn.cursor() as cur:
				cur.execute(query)
				conn.commit()
		finally:
			conn.close()

	def add_rest(self, category, latitude, longitude, description):
		conn = self.connect()
		try:
			query = 'INSERT INTO restaurants (category, latitude, longitude, description) VALUES (%s, %s, %s, %s)'
			with conn.cursor() as cur:
				cur.execute(query, (category, latitude, longitude, description))
				conn.commit()
		except Exception as e:
			print e
		finally:
			conn.close()

	def get_all_restaurants(self):
		conn = self.connect()
		try:
			query = "SELECT latitude, longitude, category, description FROM restaurants;"
			with conn.cursor() as cur:
				cur.execute(query)
			named_restaurants = []
			for rest in cur:
				named_restaurant = {
					'latitude': rest[0],
					'longitude': rest[1], 
					'category': rest[2], 
					'description': rest[3]
				}
				named_restaurants.append(named_restaurant)
			return named_restaurants
		finally:
			conn.close()
	


