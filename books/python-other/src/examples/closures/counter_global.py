count = 0
def counter():
    global count
    count += 1
    return count

print(counter())
print(counter())
print(counter())

count = -42
print(counter())
