import sqlite3

sql = 'INSERT INTO companies (name, employees, established) VALUES (?, ?, ?)'

def insert_one(conn, crs):
    company_name = 'Hostlocal'
    employee_count = 1
    year_of_establishment = 2000

    try:
        crs.execute(sql, (company_name, employee_count, year_of_establishment))
    except sqlite3.IntegrityError as err:
        print('sqlite error: ', err.args[0]) # column name is not unique
    conn.commit()


def insert_many(conn, crs):
    companies = [
        ('Google',    150_028, 1998),
        ('Facebook',   68_177, 2003),
        ('Apple',     154_000, 1977),
        ('Microsoft', 181_000, 1975),
    ]

    try:
        crs.executemany(sql, companies)
    except sqlite3.IntegrityError as err:
        print(f'sqlite error: {err.args[0]}')
    conn.commit()


def main():
    conn = sqlite3.connect("companies.db")
    crs = conn.cursor()
    insert_one(conn, crs)
    insert_many(conn, crs)
    conn.close()
    print('done')

main()
