import pymysql
import dbconfig

conn = pymysql.connect(host='localhost', user=dbconfig.db_user, passwd=dbconfig.db_password)

try:
	with conn.cursor() as cur:
		sql = "CREATE DATABASE IF NOT EXISTS rest_map"
		cur.execute(sql)
		sql = """CREATE TABLE IF NOT EXISTS rest_map.restaurants (
			id int NOT NULL AUTO_INCREMENT, latitude FLOAT(10, 6),
			longitude FLOAT(10, 6), category VARCHAR(50), 
			description VARCHAR(1000), updated_at TIMESTAMP, PRIMARY KEY (id))"""
		cur.execute(sql)
	conn.commit()
finally:
	conn.close()
