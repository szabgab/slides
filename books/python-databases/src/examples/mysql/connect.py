import mysql.connector

def main():
    conn = mysql.connector.connect(
        host = 'localhost',
        database = 'fb_db',
        user = 'foobar',
        password='no secret')

    print("Connected:", conn)

    conn.close()

if __name__ == "__main__":
    main()

