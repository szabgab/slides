from datetime import datetime
class Person():
    def __init__(self, years):
        self.age =  years

    def get_birthyear(self):
        return datetime.now().year - self.birthyear

    def set_birthyear(self, years):
        self.birthyear = datetime.now().year - years

    age = property(get_birthyear, set_birthyear)

p = Person(19)
print(p.age)       # 19

p.age = p.age + 1
print(p.age)       # 20


p.birthyear = 1992
print(p.age)       # 23
