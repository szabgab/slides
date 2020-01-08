from with_abc3 import Base

class Real(Base):
    def foo(self):
        print('foo in Real')

    def bar(self):
        print('bar in Real')

    def other(self):
        pass

r = Real('Jane')
print(r.name)      # Jane
