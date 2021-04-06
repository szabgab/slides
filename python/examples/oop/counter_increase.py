class Thing:
    count = 0
    def __init__(self):
        Thing.count += 1

def main():
    print(Thing.count)  # 0
    t1 = Thing()
    print(Thing.count)  # 1
    t2 = Thing()
    print(Thing.count)  # 2
    t3 = Thing()
    print(Thing.count)  # 3

main()
print(Thing.count)  # 3
