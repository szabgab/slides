class NegativeDeposite(Exception):
    pass

class Bank:
    def __init__(self, start):
        self.balance = start

    def deposit(self, money):
        if money < 0:
            raise NegativeDeposite('Cannot deposit negative sum')
        self.balance += money
        return

