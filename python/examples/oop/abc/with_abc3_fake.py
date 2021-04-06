from with_abc3 import Base

class Fake(Base):
    def foo(self):
        print('foo in Fake')

f = Fake('Joe')
