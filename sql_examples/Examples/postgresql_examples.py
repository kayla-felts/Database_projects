'''Examples of postgresql'''
from os import getenv
import psycopg2
import create_queries as create

PG_DBNAME = '?'
PG_USER = '?'
PG_PASSWORD = '?'
PG_HOST = '?'


# STEP1 - connect to DB
pg_conn = psycopg2.connect(dbname=PG_DBNAME, user=PG_USER,
                           password=PG_PASSWORD, host=PG_HOST)


# STEP2  - make a cursor to traverse DB
pg_curs = pg_conn.cursor()


# STEP4 - execute query
# Create
pg_curs.execute(create.CREATE_TEST)
pg_curs.execute(create.INSERT_TEST)

# Read
pg_curs.execute('SELECT * FROM test_table')

# STEP5 - fetch data
results = pg_curs.fetchall()
if __name__ == '__main__':
    print(results)
