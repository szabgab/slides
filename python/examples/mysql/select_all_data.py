import mysql.connector


def main():
    conn = mysql.connector.connect(
        host = 'localhost',
        database = 'fb_db',
        user = 'foobar',
        password='no secret')

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person")

    rows = cursor.fetchall()

    print(len(rows))
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
