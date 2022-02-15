from asyncore import read
import psycopg2
import sqlite3
import queries as q

# PostgreSQL DB Connection Variables
DBNAME = 'znshjpft'
USER = 'znshjpft'
PASSWORD = 'apVV9xniDJPSTH0Flztey9_iNSo9HcGc'
HOST = 'salt.db.elephantsql.com'

# Connect to the PostgreSQL database
pg_conn = psycopg2.connect(dbname=DBNAME, user=USER,
                           password=PASSWORD, host=HOST)
# Get a cursor from the connection
pg_curs = pg_conn.cursor()


def create_or_drop_table(curs, query):
    return curs.execute(query)


def pg_insert(curs, conn, query):
    curs.execute(query)
    conn.commit()


def read_from_table(curs, query):
    curs.execute(query)
    return curs.fetchall()


# SQLite Connection and Cursor
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

if __name__ == '__main__':
    # create_or_drop_table(pg_curs, q.DROP_TEST_TABLE)
    # create_or_drop_table(pg_curs, q.CREATE_TEST_TABLE)
    # pg_insert(pg_curs, pg_conn, q.INSERT_TEST_TABLE)
    # print(read_from_table(pg_curs, q.READ_TEST_TABLE))

    characters = read_from_table(sl_curs, q.GET_CHARACTERS)

    create_or_drop_table(pg_curs, q.DROP_CHARACTER_TABLE)

    create_or_drop_table(pg_curs, q.CREATE_CHARACTER_TABLE)

    # pg_insert(pg_curs, pg_conn, q.INSERT_RYAN)

    for character in characters:
        # print(character)
        pg_insert(pg_curs, pg_conn, f'''INSERT INTO charactercreator_character ("name", "level", "exp", "hp", "strength", "intelligence", "dexterity", "wisdom")
         VALUES ('{character[1]}', {character[2]}, {character[3]}, {character[4]}, {character[5]}, {character[6]}, {character[7]}, {character[8]})''')
