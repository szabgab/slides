import mysql.connector


def main(min_score):
    conn = mysql.connector.connect(
        host = 'localhost',
        database = 'fb_db',
        user = 'foobar',
        password='no secret')

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person WHERE score > %s", (min_score,))

    size = 2

    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        print(len(rows))
        for row in rows:
            print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main(40)

