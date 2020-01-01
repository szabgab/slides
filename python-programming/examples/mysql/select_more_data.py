import mysql.connector


def main():
    conn = mysql.connector.connect(
        host = 'localhost',
        database = 'fb_db',
        user = 'foobar',
        password='no secret')

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person")

    while True:
        row = cursor.fetchone()
        if not row:
            break
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

