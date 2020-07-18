import mysql.connector


def main():
    conn = mysql.connector.connect(
        host = 'localhost',
        database = 'fb_db',
        user = 'foobar',
        password='no secret')

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM person")

    for row in cursor:
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
