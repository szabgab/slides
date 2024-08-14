import sqlite3

def create_table(conn, crs):
    sql = '''
        CREATE TABLE qa (
           question  TEXT,
           answer    TEXT DEFAULT "42"
    );
    '''

    try:
        crs.execute(sql)
    except sqlite3.OperationalError as err:
        print(f'sqlite error: {err.args[0]}')  # table companies already exists
    conn.commit()


def insert_qa(conn, crs, question, answer):
    sql = 'INSERT INTO qa (question, answer) VALUES (?, ?)'
    try:
        crs.execute(sql, (question, answer))
    except sqlite3.IntegrityError as err:
        print('sqlite error: ', err.args[0])
    conn.commit()

def insert_q(conn, crs, question):
    sql = 'INSERT INTO qa (question) VALUES (?)'
    try:
        crs.execute(sql, (question,))
    except sqlite3.IntegrityError as err:
        print('sqlite error: ', err.args[0])
    conn.commit()


def list_rows(conn, crs):
    sql = "SELECT * FROM qa"
    for question, answer in crs.execute(sql):
        print(f"{question} - {answer}")
    print("------")


def main():
    conn = sqlite3.connect(":memory:")
    crs = conn.cursor()
    create_table(conn, crs)

    insert_qa(conn, crs, "Language?", "Python")
    list_rows(conn, crs)

    insert_qa(conn, crs, "Database?", "SQLite")
    list_rows(conn, crs)

    insert_q(conn, crs, "Meaning of life?")
    list_rows(conn, crs)

    conn.close()
    print('done')

main()

