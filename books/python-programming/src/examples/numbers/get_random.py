import random

rnd = random.random
print(rnd)            # <built-in method random of Random object at 0x124b508>



y = rnd()
print(y)              # 0.7740737563564781

print(random.random)  # <built-in method random of Random object at 0x124b508>

x = rnd
print(x)              # <built-in method random of Random object at 0x124b508>
print(x())            # 0.5598791496813703
