import sqlite3

def create_table(conn, crs):
    sql = '''
        CREATE TABLE bank (
            name TEXT PRIMARY KEY,
            balance INTEGER NOT NULL
    );
    '''

    try:
        crs.execute(sql)
    except sqlite3.OperationalError as err:
        print(f'sqlite error: {err.args[0]}')  # table companies already exists
    conn.commit()


def insert_account(conn, crs, name, balance):
    sql = 'INSERT INTO bank (name, balance) VALUES (?, ?)'
    try:
        crs.execute(sql, (name, balance))
    except sqlite3.IntegrityError as err:
        print('sqlite error: ', err.args[0])
    conn.commit()

def show(conn, crs):
    sql = "SELECT * FROM bank"
    for name, balance in crs.execute(sql):
        print(f"{name:5}: {balance:>5}")
    for (total,) in crs.execute("SELECT SUM(balance) AS total FROM bank"):
        print(f"Total: {total:>5}")
    print("------")

def update(conn, crs, name, amount):
    sql = 'UPDATE bank SET balance = (SELECT balance FROM bank WHERE name = ?) + ? WHERE name = ?';
    try:
        crs.execute(sql, (name, amount, name))
    except sqlite3.IntegrityError as err:
        print('sqlite error: ', err.args[0])
    conn.commit()

def without_transaction(conn, crs, from_name, to_name, amount):
    update(conn, crs, from_name, -amount);
    return
    update(conn, crs, to_name, amount);

def with_transaction(conn, crs, from_name, to_name, amount):
    sql = 'UPDATE bank SET balance = (SELECT balance FROM bank WHERE name = ?) + ? WHERE name = ?';
    try:
        crs.execute(sql, (from_name, -amount, from_name))
        return
        crs.execute(sql, (to_name, amount, to_name))
    except sqlite3.IntegrityError as err:
        print('sqlite error: ', err.args[0])
    print("here")
    conn.commit()


def main():
    conn = sqlite3.connect(":memory:", autocommit=False, isolation_level=None)
    crs = conn.cursor()
    create_table(conn, crs)
    insert_account(conn, crs, "Jane", 0)
    insert_account(conn, crs, "Mary", 1000)
    insert_account(conn, crs, "Ann", 1000)
    show(conn, crs)

    update(conn, crs, "Mary", -100)
    update(conn, crs, "Jane", +100)
    show(conn, crs)

    without_transaction(conn, crs, "Mary", "Jane", 100)
    show(conn, crs)

    with_transaction(conn, crs, "Mary", "Jane", 100)
    show(conn, crs)

    conn.close()

main()

