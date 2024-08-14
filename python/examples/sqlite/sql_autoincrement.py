import sqlite3

def create_table(conn, crs):
    sql = '''
        CREATE TABLE people (
           id        INTEGER PRIMARY KEY AUTOINCREMENT,
           username  VARCHAR(100) UNIQUE NOT NULL
    );
    '''

    try:
        crs.execute(sql)
    except sqlite3.OperationalError as err:
        print(f'sqlite error: {err.args[0]}')  # table companies already exists
    conn.commit()


def insert(conn, crs, username):
    sql = 'INSERT INTO people (username) VALUES (?)'
    try:
        crs.execute(sql, (username,))
    except sqlite3.IntegrityError as err:
        print('sqlite error: ', err.args[0])
    conn.commit()


def list_rows(conn, crs):
    sql = "SELECT * FROM people"
    for id, username in crs.execute(sql):
        print(f"{id} - {username}")


def main():
    conn = sqlite3.connect(":memory:")
    crs = conn.cursor()
    create_table(conn, crs)

    insert(conn, crs, "rachel")
    list_rows(conn, crs)

    insert(conn, crs, "joey")
    list_rows(conn, crs)

    insert(conn, crs, "monica")
    list_rows(conn, crs)

    insert(conn, crs, "monica")
    list_rows(conn, crs)

    conn.close()
    print('done')


main()
