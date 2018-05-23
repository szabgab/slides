import sqlite3

db_filename = 'bank.db'


class DB():
    def __init__(self):
        self.db_filename = db_filename
        self.conn = sqlite3.connect(self.db_filename)

    def create(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE account
                 (name text, ballance real)''')

    def get(self, name):
        c = self.conn.cursor()
        c.execute('SELECT ballance FROM account WHERE name=?', (name,))
        current = c.fetchone()
        if current == None:
            return current
        else:
            return current[0]

    def insert(self, name, amount):
        c = self.conn.cursor()
        c.execute('INSERT INTO account (name, ballance) VALUES (?, ?)', (name, amount))

    def update(self, name, amount):
        c = self.conn.cursor()
        c.execute('UPDATE account SET ballance = ? WHERE name = ?', (amount, name))
  
