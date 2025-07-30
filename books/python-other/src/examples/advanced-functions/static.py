
def counter():
    if 'cnt' not in counter.__dict__:
        counter.cnt = 0
    counter.cnt += 1
    return counter.cnt

print(counter())      # 1
print(counter())      # 2
print(counter())      # 3

print(counter.cnt)    # 3

counter.cnt = 6
print(counter())      # 7
