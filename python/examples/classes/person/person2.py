from datetime import datetime
class Person(object):
    def __init__(self, years):
        self.set_birthyear(years)

    def get_birthyear(self):
        return datetime.now().year - self._birthyear

    def set_birthyear(self, years):
        self._birthyear = datetime.now().year - years

    def age(self, years=None):
        if (years):
            self.set_birthyear(years)
        else:
            return self.get_birthyear()



p = Person(19)
print(p.age())       # 19

p.age(p.age() + 1)
print(p.age())       # 20
