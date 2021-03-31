import weakref

class Thing:
    things = {}
    def __init__(self):
        Thing.things[id(self)] = weakref.ref(self)

    def __del__(self):
        print('__del__')
        del(Thing.things[id(self)])


def main():
    print(Thing.things)
    t1 = Thing()
    print(Thing.things)
    t2 = Thing()
    print(Thing.things)
    t3 = Thing()
    print(Thing.things)

main()
print(Thing.things)

