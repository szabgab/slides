from datetime import datetime
class Person():
    def __init__(self, years):
        self.age =  years

    # creates "getter"
    @property
    def age(self):
        return datetime.now().year - self.birthyear

    # creates "setter"
    @age.setter
    def age(self, years):
        self.birthyear = datetime.now().year - years

p = Person(19)
print(p.age)       # 19

p.age = p.age + 1
print(p.age)       # 20


p.birthyear = 1992
print(p.age)       # 28
   # warning: this will be different if you run the example in a year different from 2020 :)
