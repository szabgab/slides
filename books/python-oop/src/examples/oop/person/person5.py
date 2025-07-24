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

