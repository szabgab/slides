def make_incrementor(n):
    def inc(x):
        return x + n
    return inc

f3 = make_incrementor(3)
f7 = make_incrementor(7)

print(f3(2))    #  5
print(f7(3))    # 10
print(f3(4))    #  7
print(f7(10))   # 17
