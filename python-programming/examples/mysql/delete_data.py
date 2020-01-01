import mysql.connector


def main(uid):
    conn = mysql.connector.connect(
        host = 'localhost',
        database = 'fb_db',
        user = 'foobar',
        password='no secret')

    cursor = conn.cursor()
    cursor.execute("DELETE FROM person WHERE id=%s", (uid,))
    conn.commit()

    conn.close()

if __name__ == "__main__":
    main(11)

