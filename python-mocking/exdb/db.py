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

    def transfer(self, src, dst, amount):
#        c = self.conn.cursor()
        self.deposit(src, -amount)
        self.deposit(dst, amount)

    def status(self, name):
        c = self.conn.cursor()
        c.execute('SELECT ballance FROM account WHERE name=?', (name,))
        current = c.fetchone()
        if current == None:
            return current
        else:
            return current[0]
  
    def deposit(self, name, amount):
        current = self.status(name)
        c = self.conn.cursor()
        if current == None:
            c.execute('INSERT INTO account (name, ballance) VALUES (?, ?)', (name, amount))
        else:
            c.execute('UPDATE account SET ballance = ? WHERE name = ?', (current+amount, name))
