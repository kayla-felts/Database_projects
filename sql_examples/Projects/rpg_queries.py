# Import libraries
import sqlite3
import queries as q


# Connect to database
def connect_to_db(db_name='rpg_db.sqlite3'):
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
