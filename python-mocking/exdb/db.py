import sqlite3


class DB():
    def __init__(self, filename):
        self.db_filename = filename
        self.conn = sqlite3.connect(self.db_filename)

    def create(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE account
                 (name text, ballance real)''')

    def transfer(self, src, dest, amount):
        c = self.conn.cursor()
        current = c.fetchone()

    def status(self, name):
        c = self.conn.cursor()
        c.execute('SELECT * FROM account WHERE name=?', (name,))
        current = c.fetchone()
        return current
  
    def deposit(self, name, amount):
        c = self.conn.cursor()
        #c.execute('
       
