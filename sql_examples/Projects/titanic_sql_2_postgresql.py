'''Creating Data Pipeline moving data from sqlite to postgresql'''
import pandas as pd
import sqlite3
import psycopg2
import create_queries as create
import read_queries as read
from sqlalchemy import create_engine


# Create in memory sql db
engine = create_engine('sqlite://', echo=False)


# Import and read csv
filepath = './titanic.csv'
df = =pd.read_csv(filepath)


# Convert form csv to db
df.to_sql('titanic.sqlite3', con=engine)


# postgresql db credentials
PG_DBNAME = '?'
PG_USER = '?'
PG_PASSWORD = '?'
PG_HOST = '?'


def initialize(pg_curs):
    '''initiliazes postgresql DB'''
    pg_curs.execute(create.CREATE_passenger)


def sl_connect(sl_db='./titanic.sqlite3'):
    '''Connects to sqlite'''
    sl_conn = sqlite3.connect(sl_db)
    sl_curs = sl_conn.cursor()
    return sl_conn, sl_curs


def pg_connect(dbname, user, password, host):
    '''Connects to postgresql'''
    pg_conn = psycopg2.connect(
        dbname=dbname, user=user, password=password, host=host)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs


# Only executes read queries
def execute_read_query(curs, query):
    '''Executes query through passed in cursor'''
    curs.execute(query)
    return curs.fetchall()


def pipeline(pg_curs, sl_curs):
    '''Handling migration of titanic_passenger table'''
    passenger_list = execute_read_query(sl_curs, read.GET_PASSENGER)
    for passenger in cpassenger_list:
        # passenger = (survived, pclass, name, ...)
        insert_statement = create.INSERT_charactercreator_character % (
            passenger[1],  # survived
            passenger[2],  # pclass
            passenger[3],  # name
            passenger[4],  # sex
            passenger[5],  # age
            passenger[6],  # siblings/spouses
            passenger[7],  # parents/children
            passenger[8]   # fare
        )
        pg_curs.execute(insert_statement)
    pg_curs.commit()
    return 'DONE!'


if __name__ == '__main__':
    sl_conn, sl_curs = sl_connect()
    pg_conn, pg_curs = pg_connect(
        PG_DBNAME,
        PG_USER,
        PG_PASSWORD,
        PG_HOST
    )
    initialize(pg_curs)
    pipeline(pg_curs, sl_curs)
