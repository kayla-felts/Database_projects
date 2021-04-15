import sqlite3
import pymongo

PASSWORD = '?'
DBNAME = '?'


def sqlite_connect(db_path='./rpg_db.sqlite3'):
    '''Create SQLite connection and cursor object'''
    conn = sqlite3.connect(db_path)
    curs = conn.cursor()
    return conn, curs


def mongo_connect(password, dbname):
    '''Creates mongoDB Client and returns DB'''
    client = pymongo.MongoClient(
        'mongodb+srv://macOS-kayla:{}@num1.hwywk.mongodb.net/{}?retryWrites=true&w=majority'
        .format(password, dbname)
    )
    return client.test
