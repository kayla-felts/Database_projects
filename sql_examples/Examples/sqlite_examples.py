'''SQLITE# eample of a connection'''
import sqlite3
import queries as q


# STEP! - makea  connection object to the DB
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)


# STEP2- Make your cursor through the conn object
# STEP4- Execute the query
# STEP5- Pull the results
def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    return results


if __name__ == '__main__':
    conn = connect_to_db()
    results = execute_q(conn, q.select_all)
    print(results[:5])
    print(len(results))
