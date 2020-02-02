class Monkey:

    def __init__(self, count):
        self.bananas = count

    def is_hungry(self):
        hungry = True
        if hungry:
            self.eat()

    def eat(self):
        self.bananas -= 1


m = Monkey(10)
print(m.bananas)       # 10
print(m.is_hungry())   # None
print(m.bananas)       # 9

Monkey.eat = lambda self: True

om = Monkey(10)
print(om.bananas)      # 10
print(om.is_hungry())  # None
print(om.bananas)      # 10

