class Bike:
    count = 0
    def __init__(self):
        Bike.count += 1

    def __del__(self):
        Bike.count -= 1

def bike_trip():
    print(Bike.count)   # 0
    a = Bike()
    print(Bike.count)   # 1
    b = Bike()
    print(Bike.count)   # 2
    c = Bike()
    print(Bike.count)   # 3
    b = None
    print(Bike.count)   # 2


bike_trip()
print(Bike.count)       # 0
