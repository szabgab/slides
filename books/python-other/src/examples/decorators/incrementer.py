

def create_incrementer(num):
    def inc(val):
        return num + val
    return inc

inc_5 = create_incrementer(5)

print(inc_5(10))  # 15
print(inc_5(0))   #  5


inc_7 = create_incrementer(7)

print(inc_7(10))  # 17
print(inc_7(0))   #  7
