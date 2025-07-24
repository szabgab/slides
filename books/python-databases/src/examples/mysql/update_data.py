import mysql.connector


def main(uid, score):
    conn = mysql.connector.connect(
        host = 'localhost',
        database = 'fb_db',
        user = 'foobar',
        password='no secret')

    cursor = conn.cursor()
    cursor.execute("UPDATE person SET score=%s WHERE id=%s",
        (score, uid))
    conn.commit()

    conn.close()

if __name__ == "__main__":
    main(12, 32)

