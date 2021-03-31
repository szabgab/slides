class Thing:
    count = 0
    def __init__(self):
        Thing.count += 1

def main():
    print(Thing.count)
    t1 = Thing()
    print(Thing.count)
    t2 = Thing()
    print(Thing.count)
    t3 = Thing()
    print(Thing.count)

main()
print(Thing.count)
