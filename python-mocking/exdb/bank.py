import db

class Bank():
    def __init__(self):
        self.db = db.DB()

    def setup(self):
        self.db.create()

    def transfer(self, src, dst, amount):
        current = self.db.status(src)
        if current and current >= amount:
            self.db.deposit(src, -amount)
            self.db.deposit(dst, amount)
        else:
            raise Exception("Not enough money")

    def status(self, name):
        return self.db.status(name)
  
    def deposit(self, name, amount):
        self.db.deposit(name, amount)

