import mysql.connector

def main():
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            database = 'fb_db',
            user = 'foobar',
            password='no secret')
    except mysql.connector.Error as e:
        print("MySQL exception: ", e)
        return
    #except Exception as e:
    #    print("Other exception", e);
    #    return

    print("Connected:", conn)

    conn.close()

if __name__ == "__main__":
    main()

