import db

class Bank():
    def __init__(self):
        self.db = db.DB()

    def setup(self):
        self.db.create()

    def transfer(self, src, dst, amount):
        src_current = self.db.get(src)
        dst_current = self.db.get(dst)
        if src_current and src_current >= amount:
            self.db.update(src, src_current-amount)
            self.db.update(dst, dst_current+amount)
        else:
            raise Exception("Not enough money")

    def status(self, name):
        return self.db.get(name)
  
    def deposit(self, name, amount):
        current = self.db.get(name)
        if current == None:
            self.db.insert(name, amount)
        else:
            self.db.update(name, current+amount)
