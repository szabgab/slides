
class Person(object):
    def __init__(self, age):
        self.age = age

p = Person(19)
print(p.age)       # 19

p.age = p.age + 1
print(p.age)       # 20
