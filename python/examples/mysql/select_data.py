import mysql.connector


def main():
    conn = mysql.connector.connect(
        host = 'localhost',
        database = 'fb_db',
        user = 'foobar',
        password='no secret')

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person")

    row = cursor.fetchone()
    print(row)

    # cursor.close()  # mysql.connector.errors.InternalError: Unread result found.
    conn.close()

if __name__ == "__main__":
    main()
