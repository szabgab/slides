import datetime

class Car:
    def __init__(self, mass, color, wheels=4):
        self.wheels = wheels
        self.mass = mass
        self.color = color
        self.production_date = datetime.datetime.now()

porshe = Car(100, "red")
print(porshe.color)
print(porshe.wheels)
print(porshe.production_date)

TODO: add move method to Ball
