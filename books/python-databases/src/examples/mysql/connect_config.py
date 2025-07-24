import configparser
import mysql.connector

config_file = 'examples/mysql/connect.ini'

def read_config(section = 'development'):
    print(section)
    cp = configparser.ConfigParser()
    cp.read(config_file)
    if not cp.has_section(section):
        raise Exception("No configuration found for '{}'".format(section))

    return cp[section]

def main():
    try:
        db = read_config()
        print(db['password'])
        print(db)
        conn = mysql.connector.connect(**db)
    except mysql.connector.Error as e:
        print("MySQL exception: ", e)
        return
    except Exception as e:
        print("Other exception", e);
        return

    if conn.is_connected():
        print("is connected")
    print("Connected:", conn)

    conn.close()

if __name__ == "__main__":
    main()


