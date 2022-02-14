# Step 0 - import sqlite3
import sqlite3
import queries as q

# DB Connect function
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

# Execute Queries and "pull the results"
def execute_q(conn, query):
    curs = conn.cursor()
    results = curs.execute(query).fetchall()
    return results

# code that will only be executed
# when the file is run as a script
if __name__ == '__main__':
    conn = connect_to_db(db_name='rpg_db.sqlite3')
    print(execute_q(conn, q.NUM_CLERIC_ITEMS))
