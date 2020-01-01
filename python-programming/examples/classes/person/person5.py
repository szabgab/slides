from datetime import datetime
class Person():
    def __init__(self, years):
        self.age =  years

    @property
    def age(self):
        return datetime.now().year - self.birthyear

    @age.setter
    def age(self, years):
        if years < 0:
            raise ValueError("Age cannot be negative")
        self.birthyear = datetime.now().year - years

# p = Person(-1)
# ValueError: Age cannot be negative

# p = Person(10)
# p.age = -1
# ValueError: Age cannot be negative

p = Person(19)
print(p.age)       # 19

p.age = p.age + 1
print(p.age)       # 20

p.birthyear = 1992
print(p.age)       # 23
