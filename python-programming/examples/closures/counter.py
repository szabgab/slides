def create_counter():
    count = 0
    def internal():
        nonlocal count
        count += 1
        return count
    return internal

counter = create_counter()

print(counter())
print(counter())
print(count)
