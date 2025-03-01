import psycopg2
from config import config

def connect():
	""" Connect to the PostgreSQL database server """
	conn = None
	try:
		# read connection parameters
		params = config()

		# connect to the PostgreSQL server
		print('Connecting to the PostgreSQL database...')
		conn = psycopg2.connect(**params)
		
		# create a cursor
		cur = conn.cursor()
		
	# execute a statement
		print('PostgreSQL database version:')
		#cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
		cur.execute("select*from actor")
		
		result1=cur.fetchall()

		
		for all in result1:
			print(all)

		cur.execute('select*from category')
		result2=cur.fetchone()
		print(result2)

		cur.execute('select*from address')
		result3=cur.fetchmany(50)
		print(result3)
		
		
	# close the communication with the PostgreSQL
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed.')


if __name__ == '__main__':
	connect()
