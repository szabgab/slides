class NegativeDeposite(Exception):
    pass

class Bank(object):
    def __init__(self, start):
        self.balance = start

    def deposit(self, money):
        if money < 0:
            raise ValueError('Cannot deposit negative sum')
        self.balance += money
        return

