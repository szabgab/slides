import mysql.connector


def main(name, birthdate, score):
    conn = mysql.connector.connect(
        host = 'localhost',
        database = 'fb_db',
        user = 'foobar',
        password='no secret')

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO person (name, birthdate, score) VALUES (%s, %s, %s)",
        (name, birthdate, score))

    if cursor.lastrowid:
        print('last insert id', cursor.lastrowid)
    else:
        print('last insert id not found')
    conn.commit()

    conn.close()

if __name__ == "__main__":
    main('Monty Python', '1969-10-05', 100)


