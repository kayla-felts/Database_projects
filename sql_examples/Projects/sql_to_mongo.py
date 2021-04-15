import mongo_query
import mongo_connection as conn_handler


def main():
    # Connection methods
    db = conn_handler.mongo_connect(conn_handler.PASSWORD, conn_handler.DBNAME)
    sl_conn, sl_curs = conn_handler.sqlite_connect()

    # Getting rpg document collection
    collection = db.test

    # getting weapons
    weapons = sl_curs.execute(mongo_query.GET_WEAPON)
    for weapon in weapon:
        mongo_document = {
            'name': character[1],  # weapon name
            'name': character[2],  # weapon name

        }
        collection.insert_one(mongo_document)

    sl_curs.close()


if __name__ == '__main__':
    main()
