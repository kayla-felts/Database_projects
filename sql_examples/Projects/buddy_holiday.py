# Import libraries
import pandas as pd 
import sqlite3
import queries as q
from sqlalchemy import create_engine

# Create in memory SQLite database
engine = create_engine('sqlite://', echo=False)


# Load csv data
filepath = './buddy_holiday.py'
df = pd.read_csv(filepath)


# Convert DF to DB
df.to_sql('buddymove_holidayiq.sqlite3', con=engine)


# Connect to database
def connect_to_db(db_name='buddymove_holidayiq.sqlite3'):
    return sqlite3.connect(db_name)


# Create function to create cursor, execute query, and pull results
def execute_q(conn, query):
    # Create cursor
    curs = conn.cursor()
    # Execute query
    curs.execute(query)
    # Pull results
    results = curs.fetchall()
    # Make sure to return results
    return results


if __name__ == '__main__':
    conn = connect_to_db()
    results = execute_q(conn, q.TOTAL_CHARACTERS)
    print(results)
    